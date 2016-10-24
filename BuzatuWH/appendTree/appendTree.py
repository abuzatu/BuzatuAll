#!/usr/bin/python
#import math
from HelperPyRoot import *
import copy

# Set up ROOT and RootCore:
#import ROOT
#from ROOT import TLatex,TPad,TList,TH1,TH1F,TH2F,TH1D,TH2D,TFile,TTree,TCanvas,TLegend,SetOwnership,gDirectory,TObject,gStyle,gROOT,TLorentzVector,TGraph,TMultiGraph,TColor,TAttMarker,TLine,TDatime,TGaxis,TF1,THStack,TAxis,TStyle,TPaveText,TAttFill

################################################################
################################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=4:
    print "You need some arguments, will ABORT!"
    print "Ex: "+sys.argv[0]+" Process  NrEntries Debug"
    print "Ex: "+sys.argv[0]+" llbb     100       0"
    assert(False)
# done if

# it will do the pretag and btag, the muon and inclusive into one step

Process=sys.argv[1]
NrEntries=sys.argv[2]
Debug=sys.argv[3]

fileName="~/data/Tree/tree_"+Process+".root"
treeName="perevent"
nrEntries=int(NrEntries)
debug=bool(int(Debug))

pathPtReco="~/data/histos_PtReco/"

list_particle="b1,b2".split(",")
list_variable="Pt,Eta,Phi,E".split(",")

useMyScaleList=True
myScaleList=[
#"PtRecoMoriondllbbOneMuPartonBukinNew",
#"PtRecoTrunkllbbOneMuPartonBukinNew",
#"PtRecoNowllbbOneMuPartonBukinNewTrue",
"PtRecoNowllbbOneMuTruthWZNoneNewTrue",
#"PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue",
"PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue",
"PtRecoHccllccOneMuTruthWZNoneNewTrue",
#
#"PtRecoNowllbbOneMuPartonBukinNewTrue",
#"PtRecoNowllbbOneMuPartonBukinMedianNewTrue",
#"PtRecoNowllbbOneMuPartonNoneNewTrue",
#"PtRecoNowllbbOneMuPartonNoneMedianNewTrue",
#"PtRecoNowllbbOneMuTruthWZBukinNewTrue",
#"PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue",
#"PtRecoNowllbbOneMuTruthWZNoneNewTrue",
#"PtRecoNowllbbOneMuTruthWZNoneMedianNewTrue",
#"PtRecoNowllbbOneMuPartonBukinNewFalse",
#"PtRecoNowllbbOneMuPartonBukinMedianNewFalse",
#"PtRecoNowllbbOneMuPartonNoneNewFalse",
#"PtRecoNowllbbOneMuPartonNoneMedianNewFalse",
#"PtRecoNowllbbOneMuTruthWZBukinNewFalse",
#"PtRecoNowllbbOneMuTruthWZBukinMedianNewFalse",
#"PtRecoNowllbbOneMuTruthWZNoneNewFalse",
#"PtRecoNowllbbOneMuTruthWZNoneMedianNewFalse",
]


dict_name_value={}
dict_name_branch={}

#test=array('d', [0])

def get_name(particle,scale,variable):
    return particle+"_"+scale+"_"+variable
# done function

def get_variable_value_from_tlv(tlv,variable):
    if variable=="Pt":
        return tlv.Pt()
    elif variable=="Eta":
        return tlv.Eta()
    elif variable=="Phi":
        return tlv.Phi()
    elif variable=="E":
        return tlv.E()
    else:
        print "Variable",variable,"not known. Will ABORT!"
        exit()
# done function

# create the list of scale here, use it in all the code
# to allow to add the scales by hand
# i.e. to just run on two or three instead of all combinations
# to allow for faster running when adding them to processes with lots of events

def get_PtRecoMoriond_dict_scale_sld_h(list_scale,dict_scale_sld_h):
    prefix="PtRecoMoriond"
    list_process="llbb".split(",")
    list_initial="OneMu,AllMu".split(",")
    list_target="Parton,TruthWZ".split(",")
    list_fitname="None,Gauss,Bukin".split(",")
    list_style="Old,New".split(",")
    dict_style_list_sld={
        "Old":"all".split(","),
        "New":"nosld,mu,el".split(",")
        }
    # create the things to return
    #list_scale=[]
    #dict_scale_sld_h={}
    # start the loops
    for process in list_process:
        for initial in list_initial:
            for target in list_target:
                for fitname in list_fitname:
                    for style in list_style:
                        scaleCurrent=prefix+process+initial+target+fitname+style
                        if debug:
                            print "scaleCurrent",scaleCurrent
                        list_scale.append(scaleCurrent)
                        inputfileName=pathPtReco+"/"+prefix+"/histos_"+process+"_"+initial+"_"+target+".root"
                        dict_sld_h={}
                        # loop over sld
                        for sld in dict_style_list_sld[style]:
                            histogramNameInitial="PtReco_"+sld+"_"+fitname
                            dict_sld_h[sld]=retrieveHistogram(inputfileName,"",histogramNameInitial,"",debug)
                        # done loop
                        dict_scale_sld_h[scaleCurrent]=dict_sld_h   
    # done all for
    if debug:
        print "list_scale",list_scale
    if debug:
        for scaleCurrent in dict_scale_sld_h:
            print "scaleCurrent",scaleCurrent,"dict_scale_sld_h[scaleCurrent]",dict_scale_sld_h[scaleCurrent]
    # done if
    #return list_scale,dict_scale_sld_h
# done function

def get_PtRecoTrunk_dict_scale_sld_h(list_scale,dict_scale_sld_h):
    prefix="PtRecoTrunk"
    list_process="llbb".split(",")
    list_initial="OneMu".split(",")
    list_target="Parton,TruthWZ".split(",")
    list_fitname="None,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
    list_style="Old,New".split(",")
    dict_style_list_sld={
        "Old":"inclusive".split(","),
        "New":"hadronic,muon,electron".split(",")
        }
    # create the things to return
    #list_scale=[]
    #dict_scale_sld_h={}
    # start the loops
    for process in list_process:
        for initial in list_initial:
            for target in list_target:
                for fitname in list_fitname:
                    for style in list_style:
                        scaleCurrent=prefix+process+initial+target+fitname+style
                        if debug:
                            print "scaleCurrent",scaleCurrent
                        list_scale.append(scaleCurrent)
                        inputfileName=pathPtReco+"/"+prefix+"/PtReco_histos_"+process+"_"+initial+"_"+target+".root"
                        dict_sld_h={}
                        # loop over sld
                        for sld in dict_style_list_sld[style]:
                            histogramNameInitial="PtReco_"+sld+"_"+fitname
                            dict_sld_h[sld]=retrieveHistogram(inputfileName,"",histogramNameInitial,"",debug)
                        # done loop
                        dict_scale_sld_h[scaleCurrent]=dict_sld_h   
    # done all for
    if debug:
        print "list_scale",list_scale
    if debug:
        for scaleCurrent in dict_scale_sld_h:
            print "scaleCurrent",scaleCurrent,"dict_scale_sld_h[scaleCurrent]",dict_scale_sld_h[scaleCurrent]
    # done if
    #return list_scale,dict_scale_sld_h
# done function



def get_PtRecoNow_dict_scale_sld_h(list_scale,dict_scale_sld_h):
    prefix="PtRecoNow"
    list_process="llbb".split(",")
    list_initial="OneMu".split(",")
    list_target="Parton,TruthWZ".split(",")
    list_fitname="None,NoneMedian,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
    list_style="New".split(",")
    list_normal="True,False".split(",")
    dict_style_list_sld={
        "Old":"inclusive".split(","),
        "New":"hadronic,semileptonic".split(",")
        }
    # create the things to return
    #list_scale=[]
    #dict_scale_sld_h={}
    # start the loops
    for process in list_process:
        for initial in list_initial:
            for target in list_target:
                for fitname in list_fitname:
                    for style in list_style:
                        for normal in list_normal:
                            scaleCurrent=prefix+process+initial+target+fitname+style+normal
                            if debug:
                                print "scaleCurrent",scaleCurrent
                            list_scale.append(scaleCurrent)
                            inputfileName=pathPtReco+"/"+prefix+"/PtReco_histos_"+process+"_"+initial+"_"+target+"_"+normal+".root"
                            dict_sld_h={}
                            # loop over sld
                            for sld in dict_style_list_sld[style]:
                                histogramNameInitial="PtReco_"+sld+"_"+fitname
                                dict_sld_h[sld]=retrieveHistogram(inputfileName,"",histogramNameInitial,"",debug)
                            # done loop
                            dict_scale_sld_h[scaleCurrent]=dict_sld_h   
    # done all for
    if debug:
        print "list_scale",list_scale
    if debug:
        for scaleCurrent in dict_scale_sld_h:
            print "scaleCurrent",scaleCurrent,"dict_scale_sld_h[scaleCurrent]",dict_scale_sld_h[scaleCurrent]
    # done if
    # return list_scale,dict_scale_sld_h
# done function

def get_PtRecoAZH_dict_scale_sld_h(list_scale,dict_scale_sld_h):
    prefix="PtRecoAZH"
    list_process="ggA800ToZH500".split(",")
    list_initial="OneMu".split(",")
    #list_target="Parton,TruthWZ".split(",")
    list_target="TruthWZ".split(",")
    list_fitname="None,NoneMedian,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
    list_style="New".split(",")
    #list_normal="True,False".split(",")
    list_normal="True".split(",")
    dict_style_list_sld={
        "Old":"inclusive".split(","),
        "New":"hadronic,semileptonic".split(",")
        }
    # create the things to return
    #list_scale=[]
    #dict_scale_sld_h={}
    # start the loops
    for process in list_process:
        for initial in list_initial:
            for target in list_target:
                for fitname in list_fitname:
                    for style in list_style:
                        for normal in list_normal:
                            scaleCurrent=prefix+process+initial+target+fitname+style+normal
                            if debug:
                                print "scaleCurrent",scaleCurrent
                            list_scale.append(scaleCurrent)
                            inputfileName=pathPtReco+"/"+prefix+"/PtReco_histos_"+process+"_"+initial+"_"+target+"_"+normal+".root"
                            dict_sld_h={}
                            # loop over sld
                            for sld in dict_style_list_sld[style]:
                                histogramNameInitial="PtReco_"+sld+"_"+fitname
                                dict_sld_h[sld]=retrieveHistogram(inputfileName,"",histogramNameInitial,"",debug)
                            # done loop
                            dict_scale_sld_h[scaleCurrent]=dict_sld_h   
    # done all for
    if debug:
        print "list_scale",list_scale
    if debug:
        for scaleCurrent in dict_scale_sld_h:
            print "scaleCurrent",scaleCurrent,"dict_scale_sld_h[scaleCurrent]",dict_scale_sld_h[scaleCurrent]
    # done if
    # return list_scale,dict_scale_sld_h
# done function

def get_PtRecoHcc_dict_scale_sld_h(list_scale,dict_scale_sld_h):
    prefix="PtRecoHcc"
    list_process="llcc".split(",")
    list_initial="OneMu".split(",")
    #list_target="Parton,TruthWZ".split(",")
    list_target="TruthWZ".split(",")
    list_fitname="None,NoneMedian,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
    list_style="New".split(",")
    #list_normal="True,False".split(",")
    list_normal="True".split(",")
    dict_style_list_sld={
        "Old":"inclusive".split(","),
        "New":"hadronic,semileptonic".split(",")
        }
    # create the things to return
    #list_scale=[]
    #dict_scale_sld_h={}
    # start the loops
    for process in list_process:
        for initial in list_initial:
            for target in list_target:
                for fitname in list_fitname:
                    for style in list_style:
                        for normal in list_normal:
                            scaleCurrent=prefix+process+initial+target+fitname+style+normal
                            if debug:
                                print "scaleCurrent",scaleCurrent
                            list_scale.append(scaleCurrent)
                            inputfileName=pathPtReco+"/"+prefix+"/PtReco_histos_"+process+"_"+initial+"_"+target+"_"+normal+".root"
                            dict_sld_h={}
                            # loop over sld
                            for sld in dict_style_list_sld[style]:
                                histogramNameInitial="PtReco_"+sld+"_"+fitname
                                dict_sld_h[sld]=retrieveHistogram(inputfileName,"",histogramNameInitial,"",debug)
                            # done loop
                            dict_scale_sld_h[scaleCurrent]=dict_sld_h   
    # done all for
    if debug:
        print "list_scale",list_scale
    if debug:
        for scaleCurrent in dict_scale_sld_h:
            print "scaleCurrent",scaleCurrent,"dict_scale_sld_h[scaleCurrent]",dict_scale_sld_h[scaleCurrent]
    # done if
    # return list_scale,dict_scale_sld_h
# done function


def get_sldMoriond(nrMu,nuEl):
    result=""
    if nrMu==0 and nrEl==0:
        result="nosld"
    elif nrMu>=1 and nrEl==0:
        result="mu"
    elif nrMu==0 and nrEl>=1:
        result="el"
    elif nrMu>=1 and nrEl>=1:
        result="mu"
    else:
        print "nrMu",nrMu,"nrEl",nrEl
        assert(False)
    return result
# done function

def get_sldTrunk(nrMu,nuEl):
    result=""
    if nrMu==0 and nrEl==0:
        result="hadronic"
    elif nrMu>=1 and nrEl==0:
        result="muon"
    elif nrEl>=1:
        result="electron"
    else:
        print "nrMu",nrMu,"nrEl",nrEl
        assert(False)
    return result
# done function

def get_sldNow(nrMu,nuEl):
    result=""
    if nrMu==0 and nrEl==0:
        result="hadronic"
    else:
        result="semileptonic"
    return result
# done function

#ex: fill_scale("PtRecoTest",1.03)
def fill_scale(scale_final,factor):
    tlv_final=tlv_initial*factor
    if debug:
        print "tlv_final"
        tlv_final.Print()
    for variable in list_variable:
        name_final=get_name(particle,scale_final,variable)
        dict_name_value[name_final][0]=get_variable_value_from_tlv(tlv_final,variable)
        if debug:
            print name_final,dict_name_value[name_final][0]
        dict_name_branch[name_final].Fill()
# done function


########################################################################################
############ Start running #############################################################
########################################################################################

list_scale=[]
dict_scale_sld_h={}
# each function appends to the previous one
get_PtRecoMoriond_dict_scale_sld_h(list_scale,dict_scale_sld_h)
get_PtRecoTrunk_dict_scale_sld_h(list_scale,dict_scale_sld_h)
get_PtRecoNow_dict_scale_sld_h(list_scale,dict_scale_sld_h)
get_PtRecoAZH_dict_scale_sld_h(list_scale,dict_scale_sld_h)
get_PtRecoHcc_dict_scale_sld_h(list_scale,dict_scale_sld_h)
#list_scale,dict_scale_sld_h=get_PtRecoMoriond_dict_scale_sld_h()
# if we want to run on fewer than all, replace list_scale with your choice
if debug:
    print "All the options available are:"
    for scaleCurrent in sorted(list_scale):
        print "ADRIAN scale",scaleCurrent

if useMyScaleList:
    list_scale=myScaleList
if debug:
    print "I will use this list_scale"
    for scaleCurrent in sorted(list_scale):
        print "scale",scaleCurrent

#exit()

# open the root file
file=TFile(fileName,"update")
tree=file.Get(treeName)

# loop over particles (b1, b2)
for particle in list_particle:
    # loop over the scales
    for scale in list_scale:
        if debug:
            print "scale",scale
        # loop over the variables
        for variable in list_variable:
            if debug:
                print "variable",variable
            name=get_name(particle,scale,variable)
            dict_name_value[name] =array('d',[0])
            dict_name_branch[name]=tree.Branch(name,dict_name_value[name],name+"/D")
        # done for loop over variable
    # done for loop over scale
# done for loop over particle

# nr de events to run on
if nrEntries<0:
    nrEntries=tree.GetEntries()
if debug:
    print("Number of input events: %s" % nrEntries)

# loop over entries
for i, entry in enumerate(tree):
    if i>=nrEntries:
        continue
    if debug or i%100==0:
        print "******* new event",i," **********"
        
    for particle in list_particle:
        if debug:
            print particle
        # initial tlv
        scale_initial="OneMu"
        tlv_initial=TLorentzVector()
        tlv_initial.SetPtEtaPhiE(getattr(entry,particle+"_"+scale_initial+"_Pt"),getattr(entry,particle+"_"+scale_initial+"_Eta"),getattr(entry,particle+"_"+scale_initial+"_Phi"),getattr(entry,particle+"_"+scale_initial+"_E"))
        if debug:
            print "tlv_initial"
            tlv_initial.Print()
        # nrMu, nrEl
        nrMu=getattr(entry,particle+"_nrMu")
        nrEl=getattr(entry,particle+"_nrEl")
        sldMoriond=get_sldMoriond(nrMu,nrEl)
        if debug:
            print "sldMoriond",sldMoriond
        sldTrunk=get_sldTrunk(nrMu,nrEl)
        if debug:
            print "sldTrunk",sldTrunk
        sldNow=get_sldNow(nrMu,nrEl)
        if debug:
            print "sldNow",sldNow
        # Pt
        Pt=tlv_initial.Pt() # CAREFULL, assumes GeV not MeV to evaluate PtReco
        #fill_scale(scale_final,namePtRecoHistogram)
        for scale in list_scale:
            # As a function of style choose which currentsld to use
            # Old: inclusive
            # New: hadronic, semileptonic
            currentsld=""
            if "New" in scale:
                if "Now" in scale:
                    currentsld=sldNow
                elif "Trunk" in scale:
                    currentsld=sldTrunk
                elif "Moriond" in scale:
                    currentsld=sldMoriond
                elif "AZH" in scale:
                    currentsld=sldNow
                elif "Hcc" in scale:
                    currentsld=sldNow
                else:
                    print "scale",scale,"should have Now, AZH, Trunk or Moriond inside its name to evaluate currentsld if New inside its name"
                    assert(False)
            elif "Old" in scale:
                if "Now" in scale:
                    currentsld="inclusive" # but does not exist yet, as we did not find it useful
                elif "Trunk" in scale:
                    currentsld="inclusive"
                elif "Moriond" in scale:
                    currentsld="all"
                else:
                    print "scale",scale,"should have Now, Trunk or Moriond inside its name to evaluate currentsld if Old inside its name. Will ABORT!!!"
                    assert(False)
            else:
                print "scale",scale,"should have New or Old inside its name. Will ABORT!!!"
                assert(False)
            if debug:
                print "Attempting to get factor for scale",scale,", currentsld",currentsld,", and Pt",Pt
            factor=dict_scale_sld_h[scale][currentsld].Interpolate(Pt)
            if debug:
                print "Start fill_scale(scale,factor) with scale",scale,"factor",factor
            fill_scale(scale,factor)
            if debug:
                print "Done fill_scale(scale,factor)"
        # done loop over scale
        if debug:
            print "Done loop over scales, go to the next particle"
    # done loop over particle
    if debug:
        print "Done loop over particles (b1,b2), go to the next entry (event)"
# done loop over entries
tree.Write("",TObject.kOverwrite) # to save only this latest tree
file.Close()


print "Finished!"
