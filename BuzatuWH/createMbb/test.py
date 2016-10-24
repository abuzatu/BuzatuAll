#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
#from ConfigWH import *
#from HelperWH import *

import copy

print "Start Python"
time_start=time()

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

####################################################
##### Start                                 ########
####################################################

debug=True
path="~/data/histos_mbb/histos_mbb_"

list_process="llbb,vvbb,ttbar".split(",")
#variable="PtRecollbbOneMuPartonMixedNew_mbb"
#variables="PtRecoBukin_Pt1,PtRecoBukin_Pt2,PtRecoBukin_mbb".split(",")
#variables="Parton_Pt1,Parton_Pt2,Parton_mbb".split(",")
#variables="Nominal_Pt1,Nominal_Pt2,Nominal_mbb".split(",")
#variables="OneMu_Pt1,OneMu_Pt2,OneMu_mbb".split(",")

scales="Parton,TruthWZ,Nominal,OneMu".split(",")
dict_variable_xaxis={
    "Pt1":"Leading jet #p_T# [GeV]",
    "Pt2":"Sub-leading jet #p_T# [GeV]",
    "mbb":"Di-#b#-jet invariant mass (mbb) [GeV]"
}

def do_overlay():
    list_tuple_h1D=[]
    for i,process in enumerate(list_process):
        h=retrieveHistogram(path+process+".root","",variablename,"",debug)
        h.Scale(1/h.Integral())
        h.SetLineColor(i+2)
        h.GetXaxis().SetTitle(xaxis)
        list_tuple_h1D.append([h,process])
    # done loop over process
    if debug:
        print "variablename",variablename
    overlayHistograms(list_tuple_h1D,fileName=variablename+"2",extensions="pdf",option="histo",addfitinfo=True,min_value=-1,max_value=-1,legend_info=[0.60,0.50,0.88,0.72,72,0.037,0],plot_option="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jet}",0.04,13,0.60,0.88,0.05),debug=False)
# done function

for scale in scales:
    for variable in dict_variable_xaxis:
        xaxis=dict_variable_xaxis[variable]
        variablename=scale+"_"+variable
        do_overlay()

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
