import classes
from functions import *

#classes info
api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
term = 'Spring 2024'
class_data = {'AS110109':[], 'AS180242':[], 'EN601220':[], 'EN601230':[]}

#downloading data?
get_mode = True

#get/load data based on download mode
if get_mode:
    class_data = read_from_web(class_data,term,api_key)
    write_data(class_data,'data.json')
else:
    class_data = read_from_file('data.json')

