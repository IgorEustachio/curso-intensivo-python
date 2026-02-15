from die import Die
import plotly.express as px

die1 = Die(6) #cria uma instância da classe Die, que representa um dado de seis lados
die2 = Die(6)
die3 = Die(6) #cria uma segunda instância da classe Die, representando um segundo dado de dez lados

#roda o dado 1000 vezes e armazena os resultados em uma lista
results = []
for roll_num in range(1_000):
    result = die1.roll() * die2.roll() * die3.roll() #roda os três dados e multiplica os resultados
    results.append(result)

#analisa os resultados
frequencies = []
max_result = die1.num_sides * die2.num_sides * die3.num_sides #o resultado máximo possível é a soma dos lados dos três dados
possible_results = range(1, max_result+1)       
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

#personaliza ainda mais o gráfico
fig.update_layout(xaxis_dtick=1)

fig.show()