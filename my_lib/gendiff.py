
import json


def generate_diff(file_path1: str, file_path2: str) -> str:

    file1 = get_file(file_path1)
    file2 = get_file(file_path2)

    all_keys = set(file1)
    all_keys.update(file2)
    all_keys = sorted(list(all_keys))
    diff_file = {}

    for key in all_keys:
        is_key_in_file1 = key in file1
        is_key_in_file2 = key in file2

        if is_key_in_file1 and is_key_in_file2:
            val1 = file1[key]
            val2 = file2[key]

            if val1 == val2:
                diff_file[f'  {key}'] = val1
            else:
                diff_file[f'- {key}'] = val1
                diff_file[f'+ {key}'] = val2
        elif is_key_in_file1:
            diff_file[f'- {key}'] = file1[key]
        else:
            diff_file[f'+ {key}'] = file2[key]

    return json.dumps(diff_file, indent=4)


def get_file(file_path: str) -> dict:

    with open(file_path) as file_data:
        return json.load(file_data)

