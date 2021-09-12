import json


def generate_dictionary(monster_name, title, price, scariness):
    return {'monster_name': monster_name, 'title': title,
            'price': price, 'scariness': scariness}


def write_to_json(dictionary_data):
    with open('monsters.json', 'w') as file:
        json.dump(dictionary_data, file)


if __name__ == '__main__':
    monster_one = generate_dictionary('Filo', 'Baker', 29, 3)
    monster_two = generate_dictionary('Timber', 'Database expert', 3, 4)
    monster_three = generate_dictionary('asdf', 'also asdf', 3, 3)
    write_to_json([monster_one, monster_two, monster_three])
