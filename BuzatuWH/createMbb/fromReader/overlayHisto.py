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
if total!=2:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayHisto.py rebin"
    print "Ex: ./overlayHisto.py 5"
    assert(False)
# done if

myrebin=int(sys.argv[1])
list_correction="Nominal,OneMu,PtRecollbbOneMuPartonBukinNew,Regression".split(",")
#list_correction="Nominal,OneMu,OneMuNu,AllMu,AllMuNu,Regression,PtRecollbbOneMuPartonBukinNew,PtRecollbbOneMuPartonGaussNew".split(",")
#list_correction="PtRecollbbOneMuPartonBukinNew".split(",")

dict_process_processinfo={}
dict_process_processinfo["ZHll125"]=["qqZllH125","S",2,myrebin]
dict_process_processinfo["ggA_300"]=["ggA300ZHllbb","S",3,myrebin]
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
#dict_process_processinfo["ZmumuB"]=["Zbb",3]
#dict_process_processinfo["ZeeB"]=["Zbb",4]
#dict_process_processinfo["singletop_s"]=["stop_s",5]
#dict_process_processinfo["singletop_t"]=["stop_t",6]
#dict_process_processinfo[""]=
#dict_process_processinfo[""]=
#exit()

debug=False
list_IncludeUnderflowOverflowBins=[False] #[False,True]
list_AddInQuadrature=[True] #[False,True]
list_WhatToCompute="sensitivity,significance".split(",") #"signaloverbackground,sensitivity,significance".split(",")
#prefix="/nfs/atlas/abuzatu01/code/CxAODFramework/submitDir2/hist-"
#prefix="/nfs/atlas/abuzatu02/data/Reader/submitDir_all/hist-"
suffix=".root"
#histoPath="Sys_withoutPU"
histoPath=""
histoPrefix="_2tag2jet_0_150ptv_SR_"
if histoPath=="":
    histoSuffix=""
else:
    histoSuffix="_"+histoPth


#inputfilepath="/nfs/atlas/abuzatu02/data/Reader/"
#outfileprefix="~/public_html/forVH/temp/"
inputfilepath="~/data/Reader/151212/" # 12 no cut, 20 with cut personalized for each correction
outfileprefix="~/data/histos_mbb_fromReader/"

for process in dict_process_processinfo:
    if debug:
        print "process",process

textoftext="#bf{#it{#bf{ATLAS } Simulation Internal}}?#bf{2lep Reader selection}"
#textoftext="#it{ATLAS} Simulation Internal?#bf{SM "+ProcessShort+" 2-b-tag}?#bf{both jets > 20 GeV}?#bf{no event weight applied}"
list_string_process=[
    #"ZHll125,ttbar,singletop_t,ZmumuB,ZeeB",
    #"ZHll125,ttbar,ZmumuB,ZeeB,singletop_t"
    #"ZHll125,ttbar",
    #"ZHll125",
    #"ggA_300,ttbar",
    #"ggA_300,ggA_400,ttbar"
    #"ggA_400,ttbar",
    #"ggA_400,ZmumuB",
    #"ZHll125,ggA_300,ggA_400,ttbar",
    #"ZHll125,ggA_300,ggA_400,ttbar,ZeeB,ZmumuB",
    #"ZHll125,ttbar,ZeeB,ZmumuB",
    #"ZHll125,ZeeB,ZmumuB,ttbar",
    "ZHll125,Zee_Pw,Zmumu_Pw,ttbar",
    "ggA_300,Zee_Pw,Zmumu_Pw,ttbar",
    "ggA_400,Zee_Pw,Zmumu_Pw,ttbar",
    #"ggA_300,ttbar,ZeeB,ZmumuB",
    #"ggA_400,ttbar,ZeeB,ZmumuB",
    #"ZHll125,ZeeB,ZmumuB",
    #"ggA_300,ZeeB,ZmumuB",
    #"ggA_400,ZeeB,ZmumuB",
    #"ZHll125,ggA_300,ggA_400,ZeeB",
    #"ggA_400,ZeeB",
    #"ggA_500,ttbar",
    #"ggA_600,ttbar",
    #"ggA_700,ttbar",
    #"ggA_800,ttbar",
    #"ggA_800,ttbar"
    #"ggA_800,ggA_300"
    ]

dict_process_newprocess={}
#dict_process_newprocess["ZHll125"]="llbb"

mBB_dict_correction_subRange={}
mBB_dict_correction_subRange["Nominal"]=[77.5,152.5] # signal efficiency 0.962274680041
mBB_dict_correction_subRange["OneMu"]=[82.5,152.5] # signal efficiency 0.957673593267
mBB_dict_correction_subRange["PtRecollbbOneMuPartonBukinNew"]=[92.5,152.5] # signal efficiency 0.935146927292
mBB_dict_correction_subRange["Regression"]=[97.5,162.5] # signal efficiency 0.934398243196

mVH_dict_correction_subRange={}
mVH_dict_correction_subRange["Nominal"]=[187.5,447.5]
mVH_dict_correction_subRange["OneMu"]=[187.5,447.5]
mVH_dict_correction_subRange["PtRecollbbOneMuPartonBukinNew"]=[187.5,447.5]
mVH_dict_correction_subRange["Regression"]=[187.5,447.5]

dict_variable_info={}
dict_variable_info["mBB"]                  =["mbb [GeV]",mBB_dict_correction_subRange,            [0.13,0.45,0.25,0.55,72,0.03,0],(textoftext,0.02,1,0.15,0.85,0.02),"histo"] #"histo,Bukin,histo+Bukin,Gauss,histo+Gauss"]
#dict_variable_info["mBB"]                  =["mbb [GeV]",[52.5,197.5],            [0.13,0.45,0.25,0.55,72,0.03,0],(textoftext,0.02,1,0.15,0.85,0.02),"histo"] #"histo,Bukin,histo+Bukin,Gauss,histo+Gauss"]
#dict_variable_info["mBB"]                  =["mbb [GeV]",[50.0,200.0],            [0.13,0.45,0.25,0.55,72,0.03,0],(textoftext,0.02,1,0.15,0.85,0.02),"histo"] #"histo,Bukin,histo+Bukin,Gauss,histo+Gauss"]
#dict_variable_info["mBB"]                  =["mbb [GeV]",[60.0,200.0],            [0.13,0.45,0.25,0.55,72,0.03,0],(textoftext,0.02,1,0.15,0.85,0.02),"histo"] #"histo,Bukin,histo+Bukin,Gauss,histo+Gauss"]
dict_variable_info["mVH"]                  =["mVH [GeV]",mVH_dict_correction_subRange,              [0.75,0.85,0.85,0.85,72,0.03,0],(textoftext,0.02,1,0.15,0.85,0.02),"histo"] #"histo,Bukin,histo+Bukin,Gauss,histo+Gauss"]
#dict_variable_info["mVH"]                  =["mVH [GeV]",[185.0,455.0],              [0.75,0.85,0.85,0.85,72,0.03,0],(textoftext,0.02,1,0.15,0.85,0.02),"histo"] #"histo,Bukin,histo+Bukin,Gauss,histo+Gauss"]

def overlay(variable,processes,correction,debug):
    fileOutputName=outfileprefix+variable
    info=dict_variable_info[variable]
    xaxisname=info[0]
    dict_correction_subRange=info[1]
    print "dict_correction_subRange",dict_correction_subRange
    subRange=dict_correction_subRange[correction]
    print "subRange",subRange
    yaxisname="Arbitrary units"
    if debug:
        print "fileOutputName",fileOutputName
        print "info",info
        print "xaxisname",xaxisname
        print "yaxisname",yaxisname
    h_S=0
    h_B=0
    counter_h_S=0
    counter_h_B=0
    list_tuple_allh1D=[]
    list_tuple_SBNotSmoothedh1D=[]
    list_tuple_SBh1D=[]
    for i,process in enumerate(processes):
        if process in dict_process_newprocess.keys():
            processnew=dict_process_newprocess[process]
        else:
            processnew=process
        if debug:
            print "adi i",i,"process",process
        processinfo=dict_process_processinfo[process]
        processNameForHisto=processinfo[0]
        processType=processinfo[1]
        color=processinfo[2]
        rebin=processinfo[3]
        fileOutputName+="_"+processnew.replace("_","")
        fileName=prefix+process+suffix
        if False:
            file=TFile(fileName,"READ")
            file.ls()
            print " ************** new directory *****"
            gDirectory.cd("Sys_withoutPU")
            gDirectory.ls()
            exit()
        # done testing
        hName=processNameForHisto+histoPrefix+variable+histoSuffix
        ho=retrieveHistogram(fileName,histoPath,hName,"",True).Clone() 
        h=get_histo_subRange(ho,subRange,debug)
        h.SetName(h.GetName()+"new")
        if debug:
            print h.GetNbinsX()
            for i in xrange(h.GetNbinsX()+1):
                print i,get_histo_values(h,i,debug)
        #exit()
        plotting=(color,0,0,1) # color, marker style, fill style, size for marker and line
        #rebin=1
        xaxis=(xaxisname,0.045,0.90) # title, title size, title offsize
        yaxis=(yaxisname,0.040,0.90) # title, title size, title offsize
        if debug:
            print "Before rebin: nrBins",h.GetNbinsX(),"integral",h.Integral()
        update_h1D_characteristics(h,rebin,plotting,xaxis,yaxis,debug)
        #h.SetFillColor(color)
        #h.SetFillStyle(4050)
        if debug:
            print "After  rebin with rebin",rebin,": nrBins",h.GetNbinsX(),"integral",h.Integral()
        if False:
            print h.GetNbinsX()
            for i in xrange(h.GetNbinsX()+1):
                print i,get_histo_values(h,i,debug)
        if False:
            print type(h),h,
            print process,h.Integral(),h.GetMean(),h.GetMaximum(),h.GetMinimum(),h.GetNbinsX()
            print "integral_before",integral_before
            print "integral_after",integral_after
            for bi in xrange(h.GetNbinsX()+2):
                print "bin",bi,"value",h.GetBinContent(bi),"low edge",h.GetBinLowEdge(bi)
        #
        if debug:
            print "h",process,processType, h.Integral(),h.GetMean(),h.GetMaximum(),h.GetMinimum(),h.GetNbinsX()
        if processType=="S":
            if counter_h_S==0:
                h_S=h.Clone()
                counter_h_S+=1
            else:
                h_S+=h.Clone()
            if debug:
                print "h_S",process,processType, h_S.Integral(),h_S.GetMean(),h_S.GetMaximum(),h_S.GetMinimum(),h_S.GetNbinsX()
        elif processType=="B":
            if counter_h_B==0:
                h_B=h.Clone()
                counter_h_B+=1
            else:
                h_B+=h.Clone()
            if debug:
                print "h_B",process,processType, h_B.Integral(),h_B.GetMean(),h_B.GetMaximum(),h_B.GetMinimum(),h_B.GetNbinsX()
        #
        list_tuple_allh1D.append([h,processnew])
    # done creating list_tuple_h1D
    h_B.SetLineColor(1)
    h_B_notsmoothed=h_B.Clone()
    h_B=get_histo_smoothed(h_B,debug)
    if debug:
        print "after smoothing"
        print "h_B",process,processType, h_B.Integral(),h_B.GetMean(),h_B.GetMaximum(),h_B.GetMinimum(),h_B.GetNbinsX()
    list_tuple_SBh1D.append([h_S,"S"])
    list_tuple_SBh1D.append([h_B,"B"])

    list_tuple_SBNotSmoothedh1D.append([h_S,"S"])
    list_tuple_SBNotSmoothedh1D.append([h_B_notsmoothed,"B"])

    stackname="stack_"+correction
    stack=THStack(stackname,stackname)
    #for tuple_allh1D in list_tuple_allh1D:
    stack.Add(list_tuple_allh1D[1][0])
    stack.Add(list_tuple_allh1D[2][0])
    stack.Add(list_tuple_allh1D[3][0])
    c=TCanvas("c","c",600,400)
    stack.Draw("HIST")
    h_S_new=h_S.Clone()
    h_S_new.Scale(20)
    h_S_new.Draw("HIST SAME")
    c.Print(stackname+".pdf")

    # WARNING! Works now for just one histogram of S and B
    # compute sensitivity
    for IncludeUnderflowOverflowBins in list_IncludeUnderflowOverflowBins:
        for AddInQuadrature in list_AddInQuadrature:
            for WhatToCompute in list_WhatToCompute:
                total=computeSB(h_S,h_B,IncludeUnderflowOverflowBins,AddInQuadrature,WhatToCompute,debug)
                f.write(" & "+"%-.4f" % (total))
    #exit()

    # we continue with plotting
    min=-1 #yaxis_size[0] # -1 would rescale automatically
    max=-1 #yaxis_size[1] # -1 would rescale automatically
    legend_info=info[2][:] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
    if debug:
        print "legend_info",legend_info
    # this changes automatically the size of the legend
    if True:
        legend_info_new=legend_info[1]-0.08*len(processes)
        if legend_info_new<0.10:
            legend_info[1]=0.10
        else:
            legend_info[1]=legend_info_new
        if debug:
            print "legend_info",legend_info
    # done

    option="HIST" # need "R" in order to be able to plot just the fit "HIST"
    text=info[3]
    filePath=""
    fileExtensions="pdf,png"
    options_fit=info[4] #"histo+Gauss" #"histo,Bukin,histo+Bukin"
    addfitinfo=False
    min=0.0
    max=h_B_notsmoothed.GetMaximum()*1.05
    # 
    for option_fit in options_fit.split(","):
        fileNameStem=fileOutputName+"_rebin_"+str(myrebin)
        overlayHistograms(list_tuple_allh1D,fileNameStem+"_all"+"_"+correction,fileExtensions,option_fit,addfitinfo,min,max,legend_info,option,text,debug)
        overlayHistograms(list_tuple_SBNotSmoothedh1D,fileNameStem+"_SBNotSmoothed"+"_"+correction,fileExtensions,option_fit,addfitinfo,min,max,legend_info,option,text,debug)
        overlayHistograms(list_tuple_SBh1D,fileNameStem+"_SB"+"_"+correction,fileExtensions,option_fit,addfitinfo,min,max,legend_info,option,text,debug)
# done function

# run        

for variable in dict_variable_info:
    if True:
        print "variable",variable
    for string_process in list_string_process:
        print ""
        print string_process
        fileOutputName=variable+"_"+string_process.replace(",","").replace("_","")+"_"+str(myrebin)+".tex"
        f = open(fileOutputName,'w')
        #f.write('\\documentclass{beamer}\n')
        #f.write('\\usepackage{tabularx}\n')
        #f.write('\\usepackage{adjustbox}\n')
        #f.write('\\usepackage{pdflscape}\n')
        #f.write('\\begin{document}\n')
        f.write('\\begin{frame}{'+variable+' and '+string_process.replace("_","\_")+' }\n')
        f.write('\\begin{center}\n')
        f.write('\\begin{landscape} \n')
        f.write('\\adjustbox{max height=\\dimexpr\\textheight-6.0cm\\relax,max width=\\textwidth}\n')
        f.write('{\n')
        f.write('\\begin{tabular}{|l|l|l|}\n')
        f.write('\hline\hline \n') 
        f.write('Correction & Sensitivity & Significance \\\\ \hline\hline \n')
        for correction in list_correction:
            print correction
            f.write(correction)
            prefix=inputfilepath+"submitDir_"+correction+"/hist-"
            processes=string_process.split(",")
            overlay(variable,processes,correction,debug)
            f.write(" \\\\ \\hline \n")
        # done loop over all corrections
        f.write('\\end{tabular}\n')
        f.write('}\n')
        f.write('\\end{landscape} \n')
        f.write('\\end{center}\n')
        f.write('\\end{frame}\n')
        #f.write('\\end{document}\n')
        f.close()
    # done loop over string_process
# done loop over variable

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
