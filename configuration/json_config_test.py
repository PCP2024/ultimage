import json

parameters = {
    'test_image': {
        'path': './demo_data/test.png'
    },
    'group_members': {
        'Gera': 'Parra',
        'Ben': 'Stephenson',
        'Joana': 'Seabra',
        'Farah': 'Abulkhair'
    }
}

with open('./configuration/config.json', 'w') as f:
    json.dump(parameters, f)