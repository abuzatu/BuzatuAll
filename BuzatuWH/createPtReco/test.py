#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

debug=True
nrEntries=111111
file=TFile("/Users/abuzatu/data/Tree/160611_1/tree_ttbar.root","read")
tree=file.Get("perjet")

if nrEntries<0:
    nrEntries=tree.GetEntries()

dict_sldOld_h={
    "hadronic":retrieveHistogram(fileName="/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root",histoPath="",histoName="PtReco_hadronic_Bukin",name="",debug=debug).Clone(),
    "muon":retrieveHistogram(fileName="/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root",histoPath="",histoName="PtReco_muon_Bukin",name="",debug=debug).Clone(),
    "electron":retrieveHistogram(fileName="/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root",histoPath="",histoName="PtReco_electron_Bukin",name="",debug=debug).Clone()
}

dict_sldNew_h={
    "hadronic":retrieveHistogram(fileName="/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_Parton_True.root",histoPath="",histoName="PtReco_hadronic_Bukin",name="",debug=debug).Clone(),
    "semileptonic":retrieveHistogram(fileName="/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_Parton_True.root",histoPath="",histoName="PtReco_semileptonic_Bukin",name="",debug=debug).Clone()
}

dict_sldOld_ratio={}
for sldOld in dict_sldOld_h:
    dict_sldOld_ratio[sldOld]=TH1F("ratio_"+sldOld,"ratio_"+sldOld,50,0.90,1.1)


for i,entry in enumerate(tree):
    if i>=nrEntries:
        continue
    if debug:
        print "**** new jet",i," *****"
    OneMuPt=getattr(entry,"OneMu_Pt")
    assert(OneMuPt>20)
    PtRecoRunIIStylePt=getattr(entry,"PtRecoRunIIStyle_Pt")
    assert(OneMuPt>20)
    factorOldFile=ratio(PtRecoRunIIStylePt,OneMuPt)
    if debug:
        print "factorOldFile",factorOldFile
    nrMu=getattr(entry,"nrMu")
    nrEl=getattr(entry,"nrEl")
    if debug:
        print "nrMu",nrMu,"nrEl",nrEl
    # sldNew and factor new
    if nrMu==0 and nrEl==0:
        sldNew="hadronic"
    else:
        sldNew="semileptonic"
    if debug:
        print "sldNew",sldNew
    factorNew=dict_sldNew_h[sldNew].Interpolate(OneMuPt)
    if debug:
        print "factorNew",factorNew
    # sldOld and factor old
    if nrMu==0 and nrEl==0:
        sldOldValue="hadronic"
    elif nrMu>=1 and nrEl==0:
        sldOldValue="muon"
    elif nrEl>=1:
        sldOldValue="electron"
    else:
        sldOldValue="other"
    if debug:
        print "sldOldValue",sldOldValue
        if sldOldValue=="other":
            print "WARNING, sldOldValue=other"
        print "factor hadronic",dict_sldOld_h["hadronic"].Interpolate(OneMuPt),"muon",dict_sldOld_h["muon"].Interpolate(OneMuPt),"electron",dict_sldOld_h["electron"].Interpolate(OneMuPt)
    factorOld=dict_sldOld_h[sldOldValue].Interpolate(OneMuPt)
    if debug:
        print "factors Old sldOld"+sldOld,factorOld,"hadronic",dict_sldOld_h["hadronic"].Interpolate(OneMuPt),"muon",dict_sldOld_h["muon"].Interpolate(OneMuPt),"electron",dict_sldOld_h["electron"].Interpolate(OneMuPt)
    #
    ratioNewToOldFile=ratio(factorNew,factorOldFile)
    if debug:
        if abs(ratioNewToOldFile-1)>0.001:
           print "ratioNewToOldFile",ratioNewToOldFile,"OneMuPt",OneMuPt,"sldNew",sldNew,"largeNew" 
        else:
            print "ratioNewToOldFile",ratioNewToOldFile,"OneMuPt",OneMuPt,"sldNew",sldNew
    # 

    ratioOldToOldFile=ratio(factorOld,factorOldFile)
    if debug:
        if abs(ratioOldToOldFile-1)>0.001:
           print "ratioOldToOldFile",ratioOldToOldFile,"OneMuPt",OneMuPt,"sldOldValue",sldOldValue,"largeOld",factorOld/factorOldFile
        else:
            print "ratioOldToOldFile",ratioOldToOldFile,"OneMuPt",OneMuPt,"sldOldValue",sldOldValue

    # fill the histogram of the current sldOldValue
    dict_sldOld_ratio[sldOldValue].Fill(ratioNewToOldFile)
# done loop over entries
for sldOld in dict_sldOld_h:
    c=TCanvas("c","c",600,400)
    dict_sldOld_ratio[sldOld].Draw()
    c.Print("ratio_"+sldOld+".pdf")

exit()
