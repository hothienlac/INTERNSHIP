import json
from count_from_json import CountFromJSON


def main():
    with open('./Squat_Video_.json') as json_file:
        data = json.load(json_file)
    
    count_from_json = CountFromJSON(data)
    print(count_from_json.count())



if __name__ == '__main__':
    main()
