# SwanKernels

Packlage that provides SWAN Kernels for:
* Multiple CVMFS repos like CMS and SFT
* Mutiple languages like python, R, octave, ROOT C++ and Go

## Requirements

Besides Jupyter, this extension requires SwanProject.

## Install

Install the package and the nbextension:

```bash
pip install swankernels
```

# Generating SWAN kernels for JupyterLab
TODO

# Using scram_list_filter

command to filter scram list stacks 
```.sh
source /cvmfs/cms.cern.ch/cmsset_default.sh

scram list | ./scram_list_filter

scram list | ./scram_list_filter | grep CMSSW | sort | uniq

for i in $(scram list | grep CMSSW | uniq | sort  | ./scram_list_filter ); do echo -n \"$i\",; done
```
