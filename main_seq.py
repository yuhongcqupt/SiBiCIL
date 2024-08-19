# Append module path.
import sys, os

from mos import mos_code_of

sys.path.append(os.getcwd())
# Import module
from coding import *
import numpy as np
import pandas as pd
df = pd.read_csv("protein_family.csv", header=None)
df = np.array(df)
df_cod = np.zeros((1, 29))
#protein coding
for i in range(len(df)):
    seq = df[i, 0]
    code_mos = []
    code_mos.append(mos_code_of(seq))
    #code_mos = mos_code_of(seq)
    df_cod = np.concatenate((df_cod, code_mos))
df_cod = pd.DataFrame(df_cod)
df_cod.to_csv('protein_family.csv', index=False)
