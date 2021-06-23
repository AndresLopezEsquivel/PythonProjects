# Andrés López Esquivel
# 06/22/2021
# PROJECT: FILTERING DATA

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    # Obtaining all python developers
    # all_python_devs = [worker['name'] for worker in DATA if worker["language"] == "python"]
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    # Obtaining all Platzi workers
    # all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    # Obtaining a list of dictionaries with adult people data from DATA
    all_adults = list(filter(lambda person: person["age"] >= 18, DATA))
    # Obtaning a list with the names of adult people from all_adults list
    adults_names = list(map(lambda person: person["name"], all_adults))
    # Creating a new list of dictionaries from DATA but adding a ner key called 'is_adult'
    # With | symbol we can add dictionaries
    people_data = list(map(lambda person: person | {"is_adult": person["age"] >= 18}, DATA))

    print("all_python_devs: ", all_python_devs)
    print("all_platzi_workers: ", all_platzi_workers)
    print("adults_names", adults_names)
    # print("people_data", people_data)


if __name__ == "__main__":
    main()