#!/usr/bin/python
from HelperPyRoot import *
ROOT.gROOT.SetBatch(True)

debug=False

string_scale="Nominal,OneMu,PtRecoBukin,Regression"
#string_scale="Nominal"
list_scale=string_scale.split(",")
string_variation="inclusive,0,1,2"
list_variation=string_variation.split(",")
list_color=[1,2,4,6]
for scale in list_scale:
    if debug:
        print "scale",scale
    list_tuple_h1D=[]
    for i,variation in enumerate(list_variation):
        if debug:
            print "variation",variation
        histoName="h_"+scale+"_"+variation
        h=retrieveHistogram("./Mbb.root","",histoName,"",debug)
        h.SetLineColor(list_color[i])
        list_tuple_h1D.append((h,variation))
    # done for loop over variation
    overlayHistograms(list_tuple_h1D,fileName="overlay_EtaStudy_"+scale,extensions="pdf",option="histo+Bukin",addfitinfo=True,min_value=-1,max_value=-1,min_value_ratio=0.0,max_value_ratio=1.2,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.12,0.50,0.30,0.82,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),debug=False)
# done for loop over scales
