#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=3:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayPtRecoFits Process Target"
    print "Ex: ./overlayPtRecoFits llbb    Parton"
    assert(False)
# done if

#Folder=sys.argv[1]       # FatJet14

import ROOT
ROOT.gROOT.SetBatch(True)
debug=True
Process=sys.argv[1]
Target=sys.argv[2]

path="~/data/histos_PtReco/"
fileName=path+"histos_"+Process+"_OneMu_"+Target+".root"
list_sld="inclusive,hadronic,muon,electron".split(",")
list_fitname="None,Gauss,Bukin".split(",")

def overlay(sld):
    None
    list_tuple_h1D=[]
    for i,fitname in enumerate(list_fitname):
        h=retrieveHistogram(fileName,"","PtReco_"+sld+"_"+fitname,"",debug)
        h.SetLineColor(i+1)
        h.SetXTitle("jet p_T after OneMu correction [GeV]")
        h.SetYTitle("PtReco"+" "+Process+" "+Target+" "+sld)
        list_tuple_h1D.append([h,fitname])
    # done loop over fitname
    if debug:
        print "list_tuple_h1D",list_tuple_h1D
    outputfileName=path+"PtReco_"+Process+"_"+Target+"_"+sld
    overlayHistograms(list_tuple_h1D,outputfileName,"pdf","histo",False)
# done

# run
for sld in list_sld:
    overlay(sld)
