#!/usr/bin/env python

'''
Dr. Rene Cejas Bolecek
reneczechdev@gmail.com
Departamento de Mecanica Computacional (MECOM), Gerencia de Investigacion Aplicada, Centro Atomico Bariloche\n\
Instituto Balseiro, Universidad Nacional de Cuyo\n\
Avenida Bustillo 9500, 8400 Bariloche, Rio Negro, Argentina\n\
MIT License\n\
'''

import pandas as pd
import numpy as np

file = './data/brainDB_test.xlsx'
# Load spreadsheet
with open(file) as f:
    xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse(xl.sheet_names[0])

#Remove nan's
df1.fillna('-', inplace=True)

columns = df1.shape[1] #df1.keys().size
rows = df1.shape[0] #int(df1.size/columns)

#Create a dict for Rowsnumbers
a = {}
for i, v in enumerate(df1.columns):
    #print(v,'\t',i)
    a[i]=v

tmp=[]
for j in df1.index:
    for i in df1.columns:
        if (df1.iloc[j][i] != '-'): 
            for key,value in a.items():
                tabulado = '\t'*int(key)
                flag = False
                if(i==value):
                    #String saved, next can be a number
                    if(not np.isreal(df1.iloc[j][i]) and len(tmp) == 0 and not flag):
                        tmp.append('{} {}'.format(tabulado,df1.iloc[j][i]))
                        flag = True

                    #Print, reset tmp and store new string
                    if(not np.isreal(df1.iloc[j][i]) and len(tmp)>0 and not flag): 
                        print(tmp[0],'\n')
                        tmp =[] #reset
                        tmp.append('{} {}'.format(tabulado,df1.iloc[j][i]))
                        flag = True

                    #Print saved String with the corresponding number
                    if(np.isreal(df1.iloc[j][i]) and len(tmp)>0 and not flag): 
                        print(tmp[0],'valor:', df1.iloc[j][i], '\n')
                        tmp =[] #reset
                        flag = True

