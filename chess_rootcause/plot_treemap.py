import plotly.express as px
import os
import json
import pandas as pd


dir_path = os.path.dirname(os.path.realpath(__file__))

input_file_path = os.path.join(dir_path, 'db', 'db.json')
with open(input_file_path) as json_file:
    input_json = json.load(json_file)

input_json = input_json['_default']

df = pd.DataFrame.from_dict(input_json, orient='index')
print(df.columns)
df = df.groupby(['primary_root_cause'])['Date'].count().reset_index()
df.rename(columns={'Date':'counts'}, inplace=True)

print(df)

fig = px.treemap(df, path=['primary_root_cause'], values='counts')
fig.data[0].textinfo = 'label+value'
fig.update_layout(uniformtext=dict(minsize=30, mode='hide'))
fig.show()