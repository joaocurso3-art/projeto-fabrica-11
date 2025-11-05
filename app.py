import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10,6)

df = pd.read_csv("Tabela_Clubes.csv")

print("=== Primeiras linhas ===")
print(df.head(), "\n")

print("=== Informações Gerais ===")
print(df.info(), "\n")

print("=== Estatísticas Descritivas ===")
print(df.describe(), "\n")

print("=== Valores Ausentes ===")
print(df.isna().sum(), "\n")

frequencia_times = df['Time'].value_counts()
total_times = df['Time'].nunique()
print(f"Total de times únicos: {total_times}")
print("Top 10 times mais frequentes:")
print(frequencia_times.head(10), "\n")

print(f"Ano mínimo registrado: {df['Ano'].min()}")
print(f"Ano máximo registrado: {df['Ano'].max()}\n")

campeoes = df[df['Posição'] == 1][['Ano', 'Time']].sort_values('Ano')
print("=== Campeões por Ano ===")
print(campeoes.head(10), "\n")

titulos = campeoes['Time'].value_counts()
print("=== Número de Títulos por Clube ===")
print(titulos, "\n")

plt.figure()
titulos.plot(kind='bar', color='gold', edgecolor='black')
plt.title("Número de Títulos por Clube")
plt.ylabel("Títulos")
plt.xlabel("Clube")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

derrotas = df.groupby('Time')['Derrotas'].sum().sort_values(ascending=False)
print("Clube com mais derrotas acumuladas:")
print(f"{derrotas.index[0]} - {derrotas.iloc[0]} derrotas\n")

print("Clube com menos derrotas acumuladas:")
print(f"{derrotas.index[-1]} - {derrotas.iloc[-1]} derrotas\n")

plt.figure()
sns.scatterplot(data=df, x='Vitorias', y='Derrotas', hue='Time', legend=False)
plt.title("Relação entre Vitórias e Derrotas por Time")
plt.xlabel("Vitórias")
plt.ylabel("Derrotas")
plt.show()

principais = titulos.head(5).index

plt.figure()
for time in principais:
    subset = df[df['Time'] == time]
    plt.plot(subset['Ano'], subset['Pontos'], marker='o', label=time)

plt.title("Evolução dos Pontos dos Maiores Clubes")
plt.xlabel("Ano")
plt.ylabel("Pontos")
plt.legend()
plt.tight_layout()
plt.show()

print("ANÁLISE CONCLUÍDA")
print("""
Resumo:
- Dominância histórica dos clubes identificada.
- Tendências de desempenho ao longo dos anos mapeadas.
- Campeões e padrões de vitórias/derrotas visualizados.
""")
