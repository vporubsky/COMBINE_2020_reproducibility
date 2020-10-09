'''run_COMBINE_archive.py

This script converts the COMBINE archive in the
file sars_cov2_infection_simulation.omex to an inline
OMEX (transparently) and executes the SED-ML.'''

import tellurium as te
te.convertAndExecuteCombineArchive('sars_cov2_infection.omex')