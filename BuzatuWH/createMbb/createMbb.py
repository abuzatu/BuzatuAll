#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for exah1D_name_rmple, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

print "Start Python"

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=6:
    print "You need some arguments, will ABORT!"
    print "Ex: ./createMbb.py InputFolder         Process  Options                                                    NrEvents OutputFolder"
    print "Ex: ./createMbb.py 161009_4_CxAOD_24_7 llbb     inclusive,2hadronic,1hadronic1semileptonic,2semileptonic   -1       161010_1"
    assert(False)
# done if

InputFolderName=sys.argv[1]
Process=sys.argv[2]
Options=sys.argv[3]
NrEvents=sys.argv[4]
OutputFolderName=sys.argv[5]

def do(Option):
    debug=False
    #fileName="/nfs/atlas/abuzatu01/code/BuzatuReadCxAOD/tree_llbb_100k.root"
    #fileName="~/data/Tree/160531_1/"+Process+".root"
    #fileName="~/data/Tree/160601_1/"+Process+".root"
    # fileName="~/data/Tree/161007_2_CxAOD_24_7/tree_"+Process+".root"
    fileName="~/data/Tree/"+InputFolderName+"/tree_"+Process+".root"
    treeName="perevent"
    numEvents=int(NrEvents)
    bs="b1,b2".split(",")    
    #process_string="llbb"
    #initial_string="OneMu,AllMu"
    #arget_string="Parton,TruthWZ"
    #fitname_string="None,Gauss,Bukin,Mixed"
    #style_string="New,Old"
    #process_string="llbb"
    #initial_string="OneMu"
    #target_string="Parton"
    #fitname_string="Mixed"
    #style_string="New"
    process_string="llbb"
    initial_string="OneMu"
    #target_string="Parton,TruthWZ"
    target_string="TruthWZ"
    #fitname_string="None,NoneMedian,Gauss,GaussMedian,Bukin,BukinMedian"
    fitname_string="None,NoneMedian,Bukin,BukinMedian"
    #fitname_string="None,Bukin"
    style_string="New"
    normal_string="True,False"
    #normal_string="True"
    list_process=process_string.split(",")
    list_initial=initial_string.split(",")
    list_target=target_string.split(",")
    list_fitname=fitname_string.split(",")
    list_style=style_string.split(",") 
    list_normal=normal_string.split(",") 
    #scalesstring="TruthWZ,Parton,Nominal,Regression,OneMu,OneMuNu,AllMu,AllMuNu,PtRecoGauss,PtRecoBukin"
    #scalesstring="TruthWZ,Parton,Nominal,Regression,OneMu,PtRecoBukin"
    #scalesstring="TruthWZ,Parton,Nominal,Regression,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle"
    #scalesstring="TruthWZ,Nominal,Regression,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle"
    #scalesstring="TruthWZ,Parton,Nominal"
    if False:
        for process in list_process:
            for initial in list_initial:
                for target in list_target:
                    for fitname in list_fitname:
                        for style in list_style:
                            for normal in list_normal:
                                scalesstring+=",PtReco"+process+initial+target+fitname+style+normal
        # done for
    # done if
    #scalesstring+=",PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuPartonNoneMedianNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,PtRecollbbOneMuPartonBukinMedianNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue"
    #scalesstring="TruthWZ,Parton,Nominal,OneMu,PtRecoRunIStyle,PtRecoRunIIStyle,PtRecollbbOneMuPartonNoneNewTrue,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZNoneMedianNewTrue,Regression,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoTrunkllbbOneMuPartonBukinNew,PtRecoMoriondllbbOneMuPartonBukinNew"
    #scalesstring="TruthWZ,Parton,Nominal,OneMu,Regression,PtRecoRunIStyle,PtRecoRunIIStyle,PtRecollbbOneMuPartonBukinNewTrue,PtRecollbbOneMuTruthWZNoneNewTrue,PtRecollbbOneMuTruthWZBukinMedianNewTrue,PtRecoMoriondllbbOneMuPartonBukinNew,PtRecoTrunkllbbOneMuPartonBukinNew,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"
    #scalesstring="TruthWZ,Parton,Nominal,OneMu,Regression,PtRecoPartonBukin,PtRecoTruthWZNone,PtRecoTruthWZBukinMedian,PtRecoMoriondllbbOneMuPartonBukinNew,PtRecoTrunkllbbOneMuPartonBukinNew,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"
    #scalesstring="TruthWZ,Parton,Nominal,OneMu,OneMuNuTruth,Regression,PtRecoPartonBukin,PtRecoTruthWZNone,PtRecoTruthWZBukinMedian,PtRecoNowllbbOneMuPartonBukinNewTrue,PtRecoNowllbbOneMuTruthWZNoneNewTrue,PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"
    #scalesstring="TruthWZ,Parton,Nominal,OneMu,PtRecoTruthWZNone,Regression,OneMuNuTruth"
    #scalesstring="TruthWZ,Nominal,OneMu,PtRecoTruthWZNone,Regression"
    #scalesstring="TruthWZ,Nominal,OneMu,PtRecoTruthWZNone,PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue"
    scalesstring="TruthWZ,Nominal,OneMu,PtRecoTruthWZNone"
    #scalesstring="TruthWZ,Nominal,OneMu,PtRecoTruthWZNone,PtRecoAZHggA800ToZH500OneMuTruthWZNoneNewTrue,PtRecoHccllccOneMuTruthWZNoneNewTrue"
    scales=scalesstring.split(",")
    if debug:
        print "scales",scales
    variableNames="Pt,Eta,Phi,E".split(",")
    outputfileName="~/data/histos_mbb/"+OutputFolderName+"/histos_mbb_"+Process+"_"+Option+".root"
    histos=[]
    if True:
        if "llbb" in Process or "llcc" in Process or "lvcc" in Process or "vvcc" in Process:
            histos.append(("Pt1",(100,0,500)))
            histos.append(("Pt2",(100,0,500)))
            histos.append(("mbb",(50,48.5,198.5))) # around 125 GeV
        elif "ttbar" in Process:
            histos.append(("Pt1",(100,0,500)))
            histos.append(("Pt2",(100,0,500)))
            histos.append(("mbb",(31,45,355))) # around 125 GeV 
        elif "H250" in Process:
            histos.append(("Pt1",(100,0,500)))
            histos.append(("Pt2",(100,0,500)))
            histos.append(("mbb",(31,45,355)))
        elif "H400" in Process:
            histos.append(("Pt1",(100,0,500)))
            histos.append(("Pt2",(100,0,500)))
            histos.append(("mbb",(46,45,505))) 
        elif "H500" in Process:
            histos.append(("Pt1",(100,0,500)))
            histos.append(("Pt2",(100,0,500)))
            histos.append(("mbb",(56,45,605))) 
        else:
            print "Process",Process,"not known. Choose llbb, llcc, lvcc, vvcc, H250, H400, H500. Will ABORT"
            assert(False)
        # done if
        #histos.append(("mbb",(40,18.5,258.5)))
        #histos.append(("mbb",(38,20,400)))
        histos.append(("Pt1_response_TruthWZ", (55,0.18,2.38)))
        histos.append(("Pt2_response_TruthWZ", (55,0.18,2.38)))
        histos.append(("mbb_response_TruthWZ", (55,0.18,2.38)))
        #histos.append(("Pt1_response_Parton",  (55,0.18,2.38)))
        #histos.append(("Pt2_response_Parton",  (55,0.18,2.38)))
        #histos.append(("mbb_response_Parton",  (55,0.18,2.38)))
    if False:
        #histos.append(("Pt1_response_TruthWZ", (86,0.19,1.91)))
        histos.append(("Pt1_response_TruthWZ", (106,0.19,2.31)))
        histos.append(("Pt2_response_TruthWZ", (106,0.19,2.31)))
        histos.append(("mbb_response_TruthWZ", (106,0.19,2.31)))
        #histos.append(("Pt1_response_Parton",  (106,0.19,2.31)))
        #histos.append(("Pt2_response_Parton",  (106,0.19,2.31)))
        #histos.append(("mbb_response_Parton",  (106,0.19,2.31)))
    if False:
        histos.append(("Pt1",(50,0,200)))
        histos.append(("Pt2",(50,0,200)))
        histos.append(("mbb",(50,0,200)))
        histos.append(("Pt1_response_TruthWZ", (200,0,2)))
        histos.append(("Pt2_response_TruthWZ", (200,0,2)))
        histos.append(("mbb_response_TruthWZ", (200,0,2)))
        #histos.append(("Pt1_response_Parton", (200,0,2)))
        #histos.append(("Pt2_response_Parton", (200,0,2)))
        #histos.append(("mbb_response_Parton", (200,0,2)))
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
    if numEvents<0 or numEvents>nrEntries:
        numEvents=nrEntries
    # create output file
    outputfile=TFile(outputfileName,"recreate")
    # create histograms
    dict_name_h1d={}
    for scale in scales:
        for histo in histos:
            if debug:
                print "histo",type(histo),histo
            histname=scale+"_"+histo[0]
            if debug:
                print "histname",histname
            dict_name_h1d[histname]=TH1F(histname,histname,*histo[1])
    # done loop over scales

    #exit()

    # loop over entries
    for i, event in enumerate(tree):
        if i>=numEvents:
            continue
        if i%1000==0:
            print "******* new event",i," **********"
        if debug:
            print "******* new event",i," **********"
        
        nrHadronic=0
        nrSemileptonic=0
        for b in bs:
            # get type of sld for this jet
            nrMu=getattr(event,b+"_nrMu")
            nrEl=getattr(event,b+"_nrEl")
            if nrMu==0 and nrEl==0:
                nrHadronic+=1
            else:
                nrSemileptonic+=1
         # done loop over bs
        if debug:
            print "nrHadronic",nrHadronic,"nrSemileptonic",nrSemileptonic

        goodEvent=True
        if Option=="inclusive":
            goodEvent=True
        elif Option=="2hadronic":
            # keep only events where both jets decay hadronically
            goodEvent = nrHadronic==2 and nrSemileptonic==0
        elif Option=="1hadronic1semileptonic":
            goodEvent = nrHadronic==1 and nrSemileptonic==1
        elif Option=="2semileptonic":
            goodEvent = nrHadronic==0 and nrSemileptonic==2
        else:
            print "Option",option,"not known. Choose inclusive, 2hadronic, 1hadronic1semileptonic, 2semileptonic. Will ABORT!!!"
            assert(False)
        # apply event selection based on goodEvent
        if not goodEvent:
            continue
        
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
                assert(dict_obj_tlv[b].Pt()>0.1)
                assert(dict_obj_tlv[b].E()>0.1)
                #dict_obj_tlv[b]*=0.001 # not needed now MeV -> GeV
                if debug:
                    dict_obj_tlv[b].Print()
                dict_obj_tlv["bb"]+=dict_obj_tlv[b]
            # done loop over the two b jets
            dict_scale_obj_tlv[scale]=dict_obj_tlv
            # bb defined as b1+b2
        # done loop over all scales

        if False:
            A=dict_scale_obj_tlv["PtRecoPartonBukin"]
            B=dict_scale_obj_tlv["PtRecoNowllbbOneMuPartonBukinNewTrue"]
        #A=dict_scale_obj_tlv["PtRecoTruthWZBukinMedian"]
        #B=dict_scale_obj_tlv["PtRecoNowllbbOneMuTruthWZBukinMedianNewTrue"]
            wrong=abs(A["bb"].M()-B["bb"].M())>0.1
            if wrong==True:
                A1=A["b1"]
                A2=A["b2"]
                B1=B["b1"]
                B2=B["b2"]
                print "A1,B1"
                A1.Print()
                B1.Print()
                print "A2,B2"
                A2.Print()
                B2.Print()
            # done if


        TruthWZ_Pt1=dict_scale_obj_tlv["TruthWZ"]["b1"].Pt()
        TruthWZ_Pt2=dict_scale_obj_tlv["TruthWZ"]["b2"].Pt()
        TruthWZ_mbb=dict_scale_obj_tlv["TruthWZ"]["bb"].M()

        if debug:
            print "TruthWZ_Pt1",TruthWZ_Pt1,"TruthWZ_Pt2",TruthWZ_Pt2,"TruthWZ_mbb",TruthWZ_mbb


        if False:
            Parton_Pt1=dict_scale_obj_tlv["Parton"]["b1"].Pt()
            Parton_Pt2=dict_scale_obj_tlv["Parton"]["b2"].Pt()
            Parton_mbb=dict_scale_obj_tlv["Parton"]["bb"].M()

            if debug:
                print "Parton_Pt1",Parton_Pt1,"Parton_Pt2",Parton_Pt2,"Parton_mbb",Parton_mbb

            goodParton_b1=Parton_Pt1>4 and dict_scale_obj_tlv["Nominal"]["b1"].DeltaR(dict_scale_obj_tlv["Parton"]["b1"])<0.4
            goodParton_b2=Parton_Pt2>4 and dict_scale_obj_tlv["Nominal"]["b2"].DeltaR(dict_scale_obj_tlv["Parton"]["b2"])<0.4
            goodParton=goodParton_b1 and goodParton_b2
            

            assert(goodParton==True)
        # end check if good parton, as we now look only on TruthWZ


        #if not goodParton:
        #    continue
        
        for scale in scales:
            #if scale=="Parton" and not goodParton:
            #    continue
            # Pt1
            Reco_Pt1=dict_scale_obj_tlv[scale]["b1"].Pt()
            if debug:
                print "scale",scale,"Reco_Pt1",Reco_Pt1
            dict_name_h1d[scale+"_Pt1"].Fill(Reco_Pt1)
            dict_name_h1d[scale+"_Pt1_response_TruthWZ"].Fill(ratio(Reco_Pt1,TruthWZ_Pt1))
            #if goodParton:
            #    dict_name_h1d[scale+"_Pt1_response_Parton"].Fill(ratio(Reco_Pt1,Parton_Pt1))
            # Pt2
            Reco_Pt2=dict_scale_obj_tlv[scale]["b2"].Pt()
            dict_name_h1d[scale+"_Pt2"].Fill(Reco_Pt2)
            dict_name_h1d[scale+"_Pt2_response_TruthWZ"].Fill(ratio(Reco_Pt2,TruthWZ_Pt2))
            #if goodParton:
            #    dict_name_h1d[scale+"_Pt2_response_Parton"].Fill(ratio(Reco_Pt1,Parton_Pt1))
            # mbb
            Reco_mbb=dict_scale_obj_tlv[scale]["bb"].M()
            dict_name_h1d[scale+"_mbb"].Fill(Reco_mbb)
            dict_name_h1d[scale+"_mbb_response_TruthWZ"].Fill(ratio(Reco_mbb,TruthWZ_mbb))
            #if goodParton:
            #    dict_name_h1d[scale+"_mbb_response_Parton"].Fill(ratio(Reco_mbb,Parton_mbb))
        # done loop over all scales
            
    # done loop over the entries in the tree (events in this case)
    outputfile.Write()
    outputfile.Close()
# done function

####################################################
##### Run                                   ########
####################################################

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

# run function
for Option in Options.split(","):
    do(Option)

####################################################
##### End                                   ########
####################################################

print "End Python"
