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

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=6:
    print "You need some arguments, will ABORT!"
    print "Ex: python overlayHistogram.py Folder Prefix Suffix FolderOutput Debug"
    print "Ex: python overlayHistogram.py ${outputroot}/local/histo_batch/readPaul_1_0_J1Pt45+2BTag_1_perevent GENWZ_1 M-j1j2_v_0_300_4 ${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent 1"
    assert(False)
# done if

Folder=sys.argv[1]
Prefix=sys.argv[2]
Suffix=sys.argv[3]
FolderOutput=sys.argv[4]
Debug=bool(int(sys.argv[5]))

debug=Debug

if debug:
    print "Folder",Folder
    print "Prefix",Prefix
    print "Suffix",Suffix
    print "FolderOutput",FolderOutput
    print "Debug",Debug

list_Suffix=Suffix.split("-")
Variable=list_Suffix[0]
Suffix=list_Suffix[1]
if debug:
    print "Variable",Variable
    print "Suffix",Suffix

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

list_LepBinsUse="all".split(",")
list_PtVBinsUse="all".split(",")
dict_process_legend={} # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
dict_process_legend["WH"]=[0.62,0.55,0.82,0.75,72,0.04,0]
dict_process_legend["ZH"]=[0.62,0.55,0.82,0.75,72,0.04,0]
dict_process_legend["Signal"]=[0.62,0.55,0.82,0.75,72,0.04,0]
dict_process_legend["WZ"]=[0.62,0.15,0.82,0.35,72,0.04,0] 
dict_process_legend["VV"]=[0.62,0.35,0.82,0.55,72,0.04,0] 
dict_process_legend["TopPair"]=[0.32,0.15,0.52,0.35,72,0.04,0] 
dict_process_legend["SingleTop"]=[0.32,0.15,0.52,0.35,72,0.04,0] 
dict_process_legend["Whf"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["Wcl"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["Wl"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["Zl"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["Zcl"]=[0.32,0.15,0.52,0.35,72,0.04,0] 
dict_process_legend["Zhf"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["MJ"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["Data"]=[0.32,0.15,0.52,0.35,72,0.04,0]
dict_process_legend["Background"]=[0.22,0.15,0.42,0.35,72,0.04,0] 

# legend for the response distribution
# it can have the same for all processes
r_legend=[0.62,0.55,0.82,0.75,72,0.04,0]


#list_corrections="GENWZ,EMJESGSMuPt,EMJESGSMuPt3,EMJESGSMuPt3NNJ1".split(",")
#list_color=[1,4,6,7,8,9,10]

# if v or r
if "_v_" in Suffix:
    Type="v"
    list_corrections="GENWZ,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3".split(",")
    list_color=[1,3,2,4,6,7,8,9,10]
elif "_r_" in Suffix:
    Type="r"
    #list_corrections="EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3".split(",")
    #list_color=[3,2,4,6,7,8,9,10]
    list_corrections="EMJES,EMJESGS,EMJESGSMu".split(",")
    list_color=[6,7,3]
else:
    print "_v_ or _r_ must be in Suffix",Suffix,". Will ABORT!!"
    assert(False)
# done if

# if v or r
if Type=="v":
    list_corrections="GENWZ,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3".split(",")
    list_color=[1,3,2,4,6,7,8,9,10]
elif Type=="r":
    list_corrections="EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3".split(",")
    list_color=[3,2,4,6,7,8,9,10]
    #list_corrections="EMJES,EMJESGS,EMJESGSMu".split(",")
    #list_color=[6,7,3]
else:
    print "Type",Type,"must be v or r. Will ABORT!!"
    assert(False)
# done if

if debug:
    print "list_LepBinsUse",list_LepBinsUse
# loop over Lep
for Lep in list_LepBinsUse:
    if debug:
        print "Lep",Lep
        print "list_PtVBinsUse",list_PtVBinsUse
    # loop over PtV
    for PtV in list_PtVBinsUse:
        if debug:
            print "PtV",PtV
            print "list_names",list_names
        #
        options_fit="histo" #"histo,Bukin,histo+Bukin"
        # loop over process
        for process in list_names:
            if debug:
                print "process",process
                print "list_corrections",list_corrections
            fileOutputName="h_"+Prefix+"_"+Lep+"_"+PtV+"_"+Variable+"_"+Suffix+"_"+process
            rebin=1
            if Type=="v":
                xaxis=[process+" di-jet invariant mass [GeV]",0.045,0.90] # title, title size, title offsize
                yaxis_title=""
                yaxis_title="Entries / 4 GeV"
            elif Type=="r":
                xaxis=[process+" di-jet invariant mass response",0.045,0.90] # title, title size, title offsize
                yaxis_title=""
                yaxis_title="Entries / 0.02"
            yaxis_size=(0.8,1.6)
            yaxis=(yaxis_title,0.045,0.99) # title, title size, title offsize
            text=("#bf{#it{#bf{ATLAS } Simulation Internal}}",0.05,13,0.50,0.85,0.09)
            list_tuple_h1D=[]
            # loop over correction
            for i,correction in enumerate(list_corrections):
                if debug:
                    print "correction",correction
                fileName=Folder+"/h_"+Prefix+"_"+Lep+"_"+PtV+"_"+Variable+"_"+correction+"_"+Suffix+".root"
                h=retrieveHistogram(fileName,"",process,"",debug).Clone()
                if True:
                    print process,correction,h.Integral()
                # setErrorsToZero(h,debug)
                plotting=(list_color[i],0,0,1) # color, marker style, fill style, size for marker and line
                update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
                # h.SetLineStyle(i+1)
                list_tuple_h1D.append([h,correction])
            # done loop over correction
            # save the file
            # options_fit="histo+Bukin" # "histo,Bukin,histo+Bukin,Gauss,histo+Gauss"
            min=-1 #yaxis_size[0] # -1 would rescale automatically
            max=-1 #yaxis_size[1] # -1 would rescale automatically
            # legend_info=[0.62,0.15,0.82,0.35,72,0.04,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
            if "_r_" in Suffix:
                legend_info=r_legend
            else:
                legend_info=dict_process_legend[process]
            option="HIST"
            filePath=FolderOutput
            fileName=fileOutputName
            fileExtensions="pdf"
            # loop over option_fit
            for option_fit in options_fit.split(","):
                overlayHistograms(option_fit,list_tuple_h1D,min,max,legend_info,option,text,filePath,fileName,fileExtensions,debug)
            # done loop over option_fit
        # done loop over process
    # done loop over PtV
# done loop over Lep


####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
