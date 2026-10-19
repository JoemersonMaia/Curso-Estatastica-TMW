# %%%
import pandas  as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

df = pd.read_csv("../data/points-tmw.csv", sep = ",")
df.head()

# %%

group_prod= (df.groupby("descProduto")["idTransacao"]
            .count().
            reset_index())
group_prod.sort_values(by="idTransacao")

# %%
plt.figure(figsize=[6,4])
sns.set_theme(style="whitegrid")
sns.barplot(group_prod, y = "descProduto", x = "idTransacao")
plt.xlabel("Quantidade Transacoes")
plt.ylabel("Produto")
plt.title("Frequência de Produtos")
plt.savefig("Gráfico de Barras dos Produtos")

# %%
df["dataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date
df.head()

# %%
group_data = df.groupby(df["dataTransacao"]).agg(
    {
        "qtdPontos" : "sum",
        "idTransacao" : "count",
    }
).reset_index()

group_data = group_data.sort_values("dataTransacao")

plt.figure(figsize=[8,6])
plt.plot(group_data["dataTransacao"], group_data["idTransacao"])
plt.ylabel("Qtde. Transações")
plt.title("Série Histótica de Transacoes")
plt.legend(["Qtde. Transações"])

# %%
