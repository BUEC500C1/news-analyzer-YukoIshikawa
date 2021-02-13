

def file_validation(fname, ftype):
  allowed_ftype = ['pdf', 'csv', 'docx', 'txt']
  if fname == "": 
    return "Failure: No file selected"
  if ftype not in allowed_ftype:
    return "Failure: Not allowed file type"
  return [fname, ftype]

def pdf_upload(fname):
  if fname == "": return "Failure: No file selected"
  
  file_path = $WORKSPACE + 'upload/pdf/' + fname
  return Uploadfile(file_path, fname)

def docx_upload(fname):
  file_path = $WORKSPACE + 'upload/docx/' + fname
  return Uploadfile(file_path, fname)

def csv_upload(fname):

def txt_upload(fname):

def upload_status():

def file_upload(fname):
  



