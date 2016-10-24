#!/usr/bin/python
from HelperPyRoot import *

debug=False

def createHistogram():
    inputFile=TFile("tree_llbb.root","READ")
    inputTree=inputFile.Get("perevent")
    outputFile=TFile("Mbb.root","RECREATE")
    list_name="inclusive,0,1,2".split(",")
    numEvents=-1
    bs="b1,b2".split(",")  
    scalesstring="TruthWZ,Parton,Nominal,Regression,OneMu,PtRecoBukin"
    #scalesstring="Nominal"
    scales=scalesstring.split(",")
    variableNames="Pt,Eta,Phi,E".split(",")
    dict_name_hist={}
    for scale in scales:
        for histoName in list_name:
            name=scale+"_"+histoName
            dict_name_hist[name]=TH1F("h_"+name,"h_"+name,40,48.5,168.5)
    #
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
        for scale in scales:
            dict_obj_tlv={}
            dict_obj_tlv["bb"]=TLorentzVector()
            for b in bs:
                values_list=[getattr(event,b+"_"+scale+"_"+var) for var in variableNames]
                if debug:
                    print values_list
                dict_obj_tlv[b]=TLorentzVector()
                dict_obj_tlv[b].SetPtEtaPhiE(*values_list)
                if debug:
                    dict_obj_tlv[b].Print()
                dict_obj_tlv["bb"]+=dict_obj_tlv[b]
            # done loop over the two b jets
            dict_scale_obj_tlv[scale]=dict_obj_tlv
            # bb defined as b1+b2
        # done loop over all scales

        dict_b_AbsEta={}
        for b in bs:
            dict_b_AbsEta[b]=abs(dict_scale_obj_tlv["Nominal"][b].Eta())
        # 
        if debug:
            print "dict_b_AbsEta",dict_b_AbsEta
        # counter
        counterNrBJetsInDesiredEtaRegion=0
        for b in bs:
            if 1.4<=dict_b_AbsEta[b]<=1.6:
                counterNrBJetsInDesiredEtaRegion+=1
        #
        if debug:
            print "counterNrBJetsInDesiredEtaRegion",counterNrBJetsInDesiredEtaRegion

        for scale in scales:
            Mbb=dict_scale_obj_tlv[scale]["bb"].M()
            # inclusive
            histoName="inclusive"
            name=scale+"_"+histoName
            dict_name_hist[name].Fill(Mbb) 
            # given category
            histoName=str(counterNrBJetsInDesiredEtaRegion)
            name=scale+"_"+histoName
            dict_name_hist[name].Fill(Mbb)
        # done loop over scales


    # done loop over entries
    outputFile.Write()
    outputFile.Close()

createHistogram()
