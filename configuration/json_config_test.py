import json

parameters = {
    'ultimage': {
        'version': '1.0.2'
    },
    'test_image': {
        'path': './demodata/test.png',
        'dimensions': (99, 150, 3)
    },
    'defaults': {
        'font': './demodata/impact.ttf',
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