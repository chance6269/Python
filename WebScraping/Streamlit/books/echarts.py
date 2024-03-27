# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:28:00 2024

@author: jcp
"""

# https://echarts.streamlit.app/
# pip install streamlit_echarts

import streamlit as st
import streamlit_echarts as echarts

option = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
}
echarts.st_echarts(
    options=option, height="400px",
)

# echarts.st_echarts(options=option)