import json

def load_defaults():
    with open('./configuration/config.json') as f:
        config = json.load(f)
        return config
    
parameters = {
    'ultimage': {
        'version': '1.0.4'
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
    'default_processing': {
        'rotate': 90,
        'mirror': 'horizontal',
        'crop': [0, 50, 0, 100],
        'scale': 1.5,
        'text': 'Hello, World!'
    },
    'default_analysis': {
        'ksize': (5, 5),
        'gauss_sigma': 1.5,
    },
    'group_members': {
        'Gera': 'Parra',
        'Ben': 'Stephenson',
        'Joana': 'Seabra',
        'Farah': 'Abulkhair'
    }
}

if __name__ == '__main__':
    with open('./configuration/config.json', 'w') as f:
        json.dump(parameters, f)