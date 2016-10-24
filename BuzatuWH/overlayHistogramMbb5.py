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

debug=False


#scalesstring="TruthWZ,Parton,Nominal,OneMu,Regression,PtRecoRunIIStyle,PtRecoMoriondllbbOneMuPartonBukinNew,PtRecoTrunkllbbOneMuPartonBukinNew,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"
#scalesstring="TruthWZ,Nominal,OneMu,Regression,PtRecoRunIIStyle,PtRecoMoriondllbbOneMuPartonBukinNew,PtRecoTrunkllbbOneMuPartonBukinNew,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"
#scalesstring="TruthWZ,Nominal,OneMu,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue,Regression"
#scalesstring="Nominal,OneMu,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue,Regression"
#scalesstring="TruthWZ,Nominal,OneMu,PtRecoNowllbbOneMuTruthWZNoneNewTrue"
scalesstring="PtRecoRunIIStyle,PtRecoTrunkllbbOneMuPartonBukinNew"
#scalesstring="PtRecoRunIStyle,PtRecoTrunkllbbOneTruthWZNoneOld"
list_variation=scalesstring.split(",")
list_sld="inclusive,2hadronic,1hadronic1semileptonic,2semileptonic".split(",")
#list_processes="llbb,ttbar,STopWt,ZqqZll,ZeeMG,ZmumuMG".split(",")
#list_processes="llbb,ttbar,STopWt,WqqZll,ZqqZll,ZeeMG,ZmumuMG".split(",")
list_processes="llbb".split(",")
date="160617_3"

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
        #if h.Integral()!=0:
        #    h.Scale(1/h.Integral()) # scale to unit area
        #else:
        #    print "WARNING integral zero for inputFile",inputFile,"histogramName",histogramName
        h.SetLineColor(histogramColor)
        h.GetXaxis().SetTitle("mbb [GeV]")
        h.GetYaxis().SetTitle("Normalised to unit area")        
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

for process in list_processes:
    list_histogram=[]
    for i,variation in enumerate(list_variation):
        list_histogram.append([variation,"/Users/abuzatu/data/histos_mbb/"+date+"/histos_mbb_"+process+"_inclusive.root","",variation+"_mbb","",list_color[i]])    
    list_tuple_h1D=get_list_tuple_h1D()
    overlayHistograms(list_tuple_h1D,fileName="overlay_comparing_variation_"+process,extensions="pdf",option="histo+Bukin",doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.45,0.30,0.48,0.72,72,0.030,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{"+process+"}?#bf{"+variation+"}",0.04,13,0.37,0.88,0.03),line_option=([0,0.5,1,0.5],2),debug=debug)
    # done loop over variations
# done loop over sld

#################################################################
################### Finished ####################################
#################################################################
