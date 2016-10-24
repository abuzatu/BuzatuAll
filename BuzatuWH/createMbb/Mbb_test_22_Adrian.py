#!/usr/bin/python
from HelperPyRoot import *
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TF1, TCanvas, TPaveText, TLegend, TLatex, TGraph
from array import array

debug=False

# retrieve the three PtReco histograms needed, use Adrian's function of retrieveHistogram, and also store the result in a dictionary
# so that we keep one data, not tree
#fileName="rootfiles/Topo_AllMu_corr_truthWZ.root" # for Yara
fileName="/Users/abuzatu/data/histos_PtReco/ttbar/Topo_AllMu_corr_truthWZ.root" # for Adrian
dict_sld_histo={}
dict_sld_histo["nosld"]=retrieveHistogram(fileName=fileName,histoPath="",histoName="corrHist_bjets_none",name="",debug=debug)
dict_sld_histo["mu"]=retrieveHistogram(fileName=fileName,histoPath="",histoName="corrHist_bjets_mu",name="",debug=debug)
dict_sld_histo["el"]=retrieveHistogram(fileName=fileName,histoPath="",histoName="corrHist_bjets_el",name="",debug=debug)

# create function that based on the number of mu and el returns which histogram should be used

def get_sldname(nrMu, nrEl, debug):
    result=""
    # different contend of the b-jets
    # nrMu==0 and nrEl==0, use nosld
    # nrMu==1 and nrEl==0, use mu
    # nrMu==0 and nrEl==1, use el
    # nrMu>=1 and nrEl>=1, use mu
    #   Jets 
    if nrMu==0 and nrEl==0:
        result="nosld"    
    elif nrMu==1 and nrEl==0:
        result="mu"  
    elif nrMu==0 and nrEl==1:
        result="el"  
    else: 
        # at least one mu and one el, use the mu
        result="mu"
    # calculation done
    return result
# done function


def createHistogram():
    inputFile=TFile("/Users/abuzatu/data/Tree/160824_1_CxAOD_alltruth/tree_llbb.root","READ")
    # inputFile=TFile("/Users/yarita/Documents/chihuahua_chihuahua/bb_physics/Adrian_Rio_2016/A_Gap_and_crack_studies_CxAOD_24-7/tree_llbb_CxAOD_24_7.root","READ")
    # inputFile=TFile("/home/thales/Pesquisa/Adrian-Run-II/tree_llbb.root","READ")
    inputTree=inputFile.Get("perevent")
    outputFileName="Mbb_corr_22_Adrian.root"
    #list_name="inclusive,0,1,2".split(",")
    numEvents= -1
    bs="b1,b2".split(",")  
    #scalesstring="Parton,TruthWZ,Nominal,Regression,OneMu,PtRecoTruthWZBukinMedian,PtRecoTruthWZNone"
    scalesstring="TruthWZ,Nominal,OneMu,PtRecoTruthWZNone,PtRecoTruthWZBukinMedian,PtRecoFromTTbar,Regression"
    scales=scalesstring.split(",")
    variableNames="Pt,Eta,Phi,E".split(",")
    #variableNames2="Pt,E".split(",")
  
    # now for the desired corrections do the plotting
    outputFile=TFile(outputFileName,"RECREATE")
    # dictionary creation for storage of the histograms
    dict_name_hist={}
    # now loop again over the scales in order to create the histograms and plot them
    for scale in scales:
        # regular corrections and added by us corrections
        histoName="h_"+scale+"_Mass"
        dict_name_hist[scale]=TH1F(histoName,histoName,50,2.5,252.5)
    # done loop over histograms

    # decide the number of events we run on
    nrEntries=inputTree.GetEntries()
    if numEvents<0 or numEvents>nrEntries:
        numEvents=nrEntries
    # loop over entries
    for i, event in enumerate(inputTree):
        if i>=numEvents:
            continue
        if debug:
            print "******* new event **********"
        #
        dict_scale_obj_tlv={}
        dict_scale_obj_tlv_corr={}
        # loop over scales
        for scale in scales:
            dict_obj_tlv={}
            dict_obj_tlv_corr={}
            dict_obj_tlv["bb"]=TLorentzVector()
            dict_obj_tlv_corr["bb"]=TLorentzVector()
            # loop over the two jets of the event, j1 and j2
            for b in bs:
                # this is what we do for scales that we compute ourselves now
                if scale=="PtRecoFromTTbar":
                    # Pt on top of which we apply the PtReco
                    Pt = getattr(event,b+"_OneMu_Pt")
                    if Pt<30.0:
                        Pt=30.0
                    # also calculate the 4-vector of OneMu, to apply the correction on top of it
                    values_list=[getattr(event,b+"_"+"OneMu"+"_"+var) for var in variableNames]
                    if debug:
                        print values_list
                    dict_obj_tlv[b]=TLorentzVector()
                    dict_obj_tlv[b].SetPtEtaPhiE(*values_list)
                    # so far the 4-vector for the desired new scale is the same as OneMu
                    # now we correct it by multiplying with a correction factor
                    # the number of muon and electron, to calculate sld value
                    bs_nrMu = getattr(event,b+"_nrMu")
                    bs_nrEl = getattr(event,b+"_nrEl")
                    # find out in which category it falls, to see which histogram we interpolate
                    sldname=get_sldname(bs_nrMu, bs_nrEl, debug)
                    # for this sldname, there is a histogram, and for that histogram, calculate the correction factor
                    if debug:
                        print "Pt",Pt,"type Pt",type(Pt)
                        print "sldname",sldname,"type of hist",type(dict_sld_histo[sldname])
                    correction_factor=dict_sld_histo[sldname].Interpolate(Pt)
                    # now scale the 4-vector (which is so far hard coded to OneMu) with this correction factor
                    dict_obj_tlv[b]*=correction_factor
                else:
                    # this is what we do for all the scales that we already have stored in the flat tree
                    values_list=[getattr(event,b+"_"+scale+"_"+var) for var in variableNames]
                    if debug:
                        print values_list
                    dict_obj_tlv[b]=TLorentzVector()
                    dict_obj_tlv[b].SetPtEtaPhiE(*values_list)
                # done if scale is already in tree or not
                if debug:
                    print scale,b
                    dict_obj_tlv[b].Print()
                    #dict_obj_tlv_corr[b].Print()
                # add the current jet to the bb TLorentz which is empty at first     
                dict_obj_tlv["bb"]+=dict_obj_tlv[b]
            # done loop over the two b jets
            # now we finished for this desired scale, so store the 4-vectors (b1, b2, bb) in a dictionary         
            dict_scale_obj_tlv[scale]=dict_obj_tlv
            # calculate histo name
            histoName="h_"+scale+"_Mass"
            # calculate mbb for this scale and for this event
            mbb=dict_scale_obj_tlv[scale]["bb"].M()
            if debug:
                print scale,"mbb",mbb
            # fill the histogram for this scale and for this event
            dict_name_hist[scale].Fill(mbb)
        # done loop over scales
    # done loop over all the events in the tree
    outputFile.Write()
    outputFile.Close()
    # done storign the histograms in a new file
# done function createHistogram()

###########################
### now run the code ######
createHistogram()
###########################
