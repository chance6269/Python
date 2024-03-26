# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:29:17 2024

@author: jcp
"""

"""
{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}
"""

import pandas as pd

df = pd.read_json('./sample.json')

print(df.to_string())