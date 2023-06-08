# coding: utf-8

"""
Configuration of the HH → bb𝜏𝜏 analysis.
"""

import os

import law
import order as od


#
# the main analysis object
#

analysis_hbt = od.Analysis(
    name="analysis_hbt",
    id=1,
)

# analysis-global versions
analysis_hbt.x.versions = {}

# files of bash sandboxes that might be required by remote tasks
# (used in cf.HTCondorWorkflow)
analysis_hbt.x.bash_sandboxes = [
    "$CF_BASE/sandboxes/cf_prod.sh",
    "$CF_BASE/sandboxes/venv_columnar.sh",
    "$HBT_BASE/sandboxes/venv_columnar_tf.sh",
]

# files of cmssw sandboxes that might be required by remote tasks
# (used in cf.HTCondorWorkflow)
analysis_hbt.x.cmssw_sandboxes = [
    # "$HBT_BASE/sandboxes/cmssw_default.sh",
]

# clear the list when cmssw bundling is disabled
if not law.util.flag_to_bool(os.getenv("HBT_BUNDLE_CMSSW", "1")):
    del analysis_hbt.x.cmssw_sandboxes[:]

# config groups for conveniently looping over certain configs
# (used in wrapper_factory)
analysis_hbt.x.config_groups = {}


#
# load configs
#

# 2017
from hbt.config.configs_run2ul import add_config as add_config_run2ul
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11


# default v9 config
add_config_run2ul(
    analysis_hbt,
    campaign_run2_2017_nano_v9.copy(),
    config_name=campaign_run2_2017_nano_v9.name,
    config_id=2,
)

# v9 config with limited number of files for faster prototyping
add_config_run2ul(
    analysis_hbt,
    campaign_run2_2017_nano_v9.copy(),
    config_name=f"{campaign_run2_2017_nano_v9.name}_limited",
    config_id=12,
    limit_dataset_files=2,
)

# v11 uhh config with limited number of files for faster prototyping
add_config_run2ul(
    analysis_hbt,
    campaign_run2_2017_nano_uhh_v11.copy(),
    config_name=f"{campaign_run2_2017_nano_uhh_v11.name}_limited",
    config_id=32,
    limit_dataset_files=2,
)

# 2018 default v11 config
add_config_run2ul(
    analysis_hbt,
    campaign_run2_2018_nano_v9.copy(),
    config_name=campaign_run2_20178_nano_v9.name,
    config_id=2,
)

# 2018 v11 uhh config with limited number of files for faster prototyping
add_config_run2ul(
    analysis_hbt,
    campaign_run2_2018_nano_uhh_v11.copy(),
    config_name=f"{campaign_run2_2018_nano_uhh_v11.name}_limited",
    config_id=55,
    limit_dataset_files=2,
)
