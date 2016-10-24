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
    print "python runThinTree.py inputFileName inputTreeName NrEvents outputFileName"
    exit()

inputFileName=sys.argv[1]
inputTreeName=sys.argv[2]
NrEvents_string=sys.argv[3]
outputFileName=sys.argv[4]

NrEvents=int(NrEvents_string)

debug=False

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
