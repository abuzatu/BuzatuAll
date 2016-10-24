#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *



total = len(sys.argv)
# number of arguments plus 1
if total!=9:
    print "You need some arguments, will ABORT!"
    print "Ex: ./createPtReco.py FolderInput         Process         NrEntries  Initial   Target           doNormal     FolderOutput debug"
    print "Ex: ./createPtReco.py ./                  llbb            -1         OneMu     Parton,TruthWZ   True,False   161010_2     0"
    print "Ex: ./createPtReco.py 161007_2_CxAOD_24_7 ggA400ToZH250   -1         OneMu     TruthWZ          True         161010_2     0"
    print "Ex: ./createPtReco.py 161009_4_CxAOD_24-7 llcc            -1         OneMu     TruthWZ          True         161010_2     0"
    assert(False)
# done if

import ROOT
ROOT.gROOT.SetBatch(True)

FolderInput=sys.argv[1]
Process=sys.argv[2]
NumEvents=sys.argv[3]
string_InitialName=sys.argv[4]
string_TargetName=sys.argv[5]
string_doNormalName=sys.argv[6]
FolderOutput=sys.argv[7]
debug=bool(int(sys.argv[8]))

#debug=True
path="~/data/histos_PtReco/"+FolderOutput # no need of / at the end
fileName="~/data/Tree/"+FolderInput+"/tree_"+Process+".root"
treeName="perjet"
numEvents=int(NumEvents)
#doNormal=False # True: Reco/Gen; False: Gen/Reco.
#list_doNormal=[True,False]
list_Initial=string_InitialName.split(",")
list_Target=string_TargetName.split(",")
list_doNormal=[]
if debug:
    print "string_doNormalName",string_doNormalName
for doNormalName in string_doNormalName.split(","):
    if doNormalName=="True":
        list_doNormal.append(True)
    elif doNormalName=="False":
        list_doNormal.append(False)
    else:
        print "doNormalName",doNormalName,"must be True or False. Will ABORT!!!"
        assert(False)
if debug:
    print "list_doNormal",list_doNormal


list_jettype="hadronic,semileptonic".split(",")
#list_jettype="inclusive,hadronic,muon,electron".split(",")
#list_jettype="muon".split(",")
#list_jettype="electron".split(",")
#list_jettype="inclusive".split(",")
#list_jettype="semileptonic".split(",")

# 125 GeV Higgs boson as signal
if True:
    dict_jettype_binedgesstring={
        #"inclusive": "20,25,30,35,40,45,50,55,60,65,70,80,90,100,130,300",
        #"inclusive": "20,60,300",
        "hadronic"         : "20,25,30,35,40,45,50,55,60,65,70,80,90,100,130,300",
        "semileptonic"     : "20,30,35,40,50,60,70,80,90,100,130,300",
        #"muon"     : "20,30,40,50,60,70,80,90,100,130,300",
        #"electron" : "20,35,50,300"
        }
# end if

# ggA800ToZH500
if False:
  dict_jettype_binedgesstring={
      "hadronic"         : "20,40,60,95,110,125,135,150,165,175,185,195,205,220,235,245,260,280,300,325,355,600",
      "semileptonic"     : "20,90,125,155,185,220,265,600",
}

# no more Gauss fits, as they do not fit well the distributions
list_valuetype="None,NoneMedian,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
#list_valuetype="None,NoneMedian,Bukin,BukinMedian".split(",")
#list_valuetype="NoneMedian".split(",")
#list_valuetype="Bukin,BukinMedian".split(",")
#list_valuetype="Bukin".split(",")
dict_valuetype_fitname={
"None"        : "None",
"NoneMedian"  : "None",
"Gauss"       : "Gauss",
"GaussMedian" : "Gauss",
"Bukin"       : "Bukin",
"BukinMedian" : "Bukin"
}

# Pt bins
dict_jettype_bins={}
dict_jettype_binedgeslist={}
for jettype in list_jettype:
    binedgesstring=dict_jettype_binedgesstring[jettype]
    dict_jettype_bins[jettype]=get_list_intervals(string_values=binedgesstring,addUnderflow=True,addOverflow=True,debug=debug)
    dict_jettype_binedgeslist[jettype]=get_array_values(binedgesstring,debug)
# done loop over jettype

# Eta bins
#string_AbsEtaBin="0.0,1.0,1.4,1.6,2.5"
#list_AbsEtaBin=get_list_intervals(string_values=string_AbsEtaBin,addUnderflow=False,addOverflow=False,debug=debug)
#inclusive_bin=(float("-inf"),float("inf"))
#list_AbsEtaBin.insert(0,inclusive_bin)
#if debug:
#    for AbsEtaBin in list_AbsEtaBin:
#        print AbsEtaBin, "string", get_bin_string(AbsEtaBin,10,debug)
#    print "find bin of 1.45",find_bin_in_list(list_AbsEtaBin,1.45,debug)

#exit()

def get_histoname(jettype,bin,doNormal,debug):
    return jettype+"_"+get_bin_string(bin,1,debug)+"_doNormal_"+str(doNormal)
# end function

def readTreePtReco(fileName,treeName,numEvents,doNormal,debug=False):
    # open file
    file=TFile(fileName,"READ")
    if not file.IsOpen():
        print "File",fileName,"does not exist, so will abort"
        assert(False)
    # open tree
    tree=file.Get(treeName)
    if tree==None:
        print "tree",treeName,"doesn't exist in file",fileName
        assert(False)
    # decide the number of events we run on
    nrEntries=tree.GetEntries()
    if numEvents<0 or numEvents>nrEntries:
        numEvents=nrEntries
        
    outputFile=TFile(path+"/PtReco_histos_"+Process+"_"+Initial+"_"+Target+"_"+str(doNormal)+".root","Recreate")
    
    dict_histoname_histo={}
    for jettype in list_jettype:
        bins=dict_jettype_bins[jettype]
        for bin in bins:
            histoname=get_histoname(jettype,bin,doNormal,debug)
            dict_histoname_histo[histoname]=TH1F(histoname,histoname, 70,0.02,2.82)
        # done loop over intervals
    # done loop over jettype
    # 
    if debug:
        for histoname in dict_histoname_histo:
            histo=dict_histoname_histo[histoname]
            print histo


    if debug:
        print "******* Star loop over tree entries ****"
    # loop over entries in tree
    for i, entry in enumerate(tree):
        if i>=numEvents:
            continue
        if debug:
            print "******* new entry ",i," **********"
        Reco=getattr(entry,RecoName) # not needed, flat tree in GeV, *0.001 # MeV -> GeV
        Gen =getattr(entry,GenName)  # not needed, flat tree in GeV *0.001 # MeV -> GeV
        if doNormal:
            Ratio=ratio(Gen,Reco)
        else:
            Ratio=ratio(Reco,Gen)
        NrMu=getattr(entry,"nrMu")
        NrEl=getattr(entry,"nrEl")
        if debug:
            print "NrMu",NrMu,"NrEl",NrEl,"Reco",Reco,"Gen",Gen,"doNormal",doNormal,"Ratio",Ratio

        # jettype category definition
        dict_jettype_select={}
        dict_jettype_select["hadronic"]= NrMu==0 and NrEl==0
        dict_jettype_select["semileptonic"]= NrMu>=1 or NrEl>=1
        #dict_jettype_select["inclusive"]= True
        #dict_jettype_select["hadronic"]= NrMu==0 and NrEl==0
        #dict_jettype_select["muon"]= NrMu>=1 and NrEl==0
        #dict_jettype_select["electron"]= NrEl>=1 # includes also a muon sometimes
        # but categories are orthogonal
        if debug:
            print "dict_jettype_select",dict_jettype_select

        # loop over the jettype
        for jettype in list_jettype:
            if debug:
                print "jettype="+jettype
            if dict_jettype_select[jettype]==False:
                continue
            # if here, this jet passes this jettype requirement
            # for this jettype, find in what bin the Reco falls into
            bins=dict_jettype_bins[jettype]
            if debug:
                print "bins",bins
            bin=find_bin_in_list(bins,Reco,debug)
            if debug:
                print "bin",bin
            # for this jettype it is for this bin that we fill the histograms
            histoname=get_histoname(jettype,bin,doNormal,debug)
            dict_histoname_histo[histoname].Fill(Ratio)
        # end loop over jettypes
    # end loop over the entries in the tree
    if debug:
        print "******* End loop over tree entries ****"

    #return 0

    if debug:
        print "******* Start create PtReco *****" 

    # create PtReco histograms
    dict_histonamePtReco_histoPtReco={}
    for jettype in dict_jettype_bins:
        if debug:
            print "jettype="+jettype
        binedgeslist=dict_jettype_binedgeslist[jettype]
        if debug:
            print "binedgeslist",binedgeslist
        numpyarraybinedges=numpy.array(binedgeslist)
        if debug:
            print "numpyarraybinedges",numpyarraybinedges
        for valuetype in list_valuetype:
            if debug:
                print "valuetype",valuetype
            histonamePtReco="PtReco_"+jettype+"_"+valuetype
            if debug:
                print "histonamePtReco",histonamePtReco
            dict_histonamePtReco_histoPtReco[histonamePtReco]=TH1F(histonamePtReco,histonamePtReco,len(binedgeslist)-1,numpy.array(binedgeslist))
            bins=dict_jettype_bins[jettype]
            for j,bin in enumerate(bins):
                if debug:
                    print "j",j,"bin",bin
                histoname=get_histoname(jettype,bin,doNormal,debug)
                if debug:
                    print "histoname",histoname
                histo=dict_histoname_histo[histoname]
                if debug:
                    print "histo",histo
                fitname=dict_valuetype_fitname[valuetype]
                if debug:
                    print "fitname",fitname
                canvasname=path+"/correction_"+Initial+"_"+Target+"_"+histoname
                f,result_fit=fit_hist(h=histo.Clone(),addMedianInFitInfo=True,fit=fitname,plot_option="",doValidationPlot=True,canvasname=canvasname,debug=debug)
                if debug:
                    print "f",f,"type(f)",type(f)
                    print "j",j,"bin",bin,"fitname",fitname,"result_fit (median,height,mean,sigma)",result_fit
                if "Median" in valuetype:           
                    choice=result_fit[0] # median
                else:
                    choice=result_fit[2] # mean or peak
                # done if
                if debug:
                    print "choice",choice
                if doNormal:
                    value=choice[0]
                    error=choice[1]
                else:
                    value=ratio(1,choice[0])
                    error=0 # to do error propagation
                dict_histonamePtReco_histoPtReco[histonamePtReco].SetBinContent(j,value)
                dict_histonamePtReco_histoPtReco[histonamePtReco].SetBinError(j,error)
            # done loop over bins
        # done loop over fitname
    # done loop over jettype
    outputFile.Write()
    outputFile.Close()
    return True
# ended function


# run
for Initial in list_Initial:
    RecoName=Initial+"_Pt"
    for Target in list_Target:
        GenName =Target+"_Pt"
        for doNormal in list_doNormal:
            readTreePtReco(fileName,treeName,numEvents,doNormal,debug)
        # done loop over normal
    # done loop over Target
# done loop over Initial


