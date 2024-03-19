import requests
import json


# MAKES API CALL
def class_api_call(class_number,term,api_key):
    url_base = f'https://sis.jhu.edu/api/classes/{class_number}/{term}?key=' + api_key
    return requests.get(url_base).json()

def time_call(class_number,section_num,DOW,term,api_key):
    url_base = f'https://sis.jhu.edu/api/classes?key={api_key}&CourseNumber={class_number}{section_num}&DaysOfWeek=any|{DOW}&Term={term}'
    return requests.get(url_base).json()

def read_time():
    print('FIXME: should read a time')
    return 0

def write_data(data_dict,filename):
    json_object = json.dumps(data_dict, indent=4)
    with open(filename, "w") as outfile:
        outfile.write(json_object)
        
def read_from_file(file_name):
    # Opening JSON file
    f = open(file_name)
 
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
 
    # Closing file
    f.close()
    
    return data
    

def read_from_web(data_dict,term,api_key):
    copy_dict = data_dict
    for key in copy_dict:
        copy_dict[key] = class_api_call(key,term,api_key)
        for section in copy_dict[key]:
            add = (time_call(key,section['SectionName'],section['DOW'],term,api_key))
            if len(add):
                section['Meetings'] = add[0]['SectionDetails'][0]['Meetings']
    return copy_dict

def all_variations(lst, index):
    if index < 0:
        return [[]]

    result = []
    for variation in all_variations(lst, index - 1):
        for item in lst[index]:
            result.append(variation + [item])

    return result
    

if __name__ == '__main__':
    api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
    # print(class_api_call('AS110109', 'Spring 2024', api_key))
    #class_data = {'AS110109':[], 'AS180242':[], 'EN601220':[], 'EN601230':[]}
    #read_from_web(class_data,'Spring 2024', api_key)
    # write_data(class_data)
    # class_data = read_from_file()
    #print(class_data)
    data = [[{'A':[]},{'B':[]},{'C':[]}],[{'1':[]},{'2':[]},{'3':[]}],[{'&':[]},{'@':[]},{'$':[]}]]
    
    print(len(all_variations(data,len(data)-1)))