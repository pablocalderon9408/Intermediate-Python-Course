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
]

def run():
    all_python_devs = [devs['name'] for devs in DATA if devs['language'] == 'python']
    all_platzi_workers = [ platzi_workers['name'] for platzi_workers in DATA if platzi_workers['organization'] == 'Platzi']
    adults = list(filter(lambda devs: devs['age'] > 18, DATA))
    adults = list(map(lambda devs: devs['name'] ,adults))
    old_people = list(map(lambda devs: devs | {'old': devs['age']>70}, DATA))
    print(all_python_devs, all_platzi_workers, adults)
    print(old_people)

if __name__ == '__main__':
    run()    