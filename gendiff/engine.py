import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1:
        data1 = json.load(file1)
    with open(file_path2, 'r') as file2:
        data2 = json.load(file2)

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
