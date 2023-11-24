import requests # makes HTTP requests
import json # encodes and decodes JSON data
# import sys # accesses Python interpreter variables e.g. can trigger program exit
import time # moduel to handle time-related tasks e.g. delays
import datetime # fetch, manipulate and format dates
from calc_file_size import calc_file_size

max_cities = 25

def simple_get_list_countries(): # NB 252
    """Grabs list of countries with info available from Teleport API. Log file and JSON file are output."""
    api_base_url = "https://api.teleport.org/api/countries/"
    headers = {"Accept" : "application/vnd.teleport.v1+json"}
    try: 
        request_country_list = requests.get(api_base_url, headers=headers)
        print(f"Status code: {request_country_list.status_code}") #capture this before json parsing
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

                with open("batch_log_countries_list.txt", "a") as log_countries_list:
                    log_countries_list.write(
                    f"{request_time} - Processed {num_results} results from {first_country} to {last_country}.\n")
            else:
                print(f"Error: 'count' not in response")       
        else:
            print(f"Error fetching data, {request_country_list.status_code}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

# simple_get_list_countries()

def get_salaries_countries(): 
    """Grabs premable and salary data for country code via Teleport API. Log file entry made for every API request. Appends each JSON object under country-code key to a dictionary, then writes this to a single JSON file at the end."""
    calc_file_size(252) # num countries 252
    with open("D:\Documents\Computer Study\CURRENT CFG GQ Degree\Group Project\Teleport\list_countries.json", "r") as countries_list:
        country_list_data = json.load(countries_list)
    
    all_countries_salary_data = {} # empty dict is appended to by each API request

    counter = 0 # counts API requests

    for country in country_list_data['_links']['country:items']:
        if counter < 500: # test run first 10 countries
            api_country_url = f"{country['href']}salaries/"
            country_code = api_country_url[-12:-10]  # Extracting 2 letter the country code excluding the /
            print(country_code)
            headers = {"Accept" : "application/vnd.teleport.v1+json"}

            try: 
                request_country_salary = requests.get(api_country_url, headers=headers)
                print(f"Status code: {request_country_salary.status_code}") #capture this before json parsing
                if request_country_salary.status_code == 200:
                    response_country_salary = request_country_salary.json()

                    if 'salaries' in response_country_salary and response_country_salary['salaries']: # checks for salary key, and that the salaries dict isn't empty
                        all_countries_salary_data[country_code] = response_country_salary
                        num_results = len(response_country_salary['salaries'])
                        first_salary = response_country_salary['salaries'][0]['job']['id'] if num_results > 0 else "N/A"
                        last_salary = response_country_salary['salaries'][-1]['job']["id"] if num_results > 0 else "N/A"
                        request_time = datetime.datetime.now()

                        with open("batch_log_country_salaries.txt", "a") as log_country_salaries:
                            log_country_salaries.write(
                            f"API Request: {counter} - Made at {request_time} - For {country_code} - Processed {num_results} results from {first_salary} to {last_salary}.\n")
                        time.sleep(0.5)

                    else:
                        print(f"Error: 'salaries' not in response")       
                else:
                    print(f"Error fetching data, {request_country_salary.status_code}")
            
            except requests.RequestException as e:
                print(f"Request failed: {e}")

            counter +=1 # increment API request counter 

    # after loop completion, write combined country salary data to file
    with open("salaries_all_countries.json", "w") as file:
        json.dump(all_countries_salary_data, file, indent = 4)

#get_salaries_countries()