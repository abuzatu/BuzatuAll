#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=1:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayPtRecoSimple.py"
    assert(False)
# done if

#Folder=sys.argv[1]       # FatJet14

import ROOT
ROOT.gROOT.SetBatch(True)
debug=False

path="~/data/histos_PtReco/"

addMoriond=True
addTrunk=True
addAdrianBug=True
addAdrianFixed=True
addAdrianFixedInversed=True
addChikuma=True

def set_properties_histogram(h,counter):
    h.SetLineColor(list_color[counter])
    h.SetLineWidth(1)
    h.GetXaxis().SetTitle("Tranverse momentum at reconstructed scale OneMu [GeV]")
    h.GetYaxis().SetTitle("Correction factors for PtReco")
# done function

def overlay():
    None
    list_tuple_h1D=[]
    counter=0
    if addMoriond:
        h_Moriond=retrieveHistogram(fileName=path+"/Moriond-CxAODMaker-00-01-33/histos_llbb_OneMu_Parton.root",histoPath="",histoName="PtReco_all_Bukin",name="",debug=debug)
        set_properties_histogram(h_Moriond,counter)
        list_tuple_h1D.append([h_Moriond,"Peak of Bukin fit of bParton/OneMu (Moriond)"])
        counter+=1
    # done if
    if addTrunk:
        h_Trunk=retrieveHistogram(fileName=path+"/Trunk/PtReco_histos_llbb_OneMu_Parton.root",histoPath="",histoName="PtReco_inclusive_Bukin",name="",debug=debug)
        set_properties_histogram(h_Trunk,counter)
        list_tuple_h1D.append([h_Trunk,"Peak of Bukin fit of bParton/OneMu (Trunk)"])
        counter+=1
    # done if
    if addAdrianBug:
        h_AdrianBug=retrieveHistogram(fileName=path+"/PtReco_Moriond_File/PtReco_histos_ZHll125_OneMu_Parton.root",histoPath="",histoName="PtReco_inclusive_Bukin",name="",debug=debug)
        set_properties_histogram(h_AdrianBug,counter)
        list_tuple_h1D.append([h_AdrianBug,"Peak of Bukin fit of bParton/OneMu (Bug)"])
        counter+=1
    # done if
    if addAdrianFixed:
        h_AdrianFixed=retrieveHistogram(fileName=path+"/PtReco_Moriond_File_Fixed/PtReco_histos_ZHll125_OneMu_Parton_True.root",histoPath="",histoName="PtReco_inclusive_Bukin",name="",debug=debug)
        set_properties_histogram(h_AdrianFixed,counter)
        list_tuple_h1D.append([h_AdrianFixed,"Peak of Bukin fit of bParton/OneMu (Adrian)"])
        counter+=1
    # done if   
    if addAdrianFixedInversed:
        h_AdrianFixedInversed=retrieveHistogram(fileName=path+"/PtReco_Moriond_File_Fixed/PtReco_histos_ZHll125_OneMu_Parton_False.root",histoPath="",histoName="PtReco_inclusive_Bukin",name="",debug=debug)
        set_properties_histogram(h_AdrianFixedInversed,counter)
        list_tuple_h1D.append([h_AdrianFixedInversed,"1 over Peak of Bukin fit of OneMu/bParton (Adrian Inverse)"])
        counter+=1
    # done if   
    if addChikuma:
        # add histogram from Chikuma
        h_Chikuma=retrieveHistogram(fileName=path+"/Chikuma/bjet_tf_160523.root",histoPath="h1_peak",histoName="h1_peak_b_signal_btag_dr4b2_worwmu_eta0_ff",name="Bukin inclusive Chikuma",debug=debug)
        set_properties_histogram(h_Chikuma,counter)
        list_tuple_h1D.append([h_Chikuma,"1 over Peak of Bukin fit of OneMu/bParton (Chikuma Inverse)"])
        counter+=1
    # done if
    if debug:
        print "list_tuple_h1D",list_tuple_h1D
    outputfileName=path+"PtReco"
    if addMoriond:
        outputfileName+="_Moriond" 
    if addTrunk:
        outputfileName+="_Trunk" 
    if addAdrianBug:
        outputfileName+="_Bug" 
    if addAdrianFixed:
        outputfileName+="_Fixed" 
    if addAdrianFixedInversed:
        outputfileName+="_FixedInversed"
    if addChikuma:
        outputfileName+="_Chikuma"
    #overlayHistograms(list_tuple_h1D,outputfileName,"pdf","histo",False)
    #overlayHistograms(list_tuple_h1D,fileName=outputfileName,extensions="pdf",option="histo",addfitinfo=False,min_value=-1,max_value=-1,legend_info=[0.50,0.50,0.88,0.72,72,0.027,0],plot_option="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets from llbb}",0.04,13,0.60,0.88,0.05),debug=False)
    overlayHistograms(list_tuple_h1D,fileName=outputfileName,extensions="pdf",option="histo",addfitinfo=False,min_value=0.95,max_value=1.4,min_value_ratio=0.98,max_value_ratio=1.2,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.20,0.50,0.88,0.72,72,0.030,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)
# done

# run
overlay()
