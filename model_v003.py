'''model_v003.py
Development build.

Development stages executed: model construction, data aggregation, parameter fitting, annotation

This script describes a model of viral replication in the
Antimony language, updated from previous versions, model_v001.py and model_v002.py

A new reaction describing binding of the virus to a host cell is added in model_v003.py.

The model described in model_v003.py is used for parameter_estimation.py and to test
aggregated data from data_aggregation.py and fitted kinetic constants in simulation.py'''

antimony_str = """
model sars_cov2_infection

// Define model equations
production_genomic_ssRNA:               -> gen_ssRNA;   k1*rep_ssRNA
transcription_genomic_ssRNA:  gen_ssRNA -> rep_ssRNA;   k2*gen_ssRNA
translation_of_viral_envelope:          -> envelope;    k3*rep_ssRNA  
degradation_of_ssRNA:         rep_ssRNA -> ;            k4*rep_ssRNA
degradation_of_envelope:       envelope -> ;            k5*envelope
formation_of_free_virus_complex: gen_ssRNA + envelope -> virus_free;  k6*gen_ssRNA*envelope
binding_of_virus_complex_to_host:  virus_free + $ACE2 -> virus_bound; k7*virus_free*ACE2

// Annotate reactions 
transcription_genomic_ssRNA.sboTerm = SBO:0000183
translation_of_viral_envelope.sboTerm = SBO:0000184

// Set global constants
k1 = 0.5; k2 = 0.025;
k3 = 1000; k4 = 0.35
k5 = 2; k6 = 7.5E-6
k7 = 0.7 # kinetic parameter value not curated

// Set initial conditions
rep_ssRNA = 1; gen_ssRNA = 0; 
envelope = 0; ACE2 = 100;
virus_free = 0; virus_bound = 0; 

end
"""