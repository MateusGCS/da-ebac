import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('gasolina.csv')
data.head()
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=data, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço médio da gasolina por dia', xlabel='Dia', ylabel='Venda')
plt.savefig('gasolina.png', bbox_inches='tight')
