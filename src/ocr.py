import config.settings as conf
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
import json


class OCR():
    '''
    Interact with Azure Computer Vision API:
    '''

    def __init__(self):
        '''
        Init class
        '''
        self.subscription_key = conf.KEY
        self.endpoint = conf.ENDPOINT

    def get_payload_parameters(self):
        '''
        Build the payload with parameters settings
        '''
        # Set Content-Type to octet-stream
        headers = {'Ocp-Apim-Subscription-Key': self.subscription_key,
                   'Content-Type': 'application/octet-stream'}

        ocr_url = self.endpoint + "vision/v2.1/ocr"

        params = {'language': 'ukn', 'detectOrientation': 'true'}
        return ocr_url, headers, params

    @staticmethod
    def get_word_infos(response):
        '''
        Extract word infos list

        Parameters:
            response: Response Object
                Response from the REST API

        Returns:
            word_infos: list
                Returns the word_infos (words and boundingbox) extracted from the response
        '''
        analysis = response.json()

        # Extract the word bounding boxes and text.
        line_infos = [region["lines"] for region in analysis["regions"]]
        word_infos = []
        for line in line_infos:
            for word_metadata in line:
                for word_info in word_metadata["words"]:
                    word_infos.append(word_info)

        return word_infos

    def plot_figure(self, response, image_path, image_output):
        '''
        Plot the figure with bouding boxes and the text extracted

        Parameters:
            response: Response Object
                Response from the REST API
            word_infos: list
                list with the words and the boundingbox associated with it
            image_path: string
                Path of the image to be used in the OCR process
            image_output: string
                Path to output the image with boundingbox and extracted text
        '''
        word_infos = self.get_word_infos(response)

        plt.figure(figsize=(25, 25))

        # Read the image into a byte array
        image_data = Image.open(BytesIO(open(image_path, "rb").read()))

        ax = plt.imshow(image_data, alpha=0.5)

        for word in word_infos:
            bbox = [int(num) for num in word["boundingBox"].split(",")]
            text = word["text"]
            origin = (bbox[0], bbox[1])
            patch = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
            ax.axes.add_patch(patch)
            plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")

        plt.savefig(image_output)

    def get_full_text(self, response):
        '''
        Extract consolidated text from response

        Parameters:
            response: Object
                Response from the REST API

        Returns:
            full_text: string
                Returns the full text extracted from the response
        '''
        word_infos = self.get_word_infos(response)

        full_text = ''
        for word in word_infos:
            full_text += word['text'] + ' '

        return full_text

    @staticmethod
    def persist_json(output_path, response):
        '''
        Persist the json file

        Parameters:
            output_path: string
                Path of json file
            response: Object
                Response from the REST API
        '''
        json_file = open(output_path, 'w')

        json_response = response.json()
        json_file.write(json.dumps(json_response, ensure_ascii=False))

    def get_extracted_text(self, image_path):
        '''
        Extract text data from images

        Parameters:
            image_path: string
                Path of the image to be used in the OCR process
        '''

        # Read the image into a byte array
        image_data = open(image_path, "rb").read()

        ocr_url, headers, params = self.get_payload_parameters()

        # put the byte array into your post request
        response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
        return response
