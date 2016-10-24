#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
import numpy

####################################################
##### Start                                 ########
####################################################

print "Start Python"
debug=False
compare="entries" # entries or yield
pathName=os.environ['initialroot']
#fileName=pathName+"/Paul/140605/WH125.root"
#fileName=pathName+"/Paul/140701/WH125_NoFix.root"
#fileName=pathName+"/Paul/140701/WH125_Fix.root"
fileNamePaul=pathName+"/140916_TruthInfo_HighStats/AnalysisManager.mc12_8TeV_p1328.OneLepton.Hists.root"
fileNameAdrian=pathName+"/140916_TruthInfo_HighStats/extracted/WlvH125.root"
fileNameManuel1=pathName+"/../OneLepton.SignalMC12.125GeV.NoPtReco.root"
fileNameManuel2=pathName+"/../OneLepton.SignalMC12.125GeV.WithPtReco.root"
treeName="WlvH125"
NrEvents=1000
#nrEvents=getNrEntries(fileName,treeName,debug)
btags=["0","1","2L","2M","2T"] # 0:0T; 1:1T; 2:2LB; 3:2MB; 4:2TB
leptons=["el","mu"] # 1:el; 2:mu

def create_dict_btag_lepton_counter(debug):
    dict_btag_lepton_counter={}
    for btag in btags:
        dict_lepton_counter={}
        for lepton in leptons:
            hname="h_"+btag+"_"+lepton
            dict_lepton_counter[lepton]=TH1F(hname,hname,1,0,1)
        # done loop over leptons
        if debug:
            print dict_lepton_counter
        dict_btag_lepton_counter[btag]=dict_lepton_counter
    # done loops over btags
    if debug:
        print dict_btag_lepton_counter
    return dict_btag_lepton_counter
# done function

#
def fill_counters_from_tree(fileName,debug):
    if debug:
        print "fileName",fileName

    dict_btag_lepton_counter=create_dict_btag_lepton_counter(debug)
    if debug:
        print "dict_btag_lepton_counter",dict_btag_lepton_counter

    # open the desied file
    file=TFile(fileName,"READ")
    # check that the file was open correctly and if not, abort
    exists(file,debug)
    # retrieve the desired tree from the file
    tree=file.Get(treeName)
    # check that the tree exists and if not, abort
    # but this does not abort even if the treeName is wrong
    exists(tree,debug)
    if debug:
        print type(tree),tree

    dict_rename_leptons={}
    dict_rename_leptons[1]="el"
    dict_rename_leptons[2]="mu"

    dict_rename_btags={}
    dict_rename_btags[0]="0"
    dict_rename_btags[1]="1"
    dict_rename_btags[2]="2L"
    dict_rename_btags[3]="2M"
    dict_rename_btags[4]="2T"

    #dict_btag_lepton_counter=create_dict_btag_lepton_counter(debug)
    #if debug:
    #    print "dict_btag_lepton_counter",dict_btag_lepton_counter

    # loop over all the entries in the tree
    for i,entry in enumerate(tree):
        if debug:
            if i>9:
                continue
        if debug:
            print "************* next tree entry *************"

        if NrEvents>0:
            if i>NrEvents:
                continue

        eventWeight=getattr(entry,"eventWeight")
        btag=getattr(entry,"btag")
        lepton=getattr(entry,"LeptonType")
        if debug:
            print "btag",dict_rename_btags[btag],"lepton",dict_rename_leptons[lepton],"eventWeight",eventWeight
        dict_btag_lepton_counter[dict_rename_btags[btag]][dict_rename_leptons[lepton]].Fill(0.5,eventWeight)
    # done loop over tree entries
    if debug:
        print "dict_btag_lepton_counter",dict_btag_lepton_counter
    if True:
        print "dict_btag_lepton_counter",dict_btag_lepton_counter
        print "Yield",dict_btag_lepton_counter["2T"]["mu"].Integral()
        for btag in btags:
            for lepton in leptons:
                print "Yield",btag,lepton,dict_btag_lepton_counter[btag][lepton].GetEntries(), dict_btag_lepton_counter[btag][lepton].Integral()

    return dict_btag_lepton_counter
# done function

#
def fill_counters_from_histo(fileName,debug):
    if debug:
        print "fileName",fileName
    dict_btag_lepton_counter=create_dict_btag_lepton_counter(debug)
    if debug:
        print dict_btag_lepton_counter

    dict_rename_leptons={}
    dict_rename_leptons["el"]="El"
    dict_rename_leptons["mu"]="Mu"

    dict_rename_btags={}
    dict_rename_btags["0"]="0"+"BTag"
    dict_rename_btags["1"]="1"+"BTag"
    dict_rename_btags["2L"]="2L"+"BTag"
    dict_rename_btags["2M"]="2M"+"BTag"
    dict_rename_btags["2T"]=""

    histoPath="BaselineOneLepton/pid_161805/"
    histoName="mJJNom"
    name=""
    #histoPathCurrent=histoPath+"SelectedMuTrig"
    #h=retrieveHistogram(fileName,histoPath,histoName,name,debug)
    #exit()


    for btag in btags:
        for lepton in leptons:
            if debug:
                print btag,lepton
            histoPathCurrent=histoPath+"Selected"+dict_rename_leptons[lepton]+"Trig"+dict_rename_btags[btag]+"/"
            if debug:
                print "histoPathCurrent",histoPathCurrent
            h=retrieveHistogram(fileName,histoPathCurrent,histoName,name,debug)
            h.Clone()
            nrentries=h.GetEntries()
            if debug:
                print "nrentries",nrentries
            dict_btag_lepton_counter[btag][lepton]=h

    return dict_btag_lepton_counter
# done function

# call functions
def compare_counters(debug):
    dict1=fill_counters_from_tree(fileNameAdrian,debug)
    #dict1=fill_counters_from_histo(fileNamePaul,debug)
    #dict1=fill_counters_from_histo(fileNameManuel1,debug)
    if debug:
        print "dict1",dict1
    if True:
        print "dict1",dict1
    dict2=fill_counters_from_histo(fileNameManuel2,debug)
    if debug:
        print "dict2",dict2

 

    for btag in btags:
        for lepton in leptons:
            if compare=="entries":
                value1=dict1[btag][lepton].GetEntries()
                value2=dict2[btag][lepton].GetEntries()
                how_to_print="%-7s %-7s %-.0f %-.0f %-.2f"
            elif compare=="yield":
                value1=dict1[btag][lepton].Integral()
                value2=dict2[btag][lepton].Integral()
                how_to_print="%-7s %-7s %-.2f %-.2f %-.2f"
            else:
                print "compare",compare,"should be entries or yield. Will ABORT!"
                exit()
            # if second value is 0, define error to 0
            if value2==0:
                error=0
            else:
                error=(value1-value2)/value2
            print how_to_print % (btag,lepton,value1,value2,error)
# done function





compare_counters(debug)

print "End Python"

####################################################
##### End                                   ########
####################################################
