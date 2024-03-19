import classes
from functions import *

#classes info
api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
term = 'Spring 2024'
class_data = {'AS110109':[], 'AS110110':[], 'AS180242':[], 'EN601220':[], 'EN601230':[]}
combos= [('AS110109','AS110110')]

#downloading data?
get_mode = False

#get/load data based on download mode
if get_mode:
    class_data = read_from_web(class_data,term,api_key)
    write_data(class_data,'data.json')
else:
    class_data = read_from_file('data.json')

#combine combo classes
if len(combos):
    for combo in combos:
        new_data = []
        combo_string = ''
        for class_num in combo:
            new_data += class_data[class_num]
            del class_data[class_num]
            combo_string += class_num + '-'
        class_data[combo_string] = new_data


