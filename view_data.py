'''view_data.py

Plot the experimental data in data.csv with simulation data to
visualize model performance.
'''
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt
from model_v100 import antimony_str
plt.style.use('ggplot')

# Load experimental dataa
data = np.genfromtxt('data.csv', dtype=float, delimiter=',')[1:,:]

# Generate simulation data
model = te.loada(antimony_str)
sim_data = model.simulate(data[0,0], data[len(data)-1, 0], len(data))

# Plot model simulation and experimental data
plt.plot(data[:,0],data[:,1:],'.')
plt.gca().set_prop_cycle(None)
plt.plot(sim_data[:,0],sim_data[:,1:],'-')
plt.xlabel('Time');  plt.ylabel('Concentration'); plt.legend(model.getFloatingSpeciesIds()); plt.show()