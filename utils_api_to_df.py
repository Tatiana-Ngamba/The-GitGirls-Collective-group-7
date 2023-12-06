import datetime # fetch, manipulate and format dates
import requests
import pandas as pd
from pandas import json_normalize
import json
import time
from utils_helper import calc_file_size, count_json_items, count_keys

#### Before running this script, your directory must include file utils_helper.py

# If you just want to run all functions in one hit to create a new dataset, use main.py. 

# If instead you only want to run individual functions, uncomment and run the API functions / print functions individually. Functions should always be left commented-out to prevent accidental large API requests, and/or uncontrolled update/overwrite of files.

##########################################################################
"""1) Function makes an API request to retrieve list of countries from Teleport API (country name and url)"""

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


"""2) Check the count of countries retrieved from API. Use this to ensure counter number in next function gets all results, and to pass into the calc_file_size function below, if required."""

filepath = "list_countries.json"
json_dict_structure = ['_links','country:items']
item_key = "name"

# print(count_json_items(filepath, json_dict_structure, item_key)) # 252

##########################################################################
"""3) Function makes an API call to Teleport to add grab overview country level data, including the currency_code which is used in the currency conversion function"""

api_calls_to_make = 252 # this should be number printed above. Set low (i.e. 10 if you only want to do a test run)

def get_overviews_countries(api_calls_to_make): 
    """Grabs currency code, geoname, country code, name & population via Teleport API for each country. Log file entry made for every API request. Appends each JSON object under country-code key to a dictionary, then writes this to a single JSON file at the end."""
    calc_file_size(api_calls_to_make) # num countries 252
    with open("list_countries.json", "r") as countries_list:
        country_list_data = json.load(countries_list)
    
    all_countries_overview_data = {} # empty dict is appended to by each API request

    counter = 0 # counts API requests

    for country in country_list_data['_links']['country:items']:
        if counter < api_calls_to_make+10: # counter can be set low for a test run
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
                    all_countries_overview_data[country_code] = "N/A processing error API"  # Placeholder for omitted overview data due to API process error

                    print(f"Error fetching data for {country_code}, status code: {request_country_overview.status_code}")
                
            except requests.RequestException as e:
                all_countries_overview_data[country_code] = "N/A processing error" # Placeholder for request exceptions
                print(f"Request failed for {country_code}: {e}")

            counter +=1 # increment API request counter 

    # after loop completion, write combined country overview data to file
    with open("overviews_all_countries.json", "w") as file:
        json.dump(all_countries_overview_data, file, indent = 4)

# get_overviews_countries()

""" 4) Counts the number of keys in the JSON dictionary which was just created, holding the salaries data for each country from Teleport. It should match the number of countries you passed into the previous function."""

filepath = "overviews_all_countries.json"
# print(count_keys(filepath)) # returns 252. Matches countries_list


##########################################################################
""" 5) Function makes API request to retrieve country-level salary data from Teleport API. It utilises JSON data retrieved from the previous two API requests. It outputs this as a DataFrame object and a sibling .csv file. Please be patient, takes c30seconds to run."""

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

    # Solution for invalid currency codes
    # Teleport API has outdated currency codes that do not match with those in the currency converter API
    result_df.loc[884:935, 'currency_code'] = 'BYN'
    result_df.loc[6032:6083, 'currency_code'] = 'MRU'
    result_df.loc[10036:10087, 'currency_code'] = 'VES'

    # For checking it works
    # print(result_df.iloc[885])
    # print(result_df.iloc[6035])
    # print(result_df.iloc[10040])

    # Print & convert the final DataFrame to CSV
    # print(result_df)
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
"""6) The following two functions are defined, then run together by calling a third function get_conversion_rates_insert_df(currency). These two have to be bundled, because the output of the first function (a timestamped currency json file) is fed into the creation of the DataFrame, to ensure consistency of the DataFrame."""

def get_gbp_conversion_rates(currency):
    """param: 3 letter currency code, str, required
    Function makes API request to open access exchangerate_api and retrieves JSON object of current exchange rates for passed in currency i.e. "GBP". Outputs a file called currency_rate_{timestamp}.json and a log file."""
    try:
        currency_request = requests.get(f"https://open.er-api.com/v6/latest/{currency}")
        print(f"Status code: {currency_request.status_code}") 
        if currency_request.status_code == 200:
            currency_response = currency_request.json()
            
            if 'rates' in currency_response:               
                request_time = datetime.datetime.now()
                currency_timestamp = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
                currency_rates_filename = f"currency_rates_{currency_timestamp}.json"
                rates_updated = currency_response['time_last_update_unix']
                
                with open(f"{currency_rates_filename}", "w") as currency_conversions:
                    json.dump(currency_response, currency_conversions, indent=4)

                with open("log_currency_rates.txt", "a") as log_currency_rates:
                            log_currency_rates.write(
                            f"{request_time} - Processed {currency} rates last updated at UNIX time {rates_updated}.\n")
            else:
                print(f"Error: 'rates' not in response")       
        else:
            print(f"Error fetching data, {currency_request.status_code}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

    return currency_rates_filename

def convert_salary_to_GBP(currency_rates_filename):
    """Function works directly on output_inc_codes.csv generated above, in conjunction with currency_rate{timestamp}.json to convert the local currency salaries given by Teleport API to GBP. Outputs a new CSV file with extra GBP salary columns and a column showing the conversion rates used. Note, this file is uniquely named with a timestamp to assist with version control."""
    # Load the JSON file with exchange rates
    with open(f'{currency_rates_filename}', 'r') as file:
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

    # The following 4 lambda functions create & populate columns using the API call data

    # Add a timestamped column stating the local to gbp conversion rates used
    df['local_to_gbp_rates'] = df['currency_code'].apply(lambda x: data['rates'].get(x, "N/A"))

    # Apply the conversion to each row (country) for all three salary %iles
    df['gbp_converted_25th'] = df.apply(lambda row: convert_to_gbp(row['salary_percentiles_percentile_25'], row['currency_code']), axis=1)

    df['gbp_converted_50th'] = df.apply(lambda row: convert_to_gbp(row['salary_percentiles_percentile_50'], row['currency_code']), axis=1)

    df['gbp_converted_75th'] = df.apply(lambda row: convert_to_gbp(row['salary_percentiles_percentile_75'], row['currency_code']), axis=1)

    #The iso_alpha2 for Namibia is "NA" however this is being displpayed as a null value.
    #Therefore the location of the Namibia values are labelled "NA".
    df.loc[6552:6603, 'iso_alpha2'] = 'NA'
    #print(df.iloc[6555])

    output_file_timestamp = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
    # Save the updated DataFrame into a new CSV
    df.to_csv(f'output_gbp_salaries_{output_file_timestamp}.csv', index=False)


def get_conversion_rates_insert_df(currency):
    # Call the function to get conversion rates and save them
    currency_rates_filename = get_gbp_conversion_rates(currency)
    # Use the generated file to convert salaries
    convert_salary_to_GBP(currency_rates_filename)

    # NB: once this function has been run and we have output_gbp_salaries_{timestamp}.csv, technically the intermediate file output_inc_codes.csv can be deleted. During development, may be helpful for troubleshooting. If we find no use for the csv at the point of final-code review, we can add a line of code here to delete output_inc_codes.csv from the directory.

##################### RUN THIS ###################

currency = "GBP"
# get_conversion_rates_insert_df(currency)
