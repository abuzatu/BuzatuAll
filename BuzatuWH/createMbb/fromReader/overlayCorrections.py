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

total = len(sys.argv)
# number of arguments plus 1
if total!=1:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayCorrections.py "
    assert(False)
# done if


debug=False
#fileName="~/data/histos_mbb/histos_mbb_"+Process+".root"
#list_process="ZHll125,ggA_300,ggA_400,Zee_Pw,Zmumu_Pw,ttbar".split(",")
#list_process="ZHll125,ggA_300,ggA_400".split(",")
#list_process="ZHll125,ggA_300".split(",")
list_process="ZHll125".split(",")

list_region=[]
string_tagjet="2tag3jet,2tag4jet,2tag5pjet"
#string_tagjet+=",2tag2jet+2tag3jet+2tag4jet+2tag5pjet"
#string_tagjet="2tag2jet,2tag3jet,2tag4jet,2tag5pjet,1tag2jet,1tag3jet,1tag4jet,1tag5pjet"
#string_tagjet="2tag2jet,2tag3jet,2tag4jet,2tag5pjet,2tag2jet+2tag3jet,2tag2jet+2tag3jet+2tag4jet,2tag2jet+2tag3jet+2tag4jet+2tag5pjet"
#string_tagjet+=",1tag2jet,1tag3jet,1tag4jet,1tag5pjet"
#,1tag2jet+1tag3jet,1tag2jet+1tag3jet+1tag4jet,1tag2jet+1tag3jet+1tag4jet+1tag5pjet"
#string_tagjet+=",1tag2jet+1tag3jet+1tag4jet+1tag5pjet"
#string_tagjet="2tag2jet"
if debug:
    print "string_tagjet",string_tagjet
for tagjet in string_tagjet.split(","):
    if debug:
        print "tagjet",tagjet
    name=""
    for i,tagjetCurrent in enumerate(tagjet.split("+")):
        if debug:
            print "i",i,"tagjetCurrent",tagjetCurrent
        current=tagjetCurrent+"_0_500ptv_SR"
        if i==0:
            name=current
        else:
            name+="+"+current
        # done if
    # done for 
    list_region.append(name)

if debug:
    print "list_region",list_region
#list_region="2tag2jet_0_500ptv_SR+2tag3jet_0_500ptv_SR".split(",")

#exit()

myrebin=10
dict_process_processinfo={}
dict_process_processinfo["ZHll125"]=["qqZllH125","S",2,myrebin]
dict_process_processinfo["ggA_300"]=["AZhllbb300","S",3,myrebin]
dict_process_processinfo["ggA_400"]=["ggA400ZHllbb","S",4,myrebin]
dict_process_processinfo["ggA_500"]=["ggA500ZHllbb","S",3,myrebin]
dict_process_processinfo["ggA_600"]=["ggA600ZHllbb","S",3,myrebin]
dict_process_processinfo["ggA_700"]=["ggA700ZHllbb","S",3,myrebin]
dict_process_processinfo["ggA_800"]=["ggA800ZHllbb","S",4,myrebin]
dict_process_processinfo["ttbar"]=["ttbar","B",6,myrebin]
dict_process_processinfo["ZmumuB"]=["Zbb","B",7,myrebin]
dict_process_processinfo["ZeeB"]=["Zbb","B",8,myrebin]
dict_process_processinfo["Zmumu_Pw"]=["Zmumu","B",7,myrebin]
dict_process_processinfo["Zee_Pw"]=["Zee","B",8,myrebin]

#fileNamePath="~/data/Reader/151212/"
#fileNamePath="~/data/Reader/160214_4/"
#fileNamePath="~/data/Reader/160219_a/"
fileNamePath="~/data/Reader/160308_b/"
dict_scale_color={}
dict_scale_color["Nominal"]=[1,"After global sequential calibration"]
dict_scale_color["OneMu"]=[2,"After muon-in-jet"]
dict_scale_color["PtRecollbbOneMuPartonBukinNew"]=[4,"After PtReco Run II style"]
dict_scale_color["PtRecollbbOneMuTruthWZNoneOld"]=[6,"After PtReco Run I style"]
dict_scale_color["Regression"]=[3,"After Regression"]
dict_scale_color["PtRecollbbOneMuPartonBukinNew2"]=[2,"Bukin2"]
dict_scale_color["PtRecollbbOneMuPartonBukinMedianNew2"]=[1,"BukinMedian2"]
dict_scale_color["PtRecollbbOneMuPartonGaussNew2"]=[3,"Gauss2"]
dict_scale_color["PtRecollbbOneMuPartonGaussMedianNew2"]=[5,"GaussMedian2"]
dict_scale_color["PtRecollbbOneMuPartonNoneNew2"]=[5,"None2"]

dict_scale_color["PtRecollbbOneMuTruthWZNoneOld2"]=[8,"After Old2"]


list_stringscales=[
    "Nominal,OneMu,PtRecollbbOneMuTruthWZNoneOld,PtRecollbbOneMuPartonBukinNew,Regression"
    #"OneMu,PtRecollbbOneMuTruthWZNoneOld,PtRecollbbOneMuPartonBukinNew,Regression"
    #"Nominal,OneMu,PtRecollbbOneMuPartonBukinNew,Regression"
    #"PtRecollbbOneMuPartonBukinNew,PtRecollbbOneMuPartonBukinNew2,PtRecollbbOneMuTruthWZNoneOld,PtRecollbbOneMuTruthWZNoneOld2,Regression"
    #"PtRecollbbOneMuPartonBukinNew,PtRecollbbOneMuPartonBukinNew2,Regression"
    #"PtRecollbbOneMuPartonBukinNew,PtRecollbbOneMuPartonBukinNew2,PtRecollbbOneMuPartonBukinMedianNew2,PtRecollbbOneMuPartonGaussMedianNew2,Regression"
    #"Nominal,OneMu,PtRecollbbOneMuPartonBukinNew"
    #"PtRecollbbOneMuPartonBukinNew"
    ]

textoftext="#bf{#it{#bf{ATLAS } Simulation Internal}}?#bf{AZh 2 lep selection}?#bf{no pileup reweight}"

dict_process_subrange={}
dict_process_subrange["ZHll125"]=[187.5,447.5]
dict_process_subrange["ggA_300"]=[252.5,352.5]
dict_process_subrange["ggA_400"]=[352.5,452.5]


dict_variable_info={}
#
dict_process_subrange={}
#dict_process_subrange["ZHll125"]=[72.5,167.5]
#dict_process_subrange["ZHll125"]=[110.0,140.0]
#dict_process_subrange["ZHll125"]=[52.5,187.5]
dict_process_subrange["ZHll125"]=[52.5,502.5]
#dict_process_subrange["ZHll125"]=[50.0,190.0]
dict_process_subrange["ggA_300"]=[72.5,167.5]
dict_process_subrange["ggA_400"]=[72.5,167.5]
#dict_variable_info["mBB"]                  =["mbb [GeV]",              [0.12,0.85,0.25,0.89,72,0.03,0],(textoftext,0.05,1,0.75,0.85,0.02),"histo+Bukin",dict_process_subrange] #"histo+Bukin"
dict_variable_info["mBBJ"]                  =["mbbj [GeV]",              [0.12,0.85,0.25,0.89,72,0.03,0],(textoftext,0.05,1,0.75,0.85,0.02),"histo+Bukin",dict_process_subrange] #"histo+Bukin"
#
#dict_process_subrange={}
#dict_process_subrange["ZHll125"]=[187.5,447.5]
#dict_process_subrange["ggA_300"]=[252.5,352.5]
#dict_process_subrange["ggA_400"]=[352.5,452.5]
#dict_variable_info["mVH"]                  =["mVH [GeV]",              [0.13,0.85,0.25,0.85,72,0.03,0],(textoftext,0.05,1,0.75,0.85,0.02),"histo+Bukin",dict_process_subrange]


def overlay(process,processinfo,variable,scales,region,debug):
    fileOutputName="~/data/histos_mbb_fromReader/"+process+"_"+region+"_"+variable
    info=dict_variable_info[variable]
    xaxisname=info[0]
    yaxisname="Arbitrary units"
    if debug:
        print "fileOutputName",fileOutputName
        print "info",info
        print "xaxisname",xaxisname
        print "yaxisname",yaxisname

    subRange=info[4][process]

    list_tuple_h1D=[]
    for i,scale in enumerate(scales):
        if debug:
            print "adi i",i,"scale",scale
        fileOutputName+="_"+scale
        fileName=fileNamePath+"/submitDir_Reader_ORNew_"+scale+"/hist-"+process+".root"
        for counterRegion,regionCurrent in enumerate(region.split("+")):
            if debug:
                print "regionCurrent",regionCurrent
            hNameCurrent=processinfo[0]+"_"+regionCurrent+"_"+variable
            if debug:
                print "hNameCurrent",hNameCurrent
            if counterRegion==0:
                ho=retrieveHistogram(fileName,"",hNameCurrent,"",debug).Clone()
            else:
                ho+=retrieveHistogram(fileName,"",hNameCurrent,"",debug).Clone()
            # done if
        # done for loop over regions
        h=get_histo_subRange(ho,subRange,debug)
        #h=ho.Clone()
        if True:
            print scale,h.Integral()
        plotting=(dict_scale_color[scale][0],0,0,2) # color, marker style, fill style, size for marker and line
        rebin=10
        xaxis=(xaxisname,0.045,0.90) # title, title size, title offsize
        yaxis=(yaxisname,0.040,0.90) # title, title size, title offsize
        update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
        list_tuple_h1D.append([h,dict_scale_color[scale][1]])
    # done creating list_tuple_h1D
    min=-1 #yaxis_size[0] # -1 would rescale automatically
    max=-1 #yaxis_size[1] # -1 would rescale automatically
    legend_info=info[1][:] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    if debug:
        print "legend_info",legend_info
    legend_info_new=legend_info[1]-0.08*len(scales)
    if legend_info_new<0.10:
        legend_info[1]=0.10
    else:
        legend_info[1]=legend_info_new
    if debug:
        print "legend_info",legend_info
    option="HIST" # need "R" in order to be able to plot just the fit "HIST"
    #text=info[2]
    print "region",region
    if region=="2tag2jet_0_500ptv_SR+2tag3jet_0_500ptv_SR+2tag4jet_0_500ptv_SR+2tag5pjet_0_500ptv_SR":
        myregion="2tag2pjet_0_500ptv_SR"
    elif region=="1tag2jet_0_500ptv_SR+1tag3jet_0_500ptv_SR+1tag4jet_0_500ptv_SR+1tag5pjet_0_500ptv_SR":
        myregion="1tag2pjet_0_500ptv_SR"
    else:
        myregion=region
    print "myregion",myregion
    text=("#it{ATLAS} Simulation Internal?#bf{"+process+"}?#bf{2lep Reader selection}?#bf{"+myregion+"}?#bf{mc15a}?#bf{no pileup applied}",0.025,1,0.705,0.85,0.03)
    filePath=""
    fileName=fileOutputName
    fileExtensions="pdf" # for pdf set line size to 1 instead of 6, and TCanvas to 600 400 instead of 6000 4000 I did for higher resolution
    options_fit=info[3] #"histo+Gauss" #"histo,Bukin,histo+Bukin"
    addfitinfo=True
    # 
    for option_fit in options_fit.split(","):
        overlayHistograms(list_tuple_h1D,fileName,fileExtensions,option_fit,addfitinfo,min,max,legend_info,option,text,debug)
# done function

# run        

def do():
    for process in list_process:
        processinfo=dict_process_processinfo[process]
        for variable in dict_variable_info:
            for stringscales in list_stringscales:
                scales=stringscales.split(",")
                for region in list_region:
                    overlay(process,processinfo,variable,scales,region,debug)
        
# done

do()

exit()

for stringscales in dict_stringscales_variable_info:
    if debug:
        print "stringscales",stringscales
    dict_variable_info=dict_stringscales_variable_info[stringscales]
    for variable in dict_variable_info:
        if debug:
            print "variable",variable
        if "response" not in variable:
            print "variable not has response",variable
            #newstringscales=stringscales+",TruthWZ"
            newstringscales=stringscales
        else:
            newstringscales=stringscales
        scales=newstringscales.split(",")
        print "scales",scales
        overlay(fileName,scales,variable,debug)

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
