"""Helper functions for main_api_to_df.py"""

import json

def calc_file_size(num_API_requests):
    """Estimates the file size of an API call. Only really needed for large API data requests. Param: number of JSON objects (int) expected from API request. """
    json_file_size_kb = 154/10 # got from test of 100 sample results, stored as a JSON
    pause = 0.5
    # batch_size = 250
    mb_filesize = (num_API_requests*json_file_size_kb)/1000
    
    if mb_filesize < 100:
        judgement = "managable."
    else:
        judgement = "getting chunky."

    print(f"For {num_API_requests} JSON objects, it will take {round(num_API_requests*pause/60,2)} mins to fetch and at {round(json_file_size_kb)} KB per object, total filesize will be {round(mb_filesize)} MB; that's {judgement}")

# calc_file_size(400)


def count_json_items(filepath, json_dict_structure, item_key):
    """ Counts the number of JSON/dictionary keys (at a specified level) in a JSON file. Params: filepath (str), the dictionary structure (list of keys, eg. ['_links','country:items'])  for the target key, and the target key (str, e.g. 'name') to be counted. Returns sentence including number of items. """
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
# filepath = "list_countries.json"
# json_dict_structure = ['_links','country:items']
# item_key = "name"
# # 252
# print(count_json_items(filepath, json_dict_structure, item_key))


def count_keys(filepath):
    """Returns count of keys in a JSON file dictionary"""
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
