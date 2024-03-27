# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:48:26 2024

@author: Solero
"""

# data download site:
# https://echarts.apache.org/examples/data/asset/data/les-miserables.json

import streamlit_echarts as echarts
import json
import streamlit as st
import pandas as pd

#%%
with open("./data/les-miserables.json", "r") as f:
    graph = json.loads(f.read())

for idx, _ in enumerate(graph["nodes"]):
    graph["nodes"][idx]["symbolSize"] = 5

#%%
option = {
    "title": {
        "text": "Les Miserables",
        "subtext": "Default layout",
        "top": "bottom",
        "left": "right",
    },
    "tooltip": {},
    "legend": [{"data": [a["name"] for a in graph["categories"]]}],
    "series": [
        {
            "name": "Les Miserables",
            "type": "graph",
            "layout": "force",
            "data": graph["nodes"],
            "links": graph["links"],
            "categories": graph["categories"],
            "roam": True,
            "label": {"position": "right"},
            "draggable": True,
            "force": {"repulsion": 100},
        }
    ],
}
echarts.st_echarts(option, height="500px")
st.table(df)
