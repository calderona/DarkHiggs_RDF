#!/bin/bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_104a/x86_64-el9-gcc11-opt/setup.sh
source /afs/cern.ch/user/c/calderon/work/private/mkShapesRDF_run2/mkShapesRDF/myenv/bin/activate
time python runner.py
cp output.root /afs/cern.ch/work/c/calderon/private/mkShapesRDF_run2/mkShapesRDF/works/DarkHiggs_RDF/Full2018_v7/rootFiles__darkHiggs2018_v7/mkShapes__darkHiggs2018_v7__ALL__${1}.root
rm output.root
rm script.py
