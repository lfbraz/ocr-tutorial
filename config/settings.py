import os

# Set the environment variables with your key and endpoint as the value.
# This key will serve all examples in this document.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ and 'COMPUTER_VISION_ENDPOINT' in os.environ:
    KEY = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    ENDPOINT = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the environment variables.\n**Restart your shell or IDE for changes to take effect.**")
