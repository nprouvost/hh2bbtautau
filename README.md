<<<<<<< HEAD
# HH → bb𝜏𝜏

[![Lint and test](https://github.com/uhh-cms/hh2bbtautau/actions/workflows/lint_and_test.yaml/badge.svg)](https://github.com/uhh-cms/hh2bbtautau/actions/workflows/lint_and_test.yaml)
[![License](https://img.shields.io/github/license/uhh-cms/hh2bbtautau.svg)](https://github.com/uhh-cms/hh2bbtautau/blob/master/LICENSE)


### Quickstart

A couple test tasks are listed below.
They might require a **valid voms proxy** for accessing input data.

```shell
# clone the project
git clone --recursive git@github.com:uhh-cms/hh2bbtautau.git
cd hh2bbtautau

# source the setup and store decisions in .setups/dev.sh (arbitrary name)
source setup.sh dev

# index existing tasks once to enable auto-completion for "law run"
law index --verbose

# run your first task
# (they are all shipped with columnflow and thus have the "cf." prefix)
law run cf.ReduceEvents \
    --version v1 \
    --dataset hh_ggf_bbtautau_madgraph \
    --branch 0

# create a plot
law run cf.PlotVariables1D \
    --version v1 \
    --datasets hh_ggf_bbtautau_madgraph \
    --producers default \
    --variables jet1_pt \
    --categories incl \
    --branch 0

# create a (test) datacard (CMS-style)
law run cf.CreateDatacards \
    --version v1 \
    --producers default \
    --inference-model test \
    --workers 3
```


### Development

- Source hosted at [GitHub](https://github.com/uhh-cms/hh2bbtautau)
- Report issues, questions, feature requests on [GitHub Issues](https://github.com/uhh-cms/hh2bbtautau/issues)
=======
# cmsdb

[![Lint and test](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml/badge.svg)](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml)
[![License](https://img.shields.io/github/license/uhh-cms/cmsdb.svg)](https://github.com/uhh-cms/cmsdb/blob/master/LICENSE)

Database of physics processes, cross sections and scientific constants as well as CMS-related campaign information on datasets.


#### Dependencies

- [order](https://github.com/riga/order) is used to model the relations between physics meta data containers (datasets, processes, systematics, ...).
- [scinum](https://github.com/riga/scinum)'s `Number` is the basis for numeric values with multiple sources of systematic uncertainties attributed to them.
>>>>>>> 4ced1aebe036fdcaf1403d00a04355f9b73da8f8
