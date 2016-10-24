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

Process="ZHll125"
inputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_Index_NominalPt_Decay.root"
fileNamePrefix="~/data/histos_PtReco/Response/"

#################################################################
################### Run ########## ##############################
#################################################################

list_Index="0_1,1_2".split(",")
list_NominalPt="20_50,50_75,75_100,100_300".split(",")
list_Decay="0_1,1_2".split(",")
list_Scale="Nominal,OneMu,PtRecoRunIIStyle,Regression".split(",")
list_Par="Par1,Par2,Ratio".split(",")
list_Fit="None,Gauss".split(",")

def get_info(Par,debug):
    if Par=="Par1":
        info=[0.5,1.5,-1,-1]
    elif Par=="Par2":
        info=[0.0,0.5,-1,-1]
    elif Par=="Ratio":
        info=[0.0,0.5,-1,-1]
    else:
        print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
        assert(False)
    return info
# done function

def get_fitInfoName(Fit,Par,debug):
    fitInfoName=""
    if Fit=="None":
        if Par=="Par1":
            fitInfoName="Histo_mean"
        elif Par=="Par2":
            fitInfoName="Histo_RMS"
        elif Par=="Ratio":
            fitInfoName="Histo_reso"
        else:
            print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
            assert(False)
    elif Fit=="Gauss":
        if Par=="Par1":
            fitInfoName="Gauss_mean"
        elif Par=="Par2":
            fitInfoName="Gauss_sigma"
        elif Par=="Ratio":
            fitInfoName="Gauss_reso"
        else:
            print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
            assert(False)
    elif Fit=="Bukin":
        if Par=="Par1":
            fitInfoName="Bukin_peak"
        elif Par=="Par2":
            fitInfoName="Bukin_width"
        elif Par=="Ratio":
            fitInfoName="Bukin_reso"
        else:
            print "Par",Par,"not known. Choose Par1, Par2, Ratio. Will ABORT!!!"
            assert(False)
    else:
        print "Fit",Fit,"not known. Choose None, Gauss, Bukin. Will ABORT!!!"
        assert(False)
    return fitInfoName
# done function

for Index in list_Index:
    for Decay in list_Decay:
        for Scale in list_Scale:
            for Fit in list_Fit:
                for Par in list_Par:
                    info=get_info(Par,debug)
                    fitInfoName=get_fitInfoName(Fit,Par,debug)
                    fileNameSuffix="Index_"+Index+"_Decay_"+Decay+"_"+Scale+"_"+fitInfoName
                    textSuffix="?#bf{"+fileNameSuffix+"}"
                    list_tuple_h1D=[]
                    for j,NominalPt in enumerate(list_NominalPt):
                        histoName="Index_"+Index+"_NominalPt_"+NominalPt+"_Decay_"+Decay+"_"+Scale+"_Pt_over_Parton_Pt_"+Fit+"_"+Par
                        if debug:
                            print "histoName",histoName
                        h=retrieveHistogram(inputFileName,"",histoName,"",debug)
                        h.SetLineColor(list_color[j])
                        h.GetXaxis().SetTitle("Absolute value of Eta at Nominal scale")
                        h.GetYaxis().SetTitle(Par+" of pT relative to b-Parton pT")
                        list_tuple_h1D.append((h,"NominalPt "+NominalPt))
                    # done for loop over Fit
                    overlayHistograms(list_tuple_h1D,fileName=fileNamePrefix+"overlay_"+fileNameSuffix,extensions="pdf,png",option="histo",addfitinfo=False,min_value=info[0],max_value=info[1],min_value_ratio=info[2],max_value_ratio=info[3],statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.12,0.65,0.25,0.88,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}"+textSuffix,0.03,13,0.40,0.88,0.05),line_option=([20,1,300,1],6),debug=False)
# done all the for loops

exit()
