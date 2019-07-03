import requests # .get()
import xlwt     # create excel spreadsheets
import sys      # .exit()
import datetime # datetime
import os       # .remove()

# Configure AirTable authentication
at_url = open("airtable_url.txt", "r")
airtable_api_key = open("airtable_config.txt", "r")
AIRTABLE_URL = at_url.read()
headers = {"Authorization": "Bearer " + airtable_api_key.read()}
at_url.close()
airtable_api_key.close()

# Retrieve AirTable data
res = requests.get(AIRTABLE_URL, headers=headers)
if res.status_code != 200:
    print("Error: status code", res.status_code, "\nExiting...")
    sys.exit()

# Create xlwt workbook
wb = xlwt.Workbook()
ws = wb.add_sheet("Resume Backup");

# Write data into corresponding columns
excel_header_dictionary = {}
count = 1
headers = 0
for record in res.json()['records']:
    for k, v in record['fields'].items():
        if k not in excel_header_dictionary:
            # Add headers to dictionary and write to excel file
            excel_header_dictionary.update({k : headers})
            ws.write(0, headers, k)
            headers += 1
        ws.write(count, excel_header_dictionary[k], v)
    count += 1

# Create name of backup file with timestamp and save
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
file_name = "Backup_test_" + time_stamp + ".xls"
wb.save(file_name)

# Login to Box
from boxsdk import JWTAuth
from boxsdk import Client
# Import JWT auth object with config file
sdk = JWTAuth.from_settings_file('box_config.json')
client = Client(sdk) # authenticated client

file_path = file_name
# Get folder ID
f_id = open("box_folder_id.txt", "r")
folder_id = f_id.read()
f_id.close()
box_file = client.folder(folder_id).upload(file_path, file_name) # upload backup to backup folder on Box

# After upload, remove from local directory
os.remove(file_name)
