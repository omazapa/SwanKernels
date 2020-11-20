# Package to generated SWAN kernels for JupyterLab

# Using scram_list_filter

command to filter scram list stacks 
```.sh
source /cvmfs/cms.cern.ch/cmsset_default.sh

scram list | ./scram_list_filter

scram list | ./scram_list_filter | grep CMSSW | sort | uniq

for i in $(scram list | grep CMSSW | uniq | sort  | ./scram_list_filter ); do echo -n \"$i\",; done
```