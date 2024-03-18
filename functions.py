import requests

api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
# MAKES API CALL
def class_api_call(class_number,term,api_key=api_key):
    url_base = 'https://sis.jhu.edu/api/classes/{course_number}/{term}?key='.format(course_number=class_number,term=term) + api_key
    return requests.get(url_base).json()

def read_time():
    print('FIXME: should read a time')
    return 0

if __name__ == '__main__':
    print(class_api_call('AS001132', 'Fall 2024'))