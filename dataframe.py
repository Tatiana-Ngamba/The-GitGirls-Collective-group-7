
import datetime # fetch, manipulate and format dates
import requests
import pandas as pd
from pandas import json_normalize
import json


def simple_get_list_countries(): # NB 252
    """Grabs list of countries with info available from Teleport API. Log file and JSON file are output."""
    api_base_url = "https://api.teleport.org/api/countries/"
    headers = {"Accept" : "application/vnd.teleport.v1+json"}
    try:
        request_country_list = requests.get(api_base_url, headers=headers)
        print(f"Status code: {request_country_list.status_code}") #capture this before json parsing
        if request_country_list.status_code == 200:
            response_country_list = request_country_list.json()
            print(response_country_list)

            if 'count' in response_country_list:
                num_results = response_country_list['count']
                first_country = response_country_list['_links']['country:items'][0]["name"]
                last_country = response_country_list['_links']['country:items'][-1]["name"]
                request_time = datetime.datetime.now()

                grab_country = json.dumps(response_country_list, indent=4)
                with open("list_countries.json", "w") as list_countries:
                    list_countries.write(grab_country)

                with open("batch_log_countries_list.txt", "a") as log_countries_list:
                    log_countries_list.write(
                    f"{request_time} - Processed {num_results} results from {first_country} to {last_country}.\n")
            else:
                print(f"Error: 'count' not in response")
        else:
            print(f"Error fetching data, {request_country_list.status_code}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

simple_get_list_countries()


with open("list_countries.json", "r") as countries_list:
    country_list_data = json.load(countries_list)

all_countries_salary_data = {}  # empty dict is appended to by each API request
counter = 0
cc = []
for country in country_list_data['_links']['country:items']:
    if counter < 500:  # test run first 10 countries
        api_country_url = f"{country['href']}salaries/"
        country_code = api_country_url[-12:-10] # Extracting 2 letter the country code excluding the /
    cc.append(country_code)

print(cc)
url = "https://api.teleport.org/api/countries/iso_alpha2:{}/salaries"

dfs = []
i=0
# Iterate over the list of country codes
for element in cc:
    # Construct the API endpoint URL for the current country
    api_endpoint = url.format(cc[i])

    # Make a GET request to the API
    response = requests.get(api_endpoint)



    if response.status_code == 200:
        api_data = response.json()
        salaries_data = api_data.get('salaries', [])

        df = json_normalize(salaries_data, sep='_')
        if not df.empty:
            # Add an extra column with the country code
            df['iso_alpha2'] = cc[i]

        dfs.append(df)


    else:
        print(f"Error: {response.status_code}")

    i=i+1

result_df = pd.concat(dfs, ignore_index=True)

# Print the final DataFrame
print(result_df)
result_df.to_csv('output.csv', index=False)