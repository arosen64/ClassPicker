import requests
import json


# MAKES API CALL
def class_api_call(class_number,term,api_key):
    url_base = f'https://sis.jhu.edu/api/classes/{class_number}/{term}?key=' + api_key
    return requests.get(url_base).json()

def time_call(class_number,section_num,DOW,term,api_key):
    url_base = f'https://sis.jhu.edu/api/classes?key={api_key}&CourseNumber={class_number}{section_num}&DaysOfWeek=any|{DOW}&Term={term}'
    return requests.get(url_base).json()

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

# returns a list of the times for a particular class
def get_times(Meetings):
    multipliers = {'M':0, 'T':24*60, 'W':2*24*60, 'Th':3*24*60, 'F':4*24*60}
    times = []
    #looping through the time periods
    for time_period in Meetings:
        time_str = time_period['Times']
        #creating the base start and end times
        start = int(time_str[0:2]) * 60 + int(time_str[3:5])
        end = int(time_str[11:13]) * 60 + int(time_str[14:16])
        #adding to the start and end if PM
        if time_str[6:8] == 'PM':
            start += 12*60
        if time_str[18:20] == 'PM':
            end += 12*60
        for letter_index in range(len(time_period['DOW'])):
            # everything other than Th and T
            if (time_period['DOW'][letter_index] != 'T') and (time_period['DOW'][letter_index].isupper()):
                times.append((start+multipliers[time_period['DOW'][letter_index]],end+multipliers[time_period['DOW'][letter_index]]))
            # checking for Th
            elif (letter_index+1 < len(time_period['DOW'])) and (time_period['DOW'][letter_index].isupper()):
                if time_period['DOW'][letter_index + 1] == 'h':
                    times.append((start+multipliers['Th'],end+multipliers['Th']))
                else:
                    times.append((start+multipliers['T'],end+multipliers['T']))
            # checking for T
            elif (time_period['DOW'][letter_index].isupper()):
                times.append((start+multipliers['T'],end+multipliers['T']))
    return times

# returns percentage of times that overlap
def compare_times(times, comparing_to):
    if len(times) == 0 or len(comparing_to) == 0:
        return 0.0
    times_in_range = 0
    for time_range1 in times:
        for time_range2 in comparing_to:
            if ((time_range1[0] >= time_range2[0]) and time_range1[0] <= (time_range2[1])) or ((time_range1[1] <= time_range2[1]) and time_range1[1] >= (time_range2[0])):
                times_in_range += 1
    return times_in_range/len(times)

def display_times(Meetings):
    for time_period in Meetings:
        print(f'{time_period["Times"]} on {time_period["DOW"]}')

def display_schedule(schedule):
    count = 1
    for clas in schedule:
        print(f'--CLASS {count}--')
        display_times(clas["Meetings"])
        print(f'Taught by {clas["Instructors"]}')
        count += 1
        
    

if __name__ == '__main__':
    api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
    # print(class_api_call('AS110109', 'Spring 2024', api_key))
    #class_data = {'AS110109':[], 'AS180242':[], 'EN601220':[], 'EN601230':[]}
    #read_from_web(class_data,'Spring 2024', api_key)
    # write_data(class_data)
    # class_data = read_from_file()
    #print(class_data)
    #data = [[{'A':[]},{'B':[]},{'C':[]}],[{'1':[]},{'2':[]},{'3':[]}],[{'&':[]},{'@':[]},{'$':[]}]]
    times = [(2070, 2145), (4950, 5025)]
    compare_to = [(2071, 2145), (4950, 5026)]
    print(compare_times(times,compare_to))
    #print(len(all_variations(data,len(data)-1)))