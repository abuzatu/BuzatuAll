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

#print "Start Python"

total = len(sys.argv)
# number of arguments plus 1
if total!=5:
    print "You need some arguments, will ABORT!"
    print "python runCleanTree.py inputFileName inputTreeName NrEvents outputFileName"
    exit()

inputFileName=sys.argv[1]
inputTreeName=sys.argv[2]
NrEvents_string=sys.argv[3]
outputFileName=sys.argv[4]

NrEvents=int(NrEvents_string)

debug=False

assert(inputTreeName=="perjet" or inputTreeName=="perevent")

#
def skim(inputFileName,inputTreeName,NrEvents,outputFileName,debug):
    if debug:
        print "inputFileName",inputFileName
    # open the desied file
    inputFile=TFile(inputFileName,"READ")
    # check that the file was open correctly and if not, abort
    exists(inputFile,debug)
    # retrieve the desired tree from the file
    inputTree=inputFile.Get(inputTreeName)
    # check that the tree exists and if not, abort
    # but this does not abort even if the treeName is wrong
    exists(inputTree,debug)
    if debug:
        print type(inputTree),inputTree
        print NrEvents,type(NrEvents)
    if(NrEvents==0):
        NrEvents=inputTree.GetEntries()
    if debug:
        print "NrEvents",NrEvents

    # create output file
    if debug:
        print "outputFileName",outputFileName
    outputFile=TFile(outputFileName,"RECREATE")
    outputTree=inputTree.CloneTree(0)

    # loop over all the entries in the tree
    for i,entry in enumerate(inputTree):
        if debug:
            if i>=10:
                continue
        if debug:
            print "************* next tree entry *************"

        if NrEvents>0:
            if i>=NrEvents:
                continue
            
        selection=True
        if False:
            if inputTreeName=="perjet":
                # selection&=bool(getattr(entry,"hasSV"))
                # selection&=bool(getattr(entry,"hasMuon"))
                selection&=getattr(entry,"SumPtTrk")<300.0
                selection&=getattr(entry,"EMJESGSCMuPt3_Pt")<300.0
                selection&=getattr(entry,"SumPtTrk_EMJESGSCMuPt3_Pt")<4.0
                selection&=getattr(entry,"SVLxy")<40.0
                selection&=getattr(entry,"SVLxyErr")<1.0
                selection&=getattr(entry,"SVLxySig")<100.0
                selection&=getattr(entry,"MuEffectPt")<60.0
                selection&=getattr(entry,"TrkWidth")>-1
                selection&=getattr(entry,"JVF")>-1
            elif inputTreeName=="perevent":
                # j1
                # selection&=bool(getattr(entry,"j1_hasSV"))
                # selection&=bool(getattr(entry,"j1_hasMuon"))
                selection&=getattr(entry,"j1_SumPtTrk")<300.0
                selection&=getattr(entry,"j1_EMJESGSCMuPt3_Pt")<300.0
                selection&=getattr(entry,"j1_SumPtTrk_EMJESGSCMuPt3_Pt")<4.0
                selection&=getattr(entry,"j1_SVLxy")<40.0
                selection&=getattr(entry,"j1_SVLxyErr")<1.0
                selection&=getattr(entry,"j1_SVLxySig")<100.0
                selection&=getattr(entry,"j1_MuEffectPt")<60.0
                selection&=getattr(entry,"j1_TrkWidth")>-1
                selection&=getattr(entry,"j1_JVF")>-1
                # j2
                # selection&=bool(getattr(entry,"j2_hasSV"))
                # selection&=bool(getattr(entry,"j2_hasMuon"))
                selection&=getattr(entry,"j2_SumPtTrk")<300.0
                selection&=getattr(entry,"j2_EMJESGSCMuPt3_Pt")<300.0
                selection&=getattr(entry,"j2_SumPtTrk_EMJESGSCMuPt3_Pt")<4.0
                selection&=getattr(entry,"j2_SVLxy")<40.0
                selection&=getattr(entry,"j2_SVLxyErr")<1.0
                selection&=getattr(entry,"j2_SVLxySig")<100.0
                selection&=getattr(entry,"j2_MuEffectPt")<60.0
                selection&=getattr(entry,"j2_TrkWidth")>-1
                selection&=getattr(entry,"j2_JVF")>-1
                # j1j2
                selection&=getattr(entry,"j1j2_EMJESGSCMuPt3_M")<300.0
        if selection:
            outputTree.Fill()
    # done loop over the entriees
    # save the file with all the histograms created
    #outputTree.Print()
    outputFile.Write()
    outputFile.Close()
#end function

skim(inputFileName,inputTreeName,NrEvents,outputFileName,debug)

#print "End Python"

####################################################
##### End                                   ########
####################################################
