from data_fetcher import fetch_animal_data


def get_user_animal_input():
    return input("Enter the animal name: ")


def generate_animal_info(animals_data, animal_name):
    """Generates a string with the required information for each animal in HTML format."""
    if not animals_data:
        return f"<h2>The animal '{animal_name}' does not exist.</h2>"

    output = '<ul class="cards">\n'
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        if 'name' in animal:
            output += f'<div class="card__title">{animal["name"]}</div>\n'
        output += '<p class="card__text">\n'
        if 'locations' in animal and animal['locations']:
            output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        output += '</p>\n'
        output += '</li>\n'
    output += '</ul>'
    return output


def replace_template_content(animals_info):
    """Replaces the placeholder in the template with the animals info and writes to output file."""
    template_path = 'animals_template.html'
    output_path = 'animals.html'

    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(updated_content)

    print(f"The HTML file has been generated successfully at: {output_path}")


def main():
    # Get the animal name from the user
    animal_name = get_user_animal_input()

    # Fetch data for the specified animal
    animals_data = fetch_animal_data(animal_name)

    # Generate HTML for the animal information
    animals_info = generate_animal_info(animals_data, animal_name)

    # Update the HTML template with the generated animal info
    replace_template_content(animals_info)


if __name__ == "__main__":
    main()
