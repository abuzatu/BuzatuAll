#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
import numpy
import sys

####################################################
##### Inputs                                ########
####################################################

debug=False

folderName="readPaul_1_1000_TruthAll_1_event+small_readEvent_1_0_All_perevent+perjet+small"
file=TFile.Open("/Users/abuzatu/Work/ATLAS/Analyses/JER/root_output/local/"+folderName+"/lvbb125.root","READ")
assert exists(file,debug)
tree=file.Get("small")
nrEntries=tree.GetEntries()
print "This file has",nrEntries,"entries."

N=nrEntries
jets="j1,j2"
corrs="EM,EMJES,EMJESGSC,EMJESGSCMu,EMJESGSCMuPt,GENWZ,GEN,GENALL"
variables="Pt,Eta,Phi,E,M"

####################################################
##### Functions                             ########
####################################################

def get_dict_generic(N,debug):
    dict_generic={}
    for i in xrange(N):
        dict_jet_corr_variable={}
        for jet in jets.split(","):
            dict_corr_variable={}
            for corr in corrs.split(","):
                dict_variable={}
                for variable in variables.split(","):
                    dict_variable[variable]=0.0
                dict_corr_variable[corr]=dict_variable
            dict_jet_corr_variable[jet]=dict_corr_variable
        dict_generic[i]=dict_jet_corr_variable        
    # done for
    if debug:
        print "dict generic:"
        print dict_generic
    # return
    return dict_generic
# done function  

def get_dict_perevent(N,file,treename,debug):
    tree=file.Get(treename)
    assert exists(tree,debug)
    result=get_dict_generic(N,debug)
    for i,entry in enumerate(tree):
        if i>=N:
            continue
        index=i
        for jet in jets.split(","):
            for corr in corrs.split(","):
                for variable in variables.split(","):
                    result[index][jet][corr][variable]=getattr(entry,jet+"_"+corr+"_"+variable)
    # done for
    if debug:
        print "dict "+treename+":"
        print result
    # return
    return result
# done function

def get_dict_perjet(N,file,treename,debug):
    tree=file.Get(treename)
    assert exists(tree,debug)
    # we need a special treatement, given that 
    # jet 2*i is j1 from event i
    # jet 2*i+1 is j2 from event i
    # first we create the dictionary
    # then we fill it
    result=get_dict_generic(N,debug)
    for i,entry in enumerate(tree):
        if i>=2*N:
            continue
        if debug:
            print "i",i
        if i%2==0:
            jet="j1"
        else:
            jet="j2"
        index=i/2
        for corr in corrs.split(","):
            for variable in variables.split(","):
                result[index][jet][corr][variable]=getattr(entry,corr+"_"+variable)
    # done for
    if debug:
        print "dict perjet:"
        print result
    # return
    return result
# done function

def string_description(i,jet,corr,variable):
    return "%-2.0f %-4s %-15s %-7s" % (i,jet,corr,variable)
# done function

def string_values(a,b,c):
    return "%-7.2f %-7.2f %-7.2f" % (a,b,c)
# done function

def compare(N,debug):
    small=get_dict_perevent(N,file,"small",debug)
    perevent=get_dict_perevent(N,file,"perevent",debug)
    perjet=get_dict_perjet(N,file,"perjet",debug)
    
    if debug:
        print "dict_small:"
        print small
        print "perevent:"
        print perevent
        print "perjet:"
        print perjet
    
    for i in xrange(N):
        for jet in jets.split(","):
            for corr in corrs.split(","):
                for variable in variables.split(","):
                    a=small[i][jet][corr][variable]
                    b=perevent[i][jet][corr][variable]
                    c=perjet[i][jet][corr][variable]
                    if abs(a-b)>0.01 or abs(a-c)>0.01:
                    #if True:
                        print string_description(i,jet,corr,variable),string_values(a,b,c)
    # done for
# done function



####################################################
##### Start running                         ########
####################################################

print "Start Python"
compare(N,debug)
print "End Python"

####################################################
##### End Python                            ########
####################################################

exit()



