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

inputFileName="/Users/abuzatu/data/histos_mbb_fromReader/submitDir/hist-ZHll125.root"
list_option="histo,histo+Bukin,Bukin".split(",")

list_list_correction=[
    "GSC,OneMu,PtReco1,KF,Regression".split(","),
    "GSC,OneMu,PtReco1,KF".split(","),
    "PtReco1,PtReco2,PtReco3".split(","),
    "PtReco1,Regression".split(","),
    "PtReco1,PtReco2".split(","),
    "PtReco1,PtReco3".split(","),
    "PtReco1,Regression".split(","),
    "PtReco1,OneMu".split(","),
]

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
        list_tuple_h1D.append((h,legendName))
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

for list_correction in list_list_correction:
    list_histogram=[]
    name=""
    for i,correction in enumerate(list_correction):
        list_histogram.append([correction,inputFileName,"","qqZllH125_2tag2pjet_0_500ptv_SR_"+correction+"_mBB","",list_color[i]])
        name+="_"+correction
    # 
    list_tuple_h1D=get_list_tuple_h1D()
    for option in list_option:
        overlayHistograms(list_tuple_h1D,fileName="overlay"+name,extensions="pdf",option=option,doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.60,0.20,0.88,0.72,72,0.037,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)
    # done for oover option
# done for over list_correction


#################################################################
################### Finished ####################################
#################################################################
