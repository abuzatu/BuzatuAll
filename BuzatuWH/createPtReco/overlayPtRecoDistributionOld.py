#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=4:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayPtRecoFits Process Initial Target"
    print "Ex: ./overlayPtRecoFits llbb    OneMu Parton"
    assert(False)
# done if

#Folder=sys.argv[1]       # FatJet14

import ROOT
ROOT.gROOT.SetBatch(True)
debug=True
Process=sys.argv[1]
Initial=sys.argv[2]
Target=sys.argv[3]

if Target=="Parton":
    textTarget="b Parton"
elif Target=="TruthWZ":
    textTarget="jet TruthWZ"
else:
    print "Target",Target,"for textTarget not known. Will ABORT!!!"
    assert(false)
# done if

path="~/data/histos_PtReco/"
#fileName=path+"PtReco_histos_"+Process+"_"+Initial+"_"+Target+".root"
fileName=path+"histos_"+Process+"_"+Initial+"_"+Target+".root"
dict_outputfileName_list_variable={}
dict_outputfileName_list_variable["inclusive"]="inclusive_20-25,inclusive_35-40,inclusive_80-90,inclusive_130-160".split(",")
dict_outputfileName_list_variable["hadronic"] ="hadronic_20-25,hadronic_35-40,hadronic_80-90,hadronic_130-160".split(",")
dict_outputfileName_list_variable["muon"]     ="muon_20-40,muon_40-50,muon_70-85,muon_120-300".split(",")
dict_outputfileName_list_variable["electron"] ="electron_20-40,electron_40-60,electron_60-120".split(",")
list_option="histo,histo+Gauss,histo+Bukin".split(",")
#list_option="histo+Gauss".split(",")

def overlay(outputfileName, list_variable, option):
    None
    list_tuple_h1D=[]
    for i,variable in enumerate(list_variable):
        variableName=variable.replace("-","_").replace("inclusive","all").replace("hadronic","nosld").replace("muon","mu").replace("electron","el")
        h=retrieveHistogram(fileName,"",variableName,"",debug)
        h.SetLineColor(i+1)
        h.SetXTitle("Ratio of pT of "+textTarget+" to jet after muon-in-jet correction")
        h.GetXaxis().SetTitleSize(0.045)
        h.GetXaxis().SetTitleOffset(0.90)
        h.GetYaxis().SetTitleSize(0.050)
        h.GetYaxis().SetTitleOffset(0.90)
        h.SetYTitle("Number of jets")
        list_tuple_h1D.append([h,variable.replace("_"," ")+" GeV"])
    # done loop over fitname
    if debug:
        print "list_tuple_h1D",list_tuple_h1D
    overlayHistograms(list_tuple_h1D,fileName=path+"PtReco_distribution_"+Target+"_"+outputfileName,extensions="pdf",option=option,addfitinfo=True,min_value=-1,max_value=-1,legend_info=[0.57,0.34,0.88,0.66,72,0.037,0],plot_option="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets at least 20 GeV}?#bf{from ZH to llbb}",0.04,13,0.58,0.88,0.05),debug=False)
# done

# run
for option in list_option:
    for outputfileName in dict_outputfileName_list_variable.keys():
        list_variable=dict_outputfileName_list_variable[outputfileName]
        overlay(outputfileName, list_variable, option)
