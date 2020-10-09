'''gen_SEDML.py

This script describes a simulation experiment using phraSED-ML,
converts it to SED-ML, and saves the SED-ML string to the file
sars_cov2_infection_simulation.xml.'''

from model_v100 import antimony_str
import tellurium as te
import phrasedml

# Write phraSED-ML string specifying the simulation study
phrasedml_str = '''
  // Set model
  sars_cov2_inf = model "sars_cov2_infection.xml"
  
  // Deterministic simulation
  det_sim = simulate uniform(0, 200, 100)
  run_det_sim = run det_sim on sars_cov2_inf
  plot "sars-cov2 infection deterministic simulation" run_det_sim.time vs run_det_sim.gen_ssRNA

  // Stochastic simulation
  stoch_sim = simulate uniform_stochastic(0, 200, 100)
  stoch_sim.algorithm.seed = 124
  run_stoch_sim = run stoch_sim on sars_cov2_inf
  run_mult_stoch_sim = repeat run_stoch_sim for local.x in uniform(0, 10, 10), reset = true
  plot "sars-cov2 infection stochastic simulation" run_mult_stoch_sim.time vs run_mult_stoch_sim.gen_ssRNA
'''

# Generate SED-ML string from the phraSED-ML string
sbml_str = te.antimonyToSBML(antimony_str)
phrasedml.setReferencedSBML("sars_cov2_infection.xml", sbml_str)
sedml_str = phrasedml.convertString(phrasedml_str)

# Save the SED-ML simulation experiment to your current working directory
te.saveToFile('sars_cov2_infection_simulation.xml', sedml_str)