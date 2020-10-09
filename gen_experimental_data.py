'''gen_experimental_data.py

This script is used to generate toy experimental data for parameter fitting.'''
import numpy as np
from model_v003 import antimony_str
import tellurium as te
import pandas as pd
import random
random.seed(a = 124)

# Load the model string into a RoadRunner object instance
model = te.loada(antimony_str)
model.k1 = 1
model.k4 = 0.25

# Generate deterministic results using CVODE
det_results = model.simulate (0, 200, 51)

# Create noisy "data"
error_level = 0.35
data = []
data.append(det_results[:,0])
for i in range(1, np.shape(det_results)[1]):
    noise = np.random.normal(0, 1, np.shape(det_results)[0])
    error_data = det_results[:,i] + noise*error_level*max(det_results[:,i])
    rec_error_data = [x if x >= 0 else 0 for x in error_data]
    data.append(rec_error_data)

# save all data to csv file
data = np.transpose(np.asarray(data))
df = pd.DataFrame(data, columns = ['time', 'gen_ssRNA', 'rep_ssRNA', 'envelope', 'virus', 'virus_bound'])
df.to_csv('data.csv', sep=',', index=False)