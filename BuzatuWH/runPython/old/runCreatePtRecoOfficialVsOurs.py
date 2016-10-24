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
filename=initialroot+"/../PtRecoCorrection_MV1c_GSC_Nov2013_v2.root"
filenameours=initialroot+"/../allbins__EMJESGSCMu_Pt_PtReco_over_AllJets.root"
rebin=1
xaxis=("Jet p_{T} at the EMJESGSCMu scale [GeV]",0.045,0.99) # title, title size, title offsize
yaxis_title="Jet p_{T} and energy correction factor"
yaxis_size=(1.0,1.2)
yaxis=(yaxis_title,0.045,0.95) # title, title size, title offsize

def overlay_PtReco(debug):
    if debug:
        print "Starting overlay_PtReco"
    name_central="Correction"
    name_up="SystUp"
    name_down="SystDown"
    name_ours="h__EMJESGSCMu_Pt_GENWZ_over_EMJESGSCMu_Pt_mean_None_PtReco_over_AllJets"
    h_central=retrieveHistogram(filename,"./",name_central,"",debug).Clone()
    h_up=retrieveHistogram(filename,"./",name_up,"",debug).Clone()
    h_down=retrieveHistogram(filename,"./",name_down,"",debug).Clone()
    h_ours=retrieveHistogram(filenameours,"./",name_ours,"",debug).Clone()
    if debug:
        for i in xrange(15):
            print "h_central bin",i,h_central.GetBinContent(i)
            print "h_up bin",i,h_up.GetBinContent(i)
            print "h_down bin",i,h_down.GetBinContent(i)
            print "h_ours bin",i,h_ours.GetBinContent(i)
            print ""
    #
    list_tuple_h1D=[]
    #
    plotting_central=(1,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_central,rebin,plotting_central,xaxis,yaxis,debug)
    list_tuple_h1D.append([h_central,"Central value from ZH"])
    #
    plotting_up=(2,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_up,rebin,plotting_up,xaxis,yaxis,debug)
    list_tuple_h1D.append([h_up,"Systematic up from ZH"])
    #
    plotting_down=(3,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_down,rebin,plotting_down,xaxis,yaxis,debug)
    # temporary do not include the down, as the same values as the up value
    #list_tuple_h1D.append([h_down,"Systematic down from ZH"])
    #
    plotting_ours=(4,0,0,1) # color, marker style, fill style
    update_h1D_characteristics(h_ours,rebin,plotting_ours,xaxis,yaxis,debug)
    list_tuple_h1D.append([h_ours,"Central value from WH"])
    #
    options_fit="histo" # "histo,Bukin,histo+Bukin,Gauss,histo+Gauss"
    min=yaxis_size[0] # -1 would rescale automatically
    max=yaxis_size[1] # -1 would rescale automatically
    legend_info=[0.55,0.60,0.70,0.80,72,0.04,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    option=""
    filePath="./plots/"
    fileName="PtRecoOfficialVsOurs"
    fileExtensions="pdf"
    for option_fit in options_fit.split(","):
        overlayHistograms(option_fit,list_tuple_h1D,min,max,legend_info,option,filePath,fileName,fileExtensions,debug)
# done function

if OverlayPtReco:
    overlay_PtReco(debug)

print "End Python"

####################################################
##### End                                   ########
####################################################
