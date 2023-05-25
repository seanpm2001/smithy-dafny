import java.net.URI
import javax.annotation.Nullable

plugins {
    `java-library`
    `maven-publish`
    id("com.github.johnrengelman.shadow") version "7.1.2"
}

group = "software.amazon.cryptography"
version = "1.0-SNAPSHOT"
description = "AwsCryptographicMaterialProviders"

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(8))
    sourceSets["main"].java {
        srcDir("src/main/java")
        srcDir("src/main/dafny-generated")
        srcDir("src/main/smithy-generated")
    }
    sourceSets["test"].java {
        srcDir("src/test/dafny-generated")
    }
}

var caUrl: URI? = null
@Nullable
val caUrlStr: String? = System.getenv("CODEARTIFACT_URL_JAVA_CONVERSION")
if (!caUrlStr.isNullOrBlank()) {
    caUrl = URI.create(caUrlStr)
}

var caPassword: String? = null
@Nullable
val caPasswordString: String? = System.getenv("CODEARTIFACT_AUTH_TOKEN")
if (!caPasswordString.isNullOrBlank()) {
    caPassword = caPasswordString
}

repositories {
    mavenCentral()
    mavenLocal()
    if (caUrl != null && caPassword != null) {
        maven {
            name = "CodeArtifact"
            url = caUrl!!
            credentials {
                username = "aws"
                password = caPassword!!
            }
        }
    }
}

dependencies {
    implementation("org.dafny:DafnyRuntime:4.1.0")
    implementation("software.amazon.smithy.dafny:conversion:0.1")
    implementation("software.amazon.cryptography:StandardLibrary:1.0-SNAPSHOT")
    implementation("software.amazon.cryptography:AwsCryptographyPrimitives:1.0-SNAPSHOT")
    implementation("software.amazon.cryptography:ComAmazonawsKms:1.0-SNAPSHOT")
    implementation("software.amazon.cryptography:ComAmazonawsDynamodb:1.0-SNAPSHOT")
    implementation(platform("software.amazon.awssdk:bom:2.19.1"))
    implementation("software.amazon.awssdk:dynamodb")
    implementation("software.amazon.awssdk:dynamodb-enhanced")
    implementation("software.amazon.awssdk:kms")
    implementation("software.amazon.awssdk:core:2.19.1")
}

publishing {
    publications.create<MavenPublication>("maven") {
        groupId = "software.amazon.cryptography"
        artifactId = "AwsCryptographicMaterialProviders"
        artifact(tasks["shadowJar"])
    }
    repositories { mavenLocal() }
}

tasks.withType<JavaCompile>() {
    options.encoding = "UTF-8"
}

tasks {
    register("runTests", JavaExec::class.java) {
        mainClass.set("TestsFromDafny")
        classpath = sourceSets["test"].runtimeClasspath
    }
}

tasks.jar {
    enabled = false
}

tasks.build {
    dependsOn(tasks.shadowJar)
}

tasks.shadowJar {
    mergeServiceFiles()
    archiveClassifier.set("")

    dependencies {
        include(dependency("software.amazon.cryptography:StandardLibrary:1.0-SNAPSHOT"))
        include(dependency("software.amazon.cryptography:AwsCryptographyPrimitives:1.0-SNAPSHOT"))
        include(dependency("software.amazon.cryptography:ComAmazonawsKms:1.0-SNAPSHOT"))
        include(dependency("software.amazon.cryptography:ComAmazonawsDynamodb:1.0-SNAPSHOT"))
    }

    configurations {
        runtimeClasspath {
            dependencies {
                // We want to package this version of BC since it is the one the Primitives depends on.
                // These dependencies need to remain in sync with one another.
               include(dependency("org.bouncycastle:bcprov-jdk18on:1.72"))
            }
        }
    }
}