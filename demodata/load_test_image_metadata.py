import json

def load_test_image_metadata(self):
    # Load test image path from config.json
    with open('./configuration/config.json') as f:
        config = json.load(f)
        return config['test_image']