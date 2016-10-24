#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for exah1D_name_rmple, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
from HelperWH import *
from ConfigWH import *

print "Start Python"

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=9:
    print "You need some arguments, will ABORT!"
    print "Ex: python createHistogramPerEvent.py inputFileName treeName NrEventStart NrEventEnd EventSelections ApplyEventWeights outputFileName debug"
    print "Ex: python createHistogramPerEvent.py ${outputroot}/batch/readPaul_1_0_J1Pt45+2BTag_1_perevent/lvbb125.root perevent 1 0 All,GENWZ 1,0 ${outputroot}/local/batch_histo/readPaul_1_0_J1Pt45+2BTag_1_perevent/lvbb125.root 1" 
    assert(False)
# done if

inputFileName=sys.argv[1]
treeName=sys.argv[2]
NrEventStart=int(sys.argv[3])
NrEventEnd=int(sys.argv[4])
EventSelections=sys.argv[5]
ApplyEventWeights=sys.argv[6]
outputFileName=sys.argv[7]
debug=bool(int(sys.argv[8]))

if debug:
    print "inputFileName",type(inputFileName),inputFileName
    print "treeName",type(treeName),treeName
    print "EventSelections",type(EventSelections),EventSelections
    print "ApplyEventWeights",type(ApplyEventWeights),ApplyEventWeights
    print "NrEventStart",type(NrEventStart),NrEventStart
    print "NrEventEnd",type(NrEventEnd),NrEventEnd
    print "outputFileName",type(outputFileName),outputFileName
    print "debug",type(debug),debug

list_EventSelection=EventSelections.split(",")
list_ApplyEventWeight=ApplyEventWeights.split(",")

if debug:
    print "list_EventSelection",list_EventSelection
    print "list_ApplyEventWeight",list_ApplyEventWeight

if debug:
    print "list_corrections",list_corrections

# run
list_h1D=[]
list_h1D+=get_list_h1D("v","None","M","j1j2",(500,0,500),(1,0,0,1),("Di-jet invariant mass [GeV]",0.045,0.90),("Entries",0.045,0.95),list_corrections,debug)
list_h1D+=get_list_h1D("r","GENWZ","M","j1j2",(300,0,3),(1,0,0,1),("Di-jet invariant mass response",0.045,0.90),("Entries",0.045,0.95),list_corrections,debug)

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

list_bin_name=concatenate_all_collections(list_bin,debug)
if debug:
    print "list_bin_name",list_bin_name
    print "len(list_bin_name)",len(list_bin_name)

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

#run
create_h1D_primary(inputFileName,treeName,outputFileName,list_EventSelection,list_ApplyEventWeight,list_bin,list_bin_name,list_h1D,NrEventStart,NrEventEnd,debug)

####################################################
##### End                                   ########
####################################################

print "End Python"
