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
if total!=13:
    print "You need some arguments, will ABORT!"
    print "Ex: python create.py inputFileName process suffix EventSelections ApplyEventWeights fits quantities physicsMeaning corrections listAllBins outputFileName debug"
    print "Ex: python create.py ${outputroot}/local/histo_PerJetPtReco_batch/readPaul_1_0_2BTag+GENWZ_1_perjet lvbb125 _1_0 All,GENWZ 1,0 None,Gauss,Bukin mean,rms,meanwithrms,rmsovermean r EMJESGSCMu ${outputroot}/local/batch_PtReco/readPaul_1_0_2BTag+GENWZ_1_perjet/lvbb125.root 1" 
    print "Ex: python create.py ${outputroot}/local/histo_PerJet_batch/readPaul_1_0_2BTag+GENWZ_1_perjet lvbb125 _1_0 All,GENWZ 1,0 None,Gauss,Bukin mean,rms,meanwithrms,rmsovermean f EM,EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3,EMJESGSMuPt3NNJ1 Type_lep-1.5-A+PtV-90,120,160,200-A+Pt_GENWZ-20,30,40,50,60,70,80,100,120,140,160,180,200,240,280-B ${outputroot}/local/batch_Response/readPaul_1_0_2BTag+GENWZ_1_perjet/lvbb125.root 1" 
    assert(False)
# done if

inputFileName=sys.argv[1]
process=sys.argv[2]
suffix=sys.argv[3]
EventSelections=sys.argv[4]
ApplyEventWeights=sys.argv[5]
fits=sys.argv[6]
quantities=sys.argv[7]
physicsMeaning=sys.argv[8]
corrections=sys.argv[9]
listAllBins=sys.argv[10]
outputFileName=sys.argv[11]
debug=bool(int(sys.argv[12]))

if debug:
    print "inputFileName",type(inputFileName),inputFileName
    print "process",type(process),process
    print "suffix",type(suffix),suffix
    print "EventSelections",type(EventSelections),EventSelections
    print "ApplyEventWeights",type(ApplyEventWeights),ApplyEventWeights
    print "fits",type(fits),fits
    print "quantities",type(quantities),quantities
    print "physicsMeaning",type(physicsMeaning),physicsMeaning
    print "corrections",type(corrections),corrections
    print "outputFileName",type(outputFileName),outputFileName
    print "debug",type(debug),debug

list_EventSelection=EventSelections.split(",")
list_ApplyEventWeight=ApplyEventWeights.split(",")

if debug:
    print "list_EventSelection",list_EventSelection
    print "list_ApplyEventWeight",list_ApplyEventWeight

inputFileName+="/"+process+suffix+".root"
outputFileName+="/"+process+".root"

if debug:
    print "inputFileName",inputFileName
    print "outputFileName",outputFileName

variables=updateListVariables("Pt_",corrections,"")
list_variable=variables.split(",")
if debug:
    print "list_variable",list_variable


# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

# run
create_PtReco_or_Response(inputFileName,outputFileName,list_EventSelection,list_ApplyEventWeight,listAllBins,fits,quantities,list_variable,physicsMeaning,debug)

####################################################
##### End                                   ########
####################################################

print "End Python"
