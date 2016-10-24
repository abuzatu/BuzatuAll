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

# this will overlay histograms for different options (OROld and ORNew)
# it will do this for different processes, signal regions, variables

total = len(sys.argv)
# number of arguments plus 1
if total!=6:
    print "You need some arguments, will ABORT!"
    print "Ex: ./overlayOR.py inputPath options variables"
    print "Ex: ./overlayOR.py /afs/phas.gla.ac.uk/user/a/abuzatu/data/Reader/160321_1 0,1,2,3,4 mBB,pTB1 OutputStem 0"
    assert(False)
# done if

#myrebin=int(sys.argv[1])
path=sys.argv[1]
string_options=sys.argv[2]
variables_string=sys.argv[3]
OutputStem=sys.argv[4]
debug=bool(int(sys.argv[5]))

bJetCorr="PtRecollbbOneMuPartonBukinNew"

options=string_options.split(",")
#options="0,1,2,3,4".split(",")
#options="0,1,3,4".split(",")
#folders="a,b".split(",")
#option="OROld"
M=2 # used for Moriond
N=4 # used now in addition to Moriond
A=8 # all
dict_option_color={"0":1,"1":N,"2":M,"3":M,"4":N,"5":N,"6":M,"7":M,"8":M,"9":M,"10":A}
dict_option_legend={"0":"Legacy","1":"Calo #mu","2":"BadJVT","3":"VarDR","4":"BTag e","5":"BTag #mu","6":"#muLikeJet","7":"DR=0.2","8":"#mu Jet","9":"Moriond","10":"Summer"}
#dict_folder_color={"a":2,"b":4}

#masses="300,800,1500".split(",")
#processes="ggA_800,gga_1500,ttbar_PwPyEG".split(",")
#processes="ZHll125".split(",")
processes="ZHll125,ttbar".split(",")
dict_process_sample={
"ggA_300":"AZhllbb300",
"ggA_800":"AZhllbb800",
"ggA_1500":"AZhllbb1500",
"ttbar_PwPyEG":"ttbar",
"ttbar":"ttbar",
"Zmumu_Pw":"Zmumu",
"Ztautau_Pw":"Ztautau",
"ZHll125":"qqZllH125"

}

dict_process_regions={
#"ggA_300":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_",
#"ggA_800":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_,_2tag1pfat0pjet_500ptv_SR_",
#"ggA_1500":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_,_2tag1pfat0pjet_500ptv_SR_",
#"ttbar_PwPyEG":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_",
#"Zmumu_Pw":"_2tag4jet_0_500ptv_SR_,_2tag1pfat0pjet_500ptv_SR_",
#"Ztautau_Pw":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_,_2tag1pfat0pjet_500ptv_SR_"
"ZHll125":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_,_2tag5pjet_0_500ptv_SR_,_1tag2jet_0_500ptv_SR_,_1tag3jet_0_500ptv_SR_,_1tag4jet_0_500ptv_SR_,_1tag5pjet_0_500ptv_SR_",
"ttbar":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_,_2tag5pjet_0_500ptv_SR_,_1tag2jet_0_500ptv_SR_,_1tag3jet_0_500ptv_SR_,_1tag4jet_0_500ptv_SR_,_1tag5pjet_0_500ptv_SR_"
#"ZHll125":"_1tag2jet_0_500ptv_SR_,_1tag3jet_0_500ptv_SR_,_1tag4jet_0_500ptv_SR_,_1tag5pjet_0_500ptv_SR_"
#"ZHll125":"_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_1tag2jet_0_500ptv_SR_,_1tag3jet_0_500ptv_SR_"
#"ZHll125":"_1tag5pjet_0_500ptv_SR_"
}


#regions="_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_".split(",")
#regions="_2tag1pfat0pjet_500ptv_SR_".split(",")
#regions="_2tag2jet_0_500ptv_SR_,_2tag3jet_0_500ptv_SR_,_2tag4jet_0_500ptv_SR_,_2tag1pfat0pjet_500ptv_SR_".split(",")
#variables="mBB,mVH,pTB1,EtaB1,pTB2,EtaB2,EtaM1,EtaM2,EtaB2,EtaE1,EtaE2,pTL1,EtaL1,mLL,pTL2,EtaL2,NJets,NSigJets".split(",")
#variables="EtaB1,EtaM1,EtaE1,EtaL1,pTB1,pTM1,pTE1,pTL1".split(",")
#variables_string="EtaB1,EtaM1,EtaB1,mBB"
#variables_string="EtaB1,EtaM1,EtaE1,EtaL1,pTB1,pTM1,pTE1,typeM1,badJvtB1"
#variables_string+=",EtaB2,EtaM2,EtaE2,EtaL2,pTB2,pTM2,pTE2,typeM2,badJvtB2"
#variables_string="mBB,pTB1,pTB2,EtaB1,EtaB2,pTL1,pTL2,pTM1,pTM2,pTE1,pTE2,EtaL1,EtaL2,EtaM1,EtaM2,EtaE1,EtaE2"
#variables_string="mBB,pTM1,pTM2,pTE1,pTE2,pTL1,pTL2,EtaM1,EtaM2,EtaE1,EtaE2,pTB1,pTB2,EtaB1,EtaB2"
#variables_string="mBB"
variables=variables_string.split(",")

dict_process_variable_info={
"ZHll125": {
        "mBB": [22.5,207.5,10],
        "pTM1": [0,240,2],
        "pTM2": [0,240,2],
        "pTE1": [0,240,2],
        "pTE2": [0,240,2],
        "pTL1": [0,240,2],
        "pTL2": [0,240,4],
        "EtaM1": [-3,3,10],
        "EtaM2": [-3,3,10],
        "EtaE1": [-3,3,10],
        "EtaE2": [-3,3,10],
        "EtaL1": [-5,5,10],
        "EtaL2": [-5,5,10],
        "pTB1": [0,200,1],
        "pTB2": [0,200,1],
        "EtaB1": [-3,3,3],
        "EtaB2": [-3,3,3]
        },
"ttbar": {
        "mBB": [0,500,40],
        "pTM1": [0,240,2],
        "pTM2": [0,240,2],
        "pTE1": [0,240,2],
        "pTE2": [0,240,2],
        "pTL1": [0,240,2],
        "pTL2": [0,240,4],
        "EtaM1": [-3,3,10],
        "EtaM2": [-3,3,10],
        "EtaE1": [-3,3,10],
        "EtaE2": [-3,3,10],
        "EtaL1": [-5,5,10],
        "EtaL2": [-5,5,10],
        "pTB1": [0,200,1],
        "pTB2": [0,200,1],
        "EtaB1": [-3,3,3],
        "EtaB2": [-3,3,3]
        }
}

folderOutput="OR_SimpleMerge500"

fileOutputName=folderOutput+"/OR.txt"
f = open(fileOutputName,'w')
title="%-50s" % ("Histogram")
for option in options:
    if debug:
        print "option",option
    title+="%-15s" % option
#done loop over option
#for folder in folders:
#    if debug:
#        print "folder",folder
#    title+="%-15s" % folder
# done loop over folder
print title
f.write(title+'\n')

#
dict_process_region_variable_value={}
for process in processes:
    if debug:
        print "process",process
    sample=dict_process_sample[process]
    if debug:
        print "sample",sample
    f.write(""+"\n")
    f.write("******************* "+sample+" ************************ \n")
    #
    dict_region_variable_value={}
    for region in dict_process_regions[process].split(","):
        if debug:
            print "region",region
        if "1" in options:
            if "2tag" in region:
                min_value_ratio=0.98
                max_value_ratio=1.05
            elif "1tag" in region:
                min_value_ratio=0.98
                max_value_ratio=1.05
            else:
                print "region",region,"does not have 2tag or 1tag in it. Will ABORT!!!!"
                assert(false)
        else:
            if "2tag" in region:
                min_value_ratio=0.98
                max_value_ratio=-1
            elif "1tag" in region:
                min_value_ratio=0.98
                max_value_ratio=-1
            else:
                print "region",region,"does not have 2tag or 1tag in it. Will ABORT!!!!"
                assert(false)
        # done if
        # rewrite to between 0.9 to 1.1
        min_value_ratio=0
        max_value_ratio=2
        if debug:
            print "region",region,"min_value_ratio",min_value_ratio,"max_value_ratio",max_value_ratio
        f.write(""+"\n")
        #
        dict_variable_value={}
        for variable in variables:
            if debug:
                print "variable",variable
            info=dict_process_variable_info[process][variable]
            histoName=sample+region+variable
            if debug:
                print "histoName",histoName
            #dict_folder_yield={}
            dict_option_yield={}
            list_tuple_h1D=[]
            for option in options:
                if debug:
                    print "option",option,type(option)
            #for folder in folders:
                #if debug:
                    #print "folder",folder
                folder=""
                inputFile=path+folder+"/submitDir_Reader_"+option+"_"+bJetCorr+"/hist-"+process+".root"
                if debug:
                    print "inputFile",inputFile
                ho=retrieveHistogram(fileName=inputFile,histoPath="",histoName=histoName,name=histoName+"_"+option,debug=debug)
                subRange=[info[0],info[1]]
                h=get_histo_subRange(ho,subRange,debug)
                h.Rebin(info[2])
                #h.SetLineColor(dict_folder_color[folder])
                h.SetLineColor(dict_option_color[option])
                if debug:
                    print type(h),"name",h.GetName(),"integral",h.Integral()
                #dict_folder_yield[folder]=h.Integral()
                dict_option_yield[option]=h.Integral()
                if debug:
                    print "histogram integral",dict_option_yield[option]
                #dict_option_yield[option]=h.GetEntries() # normally the number of calles to Fill(), but in our case it is the number of bins
                list_tuple_h1D.append([h,dict_option_legend[option]])
                if debug:
                    print "appended succesfully to list_tuple_h1D"
            # done loop over option
            if debug:
                for tuple_h1D in list_tuple_h1D:
                    print tuple_h1D[0].GetIntegral(),tuple_h1D[1]
            # calculate what to write in the yield text file
            row="%-50s" % (histoName)
            #default=dict_folder_yield["a"]
            #default=dict_option_yield["0"]
            default=dict_option_yield[options[0]] # use the first element as reference
            if debug:
                print "default",default
            #for folder in folders:
             #   if debug:
              #      print "folder",folder
               # current=dict_folder_yield[folder]
            list_option_value=[]
            for i,option in enumerate(options):
                if debug:
                    print "option",option
                current=dict_option_yield[option]
                if debug:
                    print "current",current
                comparison=(ratio(current,default)-1.0)*100
                if debug:
                    print "ratio",ratio,"comparison",comparison
                # update legend to include the change with respect to option 0
                string_comparison=" "
                string_comparison_latex=" "
                if comparison>0:
                   string_comparison+="+"
                   string_comparison_latex+="+"
                string_comparison+="%-.1f%-1s" % (comparison, "%")
                string_comparison_latex+="%-.1f%-2s" % (comparison, "\%")
                list_option_value.append(string_comparison_latex)
                list_tuple_h1D[i][1]+=string_comparison
                #row+="%-20s" % ("%-.0f %-4s %-3s" % (str(current),comparison,"%"))
                row+="%-20s" % ("%-10s" % ("%-.3f" % current) + "%-5s" % ("%-.1f %-3s" % (comparison, "%")))
                #row+="%-20s" % ("%-5s" % ("%-.3f" % current) + "%-5s" % ("%-.1f %-3s" % (comparison, "%")))
            # done loop over option
            dict_variable_value[variable]=list_option_value
            print row
            f.write(row+'\n')
            # overlay histograms
            if debug: 
                print "Start overlayHistograms"
            overlayHistograms(list_tuple_h1D,fileName=folderOutput+"/plots/overlay_"+histoName,extensions="pdf,png",option="histo",addfitinfo=False,min_value=-1,max_value=-1,min_value_ratio=0.8,max_value_ratio=1.2,statTitle="MC stat.",statColor=204,ratioTitle="Ratio to first",legend_info=[0.58,0.50,0.88,0.72,72,0.06,0],plot_option="HIST",text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{"+histoName+"}",0.04,13,0.30,0.88,0.05),debug=debug)
            if debug:
                print "Done overlayHistograms"
        # done loop over variable
        dict_region_variable_value[region]=dict_variable_value
    # done loop over region
    dict_process_region_variable_value[process]=dict_region_variable_value
# done loop over process
f.close()

debug=True

if debug:
    print "dict_process_region_variable_value"
    for variable in variables:
        if debug:
            print "variable",variable
        for process in processes:
            if debug:
                print "process",process
            for region in dict_process_regions[process].split(","):
                if debug:
                    print "region",region
                list_option_value=dict_process_region_variable_value[process][region][variable]
                print "variable",variable,"process",process,"region",region,"list_option_value",list_option_value

tags="1tag,2tag".split(",")
jets="2jet,3jet,4jet,5pjet".split(",")

for variable in variables:
    if debug:
        print "variable",variable
    for tag in tags:
        if debug:
            print "tag",tag
        fileLatexOutputName=folderOutput+"/latex_"+variable+"_"+tag+".tex"
        flatex=open(fileLatexOutputName,'w')
        flatex.write("\\begin{frame}{"+variable+" "+tag+"}\n")
        flatex.write("\\begin{figure}\n")
        flatex.write("\\begin{columns}\n")
        for jet in jets:
            flatex.write("\\column{0.25\\textwidth}\n")
            flatex.write("\\centering\n")
            flatex.write(jet+" \\\\ \n")
            change=dict_process_region_variable_value["ZHll125"]["_"+tag+jet+"_0_500ptv_SR_"][variable][1]
            flatex.write("\\zhll \ "+change+"\\\\ \n")
            #flatex.write("\\zhll \\\\ \n")
            #flatex.write(change+"\\\\ \n")
            flatex.write("\\includegraphics[width=\\textwidth]{"+OutputStem+"_"+string_options+"/OR_SimpleMerge500/plots/overlay_qqZllH125_"+tag+jet+"_0_500ptv_SR_"+variable+"_histo.pdf} \\\\ \n")
            change=dict_process_region_variable_value["ttbar"]["_"+tag+jet+"_0_500ptv_SR_"][variable][1]
            flatex.write("\\ttbar \ "+change+"\\\\ \n")
            #flatex.write("\\ttbar \\\\ \n")
            #flatex.write(change+"\\\\ \n")
            flatex.write("\\includegraphics[width=\\textwidth]{"+OutputStem+"_"+string_options+"/OR_SimpleMerge500/plots/overlay_ttbar_"+tag+jet+"_0_500ptv_SR_"+variable+"_histo.pdf} \\\\ \n")
        # done loop over jet
        flatex.write("\\end{columns}\n")
        flatex.write("\\end{figure}\n")
        flatex.write("\\end{frame}\n")
        flatex.close()
    # done loop over tag
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
