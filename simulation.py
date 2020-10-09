'''simulation.py

Simulation script for model_v003.py which imports fitted parameters
k1 and k4 from parameter_estimation.py and curated kinetic constant for k7
from data_aggregation.py.'''
from model_v003 import antimony_str
import tellurium as te
import matplotlib.pyplot as plt
from data_aggregation import k7
plt.style.use('ggplot')

# Load the model string into a RoadRunner object instance
model = te.loada(antimony_str)
model.k1 = 0.968 # set parameter value to that found in the parameter estimation stage
model.k4 = 0.222 # set parameter value to that found in the parameter estimation stage
model.k7 = k7 # set parameter value to that found in the data aggregation stage

# Generate deterministic results using CVODE
det_results = model.simulate (0, 200, 100, ['time', 'gen_ssRNA'])

# Set a seed value for reproducible stochastic output
model.seed = 124

plt.figure(2)
for i in range(10):
    # Reset variable concentrations to initial conditions
    model.reset()
    # Generate stochastic results using Gillespie's algorithm
    stoch_results = model.gillespie (0, 200, 100, ['time', 'gen_ssRNA'])
    # Plot stochastic simulation trajectory
    plt.plot(stoch_results['time'], stoch_results['gen_ssRNA'], linewidth=4, alpha=0.4)

# Plot deterministic results
plt.plot(det_results['time'], det_results['gen_ssRNA'], color='black', linewidth=2,)
plt.xlabel('Time')
plt.ylabel('[gen_ssRNA]')

# Save figure for Docker implementation and show
# plt.savefig('curated_k7_sars_cov2_infection_simulation.jpg', dpi = 300)
plt.show()

print(f'\nTimeseries of gen_ssRNA using fitted values for k1 and k4, and curated data for k7:')
print(det_results)
