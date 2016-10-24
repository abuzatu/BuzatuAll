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

list_histogram=[
# [legend,inputFile,histogramPath,histogramName,histogramRename,color]
# hadronic
["20.1 at Moriond hadronic","/Users/abuzatu/data/histos_PtReco/PtRecoMoriond/histos_llbb_OneMu_Parton.root","","PtReco_nosld_Bukin","",1],
["20.1 after Moriond hadronic","/Users/abuzatu/data/histos_PtReco/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_hadronic_Bukin","",2],
["20.7 now hadronic","/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_hadronic_Bukin","",3],
# muon 
#["20.1 at Moriond muon","/Users/abuzatu/data/histos_PtReco/PtRecoMoriond/histos_llbb_OneMu_Parton.root","","PtReco_mu_Bukin","",1],
#["20.1 after Moriond muon","/Users/abuzatu/data/histos_PtReco/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_muon_Bukin","",2],
# electron
#["20.1 at Moriond electron","/Users/abuzatu/data/histos_PtReco/PtRecoMoriond/histos_llbb_OneMu_Parton.root","","PtReco_el_Bukin","",1],
#["20.1 after Moriond electron","/Users/abuzatu/data/histos_PtReco/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_electron_Bukin","",2],
# semileptonic (muon+electron combined)
#["20.7 now semileptonic","/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_semileptonic_Bukin","",3],
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
        h.GetXaxis().SetTitle("pT at OneMu [GeV]")
        h.GetYaxis().SetTitle("Correction factor for PtReco")
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

list_tuple_h1D=get_list_tuple_h1D()
overlayHistograms(list_tuple_h1D,fileName="overlay",extensions="pdf",option="histo",doValidationPlot=True,canvasname="canvasname",addHistogramInterpolate=True,addfitinfo=False,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.55,0.50,0.88,0.72,72,0.037,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)

#################################################################
################### Finished ####################################
#################################################################
