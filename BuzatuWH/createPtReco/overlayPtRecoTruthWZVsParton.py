#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=2:
    print "You need some arguments, will ABORT!"
    print "Ex: python overlayPtRecoTruthWZVsParton.py Process"
    print "Ex: python overlayPtRecoTruthWZVsParton.py vvbb_100k"
    assert(False)
# done if

#Folder=sys.argv[1]       # FatJet14

import ROOT
ROOT.gROOT.SetBatch(True)
debug=False
Process=sys.argv[1]

path="~/data/histos_PtReco/"
fileTruthWZ=path+"histos_"+Process+"_TruthWZ.root"
fileParton =path+"histos_"+Process+"_Parton.root"

def overlay(sld):
    None
    list_tuple_h1D=[]
    h=retrieveHistogram(fileTruthWZ,"","PtReco_"+sld,"",debug)
    h.SetLineColor(1)
    h.SetXTitle("jet p_T after OneMu correction [GeV]")
    h.SetYTitle("PtReco "+sld)
    list_tuple_h1D.append([h,"TruthWZ"])
    h=retrieveHistogram(fileParton,"","PtReco_"+sld,"",debug)
    h.SetLineColor(2)
    list_tuple_h1D.append([h,"Parton"])
    overlayHistograms(list_tuple_h1D,path+"PtReco_"+Process+"_"+sld,"pdf","histo",False)
# done

# run
for sld in "all,nosld,mu,el,other".split(","):
    overlay(sld)
