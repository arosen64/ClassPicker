import requests
import json


# MAKES API CALL
def class_api_call(class_number,term,api_key):
    url_base = 'https://sis.jhu.edu/api/classes/{course_number}/{term}?key='.format(course_number=class_number,term=term) + api_key
    return requests.get(url_base).json()

def read_time():
    print('FIXME: should read a time')
    return 0

def write_data(data_dict):
    json_object = json.dumps(data_dict, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
        
def read_from_file():
    print('FIXME: should read class data from json file')
    return 0

def read_from_web(data_dict,term,api_key):
    for key in data_dict:
        data_dict[key] = class_api_call(key,term,api_key)

if __name__ == '__main__':
    api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
    # print(class_api_call('AS110109', 'Spring 2024', api_key))
    # class_data = {'AS110109':[], 'AS180242':[], 'EN601220':[], 'EN601230':[]}
    # read_from_web(class_data,'Spring 2024', api_key)
    # write_data(class_data)