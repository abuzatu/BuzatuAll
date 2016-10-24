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
if total!=1:
    print "You need some arguments, will ABORT!"
    print "Ex: python overlayHistogram.py Folder Type XAxisScaleName Scales EventSelections FolderOutput Debug"
    print "Ex: python overlayHistogram.py ${outputroot}/local/histo_PerJetPtReco/readPaul_1_0_2BTag+TruthGENWZ_1_perjet PtReco EMJESGSMu EMJESGSMu All,0Muon,1Muon,2T,2T_0Muon,2T_1Muon ${outputroot}/local/histo_overlayHistogramPtRecoOrResponse/readPaul_1_0_2BTag+TruthGENWZ_1_perjet 1"
    print "Ex: python overlayHistogram.py ${outputroot}/local/histo_PerJetResponse/readPaul_1_0_2BTag+TruthGENWZ_1_perjet Response GENWZ EM,EMJES All ${outputroot}/local/histo_overlayHistogramPtRecoOrResponse/readPaul_1_0_2BTag+TruthGENWZ_1_perjet 1"
    assert(False)
# done



debug=True
Type="PtReco"
process="llbb"

options_fit="histo" #"histo,Bukin,histo+Bukin"
list_color=[1,2,3,4,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
xaxis_scalename="muon-in-jet"
FolderOutput="./output"
fileOutputName="PtReco"
list_category="mu,nosld,all,el".split(",")
dict_category_inputfile={}
dict_category_inputfile["all"]="./input/tree_llbb_5_all_nosld_1_75.root"
dict_category_inputfile["nosld"]="./input/tree_llbb_5_all_nosld_1_75.root"
dict_category_inputfile["mu"]="./input/tree_llbb_5_mu_1_75.root"
dict_category_inputfile["el"]="./input/tree_llbb_5_el_1_75.root"


# if over Type
if Type=="PtReco":
    yaxis_name="energy and momentum correction factor"
elif Type=="Response":
    yaxis_name="response"
else:
    print "Type",Type,"not known. It should be PtReco, Response. Will ABORT!!!"
    assert(False)
# done if


def overlay(list_category,fileOutputName,debug):
    list_tuple_h1D=[]
    for i,category in enumerate(list_category):
        if debug:
            print "i",i,"category",category
        fileOutputName+="_"+category   
        fileName=dict_category_inputfile[category]
        hName=category
        h=retrieveHistogram(fileName,"",hName,"",debug).Clone()
        if debug:
            print category,h.Integral()
        plotting=(list_color[i],0,0,1) # color, marker style, fill style, size for marker and line
        rebin=1
        xaxis=("Jet p_{T} after the "+xaxis_scalename+" scale [GeV]",0.045,0.90) # title, title size, title offsize
        yaxis=("Jet p_{T} "+yaxis_name,0.040,0.90) # title, title size, title offsize
        update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
        list_tuple_h1D.append([h,category])
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
overlay(list_category,fileOutputName,debug)

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
