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

#list_variation="TruthWZ,Parton,Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,Regression".split(",")
list_variation="TruthWZ,Parton,Nominal,OneMu,Regression,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue".split(",")
list_sld="2hadronic,1hadronic1semileptonic".split(",")
date="160616"

list_histogram=[
    #["20.1 20-0 Nominal","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","Nominal_mbb","",1],
    #["20.7 21-4 Nominal","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","Nominal_mbb","",1],
    #["20.1 20-0 OneMu","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","OneMu_mbb","",2],
    #["20.7 21-4 OneMu","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","OneMu_mbb","",2],
    #["20.1 20-0 PtRecoRunIStyle","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecoRunIStyle_mbb","",3],
    #["20.7 21-4 PtRecoRunIStyle","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecoRunIStyle_mbb","",3],
    #["20.1 20-0 PtRecoRunIIStyle","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecoRunIIStyle_mbb","",4],
    #["20.7 21-4 PtRecoRunIIStyle","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecoRunIIStyle_mbb","",4],
    #["20.1 20-0 Regression","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","Regression_mbb","",5],
    #["20.7 21-4 Regression","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","Regression_mbb","",5],
    #["20.1 20-0 PtRecollbbOneMuPartonBukinNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuPartonBukinNewTrue_mbb","",6],
    #["20.7 21-4 PtRecollbbOneMuPartonBukinNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuPartonBukinNewTrue_mbb","",6],
    #["20.1 20-0 PtRecoMoriondllbbOneMuPartonBukinNew","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecoMoriondllbbOneMuPartonBukinNew_mbb","",6],
    #["20.7 21-4 PtRecoMoriondllbbOneMuPartonBukinNew","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecoMoriondllbbOneMuPartonBukinNew_mbb","",6],
    #["20.1 20-0 PtRecoTrunkllbbOneMuPartonBukinNew","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecoTrunkllbbOneMuPartonBukinNew_mbb","",6],
    #["20.7 21-4 PtRecoTrunkllbbOneMuPartonBukinNew","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecoTrunkllbbOneMuPartonBukinNew_mbb","",2],
    #["20.1 20-0 PtRecoNowllbbOneMuPartonBukinNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecoNowllbbOneMuPartonBukinNewTrue_mbb","",6],
    #["20.7 21-4 PtRecoNowllbbOneMuPartonBukinNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecoNowllbbOneMuPartonBukinNewTrue_mbb","",3],
    #["20.1 20-0 PtRecollbbOneMuPartonNoneNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuPartonNoneNewTrue_mbb","",7],
    #["20.7 21-4 PtRecollbbOneMuPartonNoneNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuPartonNoneNewTrue_mbb","",7],
    #["20.1 20-0 PtRecollbbOneMuTruthWZNoneNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuTruthWZNoneNewTrue_mbb","",1],
    #["20.7 21-4 PtRecollbbOneMuTruthWZNoneNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuTruthWZNoneNewTrue_mbb","",1],
    #["20.1 20-0 PtRecollbbOneMuTruthWZNoneMedianNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuTruthWZNoneMedianNewTrue_mbb","",9],
    #["20.7 21-4 PtRecollbbOneMuTruthWZNoneMedianNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuTruthWZNoneMedianNewTrue_mbb","",9],
]

#list_histogram=[
#["20.7 21-4 Regression","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","Regression_mbb","",1],
#["20.7 21-4 PtRecollbbOneMuPartonNoneNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuPartonNoneNewTrue_mbb","",2],
#["20.1 20-0 Regression","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","Regression_mbb","",1],
#["20.1 20-0 PtRecollbbOneMuPartonNoneNewTrue","/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0_"+sld+"/histos_mbb_llbb.root","","PtRecollbbOneMuPartonNoneNewTrue_mbb","",2],
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
        if h.Integral()!=0:
            h.Scale(1/h.Integral()) # scale to unit area
        else:
            print "WARNING integral zero for inputFile",inputFile,"histogramName",histogramName
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

for sld in list_sld:
    for variation in list_variation:
        list_histogram=[
            ["20.1 20-0 "+variation,"/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_20-0/histos_mbb_llbb_"+sld+".root","",variation+"_mbb","",1],
            ["20.7 21-4 "+variation,"/Users/abuzatu/data/histos_mbb/"+date+"_CxAOD_21-4/histos_mbb_llbb_"+sld+".root","",variation+"_mbb","",2],
        ]
        list_tuple_h1D=get_list_tuple_h1D()
        overlayHistograms(list_tuple_h1D,fileName="overlay_"+sld+"_"+variation,extensions="pdf",option="histo+Bukin",doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.38,0.50,0.88,0.72,72,0.030,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=debug)
    # done loop over variations
# done loop over sld
#for myoption in "histo,histo+Bukin,Bukin".split(","):
#    list_tuple_h1D=get_list_tuple_h1D()
#    overlayHistograms(list_tuple_h1D,fileName="overlay_"+sld+"_all",extensions="pdf",option=myoption,doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=True,addMedianInFitInfo=False,min_value=-1,max_value=-1,min_value_ratio=-1,max_value_ratio=-1,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.38,0.30,0.88,0.72,72,0.030,0],plot_option="HIST",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=debug)
# done loop over variations

#################################################################
################### Finished ####################################
#################################################################
