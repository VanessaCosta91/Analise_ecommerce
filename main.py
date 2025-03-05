import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('C:/Users/vanes/PycharmProjects/ecommerce_analise/ecommerce_estatistica.csv')

# Verificar os dados
print(df.head().to_string())

print("\nValores Nulos:\n", df.isnull().sum())


# Histograma com frequência de notas(avaliações) no ecommerce
plt.figure(figsize=(10,6))
plt.hist(df['Nota'], bins=30, color="blue", alpha=0.7, edgecolor='black')
plt.title('Avaliações Mais Frequêntes do Ecommerce')
plt.xlabel('Notas - Avaliações')
plt.ylabel('Frequência')
plt.grid(True)


# Gráfico de dispersão relacionando nota e preço
plt.figure(figsize=(10,6))
plt.scatter(df['Nota'],df['Desconto'], alpha=0.7, color='purple',edgecolor='black')
plt.title('Relação entre Nota e Desconto')
plt.xlabel('Nota')
plt.ylabel('Desconto')

# Mapa de Calor
corr = df[['Nota','Preço','Desconto','Marca_Cod']].corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm',linewidths=0.5)
plt.title('Correlação entre Variáveis')

# Gráfico de barras relação nota e quantidade vendida
plt.figure(figsize=(10,6))
sns.barplot(x=df['Nota'],y=df['Qtd_Vendidos_Cod'], width=0.9, edgecolor='black', errorbar=None)
plt.title('Quantidade de Vendidas por Nota')
plt.xlabel('Nota')
plt.ylabel('Quantidade Vendidas')

# Gráfico de Pizza - Distribuição das Notas
notas_count = df['Nota'].value_counts()
notas_count = notas_count[notas_count > 5]  # Ajuste para remover notas muito raras

plt.figure(figsize=(12, 8))
plt.pie(notas_count.values, labels=notas_count.index, autopct='%.1f%%', startangle=90)
plt.title('Distribuição das Notas no Ecommerce')

# Gráfico de Densidade - Avaliações (Notas)
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'], fill=True, color='blue')
plt.title('Densidade Avaliações - Nota')
plt.xlabel('Avaliações  - Notas')

# Gráfico de Regressão - Nota x Desconto
plt.figure(figsize=(10,6))
sns.regplot(x='Nota', y='Desconto', data=df, color='yellow', scatter_kws={'alpha': 0.5, 'color':'blue'})
plt.title('Regressão: Relação entre Nota e Desconto')
plt.xlabel('Nota')
plt.ylabel('Desconto')

plt.show()

