#!/usr/bin/python
from HelperPyRoot import *
debug=True

#string_variation="Nominal,OneMu,PtRecoBukin,Regression"
#list_variation=string_variation.split(",")
#list_tuple_h1D=[]
#for variation in list_variation:
#    if debug:
#        print "variation",variation
#    h=retrieveHistogram("./histos.root","",variation,"",debug)
#    list_tuple_h1D.append((h,variation))
# done for loop

#overlayHistograms(list_tuple_h1D,legend_info=[0.20,0.50,0.48,0.72,72,0.037,0],option="histo+Gauss",min_value_ratio=0.0,max_value_ratio=1.2)
#overlayHistograms(list_tuple_h1D,fileName="overlay",extensions="pdf",option="histo+Gauss",addfitinfo=True,min_value=-1,max_value=-1,min_value_ratio=0.0,max_value_ratio=1.2,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.20,0.50,0.48,0.72,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),debug=False)

def createHistogram():
    #string_bins="0.0,1.0,1.2,1.4,1.6,2.5"
    string_bins="0.0,1.4,1.6,2.5"
    numpyarray_bins=numpy.array([float(string_bin) for string_bin in string_bins.split(',')])
    numBins=len(numpyarray_bins)-1
    if debug:
        print "numparray_bins",numpyarray_bins
    list_bins=string_bins.split(",")
    inputFile=TFile("tree_llbb.root","READ")
    inputTree=inputFile.Get("perevent")
    outputFile=TFile("a.root","RECREATE")
    h=TH2F("hEta","Eta1 vs Eta2",numBins,numpyarray_bins,numBins,numpyarray_bins)
    inputTree.Project("hEta","fabs(b1_Nominal_Eta):fabs(b2_Nominal_Eta)")
    outputFile.Write()
    outputFile.Close()

#
createHistogram()
plotHistogram(retrieveHistogram(fileName="./a.root",histoName="hEta"),fileName="Eta",plot_option="LEGO")

