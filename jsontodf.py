import pandas as pd
import glob, os, json
df = pd.DataFrame()
path_to_json = 'path_to_your_json_folder' 
json_pattern = os.path.join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)
for file in file_list:
    data = pd.read_json(file, lines=True)
    df = df.append(data)
df = df.set_index('date')