import datetime # fetch, manipulate and format dates
import requests
import pandas as pd
from pandas import json_normalize
import json
import time
from calc_file_size import calc_file_size
from count_json_items import count_json_items, count_keys

##### Before running this script, your directory must include the files:
# calc_file_size.py
# count_json_items.py

# You can run the file all in one hit however it is advised to uncomment and run the functions / print functions individually. Functions should always be left commented out to prevent accidental large API requests.

##########################################################################
"""Function makes an API request to retrieve list of countries from Teleport API (country name and url)"""

def simple_get_list_countries(): # NB 252
    """Grabs list of countries with info available from Teleport API. Log file and JSON file are output."""
    api_base_url = "https://api.teleport.org/api/countries/"
    headers = {"Accept" : "application/vnd.teleport.v1+json"}
    try: 
        request_country_list = requests.get(api_base_url, headers=headers)
        print(f"Status code: {request_country_list.status_code}") 
        if request_country_list.status_code == 200:
            response_country_list = request_country_list.json()

            if 'count' in response_country_list: 
                num_results = response_country_list['count']
                first_country = response_country_list['_links']['country:items'][0]["name"]
                last_country = response_country_list['_links']['country:items'][-1]["name"]
                request_time = datetime.datetime.now()

                grab_country = json.dumps(response_country_list, indent=4)
                with open("list_countries.json", "w") as list_countries:
                    list_countries.write(grab_country)

                with open("log_countries_list.txt", "a") as log_countries_list:
                    log_countries_list.write(
                    f"{request_time} - Processed {num_results} results from {first_country} to {last_country}.\n")
            else:
                print(f"Error: 'count' not in response")       
        else:
            print(f"Error fetching data, {request_country_list.status_code}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

# simple_get_list_countries()

"""Check the count of countries retrieved from API"""

filepath = "list_countries.json"
json_dict_structure = ['_links','country:items']
item_key = "name"

# print(count_json_items(filepath, json_dict_structure, item_key)) # 252

##########################################################################
""" This function makes an API call to Teleport to add grab overview country level data, including the currency_code which is used in the currency conversion function"""

def get_overviews_countries(): 
    """Grabs currency code, geoname, country code, name & population via Teleport API for each country. Log file entry made for every API request. Appends each JSON object under country-code key to a dictionary, then writes this to a single JSON file at the end."""
    calc_file_size(252) # num countries 252
    with open("list_countries.json", "r") as countries_list:
        country_list_data = json.load(countries_list)
    
    all_countries_overview_data = {} # empty dict is appended to by each API request

    counter = 0 # counts API requests

    for country in country_list_data['_links']['country:items']:
        if counter < 400: # test run first 10 countries
            api_country_url = f"{country['href']}"
            country_code = api_country_url[-3:-1]  # Extracting 2 letter the country code
            print(country_code)
            headers = {"Accept" : "application/vnd.teleport.v1+json"}

            try: 
                request_country_overview = requests.get(api_country_url, headers=headers)
                print(f"Status code: {request_country_overview.status_code}") 
                if request_country_overview.status_code == 200:
                    response_country_overview = request_country_overview.json()

                    country_overview = {
                        "currency_code" : response_country_overview.get("currency_code", "N/A"),
                        "geoname_id" : response_country_overview.get("currency_code", "N/A"),
                        "iso_alpha2" : response_country_overview.get("iso_alpha2", "N/A"),
                        "iso_alpha3" : response_country_overview.get("iso_alpha3", "N/A"),
                        "name": response_country_overview.get("name", "N/A"),
                        "population" : response_country_overview.get('population', "N/A"),
                    }

                    all_countries_overview_data[country_code] = country_overview
                    country_name = response_country_overview['name']
                    request_time = datetime.datetime.now()

                    with open("log_country_overviews.txt", "a") as log_country_overviews:
                        log_country_overviews.write(
                        f"API Request: {counter} - Made at {request_time} - For {country_code} - {country_name}.\n")
                    time.sleep(0.5)
    
                else:
                    all_countries_overview_data[country_code] = "N/A procssing error API"  # Placeholder for omitted overview data due to API process error
                    print(f"Error fetching data for {country_code}, status code: {request_country_overview.status_code}")
                
            except requests.RequestException as e:
                all_countries_overview_data[country_code] = "N/A processing error" # Placeholder for request exceptions
                print(f"Request failed for {country_code}: {e}")

            counter +=1 # increment API request counter 

    # after loop completion, write combined country overview data to file
    with open("overviews_all_countries.json", "w") as file:
        json.dump(all_countries_overview_data, file, indent = 4)

# get_overviews_countries()

filepath = "overviews_all_countries.json"
# print(count_keys(filepath)) # returns 252. Matches countries_list


##########################################################################
"""This function makes an API request which retrieves country-level salary data from Teleport API. It utilises JSON data retrieved from the previous two API requests. It outputs this as a DataFrame object and a sibling .csv file. Please be patient, takes c30seconds to run."""

def api_to_dataframe():
    # Load country list data for API call from existing JSON file
    with open("list_countries.json", "r") as countries_list:
        country_list_data = json.load(countries_list)

    # Load currency_code from existing JSON file
    with open("overviews_all_countries.json", "r") as overviews_countries:
        currency_data = json.load(overviews_countries)

    # Map country_code to currency_code (country_code key is common to both json files)
    currency_mapping = {country['iso_alpha2']: country['currency_code'] for country in currency_data.values()}

    cc = []
    # Iterate over countries to extract country codes
    for country in country_list_data['_links']['country:items']:
        api_country_url = f"{country['href']}salaries/"
        country_code = api_country_url[-12:-10] # Extracting 2 letter the country code excluding the /
        cc.append(country_code)

    print(cc)
    url = "https://api.teleport.org/api/countries/iso_alpha2:{}/salaries"
    dfs = []

    # Iterate over the list of country codes
    for country_code in cc:
        # Construct the API endpoint URL for the current country_code
        api_endpoint = url.format(country_code)
        # Make a GET request to the API
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            api_data = response.json()
            salaries_data = api_data.get('salaries', [])
            currency_code = currency_mapping.get(country_code, "Unknown")
            
            df = json_normalize(salaries_data, sep='_')
            if not df.empty:
                # Add two extra columns with country_code and currency_code
                df['iso_alpha2'] = country_code
                df['currency_code'] = currency_code
                dfs.append(df)

        else:
            print(f"Error: {response.status_code}")

    # Concatenate the data retrieved from the API calls into result DataFrame
    result_df = pd.concat(dfs, ignore_index=True)

    # Print & convert the final DataFrame to CSV
    print(result_df)
    result_df.to_csv('output_inc_codes.csv', index=False)

# api_to_dataframe()

##########################################################################
def get_gbp_conversion_rates(currency):
    """param: 3 letter currency code, str, required
    Function makes API request to open access exchangerate_api and retrieves JSON object of current exchange rates for passed in currency i.e. "GBP". Outputs a file called currency_rate.json and a log file."""
    try:
        currency_request = requests.get(f"https://open.er-api.com/v6/latest/{currency}")
        print(f"Status code: {currency_request.status_code}") 
        if currency_request.status_code == 200:
            currency_response = currency_request.json()
            
            if 'rates' in currency_response:               
                request_time = datetime.datetime.now()
                rates_updated = currency_response['time_last_update_unix']
                
                with open("currency_rate.json", "w") as currency_conversions:
                    json.dump(currency_response, currency_conversions, indent=4)

                with open("log_currency_rates.txt", "a") as log_currency_rates:
                            log_currency_rates.write(
                            f"{request_time} - Processed {currency} rates last updated on {rates_updated}.\n")
            else:
                print(f"Error: 'rates' not in response")       
        else:
            print(f"Error fetching data, {currency_request.status_code}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

# get_gbp_conversion_rates("GBP")

##########################################################################
"""Function works directly on output_inc_codes.csv generated above, in conjunction with currency_rate.json to convert the local currency salaries given by Teleport API to GBP. Outputs a new CSV file with the extra GBP salary columns."""

def convert_salary_to_GBP():
    # Load the JSON file with exchange rates
    with open('currency_rate.json', 'r') as file:
        data = json.load(file)
    exchange_rates = data['rates']

    # Load CSV with the salary data to be converted
    df = pd.read_csv('output_inc_codes.csv') # use DataFrame from CSV

    # Function to convert currency to GBP
    def convert_to_gbp(amount, currency_code):
        rate = exchange_rates.get(currency_code, None)
        if rate:
            return amount / rate
        else:
            return "N/A" # Return "N/A" for missing exchange rate

    # Apply the conversion to each row (country) for all three salary %iles
    df['gbp_converted_25th'] = df.apply(lambda row: convert_to_gbp(row['salary_percentiles_percentile_25'], row['currency_code']), axis=1)

    df['gbp_converted_50th'] = df.apply(lambda row: convert_to_gbp(row['salary_percentiles_percentile_50'], row['currency_code']), axis=1)

    df['gbp_converted_75th'] = df.apply(lambda row: convert_to_gbp(row['salary_percentiles_percentile_75'], row['currency_code']), axis=1)

    # Save the updated DataFrame into a new CSV
    df.to_csv('output_gbp_salaries.csv', index=False)

# convert_salary_to_GBP()