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
if total!=10:
    print "You need some arguments, will ABORT!"
    print "Ex: python mergeHistogram.py Folder Suffix Type Quantity Object NewX EventSelections ApplyEventWeights FolderOutput Debug"
    print "Ex: python mergeHistogram.py ${outputroot}/local/histo_batch/readPaul_1_0_J1Pt45+2BTag_1_perevent All,GENWZ 1,0 1_0 M j1j2 v-100.0-150.0-5.0 ${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent 1"
    assert(False)
# done if

Folder=sys.argv[1]
Suffix=sys.argv[2]
EventSelections=sys.argv[3]
ApplyEventWeights=sys.argv[4]
Quantity=sys.argv[5]
Object=sys.argv[6]
NewX=sys.argv[7]
FolderOutput=sys.argv[8]
Debug=bool(int(sys.argv[9]))

debug=Debug

if debug:
    print "Folder",Folder
    print "Suffix",Suffix
    print "EventSelections",type(EventSelections),EventSelections
    print "ApplyEventWeights",type(ApplyEventWeights),ApplyEventWeights
    print "Quantity",Quantity
    print "Object",Object
    print "NewX",NewX
    print "FolderOutput",FolderOutput
    print "Debug",Debug

def get_items_NewX(NewX,debug):
    if debug:
        print "NewX",NewX
    list_NewX=NewX.split("-")
    Type=list_NewX[0]
    NewXMin=float(list_NewX[1])
    NewXMax=float(list_NewX[2])
    NewBinWidth=float(list_NewX[3])
    result=(Type,NewXMin,NewXMax,NewBinWidth)
    if debug:
        print "(Type,NewXMin,NewXMax,NewBinWidth)",result
    return result
# done function

#
(Type,NewXMin,NewXMax,NewBinWidth)=get_items_NewX(NewX,debug)

# if v or r
if Type=="v":
    scale_name=1
elif Type=="r":
    scale_name=100
else:
    print "Type",Type," must be v or r. Will ABORT!!"
    assert(False)
# done if


list_EventSelection=EventSelections.split(",")
list_ApplyEventWeight=ApplyEventWeights.split(",")

if debug:
    print "list_EventSelection",list_EventSelection
    print "list_ApplyEventWeight",list_ApplyEventWeight

if debug:
    print "list_corrections",list_corrections

expand_dictionary=False
if debug:
    print "expand_dictonary",expand_dictionary

# bins of criteria

inclusive_bin=(float("-inf"),float("inf"))

string_LepBins="1.5"
list_LepBins=get_list_intervals(string_LepBins,debug)
list_LepBins=[]
list_LepBins.insert(0,inclusive_bin)

#string_PtVBins="90,120,160,200"
#string_PtVBins="200"
#list_PtVBins=get_list_intervals(string_PtVBins,debug)
#list_PtVBins=[]
#list_PtVBins.insert(0,inclusive_bin)
list_PtVBins=[(200,float("inf"))]

string_QBins="20,30,40,50,60,70,80,100,120,140,160,180,200,240,280"
#string_QBins="60"
list_QBins=get_list_intervals(string_QBins,debug)
list_QBins=[]
list_QBins.insert(0,inclusive_bin)

if debug:
    print "list_LepBins",list_LepBins
    print "list_PtVBins",list_PtVBins
    print "list_QBins",list_QBins

list_bin=[]
list_bin.append(("Type_lep",list_LepBins))
list_bin.append(("PtV",list_PtVBins))
list_bin.append(("M_GENWZ_j1j2",list_QBins))

if debug:
    print "list_bin",list_bin

list_binname=concatenate_all_collections(list_bin,debug)
if debug:
    print "list_binname",list_binname
    print "len(list_binname)",len(list_binname)

def merge_histograms(Histogram,debug):
    # find the lepton category for the SF
    if "lep_inf_2" in Histogram:
        Lep="El"
    elif "lep_2_inf" in Histogram:
        Lep="Mu"
    elif "lep_inf_inf" in Histogram:
        Lep="All"
    else:
        print "Neither lep_inf_2 (meaning El), nor lep_2_inf (meaning Mu), nor lep_inf_inf (meaning All) are found in Histogram",Histogram,". Will ABORT!!!"
        assert(False)
    # done if    
    dict_name_h={}
    for name in dict_name_processes:
        processes=dict_name_processes[name]
        if debug:
            print "name",name,"list processes",processes
        for i,process in enumerate(processes):
            if debug:
                print "i",i,"process",process,"suffix",Suffix
            fileName=Folder+"/"+process+Suffix+".root"
            h=retrieveHistogram(fileName,"",Histogram,"",debug).Clone()
            if debug:
                print fileName
                print Histogram,h.Integral(),h.Integral(0,h.GetNbinsX()+1)
            # make a new histogram from h to have only the range we want
            # and rebin it accordingly
            h2=resize_h1D(h,NewXMin,NewXMax,NewBinWidth,debug)
            h2.SetTitle(name)
            h2.SetName(name)
            # scale not 1 only if it's a background
            if process in dict_type_process["Background"]:
                SF=dict_bkg_lep_SF["Background"][Lep]
            elif process in dict_type_process["DataMJ"]:
                SF=dict_bkg_lep_SF["DataMJ"][Lep]
            elif process in dict_type_process["BackgroundMJ"]:
                SF=dict_bkg_lep_SF["BackgroundMJ"][Lep]
            elif process in dict_type_process["Signal"]:
                SF=dict_bkg_lep_SF["Signal"][Lep]
            elif process in dict_type_process["Data"]:
                SF=dict_bkg_lep_SF["Data"][Lep]
            else:
                print "process",process,"not found in either Background, BackgroundMJ, DataMJ, Signal, Data. Will ABORT!!"
                assert(False)
            # let's compute the SF to scale with    
            h2.Scale(SF)
            if debug:
                print "h2",h2.Integral(),h2.Integral(0,h2.GetNbinsX()+1)
            if i==0:
                dict_name_h[name]=h2
            else:
                dict_name_h[name]+=h2
        # done for loop over processes for a given merged process
    # done loop over the merged processes
    if debug:
        print "dict_name_h",dict_name_h
    return dict_name_h
# done function

def merge_histograms_total_signal_total_background(dict_name_h,debug):
    # we add two more items, 
    # the histogram that is sum of all the signals 
    # and the histogram that is sum of all the backgrounds
    dict_name_h["Signal"]=0.0
    dict_name_h["Background"]=0.0
    counterS=0
    counterB=0
    for name in dict_name_h:  
        if name=="Signal" or name=="Background":
            continue
        h=dict_name_h[name].Clone()
        if name in dict_type_process["Signal"]:
            if debug:
                print "Signal process",name,h.Integral()
            if counterS==0:
                dict_name_h["Signal"]=h
                dict_name_h["Signal"].SetTitle("Signal")
                dict_name_h["Signal"].SetName("Signal")
            else:
                dict_name_h["Signal"]+=h
            counterS+=1
        elif name in dict_type_process["Background"]:
            if debug:
                print "Background process",name,h.Integral()
            if counterB==0:
                dict_name_h["Background"]=h
                dict_name_h["Background"].SetTitle("Background")
                dict_name_h["Background"].SetName("Background")
            else:
                dict_name_h["Background"]+=h
            counterB+=1
    if debug:
        print "dict_name_h",dict_name_h
    return dict_name_h
# done function

def expand_dictionary_for_all(dict_binname_process_hist,debug):
    DesiredLepName="Type_lep_inf_inf"
    # caveat: inf_inf should come last in alphabetical order
    for binname in sorted(dict_binname_process_hist.iterkeys(),reverse=True):
        if debug:
            print "binname",binname
        dict_process_hist=dict_binname_process_hist[binname]
        if DesiredLepName in binname:
            DesiredBinName=deepcopy(binname)
            RestName=binname.replace(DesiredLepName,"")
            LepName=binname.replace(RestName,"")
            if debug:
                print "DesiredLepName",DesiredLepName,"LepName",LepName,"RestName",RestName
            for process in dict_process_hist:
                if debug:
                    print "desired",process, dict_process_hist[process].Integral()
                dict_process_hist[process].Reset()
                if debug:
                    print process, dict_process_hist[process].Integral()
        else:
            for process in dict_process_hist:
                dict_binname_process_hist[DesiredBinName][process]+=dict_binname_process_hist[binname][process]
                if debug:
                    print process, dict_process_hist[process].Integral(), dict_binname_process_hist[DesiredBinName][process].Integral()
        # done if
    # done for
    return dict_binname_process_hist
# done function


# yield
def do_yields(dict_name_h,debug):
    for name in dict_name_h:
        current_yield=dict_name_h[name].Integral()
        if debug:
            print "name",name,"current_yield",current_yield
        print "%-10s %-.2f" % (name,current_yield)
# done function

# print to canvas
def save_to_canvas(dict_name_h,debug):
    for name in dict_name_h:
        c=TCanvas("c","c",600,400)
        h=dict_name_h[name].Clone()
        h.Draw()
        c.Print(name+".pdf")
# done function

def save_to_file(fileName,dict_name_h,debug):
    file=TFile(fileName,"RECREATE")
    for name in dict_name_h:
        dict_name_h[name].Write()
    file.Write()
    file.Close()
# done function


# run
if debug:
    print "list_corrections",list_corrections
for correction in list_corrections:
    if debug:
        print "list_EventSelection",list_EventSelection
    for EventSelection in list_EventSelection:
        if debug:
            print "list_ApplyEventWeight",list_ApplyEventWeight
        for ApplyEventWeight in list_ApplyEventWeight:
            if debug:
                print "list_binname",list_binname
                print "len(list_binname)",len(list_binname)
            dict_binname_process_hist={}
            for binname in list_binname:
                if debug:
                    print "binname",binname
                    print "EventSelection",EventSelection
                    print "ApplyEventWeight",ApplyEventWeight
                    print "correction",correction
                # ex: h_All_1_Type_lep_2_inf_PtV_inf_inf_M_GENWZ_j1j2_inf_inf_M_EMJESGSMuPt4Nu200_j1j2_r
                Histogram="h_"+EventSelection+"_"+ApplyEventWeight+"_"+binname+"_"+Quantity+"_"+correction+"_"+Object+"_"+Type
                if debug:
                    print "We need  ","h_All_1_Type_lep_2_inf_PtV_inf_inf_M_GENWZ_j1j2_inf_inf_M_EMJESGSMuPt4Nu200_j1j2_r"
                    print "Histogram",Histogram
                dict_name_h=merge_histograms(Histogram,debug)
                dict_name_h=merge_histograms_total_signal_total_background(dict_name_h,debug)
                dict_binname_process_hist[binname]=dict_name_h
            # done loop over list_binname
            if expand_dictionary==True:
                # now we manipulate this dictionary in order to add to it All for Lep and All for Pt
                dict_binname_process_hist=expand_dictionary_for_all(dict_binname_process_hist,debug)
            # now save histograms to file
            for binname in list_binname:
                # Histogram="h_"+EventSelection+"_"+ApplyEventWeight+"_"+Lep+"_"+PtV+"_"+Quantity+"_"+correction+"_"+Object+"_"+Type
                Histogram="h_"+EventSelection+"_"+ApplyEventWeight+"_"+binname+"_"+Quantity+"_"+correction+"_"+Object+"_"+Type
                fileName=FolderOutput+"/"+Histogram+"_"+str(int(NewXMin*scale_name))+"_"+str(int(NewXMax*scale_name))+"_"+str(int(NewBinWidth*scale_name))+".root"
                save_to_file(fileName,dict_binname_process_hist[binname],debug)
            # done saved histograms to file
            # done loop over list_binname
        # done loop over list_ApplyEventWeight
    # done loop over list_EventSelection
# done loop over list_corrections



####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"

