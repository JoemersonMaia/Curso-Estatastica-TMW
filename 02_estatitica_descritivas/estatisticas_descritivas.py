# %% 

import pandas as pd

df = pd.read_csv("../data/points-tmw.csv", sep = ",")

# %%

print("estatisticas de posicao para transacoes: ")

minimo = df["qtdPontos"].min()
print("minimo: ", minimo)

media = df["qtdPontos"].mean()
print("media: ",media)

quartil_1 = df["qtdPontos"].quantile(0.25)
print("1_quartil:", quartil_1)

mediana = df["qtdPontos"].median()
print("mediana: ", mediana)

qaurtil_3 = df["qtdPontos"].quantile(0.75)
print("3_quartil: ", qaurtil_3)

maximo = df["qtdPontos"].max()
print("maximo: ", maximo)

variancia = df["qtdPontos"].var()
print("variancia:", variancia)

desvio_padrao = df["qtdPontos"].std()
print("desvio padrao:", desvio_padrao)

amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()
print("amplitude:", amplitude)

df["qtdPontos"].describe()

# %%

print("estatisticas de posicao para usuario: ")

usuarios = (df.groupby(["idUsuario"]).agg(
    {
        "idTransacao" : "count",
        "qtdPontos" : "sum",
    }
    ).reset_index())

#%% 

summario = usuarios[["idTransacao", "qtdPontos"]].describe()

print(summario.to_string())
# %%
