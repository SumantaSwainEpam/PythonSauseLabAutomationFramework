import yaml
import os

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'config', 'testdata.yaml')

    with open(file_path, "r") as file:
        return yaml.safe_load(file)
