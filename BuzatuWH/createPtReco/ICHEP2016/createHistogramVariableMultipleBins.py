#!/usr/bin/python
# Adrian Buzatu, adrian.buzatu@glasgow.ac.uk, 07 April 2016
# will loop over the jet tree and fill Response of jet Pt
# in combinations of bins based on Pt, Eta, and open to other variables
# code designed to be generic, to add new veriables or bins easily
# 10 april, will remove dependece on decay, instead add it as a regular bin
# and later recombine automatically the histograms to create any binning I want


#################################################################
################### Includes ####################################
#################################################################

from HelperPyRoot import *
ROOT.gROOT.SetBatch(True)

#################################################################
################### Command line arguments ######################
#################################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=2:
    print "You need some arguments, will ABORT!"
    print "Ex: ",sys.argv[0],"Response"
    print "Ex: ",sys.argv[0],"PtReco"
    assert(False)
# done if

analysis=sys.argv[1] # Response or PtReco

#Process="ZHll125"
Process="llbb"
NumEvents=-1
debug=False
doTest=False

#Folder="160407_1" # on Adrian file
#Folder="160417_1" # on Elisabeth file
#Folder="160422_1" # on Elisabeth file veto jets with bad JVT, only 0.1% of events removed, no significant change expected
#Folder="160422_2" # on Elisabeth file veto jets with bad JVT, only 0.1% of events removed, no significant change expected, also relax b-tagging to 80% from 70%
#Folder="160422_3" # on Elisabeth file veto jets with bad JVT, only 0.1% of events removed, no significant change expected, also relax b-tagging to 80% from 70% also ask for isSignalJet (which includes extra requirements of central jet and good quality jet)
#Folder="160525_1/From-CxAOD-Elisabeth" # updated code with Elisabeth's file
#Folder="160525_1/From-CxAOD-Moriond" # updated code with Moriond tag 20-0 file
#Folder="160601_1" # based on Moriond tag 20-0 file

doReadTree=True
doMergeHisto=True
doCreateResponse=True

#################################################################
################### Test ########################################
#################################################################

#################################################################
################### Configurations ##############################
#################################################################

#
#fileName="~/data/Tree/"+Folder+"/"+Process+".root"
fileName="~/data/Tree/tree_"+Process+".root"
#treeName="perjet"
treeName="perevent"
numEvents=int(NumEvents)
#analysis="PtReco"

# old
#dict_jettype_binedgesstring={
#"inclusive": "20,25,30,35,40,45,50,55,60,65,70,80,90,100,130,300",
#"hadronic" : "20,25,30,35,40,45,50,55,60,65,70,80,90,100,130,300",
#"muon"     : "20,30,40,50,60,80,100,130,300",
#"electron" : "20,30,50,80,300"
#}

#
if analysis=="Response":
    ScalePt="NominalPt"
    Scale_Pt_xAxis_value="Nominal_Pt"
    #Scale_Pt="Parton_Pt"
    #Scale_Pt_xAxis_title="Parton p_{T}"
    Scale_Pt="TruthWZ_Pt"
    Scale_Pt_xAxis_title="TruthWZ p_{T}"
    binVariableXAxis=ScalePt # for response study as a function of Scale Pt
    #binVariableXAxis="AbsEta" # for response study as a function of AbsEtax10
    if doTest:
        string_scale="Nominal"
        dict_binVariable_listBinEdgeMerged={"Index":"0,1","AbsEta":"0.0,2.5",ScalePt:"20,30,40,50,60,70,80,90,100,130,300","Decay":"0,1"}
        list_fitName="None".split(",")
        list_fitVar="Par1".split(",")
    else:    
        string_scale="Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,Regression"
        string_scale+=",PtRecollbbOneMuPartonBukinNewTrue"
        #string_scale+=",PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonGaussNewTrue,PtRecollbbOneMuPartonGaussMedianNewTrue,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue"
        #string_scale+=",PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZGaussNewTrue,PtRecollbbOneMuTruthWZGaussMedianNewTrue,PtRecollbbOneMuTruthWZBukinNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue"
        #string_scale+=",PtRecollbbOneMuPartonNoneNewFalse,PtRecollbbOneMuPartonGaussNewFalse,PtRecollbbOneMuPartonGaussMedianNewFalse,PtRecollbbOneMuPartonBukinNewFalse,PtRecollbbOneMuPartonBukinMedianNewFalse"
        #string_scale+=",PtRecollbbOneMuTruthWZNoneNewFalse,PtRecollbbOneMuTruthWZGaussNewFalse,PtRecollbbOneMuTruthWZGaussMedianNewFalse,PtRecollbbOneMuTruthWZBukinNewFalse,PtRecollbbOneMuTruthWZBukinMedianNewFalse"

        #string_scale="Nominal"
        # good1
        #dict_binVariable_listBinEdgeMerged={"Index":"0,1,2","AbsEta":"0.0,2.5",ScalePt:"20,30,35,40,45,50,55,60,70,80,90,100,130,300","Decay":"0,1,2,3"}
        # good2
        #dict_binVariable_listBinEdgeMerged={"Index":"0,1,2","AbsEta":"0.0,2.5",ScalePt:"20,25,30,35,40,45,50,55,60,65,70,75,80","Decay":"0,1,3"}
        # good3
        #dict_binVariable_listBinEdgeMerged={"Index":"0,1,2","AbsEta":"0.0,1.0,1.4,1.6,2.5",ScalePt:"20,40,60,80,300","Decay":"0,1,2"}
        # comparing fits
        dict_binVariable_listBinEdgeMerged={"Index":"0,1,2","AbsEta":"0.0,2.5",ScalePt:"20,30,40,50,60,70,80,90,100,130,300","Decay":"0,1,2,3"}
        # comparing eta
        #dict_binVariable_listBinEdgeMerged={"Index":"0,1,2","AbsEta":"0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.5",ScalePt:"20,50,80,120,300","Decay":"0,1,2"}
        # comparing eta 2
        #dict_binVariable_listBinEdgeMerged={"Index":"0,1,2","AbsEta":"0.0,0.2,0.4,0.7,1.0,1.4,1.8,2.5",ScalePt:"20,50,75,100,300","Decay":"0,1,2"}
        if False:
            list_fitName="None,Gauss".split(",")
            list_fitVar="Par1,Par2,Ratio".split(",")
        else:
            list_fitName="None".split(",") # in some cases the Bukin fit crashes
            list_fitVar="Par1,Par2,Ratio".split(",")
elif analysis=="PtReco":
    Scale="OneMu"
    ScalePt=Scale+"Pt"
    Scale_Pt=Scale+"_Pt"
    Scale_Pt_xAxis=Scale+" p_{T}"
    # the new binning that we want based on the very fine binning we had in the beginning
    dict_binVariable_listBinEdgeMerged={"Index":"0,2","AbsEta":"0.0,2.5",ScalePt:"50,60","Decay":"0,3"}
    if doTest:
        string_scale="Parton"
    else:   
        string_scale="Parton,TruthWZ"
else:
    print "analysis",analysis,"not known. Will ABORT!!!"
    assert(False)

#
stringBinEdgePt=""
counter=0
for i in xrange(301):
    if i%5==0:
        if debug:
            print "i",i
        if counter==0:
            stringBinEdgePt+=str(i)
        else:
            stringBinEdgePt+=","+str(i)
        counter+=1
    # done if
# done for
if debug:
    print "stringBinEdgePt",stringBinEdgePt

#
stringBinEdgeAbsEta=""
counter=0
for i in xrange(26):
    if i%1==0:
        if debug:
            print "i",i
        if counter!=0:
            stringBinEdgeAbsEta+=","
        current_value=i*0.1
        stringBinEdgeAbsEta+="%.1f" % current_value
        counter+=1
    # done if
# done for
if debug:
    print "stringBinEdgeAbsEta",stringBinEdgeAbsEta

#
list_binVariable=("Index,AbsEta,"+ScalePt+",Decay").split(",")
#list_binVariable=(ScalePt+",Decay").split(",")
if doTest:
    dict_binVariable_listBinEdge={"Index":"0,1,2","AbsEta":"0.0,1.0,2.5",ScalePt:"0,50,100","Decay":"0,1,2,3"}
else:
    #dict_binVariable_listBinEdge={"Index":"0,1,2","AbsEta":stringBinEdgeAbsEta,ScalePt:stringBinEdgePt,"Decay":"0,1,2,3"} # very fine binning, too slow
    #print "ADRIAN stringBinEdgeAbsEta",stringBinEdgeAbsEta,"stringBinEdgePt",stringBinEdgePt
    dict_binVariable_listBinEdge={"Index":"0,1,2","AbsEta":"0.0,2.5",ScalePt:"20,30,40,50,60,70,80,90,100,130,300","Decay":"0,1,2,3"}
dict_binVariable_factor={"Index":1,"AbsEta":10,ScalePt:1,"Decay":1}
if debug:
    for binVariable in list_binVariable:
        factor=dict_binVariable_factor[binVariable]
        listBinEdge=dict_binVariable_listBinEdge[binVariable]
        print "binVariable",binVariable,"factor",factor,"listBinEdge",listBinEdge

#
list_scale=string_scale.split(",")
if debug:
    print "list_scale",list_scale
string_variable=string_scale
if debug:
    print "string_variable",string_variable
string_variable_updated=updateListVariables("",string_variable,"_Pt_over_"+Scale_Pt)
if debug:
    print "string_variable_updated",string_variable_updated
list_variable=string_variable_updated.split(",")
if debug:
    print "list_variable",list_variable

#
dict_variable_infoVariable={}
for scale in list_scale:
   dict_variable_infoVariable[scale+"_Pt_over_"+Scale_Pt]=[[70,0.02,2.82],[scale+" p_{T} over "+Scale_Pt_xAxis_title],["Arbitrary units"]]

#################################################################
################### Functions ###################################
#################################################################

def get_dict_binVariable_listBin(list_binVariable,dict_binVariable_listBinEdge,addInclusive,debug):
    dict_binVariable_listBin={}
    # loop over binVariable
    for binVariable in list_binVariable:
        stringBinEdge=dict_binVariable_listBinEdge[binVariable]
        if debug:
            print "binVariable",binVariable,"stringBinEdge",stringBinEdge
        if binVariable=="Decay":
            listBin=get_list_intervals(string_values=stringBinEdge,addUnderflow=False,addOverflow=False,addInclusive=False,debug=debug)
            if addInclusive:
                #listBin.append((float("0"),float("3")))
                #listBin.append((float("1"),float("3")))
                None
        elif binVariable=="Index":
            listBin=get_list_intervals(string_values=stringBinEdge,addUnderflow=False,addOverflow=False,addInclusive=False,debug=debug)
            if addInclusive:
                listBin.append((float("0"),float("2")))
                None
        elif binVariable=="AbsEta":
            listBin=get_list_intervals(string_values=stringBinEdge,addUnderflow=False,addOverflow=False,addInclusive=False,debug=debug)
            if addInclusive:
                #listBin.append((float("0"),float("2.5")))
                None
        elif binVariable==ScalePt:
            listBin=get_list_intervals(string_values=stringBinEdge,addUnderflow=False,addOverflow=False,addInclusive=False,debug=debug)
            #listBin.append((float("0"),float("inf")))
            #binMerged=(20,40)
            #listBinMerged=get_listBinMerged(listBin,binMerged,debug)
            #if debug:
            #    print "listBinMerged",listBinMerged

        else:
            print "binVariable",binVariable,"not known. Choose Index, AbsEta or Pt. Will ABORT!!!"
            assert(False)
        # end if binVariable
        if debug:
            print "listBin",listBin
        dict_binVariable_listBin[binVariable]=listBin
    # done loop over bin Variable
    return dict_binVariable_listBin
# done function

def get_dict_histoName_histo(dict_binVariable_listBin,debug):
    dict_histoName_histo={}
    if debug:
        print "dict_binVariable_listBin",dict_binVariable_listBin
    listConcatenated=get_listString_from_dict_binVariable_listBin(list_binVariable,dict_binVariable_listBin,dict_binVariable_factor,debug)
    if debug:
        print "listConcatenated",listConcatenated
    for concatenated in listConcatenated:
        histoNameBinPrefix=concatenated
        if debug:
            print "histoNameBinPrefix",histoNameBinPrefix
        for variable in list_variable:
            histoName=histoNameBinPrefix+"_"+variable
            if debug:
                print "histoName",histoName
            infoVariable=dict_variable_infoVariable[variable]
            if debug:
                print "infoVariable",infoVariable
            binningVariable=infoVariable[0]
            xAxis=infoVariable[1]
            yAxis=infoVariable[2]
            dict_histoName_histo[histoName]=TH1F(histoName,histoName, *binningVariable)
            dict_histoName_histo[histoName].GetXaxis().SetTitle(xAxis[0])
            dict_histoName_histo[histoName].GetYaxis().SetTitle(yAxis[0])
        # done loop over variable
    # done loop over concatenated
    # 
    if debug:
        for histoName in dict_histoName_histo:
            print "histoName",histoName
            histo=dict_histoName_histo[histoName]
            print type(histo),histo
    # 
    return dict_histoName_histo
# done function

def readTree(numEvents):
    # open file
    file=TFile(fileName,"READ")
    if not file.IsOpen():
        print "File",fileName,"does not exist, so will abort"
        assert(False)
    # open tree
    tree=file.Get(treeName)
    if tree==None:
        print "tree",treeName,"doesn't exist in file",fileName
        assert(False)
    # decide the number of events we run on
    nrEntries=tree.GetEntries()
    if debug:
        print "tree",treeName,"has",nrEntries,"entries."
        print "We want",numEvents,"entries"
    if numEvents<0 or numEvents>nrEntries:
        numEvents=nrEntries
    if debug:
        print "So we use",numEvents,"entries."
    
    # create the output file
    outputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_"+get_string_from_listString(list_binVariable,debug)+".root"
    outputFile=TFile(outputFileName,"Recreate")

    # create dict_binVariable_listBin without the inclusives, as not needed
    # the inclusives will be computed later on when we do the merging of what we want
    addInclusive=False
    dict_binVariable_listBin=get_dict_binVariable_listBin(list_binVariable,dict_binVariable_listBinEdge,addInclusive,debug)
    # create histograms
    dict_histoName_histo=get_dict_histoName_histo(dict_binVariable_listBin,debug)

    list_jet="b1,b2".split(",")

    if debug:
        print "******* Star loop over tree entries which is perevent with b1 and b2 ****"
    # loop over entries in tree
    for i, entry in enumerate(tree):
        if i>=numEvents:
            continue
        if debug:
            print "******* new entry ",i," **********"

        # because we are looping over the two jets as it is a perevent tree
        # since when we append new corrections to the flat tree, we append only to the perevent one
        for j,jet in enumerate(list_jet):
            # decay category definition
            NrMu=getattr(entry,jet+"_"+"nrMu")
            NrEl=getattr(entry,jet+"_"+"nrEl")
            if debug:
                print "NrMu",NrMu,"NrEl",NrEl
            # compute the the decay value
            if  NrMu==0 and NrEl==0: # hadronic, as no muon, no electron
                decay=0 # our convention
            elif  NrMu>=1 and NrEl==0: # muon, but no electron
                decay=1 # our convention
            elif NrEl>=1: # electron, but sometimes includes muon
                decay=2 # our convention

            # the values of every binVariable for this event
            dict_binVariable_value={}
            dict_binVariable_value["Index"]=j # when running per jet use i%2 # 0 means leading jet, 1 means subleading jet
            dict_binVariable_value["Decay"]=decay # 0 means hadronic, 1 means muon no electorn, 2 means electron, sometimes muon too
            dict_binVariable_value["AbsEta"]=abs(getattr(entry,jet+"_"+"Nominal_Eta"))
            dict_binVariable_value[ScalePt]=getattr(entry,jet+"_"+Scale_Pt_xAxis_value)# no more needed, we have GeV *0.001 # MeV -> GeV
            if debug:
                print "dict_binVariable_value",dict_binVariable_value

            # the variables to plot
            dict_variable_value={}
            for scale in list_scale:
                dict_variable_value[scale+"_Pt_over_"+Scale_Pt]=ratio(getattr(entry,jet+"_"+scale+"_Pt"),getattr(entry,jet+"_"+Scale_Pt))
            if debug:
                print "dict_variable_value",dict_variable_value

            # choose which bins to fill that pass the jet selection for this jet
            list_histoNameBinPrefix=[]
            if debug:
                print "dict_binVariable_listBin",dict_binVariable_listBin
            # for this decay, find in what bins we have to look into for the jet selection
            dict_binVariable_listBinSelected={}
            # loop over binVariable
            for binVariable in list_binVariable:
                listBin=dict_binVariable_listBin[binVariable]
                binValue=dict_binVariable_value[binVariable]
                listBinSelected=get_listBinSelected(listBin,binValue,debug)
                dict_binVariable_listBinSelected[binVariable]=listBinSelected
            # done loop over binVariable
            listConcatenatedSelected=get_listString_from_dict_binVariable_listBin(list_binVariable,dict_binVariable_listBinSelected,dict_binVariable_factor,debug)
            if debug:
                print "listConcatenatedSelected",listConcatenatedSelected
            # fill histograms
            for concatenated in listConcatenatedSelected:
                if debug:
                    print "concatenated",concatenated
                # loop over variables
                for variable in list_variable:
                    histoName=concatenated+"_"+variable
                    value=dict_variable_value[variable]
                    dict_histoName_histo[histoName].Fill(value)
                # done loop over variables
            # done loop over concatenated
        # done loop over the two jets in the event
    # end loop over the entries in the tree, which are events in the perevent tree
    if debug:
        print "******* End loop over tree entries ****"
    outputFile.Write()
    outputFile.Close()
# done function

def get_a(list_binVariableMerged):
    addInclusive=False # we want to have the inclusive ones as well
    dict_binVariable_listBin=get_dict_binVariable_listBin(list_binVariable,dict_binVariable_listBinEdge,addInclusive,debug)
    # the new binning that we want based on the very fine binning we had in the beginning
    #dict_binVariable_listBinEdgeMerged={"Index":"0,2","AbsEta":"0.0,2.5",ScalePt:"50,60","Decay":"0,3"}
    # the bins I want based on this merging
    #dict_binVariable_listBinMerged {'Index': [(0.0, 2.0)], 'PartonPt': [(0.0, 100.0), (100.0, 300.0)], 'AbsEta': [(0.0, 1.0), (1.0, 2.5)], 'Decay': [(0.0, 1.0), (1.0, 3.0)]}
    addInclusive=True # we want to have the inclusive ones as well
    dict_binVariable_listBinMerged=get_dict_binVariable_listBin(list_binVariableMerged,dict_binVariable_listBinEdgeMerged,addInclusive,debug)
    if debug:
        print "dict_binVariable_listBinMerged",dict_binVariable_listBinMerged
    # now create
    # big <type 'list'> [{'Index': (0.0, 2.0)}]
    # big <type 'list'> [{'AbsEta': (0.0, 1.0)}, {'AbsEta': (1.0, 2.5)}]
    # big <type 'list'> [{'PartonPt': (0.0, 100.0)}, {'PartonPt': (100.0, 300.0)}]
    # big <type 'list'> [{'Decay': (0.0, 1.0)}, {'Decay': (1.0, 3.0)}]
    listBig=[]
    for binVariable in list_binVariableMerged:
        result=get_list_dict_binVariable_bin(binVariable,dict_binVariable_listBinMerged,debug)
        if debug:
            print type(result),"result",result
        listBig.append(result)
    # done for
    if debug:
        print "listBig",listBig
        for big in listBig:
            print "big",type(big),big

    # all [{'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (0.0, 1.0), 'Decay': (0.0, 1.0)}, {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (0.0, 1.0), 'Decay': (1.0, 3.0)}, {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (0.0, 1.0), 'Decay': (0.0, 1.0)}, {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (0.0, 1.0), 'Decay': (1.0, 3.0)}, {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (1.0, 2.5), 'Decay': (0.0, 1.0)}, {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (1.0, 2.5), 'Decay': (1.0, 3.0)}, {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (1.0, 2.5), 'Decay': (0.0, 1.0)}, {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (1.0, 2.5), 'Decay': (1.0, 3.0)}]
    # e {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (0.0, 1.0), 'Decay': (0.0, 1.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (0.0, 1.0), 'Decay': (1.0, 3.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (0.0, 1.0), 'Decay': (0.0, 1.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (0.0, 1.0), 'Decay': (1.0, 3.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (1.0, 2.5), 'Decay': (0.0, 1.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (0.0, 100.0), 'AbsEta': (1.0, 2.5), 'Decay': (1.0, 3.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (1.0, 2.5), 'Decay': (0.0, 1.0)}
    # e {'Index': (0.0, 2.0), 'PartonPt': (100.0, 300.0), 'AbsEta': (1.0, 2.5), 'Decay': (1.0, 3.0)}
    list_dict_binVariable_bin=concatenate_all_list_dict_binVariable_bin(listBig,debug)
    if debug:
        print "list_dict_binVariable_bin",list_dict_binVariable_bin
        for dict_binVariable_bin in list_dict_binVariable_bin:
            print "dict_binVariable_bin",dict_binVariable_bin
    #
    return dict_binVariable_listBin,list_dict_binVariable_bin
# done function

def get_b(dict_binVariable_listBin,list_dict_binVariable_bin):
    # create list of prefix of histograms that we want to fill
    list_histoPrefix=[]
    #list_dict_binVariable_listBinToMerge=[]
    list_list_histoPrefixToMergeForOneBinCombination=[]
    for dict_binVariable_bin in list_dict_binVariable_bin:
        if debug:
            print " ********** dict_binVariable_bin **********",dict_binVariable_bin
        histoPrefix=get_string_from_dict_binVariable_bin(list_binVariable,dict_binVariable_bin,dict_binVariable_factor,debug)
        if debug:
            print "histoPrefix",histoPrefix
        list_histoPrefix.append(histoPrefix)
        #
        dict_binVariable_listBinToMerge={}
        for binVariable in list_binVariable:
            listBin=dict_binVariable_listBin[binVariable]
            binMerged=dict_binVariable_bin[binVariable]
            dict_binVariable_listBinToMerge[binVariable]=get_listBinMerged(listBin,binMerged,debug)
        # done for loop over binVariable
        if debug:
            print "dict_binVariable_listBinToMerge",dict_binVariable_listBinToMerge
        #continue
        #list_dict_binVariable_listBinToMerge.append(dict_binVariable_listBinToMerge)
        listBigToMerge=[]
        for binVariable in list_binVariable:
            result=get_list_dict_binVariable_bin(binVariable,dict_binVariable_listBinToMerge,debug)
            if debug:
                print type(result),"result",result
            listBigToMerge.append(result)
        # done for
        if debug:
            print "listBigToMerge",listBigToMerge
            for big in listBigToMerge:
                print "big",type(big),big
        # get all the combination of prefixes that we want for the histograms to add for this particular bin
        list_dict_binVariable_binToMerge=concatenate_all_list_dict_binVariable_bin(listBigToMerge,debug)
        if debug:
            print "list_dict_binVariable_binToMerge",list_dict_binVariable_binToMerge
            for dict_binVariable_binToMerge in list_dict_binVariable_binToMerge:
                print "dict_binVariable_binToMerge",dict_binVariable_binToMerge
            print "get histoPrefixToMerge"
        # now we have the list of the bins to merge, for each get the prefix name
        list_histoPrefixToMergeForOneBinCombination=[]
        for dict_binVariable_binToMerge in list_dict_binVariable_binToMerge:
            if debug:
                print "dict_binVariable_binToMerge",dict_binVariable_binToMerge
            histoPrefixToMerge=get_string_from_dict_binVariable_bin(list_binVariable,dict_binVariable_binToMerge,dict_binVariable_factor,debug)
            if debug:
                print "histoPrefixToMerge",histoPrefixToMerge
            list_histoPrefixToMergeForOneBinCombination.append(histoPrefixToMerge)
        # done loop over all the bins to merge for one bin combination
        if debug:
            for histoPrefixToMergeForOneBinCombination in list_histoPrefixToMergeForOneBinCombination:
                print "histoPrefixToMergeForOneBinCombination",histoPrefixToMergeForOneBinCombination
        list_list_histoPrefixToMergeForOneBinCombination.append(list_histoPrefixToMergeForOneBinCombination)
    # done for loop over list of list_dict_binVariable_bin (loop over bin combinations)
    if debug:
        print " "
        print " "
        print "******** Print the list of histograms to create and for each which histograms to add  *************"
    if debug:
        print "list_histoPrefix",list_histoPrefix
        for i,histoPrefix in enumerate(list_histoPrefix):
            print "i",i,"histoPrefix",histoPrefix
            for histoPrefixToMergeForOneBinCombination in list_list_histoPrefixToMergeForOneBinCombination[i]:
                print "histoPrefixToMergeForOneBinCombination",histoPrefixToMergeForOneBinCombination
            #print list_dict_binVariable_listBinToMerge[i]
            #print "list_histoPrefixToMergeForOneBinCombination",list_list_histoPrefixToMergeForOneBinCombination[i]
    # done if debug
    return list_histoPrefix,list_list_histoPrefixToMergeForOneBinCombination
# done function

def mergeHisto():
    list_binVariableMerged=list_binVariable
    dict_binVariable_listBin,list_dict_binVariable_bin=get_a(list_binVariableMerged)  
    list_histoPrefix,list_list_histoPrefixToMergeForOneBinCombination=get_b(dict_binVariable_listBin,list_dict_binVariable_bin)

    for i,histoPrefix in enumerate(list_histoPrefix):
        if debug:
            print ""
            print "***** histoPrefix ***** ",histoPrefix
    #
    #return 0

    if debug:
        print " "
        print " "
        print "******** Start create histograms *************"
    
    inputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_"+get_string_from_listString(list_binVariable,debug)+".root"
    inputFile=TFile(inputFileName,"Read")
    if not inputFile.IsOpen():
        print "File",inputFileName,"does not exist, so will abort"
        assert(False)
    
    outputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_"+get_string_from_listString(list_binVariable,debug)+".root"
    outputFile=TFile(outputFileName,"Recreate")
    #
    # create the histograms we want to fill as sums
    dict_histoName_histo={}
    for i,histoPrefix in enumerate(list_histoPrefix):
        if debug:
            print ""
            print "***** histoPrefix ***** ",histoPrefix
        list_histoPrefixToMergeForOneBinCombination=list_list_histoPrefixToMergeForOneBinCombination[i]
        if debug:
            for histoPrefixToMergeForOneBinCombination in list_histoPrefixToMergeForOneBinCombination:
                print "histoPrefixToMergeForOneBinCombination",histoPrefixToMergeForOneBinCombination
        # loop over variables
        for variable in list_variable:
            histoName=histoPrefix+"_"+variable
            if debug:
                print "histoName",histoName
            histMerged=0
            # for this histogram get all the histograms that we want to sum up
            #list_histoNameToMerge=[]
            for j,histoPrefixToMergeForOneBinCombination in enumerate(list_histoPrefixToMergeForOneBinCombination):
                histoNameToMerge=histoPrefixToMergeForOneBinCombination+"_"+variable
                if debug:
                    print "histoNameToMerge",histoNameToMerge
                #list_histoNameToMerge.append(histoNameToMerge)
                hist=inputFile.Get(histoNameToMerge)
                if hist==None:
                    print "histo",histoNameToMerge,"doesn't exist in file",inputFileName,". We will ABORT!!!!"
                    assert(False)
                if debug:
                    print "hist type",type(hist),hist.GetEntries(),hist.GetName()
                if j==0:
                    histMerged=hist
                else:
                    histMerged+=hist
            # done for loop over list_histoPrefixToMergeForOneBinCombination
            if debug:
                print "histMerged type",type(histMerged),histMerged.GetEntries(),histMerged.GetName()
            histMerged.SetName(histoName)
            histMerged.SetTitle(histoName)
            if debug:
                print "histMerged type",type(histMerged),histMerged.GetEntries(),histMerged.GetName()
            dict_histoName_histo[histoName]=histMerged.Clone()
            hist.SetDirectory(0) # do not save to three the last histoToMerge that was used
            if True:
                print "Writing histogram",histoName
        # done loop over variables
    # done loop over concatenated
    outputFile.Write()
    outputFile.Close()
    return 0
# done function

def createResponse():
    if debug:
        print ""
        print "Start createResponse()"
    inputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_"+get_string_from_listString(list_binVariable,debug)+".root"
    inputFile=TFile(inputFileName,"Read")
    if not inputFile.IsOpen():
        print "File",inputFileName,"does not exist, so will abort"
        assert(False)

    if debug:
        print "binVariableXAxis",binVariableXAxis
    if debug:
        print "list_binVariable",list_binVariable
    list_binVariableReduced=list_binVariable[:]
    list_binVariableReduced.remove(binVariableXAxis)
    if debug:
        print "list_binVariableReduced",list_binVariableReduced

    # from initial one
    if debug:
        print "dict_binVariable_listBinEdgeMerged",dict_binVariable_listBinEdgeMerged
    # x axis binning
    XAxisStringList=dict_binVariable_listBinEdgeMerged[binVariableXAxis].split(",")
    if debug:
        print "XAxisStringList",XAxisStringList
    numBins=len(XAxisStringList)-1
    if debug:
        print "numBins",numBins
    numpyarraybinedges=get_numpyarray_from_listString(XAxisStringList,debug)
    if debug:
        print "numpyarraybinedges",numpyarraybinedges


    # create histograms
    outputFileName="~/data/histos_PtReco/perjet_histos_process_"+Process+"_merged_"+get_string_from_listString(list_binVariableReduced,debug)+".root"
    outputFile=TFile(outputFileName,"Recreate")

    #return 0

    list_binVariableMerged=list_binVariableReduced
    dict_binVariable_listBin,list_dict_binVariable_bin=get_a(list_binVariableMerged)
    dict_binVariable_listBin,list_dict_binVariable_binOriginal=get_a(list_binVariable)  
    dict_histoNameCombined_histo={}
    for dict_binVariable_bin in list_dict_binVariable_bin:
        if debug:
            print "dict_binVariable_bin",dict_binVariable_bin
        histoPrefixCombined=get_string_from_dict_binVariable_bin(list_binVariableMerged,dict_binVariable_bin,dict_binVariable_factor,debug)
        if debug:
            print "histoPrefixCombinded",histoPrefixCombined
        # for this histogram, find the name of all the histograms we want to add
        list_histoPrefixToMerge=[]
        # the trick is to loop over all of them and keep only those that have the other as above
        for dict_binVariable_binOriginal in list_dict_binVariable_binOriginal:
            if debug:
                print "dict_binVariable_binOriginal",dict_binVariable_binOriginal
            # find if this one is is the same as dict_binVariable_bin but with something extra
            isGood=dict_binVariable_bin.viewitems() <=  dict_binVariable_binOriginal.viewitems()
            if debug:
                print "isGood",isGood
            if isGood==True:
                histoPrefixToMerge=get_string_from_dict_binVariable_bin(list_binVariable,dict_binVariable_binOriginal,dict_binVariable_factor,debug)
                if debug:
                    print "histoPrefixToMerge",histoPrefixToMerge
                list_histoPrefixToMerge.append(histoPrefixToMerge)
            # done if
        # done for loop over list_dict_binVariable_binOrigina
        # done list_histoPrefixToMerge
        if debug:
            print "list_histoPrefixToMerge"
            for histoPrefixToMerge in list_histoPrefixToMerge:
                print "histoPrefixToMerge",histoPrefixToMerge
        for variable in list_variable:
            if debug:
                print "variable",variable
            for fitName in list_fitName:
                if debug:
                    print "fitName",fitName
                for fitVar in list_fitVar:
                    # create the main histogram
                    histoNameCombined=histoPrefixCombined+"_"+variable+"_"+fitName+"_"+fitVar
                    if debug:
                        print "histoNameCombined",histoNameCombined 
                    dict_histoNameCombined_histo[histoNameCombined]=TH1F(histoNameCombined,histoNameCombined,numBins,numpyarraybinedges)
                    for i,histoPrefixToMerge in enumerate(list_histoPrefixToMerge):
                        histoNameEachBin=histoPrefixToMerge+"_"+variable
                        if debug:
                            print "histoNameEachBin",histoNameEachBin
                        # retrieve histogram
                        histoEachBin=inputFile.Get(histoNameEachBin)
                        if histoEachBin==None:
                            print "histo",histoNameEachBin,"doesn't exist in file",inputFileName,". We will ABORT!!!!"
                            assert(False)
                        # perform fit
                        if debug:
                            print "fitName",fitName
                        #f,result_fit=fit_hist(histoEachBin.Clone(),fitName,"",debug)
                        canvasname="~/data/histos_PtReco/canvasname_"+histoEachBin.GetName()
                        f,result_fit=fit_hist(h=histoEachBin.Clone(),fit=fitName,addMedianInFitInfo=False,plot_option="",doValidationPlot=True,canvasname=canvasname,debug=debug)
                        if debug:
                            print "fitVar",fitVar
                        value,error=get_value_error_from_result_fit(fitVar,result_fit,debug)
                        if debug:
                            print "value",value,"error",error
                        # careful, bin 0 is underflow, so use i+1
                        dict_histoNameCombined_histo[histoNameCombined].SetBinContent(i+1,value)
                        dict_histoNameCombined_histo[histoNameCombined].SetBinError(i+1,error)
                    # done loop over all the bins
                # done loop over fitVar
            # done loop over fitName
        # done loop over variable
    # histograms done, save and exit
    outputFile.Write()
    outputFile.Close()
    return 0
# done function

#################################################################
################### Run #########################################
#################################################################

if doReadTree:
    readTree(numEvents)
if doMergeHisto:
    mergeHisto()
if doCreateResponse:
    createResponse()

#################################################################
################### Finished ####################################
#################################################################
