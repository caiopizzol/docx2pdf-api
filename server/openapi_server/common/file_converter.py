import os
import re
import sys
import base64
import subprocess
import tempfile

dest_path = f'{os.getcwd()}/tmp/out'

def docx2pdf(encoded_file):
    """Convert DOCX files to PDF using LibreOffice

    :param encoded_file: Base64 encoded DOCX file
    :returns: Base64 encoded PDF file

    """
    ## decodes base64 string
    _file = decode_base64(encoded_file)

    ## creates temp file
    temp = create_temp_file(_file)
    source_path = temp.name

    ## converts temp file using headless libreoffice
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', dest_path, source_path]
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)

    ### checks if files has been converted successfully    
    converted_file = re.search('-> (.*?)', proc.stdout.decode())
    if converted_file is None:
        raise LibreOfficeError(proc.stdout.decode())
    else:
        ## opens converted file and encodes it back to base64
        file_name, file_ext = os.path.splitext(os.path.basename(source_path))
        file_out = open(f'{dest_path}/{file_name}.pdf', 'rb').read()
        return encode_file(file_out)

def libreoffice_exec():
    """Return LibreOffice path according to OS

    :returns: libreoffice CLI command

    """
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'

def decode_base64(data):
    """Decode base64

    :param data: Base64 data as an ASCII string
    :returns: The decoded byte string.

    """
    # return base64.b64decode(data)
    data += "=" * ((4 - len(data) % 4) % 4) #ugh
    return base64.b64decode(data)

def encode_file(_file):
    """Encode file to base64

    :param _file: File document
    :returns: The encoded file as an ASCII string.

    """
    return base64.b64encode(_file).decode('ascii')

def create_temp_file(_file):
    """Create a temp file

    :param _file: File byte string
    :returns: The saved temp file path 

    """
    temp = tempfile.NamedTemporaryFile(mode = 'wb', suffix='.docx')
    temp.write(_file)
    return temp

class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output
