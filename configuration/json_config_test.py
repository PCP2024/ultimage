import json

parameters = {
    'ultimage': {
        'version': '1.0.3'
    },
    'test_image': {
        'path': './demodata/test.png',
        'dimensions': (99, 150, 3)
    },
    'default_font': {
        'font': './demodata/impact.ttf',
        'color': '#ffffff',
        'size': 15,
        'coordinates': (10, 10)
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