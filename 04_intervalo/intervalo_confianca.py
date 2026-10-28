# %%

import pandas as pd
from scipy.stats import t as t_student

df = pd.read_csv("../data/points-tmw.csv", sep=",")
df.head()

usuarios = (df.groupby("idUsuario").agg({
            "qtdPontos" : "sum"
            }).reset_index())
usuarios

# %%
n=100
sample = usuarios["qtdPontos"].sample(n)

x_barra= sample.mean()

s = sample.std()

t_student.ppf(0.975, n-1)