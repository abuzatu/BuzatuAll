#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
from ConfigWH import *
from HelperWH import *

print "Start Python"
time_start=time()

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=9:
    print "You need some arguments, will ABORT!"
    print "Ex: python overlayHistogram.py Folder Type XAxisScaleName Variables Scales EventSelections FolderOutput Debug"
    print "Ex: python overlayHistogram.py ${outputroot}/local/histo_PerJetResponse/readPaul_1_0_2BTag+TruthGENWZ_1_perjet Response GENWZ rms,mean,rmsovermean EM,EMJES All ${outputroot}/local/histo_overlayHistogramPtRecoOrResponse/readPaul_1_0_2BTag+TruthGENWZ_1_perjet 1"
    assert(False)
# done if

Folder=sys.argv[1]
Type=sys.argv[2]
XAxisScaleName=sys.argv[3]
Variables=sys.argv[4]
Scales=sys.argv[5]
EventSelections=sys.argv[6]
FolderOutput=sys.argv[7]
Debug=bool(int(sys.argv[8]))

debug=Debug

if debug:
    print "Folder",Folder
    print "Type",Type
    print "XAxisScaleName",XAxisScaleName
    print "Variables",Variables
    print "Scales",Scales
    print "EventSelections",EventSelections
    print "FolderOutput",FolderOutput
    print "Debug",Debug

options_fit="histo" #"histo,Bukin,histo+Bukin"
list_color=[1,2,3,4,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
xaxis_scalename=XAxisScaleName
list_variable=Variables.split(",")
list_scale=Scales.split(",")
list_EventSelection=EventSelections.split(",")


def overlay(variable,list_scale,fileOutputName,debug):
    list_tuple_h1D=[]
    for i,scale in enumerate(list_scale):
        if debug:
            print "i",i,"scale",scale
        fileName=Folder+"/"+process+".root"
        hName="h_"+EventSelection+"_1_Type_lep_inf_inf_PtV_inf_inf_Pt_"+scale+"_None_"+variable
        h=retrieveHistogram(fileName,"",hName,"",debug).Clone()
        if debug:
            print process,h.Integral()
        plotting=(list_color[i],0,0,1) # color, marker style, fill style, size for marker and line
        rebin=1
        xaxis=("Jet p_{T} at the "+xaxis_scalename+" scale [GeV]",0.045,0.90) # title, title size, title offsize
        yaxis=("Jet p_{T} "+yaxis_name,0.040,0.90) # title, title size, title offsize
        update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
        list_tuple_h1D.append([h,scale])
    # done creating list_tuple_h1D
    min=-1 #yaxis_size[0] # -1 would rescale automatically
    max=-1 #yaxis_size[1] # -1 would rescale automatically
    legend_info=[0.27,0.60,0.48,0.85,72,0.04,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    option="HIST"
    text=("#bf{#it{#bf{ATLAS } Simulation Internal}}",0.05,13,0.50,0.85,0.09)
    filePath=FolderOutput
    fileName=fileOutputName
    fileExtensions="pdf"
    # 
    for option_fit in options_fit.split(","):
        overlayHistograms(option_fit,list_tuple_h1D,min,max,legend_info,option,text,filePath,fileName,fileExtensions,debug)
# done function

# run
for EventSelection in list_EventSelection:
    for variable in list_variable:
        # if over variable
        if variable=="mean":
            yaxis_name="response"
            file_name="response"
        elif variable=="rms":
            yaxis_name="resolution"
            file_name="resolution"
        elif variable=="rmsovermean":
            yaxis_name="resolution over response"
            file_name="resolutionoverresponse"
        else:
            print "variable",variable,"not known. It should be mean,rms,rmsovermean. Will ABORT!!!"
            assert(False)
        # done if
        for process in list_process:
            fileOutputName=file_name+"_"+EventSelection+"_"+process
            overlay(variable,list_scale,fileOutputName,debug)

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
