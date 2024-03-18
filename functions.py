import requests

api_key = 'VEpYM62bVimeAcNhoXDgpE9GRGo9OBFF'
# MAKES API CALL
def class_api_call(class_number,api_key=api_key):
    url_base = 'https://sis.jhu.edu/api/classes/{course_number}/{term}?key='.format(course_number=class_number,term='Fall 2023') + api_key
    return requests.get(url_base).json()

if __name__ == '__main__':
    print(class_api_call('AS001132'))