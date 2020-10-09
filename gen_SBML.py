'''gen_SBML.py

This script imports the viral replication model
described in model.py, converts and exports it as an SBML model
to the file sars_cov2_infection.xml.'''

from model_v100 import antimony_str
import tellurium as te

model = te.loada(antimony_str)
model.exportToSBML('sars_cov2_infection.xml')