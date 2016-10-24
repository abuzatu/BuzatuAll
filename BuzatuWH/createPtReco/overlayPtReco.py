#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=7:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayPtReco.py Process Initial     Target         sld                   fitname          doNormal"
    print "Ex: ./overlayPtReco.py llbb    OneMu,AllMu Parton,TruthWZ all,nosld,mu,el,other None,Gauss,Bukin True,False"
    assert(False)
# done if

#Folder=sys.argv[1]       # FatJet14

import ROOT
ROOT.gROOT.SetBatch(True)
debug=False
string_process=sys.argv[1]
string_initial=sys.argv[2]
string_target=sys.argv[3]
string_sld=sys.argv[4]
string_fitname=sys.argv[5]
string_doNormalName=sys.argv[6]

path="~/data/histos_PtReco/"

list_process=string_process.split(",")
list_initial=string_initial.split(",")
list_target=string_target.split(",")
list_sld=string_sld.split(",")
list_fitname=string_fitname.split(",")
list_doNormalName=string_doNormalName.split(",")
addChikuma=False
addAdrian=False

def overlay():
    None
    list_tuple_h1D=[]
    counter=0
    if addChikuma:
        # add histogram from Chikuma
        h_Chikuma=retrieveHistogram(fileName="/Users/abuzatu/data/histos_PtReco/Chikuma/bjet_tf_160523.root",histoPath="h1_peak",histoName="h1_peak_b_signal_btag_dr4b2_worwmu_eta0_ff",name="Bukin inclusive Chikuma",debug=debug)
        list_tuple_h1D.append([h_Chikuma,"Bukin Chikuma"])
        h_Chikuma.SetLineColor(list_color[counter])
        h_Chikuma.SetLineWidth(1)
        counter+=1
    # done if
    if addAdrian:
        # add my histogram produced by hand
        h_Adrian=h_Chikuma.Clone()
        h_Adrian.Reset()
        h_Adrian.SetBinContent(1,0)
        h_Adrian.SetBinContent(2,0)
        h_Adrian.SetBinContent(3,0)
        h_Adrian.SetBinContent(4,0)
        h_Adrian.SetBinContent(5,0)
        h_Adrian.SetBinContent(6,0)
        h_Adrian.SetBinContent(7,0)
        h_Adrian.SetBinContent(8,0)
        h_Adrian.SetBinContent(9,0)
        h_Adrian.SetBinContent(10,0)
        h_Adrian.SetBinContent(11,0)
        h_Adrian.SetBinContent(12,0)
    # add my histograms
    for process in list_process:
        for initial in list_initial:
            for target in list_target:
                for doNormalName in list_doNormalName:
                    inputfileName=path+"PtReco_histos_"+process+"_"+initial+"_"+target+"_"+doNormalName+".root"
                    for sld in list_sld:
                        for fitname in list_fitname:
                            histoName="PtReco_"+sld+"_"+fitname
                            h=retrieveHistogram(inputfileName,"",histoName,"",debug)
                            h.SetLineColor(list_color[counter])
                            h.SetXTitle("Jet pT after "+initial+" correction [GeV]")
                            h.SetYTitle("PtReco correction factors")
                            legendName=process+"_"+initial+"_"+target+"_"+sld+" "+fitname
                            if doNormalName=="True":
                                legendName+=" from "+target+"/"+initial
                            else:
                                legendName+=" from "+initial+"/"+target
                            list_tuple_h1D.append([h,legendName])
                            counter=counter+1
    # done all for loops
    if debug:
        print "list_tuple_h1D",list_tuple_h1D
    outputfileName=path+"PtReco_"+string_process+"_"+string_initial+"_"+string_target+"_"+string_sld+"_"+string_fitname
    if addChikuma:
        outputfileName+=",Chikuma"
    #overlayHistograms(list_tuple_h1D,outputfileName,"pdf","histo",False)
    #overlayHistograms(list_tuple_h1D,fileName=outputfileName,extensions="pdf",option="histo",addfitinfo=False,min_value=-1,max_value=-1,legend_info=[0.50,0.50,0.88,0.72,72,0.027,0],plot_option="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets from llbb}",0.04,13,0.60,0.88,0.05),debug=False)
    overlayHistograms(list_tuple_h1D,fileName=outputfileName,extensions="pdf",option="histo",addfitinfo=False,min_value=-1,max_value=-1,min_value_ratio=0.90,max_value_ratio=1.2,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.12,0.50,0.88,0.72,72,0.030,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)
# done

# run
overlay()
