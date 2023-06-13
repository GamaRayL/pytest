from utils.dicts import *

data = {"key": "value"}


def test_get_val():
    assert get_val(data, "key") == "value"
    assert get_val(data, "key", "git") == "value"
    assert get_val({}, "list") == "git"
    assert get_val({}, "dict", "git") == "git"
    assert get_val({}, "dict", "npm") == "npm"
