import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
path_to_ini_file = '/'.join([os.getcwd(), 'data/inifile.ini'])


def ADD_DoD(path_to_ini):
    '''
    add up All Dese Definitions into one big Dictionary of Dictionaries
    :param path_to_ini: a path to the file that needs to be parsed
    :return: a dictionary of dictionaries
    '''

    with open(path_to_ini, 'r') as f:
        all_dese_dictionaries = dict()
        current_primary_key = ''
        while True:
            line = f.readline()
            if line == '':
                break
            elif line.startswith('#'):
                pass
            elif line.startswith('['):
                current_primary_key = '{0:s}'.format(line.strip().replace('[', '').replace(']', ''))
                all_dese_dictionaries[current_primary_key] = dict()
            elif current_primary_key is not '' and '=' in line:
                line = line.split(sep='=', maxsplit=1)
                all_dese_dictionaries[current_primary_key][line[0].strip()] = line[1].strip()

    return all_dese_dictionaries

pp.pprint(ADD_DoD(path_to_ini_file))

