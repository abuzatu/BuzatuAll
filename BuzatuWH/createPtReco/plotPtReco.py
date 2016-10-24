#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

fileName="./histos.root"
histoPath="./"
name=""
debug=False

slds="all,mu,el,nosld".split(",")
names="20-60,60-100,100-200,200-inf".split(",")
for sld in slds:
    for name in names:
        histoName=sld+"_"+name
        h=retrieveHistogram(fileName,histoPath,histoName,name,debug).Clone()
        print h.GetName(), h.GetTitle()
        h.SetTitle(histoName)
        plotHistogram(h,"","",histoName,"pdf")
