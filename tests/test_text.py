# -*- coding: utf-8 -*-
import pytest

import iscc_sdk as idk


def test_text_meta_extract_pdf(pdf_file):
    assert idk.text_meta_extract(pdf_file) == {"name": "title from metadata"}


def test_text_meta_extract_docx(docx_file):
    assert idk.text_meta_extract(docx_file) == {"creator": "titusz", "name": "title from metadata"}


def test_text_meta_extract_epub(epub_file):
    assert idk.text_meta_extract(epub_file) == {
        "name": "Children's Literature",
        "creator": "Charles Madison Curry, Erle Elsworth Clippinger",
        "rights": "Public domain in the USA.",
    }


def test_text_extract_pdf(pdf_file):
    text = idk.text_extract(pdf_file)
    assert text.strip().startswith("Bitcoin: A Peer-to-Peer Electronic Cash System")


def test_text_extract_empty(tmp_path):
    fp = tmp_path / "empty.txt"
    fp.write_text(" \n")
    with pytest.raises(idk.IsccExtractionError):
        idk.text_extract(fp)


def test_text_extract_docx(docx_file):
    text = idk.text_extract(docx_file)
    assert text.strip().startswith("ISCC Test Document")


def test_text_name_from_uri(jpg_file):
    assert idk.text_name_from_uri("http://example.com") == "example"
    assert idk.text_name_from_uri("http://example.com/some-file.txt") == "some file"
    assert idk.text_name_from_uri("http://example.com/some_file.txt?q=x") == "some file"
    assert idk.text_name_from_uri(jpg_file) == "img"
