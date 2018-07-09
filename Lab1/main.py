from  pprint import pprint
import json


# Main function
def main():
    # Open JSON files
    with open('../Data/example.json') as jsonfile:
        data = json.load(jsonfile)
    
    actions = []
    for element in data['data']:
        for item in element['actions']:
            actions.append(item)
    
    # Print the result
    pprint(actions)


# Main function
if __name__ == "__main__":
    main()