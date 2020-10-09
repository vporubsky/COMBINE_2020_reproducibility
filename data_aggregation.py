'''data_aggregation.py

Data curation for the formation of spike glycoprotein RBD-SD1-ACE2 complex in SARS coronavirus.
Imports the kinetic constant corresponding to k7 in the sars-cov2 model_v003 from SABIO-RK.'''
import requests
import io
import pandas as pd

QUERY_URL = 'http://sabiork.h-its.org/sabioRestWebServices/kineticlawsExportTsv'

# Specify search fields and search terms
query_dict = {"Organism":'"SARS coronavirus"', "Product":'"Spike glycoprotein RBD-SD1-ACE2 complex"'}
query_string = ' AND '.join(['%s:%s' % (k,v) for k,v in query_dict.items()])

# Specify output fields and send request
query = {'fields[]':['EntryID', 'Organism', 'UniprotID','ECNumber', 'Parameter'], 'q':query_string}
request = requests.post(QUERY_URL, params = query)
request.raise_for_status()

# Print query results
print('\nThe results of SABIO-RK query for the formation of spike glycoprotein RBD-SD1-ACE2 complex in SARS coronavirus:\n')
print(request.text)
data_string = request.text
data = io.StringIO(data_string)
df = pd.read_csv(data, sep="\t")

parameter_types = list(df['parameter.type'])
if 'rate const.' in parameter_types:
    k7 = list(df['parameter.startValue'])[parameter_types.index('rate const.')]
    k7_units = list(df['parameter.unit'])[parameter_types.index('rate const.')]

print(f"\nThe formation of the spike glycoprotein RBD-SD1-ACE2 complex occurs at a rate of {k7:.3f} {k7_units}.")
