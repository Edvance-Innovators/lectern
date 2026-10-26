"""Parser smoke tests. Replace fixture with a real document before relying on these."""
import pytest
from pathlib import Path
from backend.parser import parse_document


def test_parse_missing_file_raises():
    with pytest.raises(Exception):
        parse_document("does_not_exist.pdf")


def test_parse_unsupported_extension():
    with pytest.raises(ValueError):
        parse_document("file.txt")


@pytest.mark.skipif(
    not Path("tests/fixtures/sample_lecture.pdf").exists(),
    reason="Add a sample PDF to tests/fixtures/",
)
def test_parse_sample_pdf():
    chunks = parse_document("tests/fixtures/sample_lecture.pdf")
    assert len(chunks) > 0
    assert all("id" in c and "text" in c for c in chunks)
