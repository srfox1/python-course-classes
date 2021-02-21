import pygal
from die import Die

#Create a D6.
die = Die()

#Make some rolls, and store results in alist.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyse the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
print(frequencies[2])


#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 dice 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die.visual.svg')