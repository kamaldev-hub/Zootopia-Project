import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def print_animal_info(animals_data):
    """ Prints the required information for each animal """
    for animal in animals_data:
        if 'name' in animal:
            print(f"Name: {animal['name']}")
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")
        # Assuming that 'locations' always exists and is non-empty
        print(f"First Location: {animal['locations'][0]}")
        #if 'characteristics' in animal and 'type' in animal['characteristics']:
            #print(f"Type: {animal['characteristics']['type']}")
        print("-" * 20)  # Separator for each animal's information


print(print_animal_info(animals_data))