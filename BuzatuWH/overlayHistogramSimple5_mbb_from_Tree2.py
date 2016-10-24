#!/usr/bin/python
from HelperPyRoot import *
ROOT.gROOT.SetBatch(True)

total = len(sys.argv)
# number of arguments plus 1
if total!=1:
    print "You need some arguments, will ABORT!"
    print "Ex: ",sys.argv[0]," "
    assert(False)
# done if

#################################################################
################### Configurations ##############################
#################################################################

debug=True

#list_histogram=[
# [legend,inputFile,histogramPath,histogramName,histogramRename,color]
#["20.1 hadronic","/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_hadronic_Bukin","",1],
#["20.7 hadronic","/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_hadronic_Bukin","",2],
#["20.1 muon","/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_muon_Bukin","",2],
#["20.1 electron","/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_electron_Bukin","",4],
#["20.7 semileptonic","/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_semileptonic_Bukin","",3],
#]

#################################################################
################### Functions##### ##############################
#################################################################

def get_list_tuple_h1D():
    list_tuple_h1D=[]
    for i,histo in enumerate(list_histogram):
        legendName=histo[0]
        inputFile=histo[1]
        histogramPath=histo[2]
        histogramName=histo[3]
        histogramRename=histo[4]
        histogramColor=histo[5]
        h=retrieveHistogram(inputFile,histogramPath,histogramName,histogramRename,debug)
        h.SetLineColor(histogramColor)
        h.GetXaxis().SetTitle("di-b-jet invariant mass [GeV]")
        h.GetYaxis().SetTitle("Arbitrary units")
        h.GetYaxis().SetTitleOffset(1.4)
        list_tuple_h1D.append([h,legendName])
        #subRange=[40,200]
        #list_tuple_h1D[i][0]=get_histo_subRange(list_tuple_h1D[i][0],subRange,debug)
        #list_tuple_h1D[i][0].GetXaxis().SetTitle("Di-b-jet invariant mass [GeV]")
        #list_tuple_h1D[i][0].GetYaxis().SetTitle("Arbitrary units")
        #list_tuple_h1D[i][0].SetLineColor(list_color[i])
  
    # done for
    if debug:
        print "list_tuple_h1D"
        for mytuple in list_tuple_h1D:
            print mytuple
    # done all
    return list_tuple_h1D
# done function



#################################################################
################### Run #########################################
#################################################################

#list_sld="inclusive,2hadronic,1hadronic1semileptonic,2semileptonic".split(",")
list_sld="2semileptonic".split(",")
#list_correction="TruthWZ,Nominal,OneMu,OneMuNuTruth,PtRecoTruthWZNone,Regression".split(",")
#list_option="histo,histo+Bukin,Bukin".split(",")

#list_sld="inclusive".split(",")
#list_color=[7,1,4,2,3]
#list_correction="TruthWZ,Nominal,OneMu,PtRecoTruthWZNone,Regression".split(",")
#list_color=[2,9]
#list_correction="PtRecoTruthWZNone,PtRecoPartonBukin".split(",")
list_color=[1,4,2,3]
list_correction="Nominal,OneMu,PtRecoTruthWZNone,Regression".split(",")
#list_correction="Nominal,OneMu,PtRecoTruthWZNone".split(",")
#list_correction="Parton,TruthWZ".split(",")
list_option="histo+Bukin".split(",")
dict_correction_correctionLegend={
"Nominal":"Standard correction",
"OneMu":"after muon-in-jet",
"PtRecoTruthWZNone":"after PtReco",
"Regression":"after Regression",
"Parton":"Parton",
"TruthWZ":"TruthWZ",
}

for sld in list_sld:
    list_histogram=[]
    name=""
    for i,correction in enumerate(list_correction):
        list_histogram.append([dict_correction_correctionLegend[correction],"/Users/abuzatu/data/histos_mbb/histos_mbb_llbb_"+sld+".root","",correction+"_mbb","",list_color[i]])
        name+="_"+correction
    list_tuple_h1D=get_list_tuple_h1D()
    print type(list_histogram[0][0])
    for option in list_option:
        overlayHistograms(list_tuple_h1D,fileName="overlay_"+sld+name,extensions="pdf",option=option,doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,significantDigits=("3","1","1","3"),min_value=-1,max_value=-1,doRatioPad=False,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.63,0.35,0.88,0.65,72,0.037,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{ZH to llbb 2 jet 2 b-tag}?#bf{"+sld+"}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)

#################################################################
################### Finished ####################################
#################################################################
