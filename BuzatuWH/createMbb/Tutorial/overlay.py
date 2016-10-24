#!/usr/bin/python
from HelperPyRoot import *
debug=True

string_variation="Nominal,OneMu,PtRecoBukin,Regression"
list_variation=string_variation.split(",")
list_tuple_h1D=[]
for variation in list_variation:
    if debug:
        print "variation",variation
    h=retrieveHistogram("./histos.root","",variation,"",debug)
    list_tuple_h1D.append((h,variation))
# done for loop

overlayHistograms(list_tuple_h1D,legend_info=[0.20,0.50,0.48,0.72,72,0.037,0],option="histo+Gauss",min_value_ratio=0.0,max_value_ratio=1.2)
#overlayHistograms(list_tuple_h1D,fileName="overlay",extensions="pdf",option="histo+Gauss",addfitinfo=True,min_value=-1,max_value=-1,min_value_ratio=0.0,max_value_ratio=1.2,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.20,0.50,0.48,0.72,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),debug=False)
