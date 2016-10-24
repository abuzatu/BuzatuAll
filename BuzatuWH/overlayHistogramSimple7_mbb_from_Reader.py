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
        h=retrieveHistogram(inputFile,histogramPath,histogramName,histogramRename,debug).Clone()
        h.SetLineColor(histogramColor)
        list_tuple_h1D.append([h,legendName])
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

inputFileName="/Users/abuzatu/data/histos_mbb_fromReader/submitDir_good_all3files/hist-ZllH125.root"
list_ptv="0_150ptv,200ptv".split(",")
list_scale="GSC,OneMu,PtReco,KF".split(",")
dict_scale_name={
"GSC":"GSC",
"OneMu":"OneMu",
"PtReco":"PtReco",
"KF":"KF"
}
list_color=[1,1,1,1]
list_option="Bukin".split(",")

for ptv in list_ptv:
    list_histogram=[]
    name=""
    for i,scale in enumerate(list_scale):
        list_histogram.append([scale,inputFileName,"","qqZllH125_2tag2jet_"+ptv+"_SR_"+scale+"_mBB","",list_color[i]])
        name+="_"+scale
    list_tuple_h1D=get_list_tuple_h1D()
    print type(list_histogram[0][0])
    #subRange=[60,200]
    #list_tuple_h1D[i][0]=get_histo_subRange(list_tuple_h1D[i][0],subRange,debug)
    #list_tuple_h1D[i][0].GetXaxis().SetTitle("Di-b-jet invariant mass [GeV]")
    #list_tuple_h1D[i][0].GetYaxis().SetTitle("Arbitrary units")
    #list_tuple_h1D[i][0].SetLineColor(4)
    for option in list_option:
        overlayHistograms(list_tuple_h1D,fileName="overlay_mbb_from_Reader_ptv_"+ptv+"_"+name,extensions="pdf",option=option,doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.15,0.40,0.35,0.82,72,0.037,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{llbb 2jet 2tag}?#bf{ptv "+ptv+"}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)

#################################################################
################### Finished ####################################
#################################################################
