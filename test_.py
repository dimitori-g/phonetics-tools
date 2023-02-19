import pytest

from utils.utils import parse_unihan_readings


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        (
            0,
            [
                "0x3400",
                "㐀",
                "qiū",
                "jau1",
                None,
                None,
                None,
                "(same as U+4E18 丘) hillock or mound",
            ],
        )
    ],
)
def test_unihan(line: int, expected: list) -> None:
    assert parse_unihan_readings()[line] == expected
