#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
import numpy
import sys


####################################################
##### Start                                 ########
####################################################

print "Start Python"

# goal, overlay the official PtReco from our analysis with +/- 1 sigma

debug=True
OverlayPtReco=True

initialroot=os.environ['initialroot']
rebin=1
xaxis=("Jet p_{T} at the EMJESGSCMu scale [GeV]",0.045,0.90) # title, title size, title offsize
yaxis_title="Jet p_{T} and energy correction factor"
yaxis_size=(0.97,1.4)
yaxis=(yaxis_title,0.045,0.90) # title, title size, title offsize

def overlay_PtReco(muonname,debug):
    if debug:
        print "Starting overlay_PtReco"
    h_LL=retrieveHistogram(initialroot+"/../TruthAll+2LBTag/ptCorr_"+muonname+"_Mean_Mu.root","./","new_corr","LL",debug).Clone()
    h_MM=retrieveHistogram(initialroot+"/../TruthAll+2MBTag/ptCorr_"+muonname+"_Mean_Mu.root","./","new_corr","MM",debug).Clone()
    h_TT=retrieveHistogram(initialroot+"/../TruthAll+2TBTag/ptCorr_"+muonname+"_Mean_Mu.root","./","new_corr","TT",debug).Clone()
    if debug:
        for i in xrange(15):
            print "h_LL bin",i,h_LL.GetBinContent(i)
            print "h_MM bin",i,h_MM.GetBinContent(i)
            print "h_TT bin",i,h_TT.GetBinContent(i)
            print ""
    #
    list_tuple_h1D=[]
    #
    plotting_LL=(1,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_LL,rebin,plotting_LL,xaxis,yaxis,debug)
    list_tuple_h1D.append([h_LL,"LL b-tagging"])
    #
    plotting_MM=(2,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_MM,rebin,plotting_MM,xaxis,yaxis,debug)
    list_tuple_h1D.append([h_MM,"MM b-tagging"])
    #
    plotting_TT=(3,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_TT,rebin,plotting_TT,xaxis,yaxis,debug)
    list_tuple_h1D.append([h_TT,"TT b-tagging"])
    #
    options_fit="histo" # "histo,Bukin,histo+Bukin,Gauss,histo+Gauss"
    min=yaxis_size[0] # -1 would rescale automatically
    max=yaxis_size[1] # -1 would rescale automatically
    legend_info=[0.65,0.65,0.82,0.87,72,0.04,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    option=""
    filePath="./plots/"
    fileName="PtRecoBTagging_"+muonname
    fileExtensions="pdf"
    for option_fit in options_fit.split(","):
        overlayHistograms(option_fit,list_tuple_h1D,min,max,legend_info,option,filePath,fileName,fileExtensions,debug)
# done function

if OverlayPtReco:
    overlay_PtReco("Muons",debug)
    overlay_PtReco("noMuons",debug)

print "End Python"

####################################################
##### End                                   ########
####################################################
