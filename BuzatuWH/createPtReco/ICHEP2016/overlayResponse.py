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

#Index_0_2_AbsEtax10_0_25_Decay_1_3_Regression_Pt_over_Parton_Pt_Gauss_Ratio
Process="ZHll125"
#inputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_Index_AbsEta_Decay.root"
inputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_Index_NominalPt_Decay.root"
#list_scale="Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,Regression".split(",")
list_scale="Nominal,OneMu,PtRecoRunIIStyle,Regression".split(",")
#list_scale="Nominal".split(",")
#list_scale="Nominal,OneMu".split(",")

dict_textSuffix={
"Index":{"0_1":"Leading jet", "1_2":"Subleading jet", "0_2":"Both jets"},
"AbsEtax10":{"0_10":"AbsEta 0.0-1.0","10_14":"AbsEta 1.0-1.4","14_16":"AbsEta 1.4-1.6","16_25":"AbsEta 1.6-2.5","0_25":"AbsEta inclusive"},
"Decay":{"0_1":"Decay hadronic", "1_2":"Decay muon", "2_3": "Decay electron", "1_3": "Decay semileptonic", "0_3":"Decay inclusive"}
}
list_binVariable="Index,AbsEtax10,Decay".split(",")
list_dict_binVariable_string=[
#{"Index":"0_1","AbsEtax10":"0_25","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"0_25","Decay":"0_1"},
#{"Index":"0_2","AbsEtax10":"0_25","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"0_25","Decay":"1_3"},
#{"Index":"1_2","AbsEtax10":"0_25","Decay":"1_3"},
#{"Index":"0_2","AbsEtax10":"0_25","Decay":"1_2"},
#{"Index":"0_1","AbsEtax10":"0_25","Decay":"2_3"},
#{"Index":"1_2","AbsEtax10":"0_25","Decay":"2_3"},
#{"Index":"0_2","AbsEtax10":"0_25","Decay":"2_3"},
#{"Index":"0_1","AbsEtax10":"0_25","Decay":"1_3"},
#{"Index":"1_2","AbsEtax10":"0_25","Decay":"1_3"},
#{"Index":"0_2","AbsEtax10":"0_25","Decay":"1_3"},
#{"Index":"0_1","AbsEtax10":"0_25","Decay":"0_3"},
#{"Index":"1_2","AbsEtax10":"0_25","Decay":"0_3"},
#{"Index":"0_2","AbsEtax10":"0_25","Decay":"0_3"},
#
#{"Index":"0_1","AbsEtax10":"0_10","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"10_25","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"0_10","Decay":"1_2"},
#{"Index":"0_1","AbsEtax10":"10_25","Decay":"1_2"},
#{"Index":"1_2","AbsEtax10":"0_10","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"10_25","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"0_10","Decay":"1_2"},
#{"Index":"1_2","AbsEtax10":"10_25","Decay":"1_2"},
#
#
#{"Index":"0_1","AbsEtax10":"0_10","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"10_14","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"14_16","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"16_25","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"0_10","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"10_14","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"14_16","Decay":"0_1"},
#{"Index":"1_2","AbsEtax10":"16_25","Decay":"0_1"},
#{"Index":"0_1","AbsEtax10":"0_10","Decay":"1_2"},
#{"Index":"0_1","AbsEtax10":"10_14","Decay":"1_2"},
#{"Index":"0_1","AbsEtax10":"14_16","Decay":"1_2"},
#{"Index":"0_1","AbsEtax10":"16_25","Decay":"1_2"},
{"Index":"1_2","AbsEtax10":"0_10","Decay":"1_2"},
{"Index":"1_2","AbsEtax10":"10_14","Decay":"1_2"},
{"Index":"1_2","AbsEtax10":"14_16","Decay":"1_2"},
{"Index":"1_2","AbsEtax10":"16_25","Decay":"1_2"},
]

dict_statistic={
"None_Par1":("Histo mean",[-1,-1,-1,-1]),
"None_Par2":("Histo RMS",[-1,-1,-1,-1]),
"None_Ratio":("Histo resolution",[-1,-1,-1,-1]),
"Gauss_Par1":("Gauss mean",[0.4,1.5,-1,-1]),
"Gauss_Par2":("Gauss sigma",[0.07,0.30,-1,-1]),
"Gauss_Ratio":("Gauss resolution",[0.07,0.45,-1,-1]),
"Bukin_Par1":("Bukin peak",[-1,-1,-1,-1]),
"Bukin_Par2":("Bukin width",[-1,-1,-1,-1]),
"Bukin_Ratio":("Bukin resolution",[-1,-1,-1,-1]),
}
#list_statistic="None_Par1,None_Par2,None_Ratio,Gauss_Par1,Gauss_Par2,Gauss_Ratio,Bukin_Par1,Bukin_Par2,Bukin_Ratio".split(",")
list_statistic="Gauss_Par1,Gauss_Par2,Gauss_Ratio".split(",")
#list_statistic="Bukin_Par1,Bukin_Par2".split(",")
#list_statistic="None_Par1".split(",")

#################################################################
################### Functions ###################################
#################################################################

def do(dict_binVariable_string,statistic):
    histoPrefix=""
    textSuffix=""
    for i,binVariable in enumerate(list_binVariable):
        if i!=0:
            histoPrefix+="_"
        histoPrefix+=binVariable+"_"+dict_binVariable_string[binVariable]
        textSuffix+="?#bf{"+dict_textSuffix[binVariable][dict_binVariable_string[binVariable]]+"}"
    # done for 
    if debug:
        print "histoPrefix",histoPrefix
        print "textSuffix",textSuffix
    fileNamePrefix="~/data/histos_PtReco/Response/"
    if debug:
        print "fileNamePrefix",fileNamePrefix
    histoSuffix="Pt_over_Parton_Pt_"+statistic
    if debug:
        print "histoSuffix",histoSuffix
    fileNameSuffix=histoPrefix+"_"+histoSuffix
    if debug:
        print "fileNameSuffix",fileNameSuffix
    YAxisPrefix=dict_statistic[statistic][0]
    if debug:
        print "YAxisPrefix",YAxisPrefix
    info=dict_statistic[statistic][1]
    if debug:
        print "info",info
    list_tuple_h1D=[]
    for j,scale in enumerate(list_scale):
        if debug:
            print "scale",scale
        histoName=histoPrefix+"_"+scale+"_"+histoSuffix
        h=retrieveHistogram(inputFileName,"",histoName,"",debug)
        h.SetLineColor(list_color[j])
        h.GetXaxis().SetTitle("Nominal pT [GeV]")
        h.GetYaxis().SetTitle(YAxisPrefix+" of pT relative to b-Parton pT")
        list_tuple_h1D.append((h,scale))
    # done for loop over scale
    overlayHistograms(list_tuple_h1D,fileName=fileNamePrefix+"overlay_"+fileNameSuffix,extensions="pdf",option="histo",addfitinfo=False,min_value=info[0],max_value=info[1],min_value_ratio=info[2],max_value_ratio=info[3],statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.30,0.65,0.48,0.88,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}"+textSuffix,0.04,13,0.60,0.88,0.05),line_option=([20,1,80,1],6),debug=False)
    None
# done function

def doEta(scale,statistic):
    textSuffix=""
    #for i,binVariable in enumerate(list_binVariable):
    #    if i!=0:
    #        histoPrefix+="_"
    #    histoPrefix+=binVariable+"_"+dict_binVariable_string[binVariable]
    #    textSuffix+="?#bf{"+dict_textSuffix[binVariable][dict_binVariable_string[binVariable]]+"}"
    # done for 

    #print "textSuffix",textSuffix
    fileNamePrefix="~/data/histos_PtReco/Response/"
    if debug:
        print "fileNamePrefix",fileNamePrefix
    histoSuffix="Pt_over_Parton_Pt_"+statistic
    if debug:
        print "histoSuffix",histoSuffix
    fileNameSuffix=scale+"_"+histoSuffix
    if debug:
        print "fileNameSuffix",fileNameSuffix
    YAxisPrefix=dict_statistic[statistic][0]
    if debug:
        print "YAxisPrefix",YAxisPrefix
    info=dict_statistic[statistic][1]
    if debug:
        print "info",info
    list_tuple_h1D=[]
    for j,dict_binVariable_string in enumerate(list_dict_binVariable_string):
        if debug:
            print "dict_binVariable_string",dict_binVariable_string
        histoPrefix=""
        for i,binVariable in enumerate(list_binVariable):
            if i!=0:
                histoPrefix+="_"
            histoPrefix+=binVariable+"_"+dict_binVariable_string[binVariable]
        # done for
        if debug:
            print "histoPrefix",histoPrefix
        histoName=histoPrefix+"_"+scale+"_"+histoSuffix
        h=retrieveHistogram(inputFileName,"",histoName,"",debug)
        h.SetLineColor(list_color[j])
        h.GetXaxis().SetTitle("Nominal pT [GeV]")
        h.GetYaxis().SetTitle(YAxisPrefix+" of pT relative to b-Parton pT")
        legendName=dict_textSuffix["AbsEtax10"][dict_binVariable_string["AbsEtax10"]]
        list_tuple_h1D.append((h,legendName))
    # done for loop over scale
    overlayHistograms(list_tuple_h1D,fileName=fileNamePrefix+"overlay_Subleading_Muon_"+fileNameSuffix,extensions="pdf",option="histo",addfitinfo=False,min_value=info[0],max_value=info[1],min_value_ratio=info[2],max_value_ratio=info[3],statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.12,0.65,0.55,0.88,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}"+textSuffix,0.04,13,0.60,0.88,0.05),line_option=([20,1,300,1],6),debug=False)
    None
# done function


#################################################################
################### Run #########################################
#################################################################

if doPt:
    for dict_binVariable_string in list_dict_binVariable_string:
        for statistic in list_statistic:
            do(dict_binVariable_string,statistic)

if doEta:
    for scale in list_scale:
        for statistic in list_statistic:
            doEta(scale,statistic)

#################################################################
################### Finished ####################################
#################################################################
exit()
