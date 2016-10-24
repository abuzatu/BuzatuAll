#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH

from ConfigNN import *

print "Start Python"
time_start=time()

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=2:
    print "You need some arguments, will ABORT!"
    print "python runTrainNN.py A1"
    print "python runTrainNN.py B1"
    print "A1, B1"
    assert(False)
# done if

listName=sys.argv[1]

list_NN=get_list_NN_all(listName)
print_list_NN(list_NN)

# assert(False)

######################################################
### train the NNs that we want #######################
### either per-jet or per-event ######################
######################################################

debug=True
step_1=True
step_2=False
doRandomizeStep1=True # true if you want different random numbers, false if all NNs start from the same point
doRandomizeStep2=True # always false

# file that will remember the characteristics of the NNs that we train 
# including how long it took to train for each NN in seconds
file_training_name="./training/training"+listName+".txt"
file_training=open(file_training_name,"w")
file_training.close()
# loop over all NNs to train them
for i,dict_tree_NN in enumerate(list_NN):
    # print i,dict_tree_NN
    for tree in dict_tree_NN:
        NN=dict_tree_NN[tree]
        if debug:
            print stringNN(NN,"b")
        if step_1:
            NN1=NN[:]
            doRandomize=doRandomizeStep1
            bestNrEpoch,bestTestError=trainNN(file_training_name,doRandomize,NN1,"_1",debug)
            if debug:
                print "ADI step 1 (old) training_file",tree,"bestNrEpoch",bestNrEpoch,"bestTestError",bestTestError
        if step_2:
            NN2=NN[:]
            # now update the number of epochs of the NN to the best nrEpoch
            NN2[6]=bestNrEpoch
            # as the previous NN
            # now train again with the the new NN of epochs, the previous files will be overwritten
            # print NN
            # print NN_new
            doRandomize=doRandomizeStep2
            bestNrEpoch,bestTestError=trainNN(file_training_name,doRandomize,NN2,"_2",debug)
            if debug:
                print "ADI step 2 (new) training_file",tree,"bestNrEpoch",bestNrEpoch,"bestTestError",bestTestError
# ended for loop over NNs

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
