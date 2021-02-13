from stubAPI import *
import pytest 
  
def test_pdf_upload(fname):
   assert pdf_upload("input.pdf") == Uploadfile( "/upload/pdf/input", fname)
