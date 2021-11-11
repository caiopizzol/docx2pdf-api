import requests
import json
import base64
import subprocess
import tempfile
import os.path

"""
Demo script to test end-to-end API usage

"""

## Searching for example DOCX files
print('# Iterating example DOCX files\n')
examples_path = f'{os.getcwd()}/examples'
for _file in os.listdir(examples_path):
       
    if _file.endswith(".docx"):
        print(_file)
        ## Enconding file into base64
        print('> Enconding file into base64')
        in_file = open(os.path.join(examples_path, _file), 'rb').read()
        in_file_encoded = base64.b64encode(in_file).decode('ascii')

        ## Requesting docx2pdf conversion to API
        print('> Requesting docx2pdf conversion to API')
        url = 'http://localhost:8080/v1/file/convert'
        api_key = 'baa1db04-f87c-4b5c-92da-3e39b8e3d1b0'

        headers = {"api_key": api_key, "Content-Type": "application/json"}
        data = {
          "fileBase64": in_file_encoded,
          "fileType": "DOCX"
        }

        r = requests.request("POST", url, headers=headers, data=json.dumps(data))
        print(r)
        response = r.json()
        
        ## Decoding base64 response and saving into a file
        print('> Decoding base64 response and saving into a file\n')
        out_file_decoded = base64.b64decode(response['file_base64'])

        with open(f'{examples_path}/{os.path.splitext(_file)[0]}.pdf', 'wb') as f:
            f.write(out_file_decoded)
            f.close()

print('# Process ended.')        

