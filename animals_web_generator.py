import requests


def fetch_animal_data(animal_name):
    """Fetches animal data from the Ninja API"""
    API_KEY = "gTbcY2BwGi1Gj/oarE+aWg==FWIsZ8CbNm9KwGQN"
    BASE_URL = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(BASE_URL, headers=headers)
    animals_data = response.json()
    return animals_data


def generate_animal_info(animals_data, animal_name):
    """Generates a string with the required information for each animal in HTML format."""
    if not animals_data:
        return f"<h2>the animal '{animal_name}' does not exist.</h2>"

    output = '<ul class="cards">\n'  # Start the unordered list#
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        if 'name' in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'  # Close the list item
    output += '</ul>'  # Close the unordered list
    return output


def replace_template_content(template_path, animals_info, output_path):
    """Replaces the placeholder in the template with the animals info and writes to output file."""
    # Step 1: Read the HTML template file
    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Open a new file (or overwrite if it exists) in write mode
    with open('animals.html', 'w') as output_file:
        # Write the updated content to the file
        output_file.write(updated_content)

    print("The HTML file has been generated successfully.")


def gets_users_animal_input():
    animal_name = input("Enter the animal name: ")
    return animal_name


animal_name = gets_users_animal_input()

animals_data = fetch_animal_data(animal_name)

# Generate the animal information string
animals_info = generate_animal_info(animals_data, animal_name)

# Replace the template content and write to a new file
replace_template_content('animals_template.html', animals_info, 'animals.html')
