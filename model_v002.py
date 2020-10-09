'''model_v002.py
Development_build.

Development stages executed: annotation

This script describes a model of viral replication in the
Antimony language, with SBO annotations added to model_v001.py.'''

antimony_str = """
model sars_cov2_infection

// Define model equations
production_genomic_ssRNA:               -> gen_ssRNA;   k1*rep_ssRNA
transcription_genomic_ssRNA:  gen_ssRNA -> rep_ssRNA;   k2*gen_ssRNA
translation_of_viral_envelope:          -> envelope;    k3*rep_ssRNA  
degradation_of_ssRNA:         rep_ssRNA -> ;            k4*rep_ssRNA
degradation_of_envelope:       envelope -> ;            k5*envelope
formation_of_free_virus_complex: gen_ssRNA + envelope -> virus_free;  k6*gen_ssRNA*envelope

// Annotate reactions 
transcription_genomic_ssRNA.sboTerm = SBO:0000183
translation_of_viral_envelope.sboTerm = SBO:0000184

// Set global constants
k1 = 0.5; k2 = 0.025;
k3 = 1000; k4 = 0.35
k5 = 2; k6 = 7.5E-6

// Set initial conditions
rep_ssRNA = 1; gen_ssRNA = 0; 
envelope = 0; virus_free = 0; 

end
"""