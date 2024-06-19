import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def generate_animal_info(animals_data):
    """Generates a string with the required information for each animal in HTML format."""
    output = '<ul class="cards">\n'  # Start the unordered list
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        if 'name' in animal:
            output += f"Name: {animal['name']}<br/>\n"
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"Location: {animal['locations'][0]}<br/>\n"
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


# Generate the animal information string
animals_info = generate_animal_info(animals_data)

# Replace the template content and write to a new file
replace_template_content('animals_template.html', animals_info, 'animals.html')