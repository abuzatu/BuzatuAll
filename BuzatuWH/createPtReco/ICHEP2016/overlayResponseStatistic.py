#!/usr/bin/python
from HelperPyRoot import *
ROOT.gROOT.SetBatch(True)
debug=True

doPt=True
doEta=False

#################################################################
################### Test ########################################
#################################################################

#################################################################
################### Configurations ##############################
#################################################################

#Process="ZHll125"
Process="llbb"
#inputFileName="~/data/histos_PtReco/160601_7/perjet_histos_process_"+Process+"_merged_Index_AbsEta_Decay.root"
inputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_Index_AbsEta_Decay.root"
fileNamePrefix="~/data/histos_PtReco/Response/"

#################################################################
################### Run ########## ##############################
#################################################################

list_Index="0_1,1_2,0_2".split(",")
list_AbsEtax10="0_25".split(",")
list_Decay="0_1,1_2,2_3".split(",")
#list_Scale="Nominal,OneMu,PtRecoRunIIStyle,Regression,PtRecollbbOneMuPartonBukinMedianNewFalse".split(",")
#string_scale=""
#string_scale+="PtRecoRunIIStyle,Nominal,OneMu,PtRecoRunIStyle,Regression"
#string_scale+="PtRecoRunIIStyle,Nominal,OneMu,PtRecoRunIStyle,Regression"
#string_scale+=",PtRecoRunIIStyle,PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonGaussNewTrue,PtRecollbbOneMuPartonGaussMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue"
#string_scale+="PtRecoRunIIStyle,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZGaussNewTrue,PtRecollbbOneMuTruthWZGaussMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue"
#string_scale+=",PtRecoRunIIStyle,PtRecollbbOneMuPartonNoneNewFalse,PtRecollbbOneMuPartonGaussNewFalse,PtRecollbbOneMuPartonGaussMedianNewFalse,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse"
#string_scale+="PtRecoRunIIStyle,PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZGaussNewFalse,PtRecollbbOneMuTruthWZGaussMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse"

string_scale=""
#string_scale+="PtRecoRunIIStyle,Regression"
#string_scale+="PtRecoRunIIStyle,Nominal,OneMu,PtRecoRunIStyle,Regression"
#string_scale+="PtRecollbbOneMuPartonGaussNewTrue,PtRecollbbOneMuPartonGaussMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue"
#string_scale+="PtRecollbbOneMuPartonNoneNewFalse,PtRecollbbOneMuPartonGaussNewFalse,PtRecollbbOneMuPartonGaussMedianNewFalse,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse"
#string_scale="PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse,Regression"
#string_scale="PtRecollbbOneMuPartonGaussNewTrue,PtRecollbbOneMuPartonGaussMedianNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue,PtRecollbbOneMuPartonGaussNewFalse,PtRecollbbOneMuPartonGaussMedianNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse,"
#string_scale="PtRecollbbOneMuPartonGaussMedianNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse"
#string_scale="PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse,Regression"
#string_scale="PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewTrue,PtRecollbbOneMuPartonBukinMedianNewFalse,Regression"
#string_scale= "PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZGaussNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue"
string_scale= "PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue"

list_Scale=string_scale.split(",")
list_Par="Par1,Par2,Ratio".split(",") # "Par1,Par2,Ratio"
list_Fit="None".split(",") # ="None,Gauss"

def get_info(Par,debug):
    if Par=="Par1":
        info=[0.6,1.3,-1,-1]
    elif Par=="Par2":
        info=[0.05,0.50,-1,-1]
    elif Par=="Ratio":
        info=[0.05,0.50,-1,-1]
    else:
        print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
        assert(False)
    return info
# done function

def get_legendName(Fit,Par,debug):
    legendName=""
    if Fit=="None":
        if Par=="Par1":
            legendName="Histo mean"
        elif Par=="Par2":
            legendName="Histo RMS"
        elif Par=="Ratio":
            legendName="Histo resolution"
        else:
            print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
            assert(False)
    elif Fit=="Gauss":
        if Par=="Par1":
            legendName="Gauss mean"
        elif Par=="Par2":
            legendName="Histo sigma"
        elif Par=="Ratio":
            legendName="Gauss resolution"
        else:
            print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
            assert(False)
    elif Fit=="Bukin":
        if Par=="Par1":
            legendName="Bukin peak"
        elif Par=="Par2":
            legendName="Bukin width"
        elif Par=="Ratio":
            legendName="Bukin resolution"
        else:
            print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
            assert(False)
    else:
        print "Fit",Fit,"not known. Choose None, Gauss, Bukin. Will ABORT!!!"
        assert(False)
    return legendName
# done function

for Index in list_Index:
    for AbsEtax10 in list_AbsEtax10:
        for Decay in list_Decay:
            for Par in list_Par:
                info=get_info(Par,debug)
                for Fit in list_Fit:
                    list_tuple_h1D=[]
                    for j,Scale in enumerate(list_Scale):
                        fileNameSuffix="Index_"+Index+"_AbsEtax10_"+AbsEtax10+"_Decay_"+Decay+"_"+Fit+"_"+Par
                        textSuffix="?#bf{"+fileNameSuffix+"}"
                        #histoName="Index_"+Index+"_AbsEtax10_"+AbsEtax10+"_Decay_"+Decay+"_"+Scale+"_Pt_over_Parton_Pt_"+Fit+"_"+Par
                        histoName="Index_"+Index+"_AbsEtax10_"+AbsEtax10+"_Decay_"+Decay+"_"+Scale+"_Pt_over_TruthWZ_Pt_"+Fit+"_"+Par
                        if debug:
                            print "histoName",histoName
                        legendName=get_legendName(Fit,Par,debug)
                        h=retrieveHistogram(inputFileName,"",histoName,"",debug)
                        h.SetLineColor(list_color[j])
                        h.GetXaxis().SetTitle("Nominal pT [GeV]")
                        h.GetYaxis().SetTitle(Par+" of pT relative to b-Parton pT")
                        list_tuple_h1D.append((h,Scale))
                    # done for loop over Scale
                    overlayHistograms(list_tuple_h1D,fileName=fileNamePrefix+"overlay_"+fileNameSuffix,extensions="pdf",option="histo",doValidationPlot=False,canvasname="canvasname",addfitinfo=False,addMedianInFitInfo=False,min_value=info[0],max_value=info[1],min_value_ratio=info[2],max_value_ratio=info[3],statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.12,0.65,0.25,0.88,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}",0.03,13,0.60,0.88,0.05),line_option=([20,1,300,1],ROOT.kOrange),debug=False)
#text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}"+textSuffix
# done all the for loops

exit()
