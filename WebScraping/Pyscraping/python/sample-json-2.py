# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:36:24 2024

@author: jcp
"""

json_data = """{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}
"""

import json

# json -> dict
# key : employees
# value : list
json_dict = json.loads(json_data)

# %%

import pandas as pd
df = pd.DataFrame(json_dict)

for dx in range(len(df)):
    rows = df.iloc[dx,:]
    print(rows) # Series
    print(type(rows.values[0]), rows.values[0]) # dict