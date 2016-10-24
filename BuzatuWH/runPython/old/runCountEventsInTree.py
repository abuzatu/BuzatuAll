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
if total!=3:
    print "You need some arguments, will ABORT!"
    print "python runCountEventsInTree.py inputFileName inputTreeName"
    exit()

inputFileName=sys.argv[1]
inputTreeName=sys.argv[2]

debug=False

#
def do(inputFileName,inputTreeName,debug):
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
    NrEvents=inputTree.GetEntries()
    if debug:
        print "NrEvents",NrEvents
    print NrEvents
    os.environ["NrEvents"] = str(NrEvents)
#end function

do(inputFileName,inputTreeName,debug)

#print "End Python"

####################################################
##### End                                   ########
####################################################
