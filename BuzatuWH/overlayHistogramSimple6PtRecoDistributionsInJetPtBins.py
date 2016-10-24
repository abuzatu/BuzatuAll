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
    for histo in list_histogram:
        legendName=histo[0]
        inputFile=histo[1]
        histogramPath=histo[2]
        histogramName=histo[3]
        histogramRename=histo[4]
        histogramColor=histo[5]
        h=retrieveHistogram(inputFile,histogramPath,histogramName,histogramRename,debug)
        h.SetLineColor(histogramColor)
        h.SetLineWidth(2)
        h.GetXaxis().SetTitle("Ratio of p_{T} of truth jet to reconstructed after muon-in-jet correction")
        h.GetYaxis().SetTitle("Arbitrary units")
        h.GetYaxis().SetTitleOffset(1.2)
        list_tuple_h1D.append((h,legendName))
    # done for
    if debug:
        print "list_tuple_h1D"
        for mytuple in list_tuple_h1D:
            print mytuple
    # done all
    return list_tuple_h1D
# done function

def get_bin_nameLegend(nameString,debug):
    list_bin=nameString.split("_")
    result="Jet p_{T} "+list_bin[0]+" - "+list_bin[1]+" GeV"
    if debug:
        print "result",result
    return result
# done function

#################################################################
################### Run #########################################
#################################################################

inputFileName="/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_TruthWZ_True.root"
list_sld="hadronic,semileptonic".split(",")
dict_sld_bins={
"hadronic":"20_25,40_45,70_80,130_300",
"semileptonic":"20_30,40_50,70_80,130_300",
}
list_color=[1,4,2,3]
list_option="histo".split(",")

for sld in list_sld:
    list_histogram=[]
    name=""
    for i,binname in enumerate(dict_sld_bins[sld].split(",")):
        list_histogram.append([get_bin_nameLegend(binname,debug),inputFileName,"",sld+"_"+binname+"_doNormal_True","",list_color[i]])
        name+="_"+binname
    list_tuple_h1D=get_list_tuple_h1D()
    print type(list_histogram[0][0])
    for option in list_option:
        overlayHistograms(list_tuple_h1D,fileName="overlay_"+sld,extensions="pdf,png,eps",option=option,doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,significantDigits=("3","3","3","3"),min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.55,0.20,0.88,0.65,72,0.037,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{ZH to llbb 2 jet 2 b-tag}?#bf{"+sld+" jet decay}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)

#################################################################
################### Finished ####################################
#################################################################
