from file_uploader import *
import pytest

def test_upload_file():
	assert upload_file("sample.txt") ==  "You successfully uploaded file"