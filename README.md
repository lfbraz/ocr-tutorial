# OCR using Azure Cognitive Services **(Computer Vision API)**
This implementation is for learning purposes. The class ocr.py could be used to extract text from images (OCR) using the Azure Computer Vision REST API.

Could be used in a lot of scenarios to help extract valuable information from images.
Use your creativity to expand the use ~~to have fun~~ to fix a lot of real world problems and feel free to clone this repo and adapt this code for your requirements :)

This tutorial was inspired from [Microsoft Oficial Quickstart Tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-print-text).

## [Activate environment](https://pipenv.readthedocs.io/en/latest/)
Pipenv will install all the libraries required automatically.
`pipenv shell`

## Flake8 config
Use the bellow code to adjust the max line length limit
flake8 --max-line-length=140

If you use VSCode you can add this config to settings.json adding the code:

```
"python.linting.flake8Args": [
        "--max-line-length=140",
    ]
```

## Set environment variables
### You can find API Key in Quick start section of your API on Azure Portal
`export COMPUTER_VISION_SUBSCRIPTION_KEY=<KEY_1>`
### You can find API endpoint in Quick start section of your API on Azure Portal
`export COMPUTER_VISION_ENDPOINT=<COMPUTER_VISION_ENDPOINT>`


## How to run
Run `run.py` and change the variables `IMAGE_PATH`, `OUTPUT_JSON_PATH` and `OUTPUT_IMAGE_PATH`.

**IMAGE_PATH**: is the path of the image that will be used to extract the text from its content

**OUTPUT_JSON_PATH** : is the path to the json file generated from the OCR process

**OUTPUT_IMAGE_PATH**: is the path of the image with the _boundingBoxes_
_TODO: Need to make more tests (I know that is not working in images with multiple pages)_

## Clean up resources
To clean up resources you can delete the Resource Group or the API using Azure Portal.
