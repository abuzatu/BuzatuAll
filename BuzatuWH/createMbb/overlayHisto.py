#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
#from ConfigWH import *
#from HelperWH import *

import copy

print "Start Python"
time_start=time()

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=5:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayHisto.py FolderName Process Options                                                    Debug"
    print "Ex: ./overlayHisto.py 161010_1   llbb    inclusive,2hadronic,1hadronic1semileptonic,2semileptonic   0"
    assert(False)
# done if

FolderName=sys.argv[1]
Process=sys.argv[2]
ProcessShort=Process
Options=sys.argv[3]
debug=bool(int(sys.argv[4]))

#list_color=[7,6,1,2,3,4,5,7,12,9,14,29,38,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#list_color=[ROOT.kGreen+3,ROOT.kMagenta+2,1,4,2,ROOT.kYellow+1,ROOT.kCyan-4,8,9,10]
list_color=[1,2,4,3,5,6,3,7,8]
#debug=True
#list_sld="2hadronic,1hadronic1semileptonic,2semileptonic,inclusive".split(",")
#list_sld="inclusive".split(",")
list_sld=Options.split(",")

#fileName="~/data/histos_mbb/160601_1/histos_mbb_"+Process+".root"
#fileName="~/data/histos_mbb/histos_mbb_"+Process+"_2hadronic.root"
#fileName="~/data/histos_mbb/histos_mbb_"+Process+"_1hadronic1semileptonic.root"
#fileName="~/data/histos_mbb/histos_mbb_"+Process+"_inclusive.root"
dict_scale_color={}
dict_scale_color["TruthWZ"]=12
dict_scale_color["PtRecoGauss"]=ROOT.kCyan
dict_scale_color["Regression"]=2
dict_scale_color["PtRecollbbOneMuPartonMixedNew"]=4
dict_scale_color["OneMu"]=ROOT.kOrange
dict_scale_color["OneMuNu"]=7
dict_scale_color["AllMu"]=8
dict_scale_color["AllMuNu"]=9
dict_scale_color["PtRecoRunIStyle"]=3
dict_scale_color["PtRecoRunIIStyle"]=6
dict_scale_color["Nominal"]=1
dict_scale_color["PtRecoPartonOld"]=ROOT.kOrange
dict_scale_color["PtRecoPartonNew"]=9
dict_scale_color["Parton"]=15
# old
dict_scale_color["PtRecollbbOneMuPartonNoneOldTrue"]=1
dict_scale_color["PtRecollbbOneMuPartonGaussOldTrue"]=2
dict_scale_color["PtRecollbbOneMuPartonBukinOldTrue"]=3
dict_scale_color["PtRecollbbOneMuTruthWZNoneOldTrue"]=4
dict_scale_color["PtRecollbbOneMuTruthWZGaussOldTrue"]=5
dict_scale_color["PtRecollbbOneMuTruthWZBukinOldTrue"]=6
dict_scale_color["PtRecollbbAllMuPartonNoneOldTrue"]=1
dict_scale_color["PtRecollbbAllMuPartonGaussOldTrue"]=2
dict_scale_color["PtRecollbbAllMuPartonBukinOldTrue"]=3
dict_scale_color["PtRecollbbAllMuTruthWZNoneOldTrue"]=4
dict_scale_color["PtRecollbbAllMuTruthWZGaussOldTrue"]=5
dict_scale_color["PtRecollbbAllMuTruthWZBukinOldTrue"]=6
# New
# Parton, True
dict_scale_color["PtRecollbbOneMuPartonBukinNewTrue"]=ROOT.kOrange
dict_scale_color["PtRecollbbOneMuPartonBukinMedianNewTrue"]=3
dict_scale_color["PtRecollbbOneMuPartonNoneNewTrue"]=2
dict_scale_color["PtRecollbbOneMuPartonNoneMedianNewTrue"]=1
dict_scale_color["PtRecollbbOneMuPartonGaussNewTrue"]=2
dict_scale_color["PtRecollbbOneMuPartonGaussMedianNewTrue"]=3
# TruthWZ, True
dict_scale_color["PtRecollbbOneMuTruthWZBukinNewTrue"]=4
dict_scale_color["PtRecollbbOneMuTruthWZBukinMedianNewTrue"]=3
dict_scale_color["PtRecollbbOneMuTruthWZNoneNewTrue"]=2
dict_scale_color["PtRecollbbOneMuTruthWZNoneMedianNewTrue"]=1
dict_scale_color["PtRecollbbOneMuTruthWZGaussNewTrue"]=3
dict_scale_color["PtRecollbbOneMuTruthWZGaussMedianNewTrue"]=4
# Parton, False
dict_scale_color["PtRecollbbOneMuPartonBukinNewFalse"]=4
dict_scale_color["PtRecollbbOneMuPartonBukinMedianNewFalse"]=3
dict_scale_color["PtRecollbbOneMuPartonNoneNewFalse"]=2
dict_scale_color["PtRecollbbOneMuPartonNoneMedianNewFalse"]=1
dict_scale_color["PtRecollbbOneMuPartonGaussNewFalse"]=2
dict_scale_color["PtRecollbbOneMuPartonGaussMedianNewFalse"]=3
# TruthWZ, False
dict_scale_color["PtRecollbbOneMuTruthWZBukinNewFalse"]=4
dict_scale_color["PtRecollbbOneMuTruthWZBukinMedianNewFalse"]=3
dict_scale_color["PtRecollbbOneMuTruthWZNoneNewFalse"]=2
dict_scale_color["PtRecollbbOneMuTruthWZNoneMedianNewFalse"]=1
dict_scale_color["PtRecollbbOneMuTruthWZGaussNewFalse"]=3
dict_scale_color["PtRecollbbOneMuTruthWZGaussMedianNewFalse"]=4

# new
dict_scale_color["PtRecollbbOneMuTruthWZNoneNewTrue"]=2
dict_scale_color["PtRecollbbOneMuTruthWZBukinMedianNewTrue"]=4
dict_scale_color["PtRecollbbOneMuPartonBukinNewTrue"]=ROOT.kYellow+1
dict_scale_color["PtRecoNowllbbOneMuTruthWZNoneNewTrue"]=10
dict_scale_color["PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"]=20
dict_scale_color["PtRecoNowllbbOneMuPartonBukinNewTrue"]=30
dict_scale_color["PtRecoTrunkllbbOneMuPartonBukinNew"]=30
dict_scale_color["Parton"]=ROOT.kCyan-4
dict_scale_color["TruthWZ"]=ROOT.kMagenta+2

#list_color=[1,2,3,4,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#string_scales="Nominal,OneMu,OneMuNu,AllMu,AllMuNu,PtRecoOld,PtRecoNew,Regression"
#string_scales="Nominal,OneMu,OneMuNu,Regression,PtRecoNew"
textoftext="#bf{#it{#bf{ATLAS } Simulation Internal}}?#bf{SM "+ProcessShort+" 2-b-tag}?#bf{both jets > 20 GeV}?#bf{no event weight applied}"
#textoftext="#it{ATLAS} Simulation Internal?#bf{SM "+ProcessShort+" 2-b-tag}?#bf{both jets > 20 GeV}?#bf{no event weight applied}"
list_string_scales=[
    #"TruthWZ",
    #"Parton",
    #"PtRecollbbOneMuTruthWZNoneOld,PtRecollbbOneMuTruthWZGaussOld,PtRecollbbOneMuTruthWZBukinOld,PtRecollbbOneMuPartonNoneOld,PtRecollbbOneMuPartonGaussOld,PtRecollbbOneMuPartonBukinOld",
    #"PtRecollbbOneMuTruthWZNoneNew,PtRecollbbOneMuTruthWZGaussNew,PtRecollbbOneMuTruthWZBukinNew,PtRecollbbOneMuPartonNoneNew,PtRecollbbOneMuPartonGaussNew,PtRecollbbOneMuPartonBukinNew",
    #"Nominal,OneMu,PtRecoRunIIStyle",
    #"Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,Regression",
    #"PtRecoRunIIStyle,Regression",PtRecollbbOneMuPartonBukinNewTrue
    #"Nominal",
    #"PtRecollbbAllMuPartonBukinNew,PtRecollbbAllMuPartonGaussNew,PtRecollbbOneMuPartonBukinNew,PtRecollbbOneMuPartonGaussNew,Regression",
    #"PtRecollbbOneMuPartonMixedNew,Regression,PtRecoBukin,PtRecoGauss,OneMu,Nominal"
    #"OneMu,AllMu,OneMuNu,AllMuNu"
    #"PtRecoRunIIStyle,PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonGaussNewTrue,PtRecollbbOneMuPartonGaussMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue",
    #"PtRecoRunIIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZGaussNewTrue,PtRecollbbOneMuTruthWZGaussMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue",
    #"PtRecoRunIIStyle,PtRecollbbOneMuPartonNoneNewFalse,PtRecollbbOneMuPartonGaussNewFalse,PtRecollbbOneMuPartonGaussMedianNewFalse,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse",
    #"PtRecoRunIIStyle,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZGaussNewFalse,PtRecollbbOneMuTruthWZGaussMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinNewFalse,Regression",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewTrue,PtRecollbbOneMuPartonBukinMedianNewFalse,Regression"
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZGaussNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZGaussNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse",
    #
    #"Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,Regression,PtRecollbbOneMuPartonBukinNewTrue",
    #"Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,Regression,PtRecollbbOneMuPartonBukinNewTrue,TruthWZ",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue,PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonNoneMedianNewTrue",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse,PtRecollbbOneMuPartonNoneNewFalse,PtRecollbbOneMuPartonNoneMedianNewFalse",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse",
    #"Nominal,OneMu,Regression,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse"
    #"Nominal,OneMu,Regression"
    #"OneMu,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue"
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue"
    #"PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse"
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse"
    #"Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,Regression",
    #"Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,Regression",
    #"PtRecoRunIStyle,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue",
    #"TruthWZ,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonNoneMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,OneMu,Nominal,Regression",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonBukinNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonBukinMedianNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonNoneNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonNoneMedianNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZBukinNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZBukinMedianNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZNoneNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZNoneMedianNewTrue",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonBukinNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonBukinMedianNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonNoneNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuPartonNoneMedianNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZBukinNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZBukinMedianNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZNoneNewFalse",
    #"TruthWZ,Parton,PtRecollbbOneMuTruthWZNoneMedianNewFalse",
    #"TruthWZ,Parton,OneMu",
    #"TruthWZ,Parton,Nominal",
    #"TruthWZ,Parton,Regression",
    #"TruthWZ,Parton,PtRecoRunIStyle",
    #"TruthWZ,Parton,PtRecoRunIIStyle",
    #"PtRecoRunIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue",
    #"PtRecoRunIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,Regression",
    #"PtRecoRunIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,Regression,TruthWZ,Parton",
    #"TruthWZ,PtRecollbbOneMuPartonBukinNewTrue",
    #"TruthWZ,PtRecollbbOneMuPartonBukinMedianNewTrue",
    #"TruthWZ,PtRecollbbOneMuPartonNoneNewTrue",
    #"TruthWZ,PtRecollbbOneMuPartonNoneMedianNewTrue",
    #"TruthWZ,PtRecollbbOneMuTruthWZBukinNewTrue",
    #"TruthWZ,PtRecollbbOneMuTruthWZBukinMedianNewTrue",
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneNewTrue",
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneMedianNewTrue",
    #"TruthWZ,PtRecollbbOneMuPartonBukinNewFalse",
    #"TruthWZ,PtRecollbbOneMuPartonBukinMedianNewFalse",
    #"TruthWZ,PtRecollbbOneMuPartonNoneNewFalse",
    #"TruthWZ,PtRecollbbOneMuPartonNoneMedianNewFalse",
    #"TruthWZ,PtRecollbbOneMuTruthWZBukinNewFalse",
    #"TruthWZ,PtRecollbbOneMuTruthWZBukinMedianNewFalse",
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneNewFalse",
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneMedianNewFalse",
    #"TruthWZ,OneMu",
    #"TruthWZ,Nominal",
    #"TruthWZ,Regression",
    #"TruthWZ,PtRecoRunIStyle",
    #"TruthWZ,PtRecoRunIIStyle",
    #"PtRecoRunIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue",
    #"PtRecoRunIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,Regression",
    #"PtRecoRunIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,Regression,TruthWZ,Parton",
    #"Regression,PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonNoneMedianNewTrue",
    #"Regression,PtRecollbbOneMuPartonNoneNewTrue,PtRecoRunIIStyle",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewFalse",
    #"Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,Regression",
    #"PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse"
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue",
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse"
    #"PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse"
    #"PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse,TruthWZ"
    #"TruthWZ,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZNoneMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse"
    # 
    # for mbb
    #"PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,Parton,TruthWZ",
    # for mbb response
    #"PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue",
    #"PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,Parton",
    #"PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,TruthWZ",
    #"PtRecoRunIIStyle,PtRecoTrunkllbbOneMuPartonBukinNew",
    #"PtRecoPartonBukin,PtRecoNowllbbOneMuPartonBukinNewTrue",
    #"PtRecoTruthWZNone,PtRecoNowllbbOneMuTruthWZNoneNewTrue",
    #"PtRecoTruthWZBukinMedian,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue",
    #"Nominal,OneMu,PtRecoTruthWZNone,Regression",
    #"PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue,PtRecoNowllbbOneMuPartonBukinNewTrue",
    #"PtRecoTruthWZNone,PtRecoTruthWZBukinMedian,PtRecoPartonBukin",
    #"OneMu,OneMuNuTruth",
    #"OneMu,OneMuNuTruth,PtRecoTruthWZNone",
    #"Nominal,OneMu,OneMuNuTruth,PtRecoTruthWZNone,Regression"
    #"Nominal,OneMu,PtRecoTruthWZNone,Regression"
    #"Nominal,OneMu,PtRecoTruthWZNone",
    #"Nominal,OneMu,PtRecoTruthWZNone,TruthWZ",
    #"Nominal,OneMu,PtRecoTruthWZNone,PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue",
    #"Nominal,OneMu,PtRecoTruthWZNone,PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue,TruthWZ",
    #"Nominal,OneMu,PtRecoTruthWZNone,PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue,PtRecoHccllccOneMuTruthWZNoneNewTrue",
    #"Nominal,OneMu,PtRecoTruthWZNone,PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue,PtRecoHccllccOneMuTruthWZNoneNewTrue,TruthWZ",
    "Nominal,OneMu,PtRecoTruthWZNone,PtRecoHccllccOneMuTruthWZNoneNewTrue",
    "Nominal,OneMu,PtRecoTruthWZNone,PtRecoHccllccOneMuTruthWZNoneNewTrue,TruthWZ",
    ]

dict_scale_newscale={}
dict_scale_newscale["PtRecoTruthWZNone"]="PtReco trained llbb H125"
dict_scale_newscale["PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue"]="PtReco trained A800 to ZH500"
dict_scale_newscale["PtRecoHccllccOneMuTruthWZNoneNewTrue"]="PtReco trained in llcc H125"
dict_scale_newscale["PtRecollbbOneMuPartonMixedNew"]="PtRecoAverageBukinAndGauss"
# New
# Parton, True
dict_scale_newscale["PtRecollbbOneMuPartonNoneNewTrue"]="Parton True None"
dict_scale_newscale["PtRecollbbOneMuPartonNoneMedianNewTrue"]="Parton True NoneMedian"
dict_scale_newscale["PtRecollbbOneMuPartonGaussNewTrue"]="Porton True Gauss"
dict_scale_newscale["PtRecollbbOneMuPartonGaussMedianNewTrue"]="Parton True GaussMedian"
dict_scale_newscale["PtRecollbbOneMuPartonBukinNewTrue"]="Parton True Bukin"
dict_scale_newscale["PtRecollbbOneMuPartonBukinMedianNewTrue"]="Parton True BukinMedian"
# TruthWZ, True
dict_scale_newscale["PtRecollbbOneMuTruthWZNoneNewTrue"]="TruthWZ True None"
dict_scale_newscale["PtRecollbbOneMuTruthWZNoneMedianNewTrue"]="TruthWZ True NoneMedian"
dict_scale_newscale["PtRecollbbOneMuTruthWZGaussNewTrue"]="TruthWZ True Gauss"
dict_scale_newscale["PtRecollbbOneMuTruthWZGaussMedianNewTrue"]="TruthWZ True GaussMedian"
dict_scale_newscale["PtRecollbbOneMuTruthWZBukinNewTrue"]="TruthWZ True Bukin"
dict_scale_newscale["PtRecollbbOneMuTruthWZBukinMedianNewTrue"]="TruthWZ True BukinMedian"
# Parton, False
dict_scale_newscale["PtRecollbbOneMuPartonNoneNewFalse"]="Parton False None"
dict_scale_newscale["PtRecollbbOneMuPartonNoneMedianNewFalse"]="Parton False NoneMedian"
dict_scale_newscale["PtRecollbbOneMuPartonGaussNewFalse"]="Parton False Gauss"
dict_scale_newscale["PtRecollbbOneMuPartonGaussMedianNewFalse"]="Parton False GaussMedian"
dict_scale_newscale["PtRecollbbOneMuPartonBukinNewFalse"]="Parton False Bukin"
dict_scale_newscale["PtRecollbbOneMuPartonBukinMedianNewFalse"]="Parton False BukinMedian"
# TruthWZ, False
dict_scale_newscale["PtRecollbbOneMuTruthWZNoneNewFalse"]="TruthWZ False None"
dict_scale_newscale["PtRecollbbOneMuTruthWZNoneMedianNewFalse"]="TruthWZ False NoneMedian"
dict_scale_newscale["PtRecollbbOneMuTruthWZGaussNewFalse"]="TruthWZ False Gauss"
dict_scale_newscale["PtRecollbbOneMuTruthWZGaussMedianNewFalse"]="TruthWZ False GaussMedian"
dict_scale_newscale["PtRecollbbOneMuTruthWZBukinNewFalse"]="TruthWZ False Bukin"
dict_scale_newscale["PtRecollbbOneMuTruthWZBukinMedianNewFalse"]="TruthWZ False BukinMedian"

dict_stringscales_variable_info={}
for stringscales in list_string_scales:
    dict_variable_info={}
    #dict_variable_info["mbb_response_TruthWZ"]  =["mbb response to TruthWZ", [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo,histo+Bukin,Bukin"]
    #dict_variable_info["mbb_response_Parton"]  =["mbb response to Parton", [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo,histo+Bukin,Bukin,Bukin"]
    #dict_variable_info["mbb"]                   =["mbb [GeV]",               [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo,histo+Bukin,Bukin"]
    #dict_variable_info["mbb_response_TruthWZ"]  =["mbb response to TruthWZ", [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo,histo+Bukin,Bukin"]
    #dict_variable_info["mbb_response_Parton"]  =["mbb response to Parton", [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo,histo+Bukin,Bukin"]
    dict_variable_info["mbb"]                   =["mcc [GeV]",               [0.13,0.89,0.33,0.89,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo,histo+Bukin,Bukin"]
    # 
    #dict_variable_info["mbb_response_TruthWZ"]  =["mbb response to TruthWZ", [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo"]
    #dict_variable_info["mbb_response_Parton"]  =["mbb response to Parton", [0.60,0.73,0.80,0.73,72,0.03,0],(textoftext,0.02,1,0.75,0.85,0.02),"histo"]

    dict_stringscales_variable_info[stringscales]=dict_variable_info
# 


def overlay(sld,scales,variable,debug):
    fileName="~/data/histos_mbb/"+FolderName+"/histos_mbb_"+Process+"_"+sld+".root"
    fileOutputName="~/data/histos_mbb/"+FolderName+"/"+ProcessShort+"_"+sld+"_"+variable
    info=dict_variable_info[variable]
    xaxisname=info[0]
    yaxisname="Arbitrary units"
    if debug:
        print "fileOutputName",fileOutputName
        print "info",info
        print "xaxisname",xaxisname
        print "yaxisname",yaxisname

    list_tuple_h1D=[]
    for i,scale in enumerate(scales):
        if scale in dict_scale_newscale.keys():
            scalenew=dict_scale_newscale[scale]
        else:
            scalenew=scale
        if debug:
            print "adi i",i,"scale",scale
        fileOutputName+="_"+scale
        hName=scale+"_"+variable
        h=retrieveHistogram(fileName,"",hName,"",debug).Clone()
        if debug:
            print "scale",scale,"integral",h.Integral(1,h.GetXaxis().GetNbins()+1)
        #plotting=(dict_scale_color[scale],0,0,1) # color, marker style, fill style, size for marker and line
        plotting=(list_color[i],0,0,1) # color, marker style, fill style, size for marker and line
        rebin=1
        xaxis=(xaxisname,0.045,0.90) # title, title size, title offsize
        yaxis=(yaxisname,0.040,0.90) # title, title size, title offsize
        update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
        list_tuple_h1D.append([h,scalenew])
    # done creating list_tuple_h1D
    min=-1 #yaxis_size[0] # -1 would rescale automatically
    max=-1 #yaxis_size[1] # -1 would rescale automatically
    legend_info=info[1][:] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    if debug:
        print "legend_info",legend_info
    legend_info_new=legend_info[1]-0.08*len(scales)
    if legend_info_new<0.10:
        legend_info[1]=0.10
    else:
        legend_info[1]=legend_info_new
    if debug:
        print "legend_info",legend_info
    option="HIST" # need "R" in order to be able to plot just the fit "HIST"
    text=info[2]
    filePath=""
    fileName=fileOutputName
    fileExtensions="pdf,png"
    options_fit=info[3] #"histo+Gauss" #"histo,Bukin,histo+Bukin"
    addfitinfo=True
    # 
    for option_fit in options_fit.split(","):
        #overlayHistograms(list_tuple_h1D,fileName,fileExtensions,option_fit,addfitinfo,min,max,legend_info,option,text,debug)
        overlayHistograms(list_tuple_h1D,fileName=fileName,extensions=fileExtensions,option=option_fit,doValidationPlot=False,canvasname="~/data/histos_mbb/canvasname",addfitinfo=True,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=0.8,max_value_ratio=1.2,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=legend_info,plot_option="HIST E",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{"+Process+"}?#bf{"+sld+"}",0.04,13,0.60,0.88,0.05),line_option=([0,0,0,0],1),debug=debug)
# done function

# run        

for stringscales in dict_stringscales_variable_info:
    if debug:
        print "stringscales",stringscales
    dict_variable_info=dict_stringscales_variable_info[stringscales]
    for variable in dict_variable_info:
        if debug:
            print "variable",variable
        if "response" not in variable:
            print "variable not has response",variable
            #newstringscales=stringscales+",TruthWZ"
            newstringscales=stringscales
        else:
            newstringscales=stringscales
        scales=newstringscales.split(",")
        print "scales",scales
        for sld in list_sld:
            print "sld",sld
            overlay(sld,scales,variable,debug)

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
