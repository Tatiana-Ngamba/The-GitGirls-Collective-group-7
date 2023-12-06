"""Only run this script if you want to create a full fresh dataset. Otherwise, run selected functions individually from utils_api_to_df.py"""

from utils_helper import count_json_items, count_keys
from utils_api_to_df import simple_get_list_countries, get_overviews_countries,api_to_dataframe, get_conversion_rates_insert_df

#### Before running this script, your directory must include the files:
# utils_api_to_df.py
# utils_helper.py

""" 1) Function makes an API request to retrieve list of countries from Teleport API (country name and url)"""
simple_get_list_countries()


""" 2) Check the count of countries retrieved from API. Use this to ensure counter number in next function gets all results, and to pass into the calc_file_size function below, if required."""

filepath = "list_countries.json"
json_dict_structure = ['_links','country:items']
item_key = "name"

print(count_json_items(filepath, json_dict_structure, item_key))

""" 3) Function makes an API call to Teleport to add grab overview country level data, including the currency_code which is used in the currency conversion function. Please be patient, takes a minute to run."""

api_calls_to_make = 252 # this should be number printed above. Set low (i.e. 10 if you only want to do a test run)
get_overviews_countries(api_calls_to_make)


""" 4) Counts the number of keys in the JSON dictionary which was just created, holding the salaries data for each country from Teleport. It should match the number of countries you passed into the previous function."""

filepath = "overviews_all_countries.json"
print(count_keys(filepath)) # should return 252 to matches countries_list

""" 5) Function makes API request to retrieve country-level salary data from Teleport API. It utilises JSON data retrieved from the previous two API requests. It outputs this as a DataFrame object and a sibling .csv file. Please be patient, takes c30seconds to run."""

api_to_dataframe()

""" 6) The following calls two functions one after the other to produce our final DataFrame which has country info, currency info, conversion rates, and converted salaries."""
currency = "GBP"
get_conversion_rates_insert_df(currency)


#### After running this script, you should end up with:
# From 1), list_countries.json & log_list_countries.txt
# From 3), overviews_all_countries.json & log_countries_overviews.txt
# From 5), output_inc_codes.csv. This is an intermediate file and can be deleted
# From 6) currency_rates_{timestamp}.json, output_gbp_salaries_{timestamp}.csv and log_currency_rates.txt


""" output_gbp_salaries_{timestamp}.csv is the file to use in Jupyter Notebooks for data analysis. Have fun!"""