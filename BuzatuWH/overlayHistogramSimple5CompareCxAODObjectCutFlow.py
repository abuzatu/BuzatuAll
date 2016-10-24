#!/usr/bin/python
from HelperPyRoot import *
ROOT.gROOT.SetBatch(True)

total = len(sys.argv)
# number of arguments plus 1
if total!=1:
    print "You need some arguments, will ABORT!"
    print "Ex: ",sys.argv[0]," "
    assert(False)
# done if

#################################################################
################### Configurations ##############################
#################################################################

debug=True

"CutFlow/PreselectionCutFlow"
"CutFlow_Nominal/muon_Nominal"

#list_histogram=[
# [legend,inputFile,histogramPath,histogramName,histogramRename,color]
#["20.1 hadronic","/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_hadronic_Bukin","",1],
#["20.7 hadronic","/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_hadronic_Bukin","",2],
#["20.1 muon","/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_muon_Bukin","",2],
#["20.1 electron","/Users/abuzatu/Downloads/PtRecoTrunk/PtReco_histos_llbb_OneMu_Parton.root","","PtReco_electron_Bukin","",4],
#["20.7 semileptonic","/Users/abuzatu/data/histos_PtReco/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_semileptonic_Bukin","",3],
#]

#################################################################
################### Functions##### ##############################
#################################################################

def get_list_tuple_h1D():
    list_tuple_h1D=[]
    for i,histo in enumerate(list_histogram):
        legendName=histo[0]
        inputFile=histo[1]
        histogramPath=histo[2]
        histogramName=histo[3]
        histogramRename=histo[4]
        histogramColor=histo[5]
        h=retrieveHistogram(inputFile,histogramPath,histogramName,histogramRename,debug)
        h.SetLineColor(histogramColor)
        #h.GetXaxis().SetTitle("CxAOD object cut flow")
        h.GetYaxis().SetTitle("Arbitrary units")
        list_tuple_h1D.append([h,legendName])
        #subRange=[40,200]
        #list_tuple_h1D[i][0]=get_histo_subRange(list_tuple_h1D[i][0],subRange,debug)
        #list_tuple_h1D[i][0].GetXaxis().SetTitle("Di-b-jet invariant mass [GeV]")
        #list_tuple_h1D[i][0].GetYaxis().SetTitle("Arbitrary units")
        #list_tuple_h1D[i][0].SetLineColor(list_color[i])
  
    # done for
    if debug:
        print "list_tuple_h1D"
        for mytuple in list_tuple_h1D:
            print mytuple
    # done all
    return list_tuple_h1D
# done function



#################################################################
################### Run #########################################
#################################################################

#list_object="muon,tau,electron,jet,fatJet,trackJet".split(",")
#list_derivation="HIGG5D1,HIGG5D2,HIGG2D4".split(",")
list_physicsobject="electron,muon,jet,fatJet".split(",")
list_derivation="HIGG5D2".split(",")
list_change="Athena,AthenaMP".split(",")
list_color=[2,4,1,3]


for derivation in list_derivation:
    for physicsobject in list_physicsobject:
        list_histogram=[]
        name=""
        for i,change in enumerate(list_change):
            legendName=change
            fileFolderName="/Users/abuzatu/data/CxAOD/160906/group.phys-higgs.data16_13TeV.00305291.physics_Main."+derivation+".24-11-AB2"+change+"_hist"
            folderName="CutFlow_Nominal"
            fileName=""
            if derivation=="HIGG5D1":
                if change=="Athena":
                    fileName="group.phys-higgs.9360169._000001.hist-output.root"
                elif change=="AthenaMP":
                    fileName="group.phys-higgs.9360474._000001.hist-output.root"
                else:
                    print "change",change,"not known. Choose Athena or AthenaMP. Will ABORT!!"
                    assert(False)
            elif derivation=="HIGG5D2":
                if change=="Athena":
                    fileName="group.phys-higgs.9360292._000001.hist-output.root"
                elif change=="AthenaMP":
                    fileName="group.phys-higgs.9360497._000001.hist-output.root"
                else:
                    print "change",change,"not known. Choose Athena or AthenaMP. Will ABORT!!"
                    assert(False)
            elif derivation=="HIGG2D4":
                if change=="Athena":
                    fileName="group.phys-higgs.9360335._000001.hist-output.root"
                elif change=="AthenaMP":
                    fileName="group.phys-higgs.9360516._000001.hist-output.root"
                else:
                    print "change",change,"not known. Choose Athena or AthenaMP. Will ABORT!!"
                    assert(False)
            else:
                print "Derivation",derivation,"not known. Choose HIGG5D1,HIGG5D2,HIGG2D4. Will ABORT!"
                assert(False)
            # end done if
            histoName=physicsobject+"_Nominal"
            list_histogram.append([legendName,fileFolderName+"/"+fileName,folderName,histoName,"",list_color[i]])
        # done for over change
        list_tuple_h1D=get_list_tuple_h1D()
        print type(list_histogram[0][0])
        name+="_"+derivation+"_"+physicsobject
        list_option="histo".split(",")
        for option in list_option:
            overlayHistograms(list_tuple_h1D,fileName="overlay_"+name,extensions="pdf,png",option="histo",doValidationPlot=False,canvasname="canvasname",addHistogramInterpolate=False,addfitinfo=False,addMedianInFitInfo=False,significantDigits=("3","3","3","3"),min_value=-1,max_value=-1,doRatioPad=True,min_value_ratio=0.0,max_value_ratio=2.00,statTitle="MC. stat uncertainty",statColor=6,ratioTitle="Ratio to first",legend_info=[0.60,0.50,0.78,0.62,72,0.037,0],plot_option="HIST E",plot_option_ratio="HIST",text_option=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{"+derivation+"}?#bf{"+physicsobject+"}",0.04,13,0.60,0.88,0.05),line_option=([0,0.5,1,0.5],2),debug=False)
        # done loop over list_option
    # done loop over list_option
# done loop over list_derivation

#################################################################
################### Finished ####################################
#################################################################
