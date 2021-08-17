import os
import pandas as pd
import json


def json_load(json_path, dir):
    pathed = os.path.normpath(json_path)
    with open(dir +'/' + pathed, 'r') as f:
        loaded = json.load(f)
        return loaded

def json_to_df(directory_path):
    list_df = []
    for file in os.listdir(directory_path):
        if file.endswith('.json'):
            loaded = json_load(file, directory_path)
            list_df.append(pd.DataFrame(loaded['results']))
            # there are multiple types of data in your json file so you have to pick which group
            # of data. Cause we want to look at 'results', we pick 'results'

    return pd.concat(list_df)
