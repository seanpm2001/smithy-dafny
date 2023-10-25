# Code generated by smithy-python-codegen DO NOT EDIT.

from typing import Any, Dict, List, Optional


class ComplexListElement:
    value: Optional[str]
    blob: Optional[bytes | bytearray]
    def __init__(
        self,
        *,
        value: Optional[str] = None,
        blob: Optional[bytes | bytearray] = None,
    ):
        self.value = value
        self.blob = blob

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ComplexListElement to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.value is not None:
            d["value"] = self.value

        if self.blob is not None:
            d["blob"] = self.blob

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ComplexListElement":
        """Creates a ComplexListElement from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "value" in d:
            kwargs["value"] = d["value"]

        if "blob" in d:
            kwargs["blob"] = d["blob"]

        return ComplexListElement(**kwargs)

    def __repr__(self) -> str:
        result = "ComplexListElement("
        if self.value is not None:
            result += f"value={repr(self.value)}, "

        if self.blob is not None:
            result += f"blob={repr(self.blob)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ComplexListElement):
            return False
        attributes: list[str] = ['value','blob',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetConstraintsInput:
    my_string: Optional[str]
    non_empty_string: Optional[str]
    string_less_than_or_equal_to_ten: Optional[str]
    my_blob: Optional[bytes | bytearray]
    non_empty_blob: Optional[bytes | bytearray]
    blob_less_than_or_equal_to_ten: Optional[bytes | bytearray]
    my_list: Optional[list[str]]
    non_empty_list: Optional[list[str]]
    list_less_than_or_equal_to_ten: Optional[list[str]]
    my_map: Optional[dict[str, str]]
    non_empty_map: Optional[dict[str, str]]
    map_less_than_or_equal_to_ten: Optional[dict[str, str]]
    alphabetic: Optional[str]
    one_to_ten: int
    greater_than_one: int
    less_than_ten: int
    my_unique_list: Optional[list[str]]
    my_complex_unique_list: Optional[list[ComplexListElement]]
    my_utf8_bytes: Optional[str]
    my_list_of_utf8_bytes: Optional[list[str]]
    def __init__(
        self,
        *,
        my_string: Optional[str] = None,
        non_empty_string: Optional[str] = None,
        string_less_than_or_equal_to_ten: Optional[str] = None,
        my_blob: Optional[bytes | bytearray] = None,
        non_empty_blob: Optional[bytes | bytearray] = None,
        blob_less_than_or_equal_to_ten: Optional[bytes | bytearray] = None,
        my_list: Optional[list[str]] = None,
        non_empty_list: Optional[list[str]] = None,
        list_less_than_or_equal_to_ten: Optional[list[str]] = None,
        my_map: Optional[dict[str, str]] = None,
        non_empty_map: Optional[dict[str, str]] = None,
        map_less_than_or_equal_to_ten: Optional[dict[str, str]] = None,
        alphabetic: Optional[str] = None,
        one_to_ten: int = 0,
        greater_than_one: int = 0,
        less_than_ten: int = 0,
        my_unique_list: Optional[list[str]] = None,
        my_complex_unique_list: Optional[list[ComplexListElement]] = None,
        my_utf8_bytes: Optional[str] = None,
        my_list_of_utf8_bytes: Optional[list[str]] = None,
    ):
        self.my_string = my_string
        self.non_empty_string = non_empty_string
        self.string_less_than_or_equal_to_ten = string_less_than_or_equal_to_ten
        self.my_blob = my_blob
        self.non_empty_blob = non_empty_blob
        self.blob_less_than_or_equal_to_ten = blob_less_than_or_equal_to_ten
        self.my_list = my_list
        self.non_empty_list = non_empty_list
        self.list_less_than_or_equal_to_ten = list_less_than_or_equal_to_ten
        self.my_map = my_map
        self.non_empty_map = non_empty_map
        self.map_less_than_or_equal_to_ten = map_less_than_or_equal_to_ten
        self.alphabetic = alphabetic
        self.one_to_ten = one_to_ten
        self.greater_than_one = greater_than_one
        self.less_than_ten = less_than_ten
        self.my_unique_list = my_unique_list
        self.my_complex_unique_list = my_complex_unique_list
        self.my_utf8_bytes = my_utf8_bytes
        self.my_list_of_utf8_bytes = my_list_of_utf8_bytes

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetConstraintsInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.my_string is not None:
            d["MyString"] = self.my_string

        if self.non_empty_string is not None:
            d["NonEmptyString"] = self.non_empty_string

        if self.string_less_than_or_equal_to_ten is not None:
            d["StringLessThanOrEqualToTen"] = self.string_less_than_or_equal_to_ten

        if self.my_blob is not None:
            d["MyBlob"] = self.my_blob

        if self.non_empty_blob is not None:
            d["NonEmptyBlob"] = self.non_empty_blob

        if self.blob_less_than_or_equal_to_ten is not None:
            d["BlobLessThanOrEqualToTen"] = self.blob_less_than_or_equal_to_ten

        if self.my_list is not None:
            d["MyList"] = self.my_list

        if self.non_empty_list is not None:
            d["NonEmptyList"] = self.non_empty_list

        if self.list_less_than_or_equal_to_ten is not None:
            d["ListLessThanOrEqualToTen"] = self.list_less_than_or_equal_to_ten

        if self.my_map is not None:
            d["MyMap"] = self.my_map

        if self.non_empty_map is not None:
            d["NonEmptyMap"] = self.non_empty_map

        if self.map_less_than_or_equal_to_ten is not None:
            d["MapLessThanOrEqualToTen"] = self.map_less_than_or_equal_to_ten

        if self.alphabetic is not None:
            d["Alphabetic"] = self.alphabetic

        if self.one_to_ten is not None:
            d["OneToTen"] = self.one_to_ten

        if self.greater_than_one is not None:
            d["GreaterThanOne"] = self.greater_than_one

        if self.less_than_ten is not None:
            d["LessThanTen"] = self.less_than_ten

        if self.my_unique_list is not None:
            d["MyUniqueList"] = self.my_unique_list

        if self.my_complex_unique_list is not None:
            d["MyComplexUniqueList"] = _my_complex_unique_list_as_dict(self.my_complex_unique_list),

        if self.my_utf8_bytes is not None:
            d["MyUtf8Bytes"] = self.my_utf8_bytes

        if self.my_list_of_utf8_bytes is not None:
            d["MyListOfUtf8Bytes"] = self.my_list_of_utf8_bytes

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetConstraintsInput":
        """Creates a GetConstraintsInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "MyString" in d:
            kwargs["my_string"] = d["MyString"]

        if "NonEmptyString" in d:
            kwargs["non_empty_string"] = d["NonEmptyString"]

        if "StringLessThanOrEqualToTen" in d:
            kwargs["string_less_than_or_equal_to_ten"] = d["StringLessThanOrEqualToTen"]

        if "MyBlob" in d:
            kwargs["my_blob"] = d["MyBlob"]

        if "NonEmptyBlob" in d:
            kwargs["non_empty_blob"] = d["NonEmptyBlob"]

        if "BlobLessThanOrEqualToTen" in d:
            kwargs["blob_less_than_or_equal_to_ten"] = d["BlobLessThanOrEqualToTen"]

        if "MyList" in d:
            kwargs["my_list"] = d["MyList"]

        if "NonEmptyList" in d:
            kwargs["non_empty_list"] = d["NonEmptyList"]

        if "ListLessThanOrEqualToTen" in d:
            kwargs["list_less_than_or_equal_to_ten"] = d["ListLessThanOrEqualToTen"]

        if "MyMap" in d:
            kwargs["my_map"] = d["MyMap"]

        if "NonEmptyMap" in d:
            kwargs["non_empty_map"] = d["NonEmptyMap"]

        if "MapLessThanOrEqualToTen" in d:
            kwargs["map_less_than_or_equal_to_ten"] = d["MapLessThanOrEqualToTen"]

        if "Alphabetic" in d:
            kwargs["alphabetic"] = d["Alphabetic"]

        if "OneToTen" in d:
            kwargs["one_to_ten"] = d["OneToTen"]

        if "GreaterThanOne" in d:
            kwargs["greater_than_one"] = d["GreaterThanOne"]

        if "LessThanTen" in d:
            kwargs["less_than_ten"] = d["LessThanTen"]

        if "MyUniqueList" in d:
            kwargs["my_unique_list"] = d["MyUniqueList"]

        if "MyComplexUniqueList" in d:
            kwargs["my_complex_unique_list"] = _my_complex_unique_list_from_dict(d["MyComplexUniqueList"]),

        if "MyUtf8Bytes" in d:
            kwargs["my_utf8_bytes"] = d["MyUtf8Bytes"]

        if "MyListOfUtf8Bytes" in d:
            kwargs["my_list_of_utf8_bytes"] = d["MyListOfUtf8Bytes"]

        return GetConstraintsInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetConstraintsInput("
        if self.my_string is not None:
            result += f"my_string={repr(self.my_string)}, "

        if self.non_empty_string is not None:
            result += f"non_empty_string={repr(self.non_empty_string)}, "

        if self.string_less_than_or_equal_to_ten is not None:
            result += f"string_less_than_or_equal_to_ten={repr(self.string_less_than_or_equal_to_ten)}, "

        if self.my_blob is not None:
            result += f"my_blob={repr(self.my_blob)}, "

        if self.non_empty_blob is not None:
            result += f"non_empty_blob={repr(self.non_empty_blob)}, "

        if self.blob_less_than_or_equal_to_ten is not None:
            result += f"blob_less_than_or_equal_to_ten={repr(self.blob_less_than_or_equal_to_ten)}, "

        if self.my_list is not None:
            result += f"my_list={repr(self.my_list)}, "

        if self.non_empty_list is not None:
            result += f"non_empty_list={repr(self.non_empty_list)}, "

        if self.list_less_than_or_equal_to_ten is not None:
            result += f"list_less_than_or_equal_to_ten={repr(self.list_less_than_or_equal_to_ten)}, "

        if self.my_map is not None:
            result += f"my_map={repr(self.my_map)}, "

        if self.non_empty_map is not None:
            result += f"non_empty_map={repr(self.non_empty_map)}, "

        if self.map_less_than_or_equal_to_ten is not None:
            result += f"map_less_than_or_equal_to_ten={repr(self.map_less_than_or_equal_to_ten)}, "

        if self.alphabetic is not None:
            result += f"alphabetic={repr(self.alphabetic)}, "

        if self.one_to_ten is not None:
            result += f"one_to_ten={repr(self.one_to_ten)}, "

        if self.greater_than_one is not None:
            result += f"greater_than_one={repr(self.greater_than_one)}, "

        if self.less_than_ten is not None:
            result += f"less_than_ten={repr(self.less_than_ten)}, "

        if self.my_unique_list is not None:
            result += f"my_unique_list={repr(self.my_unique_list)}, "

        if self.my_complex_unique_list is not None:
            result += f"my_complex_unique_list={repr(self.my_complex_unique_list)}, "

        if self.my_utf8_bytes is not None:
            result += f"my_utf8_bytes={repr(self.my_utf8_bytes)}, "

        if self.my_list_of_utf8_bytes is not None:
            result += f"my_list_of_utf8_bytes={repr(self.my_list_of_utf8_bytes)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetConstraintsInput):
            return False
        attributes: list[str] = ['my_string','non_empty_string','string_less_than_or_equal_to_ten','my_blob','non_empty_blob','blob_less_than_or_equal_to_ten','my_list','non_empty_list','list_less_than_or_equal_to_ten','my_map','non_empty_map','map_less_than_or_equal_to_ten','alphabetic','one_to_ten','greater_than_one','less_than_ten','my_unique_list','my_complex_unique_list','my_utf8_bytes','my_list_of_utf8_bytes',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetConstraintsOutput:
    my_string: Optional[str]
    non_empty_string: Optional[str]
    string_less_than_or_equal_to_ten: Optional[str]
    my_blob: Optional[bytes | bytearray]
    non_empty_blob: Optional[bytes | bytearray]
    blob_less_than_or_equal_to_ten: Optional[bytes | bytearray]
    my_list: Optional[list[str]]
    non_empty_list: Optional[list[str]]
    list_less_than_or_equal_to_ten: Optional[list[str]]
    my_map: Optional[dict[str, str]]
    non_empty_map: Optional[dict[str, str]]
    map_less_than_or_equal_to_ten: Optional[dict[str, str]]
    alphabetic: Optional[str]
    one_to_ten: int
    greater_than_one: int
    less_than_ten: int
    my_unique_list: Optional[list[str]]
    my_complex_unique_list: Optional[list[ComplexListElement]]
    my_utf8_bytes: Optional[str]
    my_list_of_utf8_bytes: Optional[list[str]]
    def __init__(
        self,
        *,
        my_string: Optional[str] = None,
        non_empty_string: Optional[str] = None,
        string_less_than_or_equal_to_ten: Optional[str] = None,
        my_blob: Optional[bytes | bytearray] = None,
        non_empty_blob: Optional[bytes | bytearray] = None,
        blob_less_than_or_equal_to_ten: Optional[bytes | bytearray] = None,
        my_list: Optional[list[str]] = None,
        non_empty_list: Optional[list[str]] = None,
        list_less_than_or_equal_to_ten: Optional[list[str]] = None,
        my_map: Optional[dict[str, str]] = None,
        non_empty_map: Optional[dict[str, str]] = None,
        map_less_than_or_equal_to_ten: Optional[dict[str, str]] = None,
        alphabetic: Optional[str] = None,
        one_to_ten: int = 0,
        greater_than_one: int = 0,
        less_than_ten: int = 0,
        my_unique_list: Optional[list[str]] = None,
        my_complex_unique_list: Optional[list[ComplexListElement]] = None,
        my_utf8_bytes: Optional[str] = None,
        my_list_of_utf8_bytes: Optional[list[str]] = None,
    ):
        self.my_string = my_string
        self.non_empty_string = non_empty_string
        self.string_less_than_or_equal_to_ten = string_less_than_or_equal_to_ten
        self.my_blob = my_blob
        self.non_empty_blob = non_empty_blob
        self.blob_less_than_or_equal_to_ten = blob_less_than_or_equal_to_ten
        self.my_list = my_list
        self.non_empty_list = non_empty_list
        self.list_less_than_or_equal_to_ten = list_less_than_or_equal_to_ten
        self.my_map = my_map
        self.non_empty_map = non_empty_map
        self.map_less_than_or_equal_to_ten = map_less_than_or_equal_to_ten
        self.alphabetic = alphabetic
        self.one_to_ten = one_to_ten
        self.greater_than_one = greater_than_one
        self.less_than_ten = less_than_ten
        self.my_unique_list = my_unique_list
        self.my_complex_unique_list = my_complex_unique_list
        self.my_utf8_bytes = my_utf8_bytes
        self.my_list_of_utf8_bytes = my_list_of_utf8_bytes

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetConstraintsOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.my_string is not None:
            d["MyString"] = self.my_string

        if self.non_empty_string is not None:
            d["NonEmptyString"] = self.non_empty_string

        if self.string_less_than_or_equal_to_ten is not None:
            d["StringLessThanOrEqualToTen"] = self.string_less_than_or_equal_to_ten

        if self.my_blob is not None:
            d["MyBlob"] = self.my_blob

        if self.non_empty_blob is not None:
            d["NonEmptyBlob"] = self.non_empty_blob

        if self.blob_less_than_or_equal_to_ten is not None:
            d["BlobLessThanOrEqualToTen"] = self.blob_less_than_or_equal_to_ten

        if self.my_list is not None:
            d["MyList"] = self.my_list

        if self.non_empty_list is not None:
            d["NonEmptyList"] = self.non_empty_list

        if self.list_less_than_or_equal_to_ten is not None:
            d["ListLessThanOrEqualToTen"] = self.list_less_than_or_equal_to_ten

        if self.my_map is not None:
            d["MyMap"] = self.my_map

        if self.non_empty_map is not None:
            d["NonEmptyMap"] = self.non_empty_map

        if self.map_less_than_or_equal_to_ten is not None:
            d["MapLessThanOrEqualToTen"] = self.map_less_than_or_equal_to_ten

        if self.alphabetic is not None:
            d["Alphabetic"] = self.alphabetic

        if self.one_to_ten is not None:
            d["OneToTen"] = self.one_to_ten

        if self.greater_than_one is not None:
            d["GreaterThanOne"] = self.greater_than_one

        if self.less_than_ten is not None:
            d["LessThanTen"] = self.less_than_ten

        if self.my_unique_list is not None:
            d["MyUniqueList"] = self.my_unique_list

        if self.my_complex_unique_list is not None:
            d["MyComplexUniqueList"] = _my_complex_unique_list_as_dict(self.my_complex_unique_list),

        if self.my_utf8_bytes is not None:
            d["MyUtf8Bytes"] = self.my_utf8_bytes

        if self.my_list_of_utf8_bytes is not None:
            d["MyListOfUtf8Bytes"] = self.my_list_of_utf8_bytes

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetConstraintsOutput":
        """Creates a GetConstraintsOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "MyString" in d:
            kwargs["my_string"] = d["MyString"]

        if "NonEmptyString" in d:
            kwargs["non_empty_string"] = d["NonEmptyString"]

        if "StringLessThanOrEqualToTen" in d:
            kwargs["string_less_than_or_equal_to_ten"] = d["StringLessThanOrEqualToTen"]

        if "MyBlob" in d:
            kwargs["my_blob"] = d["MyBlob"]

        if "NonEmptyBlob" in d:
            kwargs["non_empty_blob"] = d["NonEmptyBlob"]

        if "BlobLessThanOrEqualToTen" in d:
            kwargs["blob_less_than_or_equal_to_ten"] = d["BlobLessThanOrEqualToTen"]

        if "MyList" in d:
            kwargs["my_list"] = d["MyList"]

        if "NonEmptyList" in d:
            kwargs["non_empty_list"] = d["NonEmptyList"]

        if "ListLessThanOrEqualToTen" in d:
            kwargs["list_less_than_or_equal_to_ten"] = d["ListLessThanOrEqualToTen"]

        if "MyMap" in d:
            kwargs["my_map"] = d["MyMap"]

        if "NonEmptyMap" in d:
            kwargs["non_empty_map"] = d["NonEmptyMap"]

        if "MapLessThanOrEqualToTen" in d:
            kwargs["map_less_than_or_equal_to_ten"] = d["MapLessThanOrEqualToTen"]

        if "Alphabetic" in d:
            kwargs["alphabetic"] = d["Alphabetic"]

        if "OneToTen" in d:
            kwargs["one_to_ten"] = d["OneToTen"]

        if "GreaterThanOne" in d:
            kwargs["greater_than_one"] = d["GreaterThanOne"]

        if "LessThanTen" in d:
            kwargs["less_than_ten"] = d["LessThanTen"]

        if "MyUniqueList" in d:
            kwargs["my_unique_list"] = d["MyUniqueList"]

        if "MyComplexUniqueList" in d:
            kwargs["my_complex_unique_list"] = _my_complex_unique_list_from_dict(d["MyComplexUniqueList"]),

        if "MyUtf8Bytes" in d:
            kwargs["my_utf8_bytes"] = d["MyUtf8Bytes"]

        if "MyListOfUtf8Bytes" in d:
            kwargs["my_list_of_utf8_bytes"] = d["MyListOfUtf8Bytes"]

        return GetConstraintsOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetConstraintsOutput("
        if self.my_string is not None:
            result += f"my_string={repr(self.my_string)}, "

        if self.non_empty_string is not None:
            result += f"non_empty_string={repr(self.non_empty_string)}, "

        if self.string_less_than_or_equal_to_ten is not None:
            result += f"string_less_than_or_equal_to_ten={repr(self.string_less_than_or_equal_to_ten)}, "

        if self.my_blob is not None:
            result += f"my_blob={repr(self.my_blob)}, "

        if self.non_empty_blob is not None:
            result += f"non_empty_blob={repr(self.non_empty_blob)}, "

        if self.blob_less_than_or_equal_to_ten is not None:
            result += f"blob_less_than_or_equal_to_ten={repr(self.blob_less_than_or_equal_to_ten)}, "

        if self.my_list is not None:
            result += f"my_list={repr(self.my_list)}, "

        if self.non_empty_list is not None:
            result += f"non_empty_list={repr(self.non_empty_list)}, "

        if self.list_less_than_or_equal_to_ten is not None:
            result += f"list_less_than_or_equal_to_ten={repr(self.list_less_than_or_equal_to_ten)}, "

        if self.my_map is not None:
            result += f"my_map={repr(self.my_map)}, "

        if self.non_empty_map is not None:
            result += f"non_empty_map={repr(self.non_empty_map)}, "

        if self.map_less_than_or_equal_to_ten is not None:
            result += f"map_less_than_or_equal_to_ten={repr(self.map_less_than_or_equal_to_ten)}, "

        if self.alphabetic is not None:
            result += f"alphabetic={repr(self.alphabetic)}, "

        if self.one_to_ten is not None:
            result += f"one_to_ten={repr(self.one_to_ten)}, "

        if self.greater_than_one is not None:
            result += f"greater_than_one={repr(self.greater_than_one)}, "

        if self.less_than_ten is not None:
            result += f"less_than_ten={repr(self.less_than_ten)}, "

        if self.my_unique_list is not None:
            result += f"my_unique_list={repr(self.my_unique_list)}, "

        if self.my_complex_unique_list is not None:
            result += f"my_complex_unique_list={repr(self.my_complex_unique_list)}, "

        if self.my_utf8_bytes is not None:
            result += f"my_utf8_bytes={repr(self.my_utf8_bytes)}, "

        if self.my_list_of_utf8_bytes is not None:
            result += f"my_list_of_utf8_bytes={repr(self.my_list_of_utf8_bytes)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetConstraintsOutput):
            return False
        attributes: list[str] = ['my_string','non_empty_string','string_less_than_or_equal_to_ten','my_blob','non_empty_blob','blob_less_than_or_equal_to_ten','my_list','non_empty_list','list_less_than_or_equal_to_ten','my_map','non_empty_map','map_less_than_or_equal_to_ten','alphabetic','one_to_ten','greater_than_one','less_than_ten','my_unique_list','my_complex_unique_list','my_utf8_bytes','my_list_of_utf8_bytes',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

def _my_complex_unique_list_as_dict(given: list[ComplexListElement]) -> List[Any]:
    return [v.as_dict() for v in given]

def _my_complex_unique_list_from_dict(given: List[Any]) -> list[ComplexListElement]:
    return [ComplexListElement.from_dict(v) for v in given]

class Unit:
    pass
