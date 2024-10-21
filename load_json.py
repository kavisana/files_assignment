import json

def load_json():
    file_path = "C:/Users/user/OneDrive/Documents/GitHub/files_assignment/Keerthana_Avisana_adoptions.json"

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except json.JSONDecodeError:
        print("JSON file could not be read.")
