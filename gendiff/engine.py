import json
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from pathlib import Path


def generate_diff(file_path1, file_path2):    # noqa: C901
    with open(file_path1, 'r') as file1:
        if Path(file_path1).suffix == '.json':
            data1 = json.load(file1)
        elif Path(file_path1).suffix == '.yaml' \
                or Path(file_path1).suffix == '.yml':
            data1 = yaml.load(file1, Loader=Loader)
        else:
            print("Error: uncorrect extension in file! \
                  (not *.json, *.yaml, *.yml)")
            # TODO нужно остановить выполнение скрипта!
    with open(file_path2, 'r') as file2:
        if Path(file_path2).suffix == '.json':
            data2 = json.load(file2)
        elif Path(file_path2).suffix == '.yaml' \
                or Path(file_path2).suffix == '.yml':
            data2 = yaml.load(file2, Loader=Loader)
        else:
            print("Error: uncorrect extension in file! \
                  (not *.json, *.yaml, *.yml)")
            # TODO нужно остановить выполнение скрипта!

    sort_list_1 = sorted(data1)  # sorted key list in json file1
    sort_list_2 = sorted(data2)
    set2 = set(sort_list_2).difference(sort_list_1)
    sort_list_2 = sorted(list(set2))  # sorted uniqe keys in json file2

    result_list = ['{']  # make result list
    for key in sort_list_1:
        if key not in data2:
            result_list.append(f'  - {key}: {data1.get(key)}')
        elif key in data2 and data1[key] == data2[key]:
            result_list.append(f'    {key}: {data1.get(key)}')
        elif key in data2 and data1[key] != data2[key]:
            result_list.append(f'  - {key}: {data1.get(key)}')
            result_list.append(f'  + {key}: {data2.get(key)}')

    for key in sort_list_2:
        result_list.append(f'  + {key}: {data2.get(key)}')
    result_list.append('}')

    final_list = [x.lower() for x in result_list]

    final_string = "\n".join(final_list)   # make diff in str
    return final_string
