import re

def get_config():
    with open('../config','r',encoding='utf8')as f:
        lines = f.readlines()
    config_dict = {}
    for line in lines:
        match = re.search(r'(?P<key>.*\b)\s*=\s*(?P<val>\b.*)',line)
        if match:
            config_dict[match['key'].strip()] = match['val'].strip()
    with open('../data/config.py','w')as f:
        f.write('config=')
        f.write(str(config_dict))
