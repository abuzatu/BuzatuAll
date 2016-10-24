#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=5:
    print "You need some arguments, will ABORT!"
    print "Ex: ./interpolatePtReco.py Process Initial Target Normal"
    print "Ex: ./interpolatePtReco.py llbb    OneMu   Parton True"
    assert(False)
# done if

string_Process=sys.argv[1]
string_Initial=sys.argv[2]
string_Target=sys.argv[3]
string_Normal=sys.argv[4]

list_Process=string_Process.split(",")
list_Initial=string_Initial.split(",")
list_Target=string_Target.split(",")
list_Normal=string_Normal.split(",")


# Batch mode quietens histogram output
ROOT.gROOT.SetBatch(True)

#list_valuetype="None,NoneMedian,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
#list_valuetype="Bukin".split(",")
list_valuetype="None".split(",")

path="/Users/abuzatu/data/histos_PtReco/161007_2/"
path="/Users/abuzatu/data/histos_PtReco/"
#Normal="True"

debug=False
list_jettype="hadronic,semileptonic".split(",")
#list_jettype="inclusive,hadronic,muon,electron".split(",")
#list_jettype="inclusive".split(",")

dict_jettype_color={
    "inclusive":1,
    "hadronic":2,
    "muon":8,
    "electron":4,
    "semileptonic":8
    
}



#def get_interpolated_graph_for_histo(h,debug):
#    xMin=20.0
#    stepWidth=1.0
#    nrSteps=350
#    xList=[]
#    yList=[]
#    for i in xrange(nrSteps+1):
#        #print i
#        x=xMin+i*stepWidth
#        y=h.Interpolate(x)
#        if debug:
#            print i, x, y
#        xList.append(x)
#        yList.append(y)
#    # done loop over steps
#    if False:
#        print "xList",xList
#        print "yList",yList
#    xNumpyArray=numpy.array(xList)
#    yNumpyArray=numpy.array(yList)
#    result=TGraph(nrSteps,xNumpyArray,yNumpyArray)
#    return result
# done function

def get_dict_jettype_hg(inputFileName,list_jettype,valuetype,debug):
    result={}
    for jettype in list_jettype:
        histoName="PtReco_"+jettype+"_"+valuetype
        color=dict_jettype_color[jettype]
        h=retrieveHistogram(inputFileName,"",histoName,"",debug)
        h.SetLineColor(color)
        h.SetLineStyle(2)
        g=get_interpolated_graph_for_histo(h,debug)
        g.SetLineColor(color)
        result[jettype]=[h,g]
    # done for loop
    return result
# done function

def do_plot(Process,Initial,Target,Normal,list_jettype,valuetype,debug):

    inputFileName=path+"PtReco_histos_"+Process+"_"+Initial+"_"+Target+"_"+Normal+".root"

    gROOT.ForceStyle()
    canvas=TCanvas()

    frame=canvas.DrawFrame(0,0.97,650,1.56)
    frame.SetXTitle("Jet transverse momentum (pT) after muon-in-jet correction [GeV]")
    frame.SetYTitle("PtReco correction factors")
    frame.GetXaxis().SetTitleSize(0.045)
    frame.GetXaxis().SetTitleOffset(0.90)
    frame.GetYaxis().SetTitleSize(0.050)
    frame.GetYaxis().SetTitleOffset(0.90)
    
    canvas.Modified()
    
    gStyle.SetFillStyle(4000)
    gStyle.SetStatStyle(0)
    gStyle.SetTitleStyle(0)
    gStyle.SetCanvasBorderSize(0)
    gStyle.SetFrameBorderSize(0)
    gStyle.SetLegendBorderSize(0)
    gStyle.SetStatBorderSize(0)
    gStyle.SetTitleBorderSize(0)
    gStyle.SetLabelSize(1.0) 
    gROOT.ForceStyle()

    legend=TLegend(0.42,0.45,0.9,0.65)
    legend.SetTextSize(0.045)

    dict_jettype_hg=get_dict_jettype_hg(inputFileName,list_jettype,valuetype,debug)
    for jettype in list_jettype:
        if debug:
            print "jettype",jettype
        h=dict_jettype_hg[jettype][0]
        g=dict_jettype_hg[jettype][1]
        h.SetLineWidth(2)
        g.SetLineWidth(2)
        h.Draw("same")
        g.Draw("same")
        #legend.AddEntry(g,jettype,"l")
        legend.AddEntry(h,"PtReco ("+jettype+")","l")
        legend.AddEntry(g,"Interpolation ("+jettype+")","l")
    # done loop over name
    legend.Draw("same")

    if valuetype=="None":
        textValueType="means of histogram"
    elif valuetype=="NoneMedian":
        textValueType="medians of histogram"
    elif valuetype=="Gauss":
        textValueType="means of Gauss fit"
    elif valuetype=="GaussMedian":
        textValueType="medians of Gauss fit"    
    elif valuetype=="Bukin":
        textValueType="peaks of Bukin fit"
    elif valuetype=="BukinMedian":
        textValueType="medians of Bukin fit"
    else:
        print "valuetype",valuetype,"not known for textValueType. Will ABORT!!!"
        assert(false)
    # done if

    if Target=="Parton":
        textTarget="b Parton"
    elif Target=="TruthWZ":
        textTarget="jet TruthWZ"
    else:
        print "Target",Target,"for textTarget not known. Will ABORT!!!"
        assert(false)
    # done if

    print "Normal",Normal
    if Normal=="True":
        #text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets 20 GeV or more from ZH to llbb}?#bf{Correction factors from "+textValueType+" of}?#bf{Ratio of pT of "+textTarget+" to jet after muon-in-jet corr.}",0.04,13,0.25,0.88,0.05)
        text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets from SM VH125}?#bf{Ratio of truth jet to corrected jet pT (correction factors)}",0.04,13,0.25,0.88,0.05)
    else:
        text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets 20 GeV or more from ZH to llbb}?#bf{Correction factors from inverse of "+textValueType+" of}?#bf{Ratio of jet after muon-in-jet corr to pT of "+textTarget+".}",0.04,13,0.25,0.88,0.05)

    #text2=("#bf{Dotted line: PtReco histogram.}?#bf{Solid line: histogram interpolation.}",0.04,13,0.25,0.63,0.05)

    setupTextOnPlot(*text)
    #setupTextOnPlot(*text2)

    outputFileName=path+"PtReco_interpolate_"+Process+"_"+Initial+"_"+Target+"_"+Normal+"_"+valuetype

    canvas.SaveAs(outputFileName+".pdf")
    canvas.SaveAs(outputFileName+".eps")
    canvas.SaveAs(outputFileName+".png")
    
# done function

# run
for Process in list_Process:
    for Initial in list_Initial:
        for Target in list_Target:
            for Normal in list_Normal:
                for valuetype in list_valuetype:
                    do_plot(Process,Initial,Target,Normal,list_jettype,valuetype,debug)
