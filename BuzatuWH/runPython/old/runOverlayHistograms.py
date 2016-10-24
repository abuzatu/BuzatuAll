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

debug=True
OverlayPtReco=True
initialroot=os.environ['initialroot']

def overlay_PtReco(bins_type,quantity_type,fit_type,debug):
    list_names="WithMuon,NoMuon,AllJets"
    rebin=1
    tempname=bins_type.split("_")
    scalename=tempname[0]
    xaxis=("Jet p_{T} at the "+scalename+" scale [GeV]",0.045,0.90) # title, title size, title offsize
    yaxis_title=""
    if quantity_type=="mean":
        #yaxis_title="Scale "
        yaxis_title="Jet p_{T} and energy correction factor"
        yaxis_size=(0.95,1.30)
    elif quantity_type=="rms":
        yaxis_title="Resolution "
        yaxis_size=(0.05,0.35)
    elif quantity_type=="rmsovermean":
        yaxis_title="Resolution divided by Scale "
        yaxis_size=(0.05,0.30)
    elif quantity_type=="meanwithrms":
        yaxis_title="Scale as dots, Resolution as bars, "
        yaxis_size=(0.8,1.6)
    else:
        print "quantity_type",quantity_type,"unknown. Choose from mean, scale, meanwithrms, rmsovermean. Will ABORT!!!"
        exit()
    # done if quantity_type
    if fit_type=="None":
        yaxis_title+=" from histogram"
    elif fit_type=="Bukin":
        yaxis_title+=" from Bukin fit"
    elif fit_type=="Gauss":
        yaxis_title+=" from Gauss fit"
    else:
        print "fit_type",fit_type,"unknown. Choose from None, Bukin, Gauss. Will ABORT!!!"
        exit()
    # done if fit_type
    yaxis=(yaxis_title,0.040,0.90) # title, title size, title offsize
    list_tuple_h1D=[]
    for i,name in enumerate(list_names.split(",")):
        h=retrieveHistogram(initialroot+"/../allbins__"+bins_type+"_PtReco_over_"+name+".root","./","h__"+bins_type+"_GENWZ_over_"+bins_type+"_"+quantity_type+"_"+fit_type+"_PtReco_over_"+name,name,debug).Clone()
        plotting=(i+1,20,0,1) # color, marker style, fill style
        update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
        list_tuple_h1D.append([h,name])
    # done for loop over the histograms to overlap
    options_fit="histo" # "histo,Bukin,histo+Bukin,Gauss,histo+Gauss"
    min=yaxis_size[0] # -1 would rescale automatically
    max=yaxis_size[1] # -1 would rescale automatically
    legend_info=[0.60,0.65,0.80,0.85,72,0.04,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    option=""
    filePath="./plots/"
    fileName=bins_type+"_"+quantity_type+"_"+fit_type
    fileExtensions="pdf"
    for option_fit in options_fit.split(","):
        overlayHistograms(option_fit,list_tuple_h1D,min,max,legend_info,option,filePath,fileName,fileExtensions,debug)
    None
# done function

if OverlayPtReco:
    bins_types="EMJESGSCMu_Pt"
    quantity_types="mean,rms,meanwithrms,rmsovermean"
    fit_types="None,Bukin"
    for bins_type in bins_types.split(","):
        for quantity_type in quantity_types.split(","):            
            for fit_type in fit_types.split(","):
                overlay_PtReco(bins_type,quantity_type,fit_type,debug)



print "End Python"

####################################################
##### End                                   ########
####################################################
