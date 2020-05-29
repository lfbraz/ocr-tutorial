from src.ocr import OCR

IMAGE_PATH = 'images/imagem_1.jpg'
OUTPUT_JSON_PATH = 'output/imagem_1.json'
OUTPUT_IMAGE_PATH = 'output/imagem_1.png'

ocr = OCR()

# Get response
response = ocr.get_extracted_text(image_path=IMAGE_PATH)

# Get full text from response
print(ocr.get_full_text(response))

# Persist the file
ocr.persist_json(OUTPUT_JSON_PATH, response)

# Plot the figure
# TODO: We need to make more tests to plot the original figure with boundingboxes and extracted text
# ocr.plot_figure(response, IMAGE_PATH, OUTPUT_IMAGE_PATH)
