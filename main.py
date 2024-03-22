import classes
from functions import *

#classes info
preferences = get_preferences('preferences.json')
api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
term = preferences["term"]
class_data = preferences["classes"]
combos= []

#weights
time_weight = int(preferences["time weight"])/100
professor_weight = int(preferences["professor weight"])/100
seat_weight = int(preferences["seat weight"])/100

#acceptable times and professors
g_times = preferences["good times"]
g_profs = []

#downloading data?
get_mode = int(preferences["get mode"])

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

#putting all data into a list
all_schedules = []

for key in class_data:
    all_schedules.append(class_data[key])

#creating every variation of the classes
all_schedules = all_variations(all_schedules, len(all_schedules)-1)
#print(len(all_schedules))

schedules_and_scores = []

#TESTS
#print(get_times(all_schedules[0][0]['Meetings']))
#print(all_schedules[0][0]['Meetings'])

# calculating scores and eliminating schedules that don't work
for schedule in all_schedules:
    times = is_valid_schedule(schedule, preferences)
    if len(times):
        score = score_schedule(time_weight,seat_weight,professor_weight,g_times,g_profs,times,schedule)
        schedules_and_scores.append((schedule, score))

        
    
schedules_and_scores = sorted(schedules_and_scores, key=lambda x: x[1], reverse=True)
print(len(schedules_and_scores))
for i in range(len(schedules_and_scores)):
    print(f'score: {schedules_and_scores[i][1]}')
    display_schedule(schedules_and_scores[i][0])
    input("")
    
    
        
        
    
    


