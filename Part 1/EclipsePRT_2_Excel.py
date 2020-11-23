# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 18:15:34 2018

@author: Jamiu
"""

# In[]

import pandas as pd

filename = "LOW_SALT.PRT"

file = open(filename)
file_line = file.readlines()

Steps = ["-"]; Times = ["day"]; Pave = ["Barsa"]; Wcut = ["fraction"]; GOR = ["sm3/sm3"]; WGR = ["sm3/sm3"]

for ind in range(len(file_line)):
    if file_line[ind][1:5] == "STEP":
        Steps.append(int(((file_line[ind]).split())[1]))
        Times.append(float(((file_line[ind]).split())[3]))
        Pave.append(float(((file_line[ind+1]).split())[1]))
        Wcut.append(float(((((file_line[ind+1]).split())[3]).split('='))[1]))
        GOR.append(float(((file_line[ind+1]).split())[5]))
        WGR.append(float(((file_line[ind+1]).split())[8]))

data = {"STEP": Steps,"TIME": Times,"PAVE": Pave, "WCUT": Wcut, "GOR": GOR,"WGR": WGR}

col_names = list(data.keys())

df = pd.DataFrame(data, index = None)
    
df = df[col_names]

name = filename.split(".")[0]

writer = pd.ExcelWriter(name +".xlsx")

df.to_excel(writer, sheet_name = name, index = False, header = col_names, startrow = 2, startcol = 1)
