import json
import pprint

def parse_json(filename):
    '''This function reads JSON file and prints some information from that file
    and returns it.'''

    f = open('example.json', encoding='utf-8')
    ff = json.load(f)
    username, user_id = ff['user'],  ff['id']
    print('ID of user {} is {}'.format(username, user_id))

    f.close()

    return username, user_id

if __name__ == '__main__':
    parse_json('example.json')
