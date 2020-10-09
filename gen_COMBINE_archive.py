import tellurium as te
import os
from gen_SEDML import phrasedml_str
from model_v100 import antimony_str

# create an inline OMEX string
inline_omex = '\n'.join([antimony_str, phrasedml_str])

# export to a COMBINE archive
archive_name = os.path.join(os.getcwd(), 'sars_cov2_infection.omex')
te.exportInlineOmex(inline_omex, archive_name)

