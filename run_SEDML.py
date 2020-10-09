'''run_SEDML.py

This script executes the simulation experiment specified
with SED-ML in the file sars_cov2_infection_simulation.xml.'''

import tellurium as te

te.executeSEDML('sars_cov2_infection_simulation.xml')