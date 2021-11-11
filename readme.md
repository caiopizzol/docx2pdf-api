# Docx2pdf API

> A Python based API automagically converts DOCX files into PDFs.

### Files Structure

This is how this repo is structured

```
├── demo    <-- Folder with example files and demo script for testing
│   ├── examples
│       ├── example1.docx
│       ├── example2.docx
│       ├── example3.docx
|   ├── requirements.txt
│   ├── run.py
├── server  <-- OpenAPI server folder        
│   ├── openapi_server
│       ├── __init__.py
│       ├── __main__.py
│       ├── common
│       ├── controllers
│       ├── models
│       ├── openapi     <-- OpenAPI configuration .yaml file 
│       ├── test
│   ├── Dockerfile
└── README.md
```

## Requirements

To locally run the OpenAPI server you should have installed at least `<Docker>` and `<Python3>` with `<pip>` and `<virtualenv>` libs.

Make sure to run this project on a `<Linux>` or `<Mac>` environment.

## Installation

To have the server up and running you should first access the `<server>` folder and run following commands:

- Build Docker image:
```
cd server
docker build -t docx2pdf .
```

- Run Docker container on port 8080
```
docker run --name docx2pdf-container -p 8080:8080 docx2pdf
```

After that you should see the following message on terminal:

```
 * Serving Flask app "__main__" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 ```

## Usage

There are several ways to use the API service that are detailed below:

First create a the virtual environment

- Creating VirtualEnv:
```
python3 -m virtualenv .venv
source .venv/bin/activate
```

### 1. Demo Script

For easier usage, just access the `<demo>` folder and execute the run.py script (make sure to have the created virtualenv activated).

- Accessing folder and installing requirements:
```
cd demo
pip install -r requirements.txt
```

- Running the script:
```
python run.py
```

All converted files should be found on examples folder with same name as the origin file but with the .pdf extension

### 2. Swagger UI / Documentation

Together with the API documentation, it is also possible to simulate the API service through Swagger UI. 

- Open your browser and access the url:

```
http://localhost:8080/v1/ui/
```

You should see something like this:

<img src="https://i.imgur.com/00nYbd0.png" alt="exemplo imagem">

- Authenticate using the provided API key:
```baa1db04-f87c-4b5c-92da-3e39b8e3d1b0```

- Click the **Authorize** button and insert the key:

<img src="https://i.imgur.com/adIsZ1o.png" alt="exemplo imagem">

- Open the /file/convert method and press the **Try it out** button:

<img src="https://i.imgur.com/0DfxRuj.png" alt="exemplo imagem">

- Click **Execute** to the convert base64 docx example provided or change the *fileBase64* payload key.

<img src="https://i.imgur.com/8UCRlyK.png" alt="exemplo imagem">

### 3. cURL

Last but not least, you can also cURL the API endpoint for docx2pdf conversion. To do so, just run the following code on your terminal:

```
curl -X 'POST' \
  'http://localhost:8080/v1/file/convert' \
  -H 'accept: application/json' \
  -H 'api_key: baa1db04-f87c-4b5c-92da-3e39b8e3d1b0' \
  -H 'Content-Type: application/json' \
  -d '{
  "fileBase64": "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",
  "fileType": "DOCX"
}'
```

## Testing

**must have `<libreoffice>` installed** ```brew install --cask libreoffice```

For integration tests you should access the `<test>` folder inside the `<openapi_server>`:

```
cd server/openapi-server/test
```

- Reactivate the created VirtualEnv (in case you deactivated it):
```
source ../../../.venv/bin/activate
```

- Install tox lib and execute it:
```
pip install tox
tox
```

- Final test report:
<img src="https://i.imgur.com/4NNvT1I.png" alt="exemplo imagem">
