'''parameter_estimation.py

This script performs parameter fitting on the model specified in model_v003.py.
Parameters k1 and k4 are fit to synthetic experimental data generated
using gen_experimental_data.py'''

from model_fitting import model_fitting
from model_v003 import antimony_str
import tellurium as te
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# Use differential evolution to fit parameters k1 and k4 using experimental data
parameter_list = ['k1', 'k4']
print(f'\nEstimating kinetic parameters {parameter_list[0]} and {parameter_list[1]}:')
mf = model_fitting(data_file = 'data.csv', antimony_str = antimony_str, parameter_list = parameter_list, seed_val = 124)
model_fit_params = mf.differential_evolution()

# Show differential evolution fit results
print('\nDifferential evolution routine terminated successfully:')
print(model_fit_params)
print(f'\nThe fitted value for k1 is: {model_fit_params.x[0]:.3f}; The fitted value for k4 is: {model_fit_params.x[1]:.3f}')
k1 = model_fit_params.x[0]
k4 = model_fit_params.x[1]

# Plot fitted result
model = te.loada(antimony_str)
sim_data = mf.simulate_model(model_fit_params.x) # simulate model with fitted parameters
plt.figure(1)
plt.plot(mf.data[:,0],mf.data[:,1:],'.')
plt.gca().set_prop_cycle(None)
plt.plot(sim_data[:,0],sim_data[:,1:],'-')
plt.xlabel('Time'); plt.ylabel('Concentration'); plt.legend(model.getFloatingSpeciesIds());

# Save figure for Docker implementation
# plt.savefig('parameter_fitting_sars_cov2_infection_simulation.jpg', dpi = 300)
plt.show()

# Use Monte Carlo algorithm to generate distrib
CI_dict = mf.fitted_percentile(percentile=95, num_itr=10)

print(f"\nThe 95% confidence interval for k1 is [{CI_dict['CI_lower'][0]:.3f}, {CI_dict['CI_upper'][0]:.3f}]")
print(f"\nThe 95% confidence interval for k4 is [{CI_dict['CI_lower'][1]:.3f}, {CI_dict['CI_upper'][1]:.3f}]")

# Save fitted parameter sets to csv file
df = pd.DataFrame(CI_dict['Fitted_parameter_sets'], columns = parameter_list)
df.to_csv('fitted_parameter_sets.csv', sep=',', index=False)