from die import Die
import plotly.express as px

die = Die() #cria uma instância da classe Die, que representa um dado de seis lados

#roda o dado 100 vezes e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analisa os resultados
frequencies = []
possible_results = range(1, die.num_sides+1)    
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)



title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.show()