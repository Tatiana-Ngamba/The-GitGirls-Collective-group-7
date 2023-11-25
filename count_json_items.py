import json

def count_json_items(filepath, json_dict_structure, item_key):
    """takes filepath, the dictionary key structure, and the key to be counted as parameters. Returns sentence including number of items."""
    try: 
        with open(filepath, "r") as json_file:
            json_data = json.load(json_file)

        for key in json_dict_structure:
            json_data = json_data[key]

        num_entries = sum(item_key in item for item in json_data)

        return f"The number of entries under '{item_key}' key in this JSON file is {num_entries}"
        
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except KeyError as e:
        print(f"Key error: {e}")

# Test params
# filepath = "D:\Documents\Computer Study\CURRENT CFG GQ Degree\Group Project\Teleport\list_countries.json"
# json_dict_structure = ['_links','country:items']
# item_key = "name"
# # 252
# print(count_json_items(filepath, json_dict_structure, item_key))


def count_keys(filepath):
    """ Function return count of keys in a JSON file dictionary"""
    try:
        with open(filepath, "r") as json_file:
            json_data = json.load(json_file)

        num_keys = len(json_data.keys())
        print("Keys found:", list(json_data.keys()))  # For debugging

        return f"The number of top-level keys in this JSON file is {num_keys}"
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except KeyError as e:
        print(f"Key error: {e}")
