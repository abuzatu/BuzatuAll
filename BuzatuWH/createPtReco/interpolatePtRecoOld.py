#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

total = len(sys.argv)
# number of arguments plus 1
if total!=4:
    print "You need some arguments, will ABORT!"
    print "Ex: ./interpolatePtReco.py Process Initial Target"
    print "Ex: ./interpolatePtReco.py llbb    OneMu Parton"
    assert(False)
# done if

Process=sys.argv[1]
Initial=sys.argv[2]
Target=sys.argv[3]

# Batch mode quietens histogram output
ROOT.gROOT.SetBatch(True)

#list_valuetype="None,Gauss,GaussMedian,Bukin,BukinMedian".split(",")
list_valuetype="Bukin".split(",")
#list_valuetype="BukinMedian".split(",")

path="/Users/abuzatu/data/histos_PtReco/"

#inputFileName=path+"PtReco_histos_"+Process+"_"+Initial+"_"+Target+".root"
inputFileName=path+"histos_"+Process+"_"+Initial+"_"+Target+".root"

debug=True
list_jettype="inclusive,hadronic,muon,electron".split(",")
#list_jettype="inclusive".split(",")

dict_jettype_color={
    "inclusive":1,
    "hadronic":2,
    "muon":8,
    "electron":4
}

dict_jettype_name={
    "inclusive":"all",
    "hadronic":"nosld",
    "muon":"mu",
    "electron":"el"
}



def get_interpolated_graph_for_histo(h,debug):
    xMin=20.0
    stepWidth=1.0
    nrSteps=350
    xList=[]
    yList=[]
    for i in xrange(nrSteps+1):
        #print i
        x=xMin+i*stepWidth
        y=h.Interpolate(x)
        if debug:
            print i, x, y
        xList.append(x)
        yList.append(y)
    # done loop over steps
    if False:
        print "xList",xList
        print "yList",yList
    xNumpyArray=numpy.array(xList)
    yNumpyArray=numpy.array(yList)
    result=TGraph(nrSteps,xNumpyArray,yNumpyArray)
    return result
# done function

def get_dict_jettype_hg(list_jettype,valuetype,debug):
    result={}
    for jettype in list_jettype:
        histoName="PtReco_"+dict_jettype_name[jettype]+"_"+valuetype
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

def do_plot(list_jettype,valuetype,debug):
    gROOT.ForceStyle()
    canvas=TCanvas()

    frame=canvas.DrawFrame(0,0.90,350,1.55)
    frame.SetXTitle("Jet transverse momentum (pT) after muon-in-jet correction [GeV]")
    frame.SetYTitle("PtReco correction factors")
    frame.GetXaxis().SetTitleSize(0.045)
    frame.GetXaxis().SetTitleOffset(0.90)
    frame.GetYaxis().SetTitleSize(0.045)
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

    legend=TLegend(0.7,0.34,0.9,0.64)
    legend.SetTextSize(0.055)

    dict_jettype_hg=get_dict_jettype_hg(list_jettype,valuetype,debug)
    for jettype in list_jettype:
        if debug:
            print "jettype",jettype
        h=dict_jettype_hg[jettype][0]
        g=dict_jettype_hg[jettype][1]
        g.Draw("same")
        h.Draw("same")
        legend.AddEntry(g,jettype,"l")
    # done loop over name
    legend.Draw("same")

    if valuetype=="None":
        textValueType="means of histogram"
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

    text=("#bf{#it{#bf{ATLAS} Simulation Internal}}?#bf{#sqrt{s}=13 TeV}?#bf{b-tagged jets 20 GeV or more from ZH to llbb}?#bf{Correction factors extracted as "+textValueType+" of}?#bf{Ratio of pT of "+textTarget+" to jet after muon-in-jet corr.}",0.04,13,0.25,0.88,0.05)

    text2=("#bf{Dotted line: PtReco histogram}?#bf{Solid line: histogram interpolation}",0.04,13,0.25,0.63,0.05)

    setupTextOnPlot(*text)
    setupTextOnPlot(*text2)

    outputFileName=path+"PtReco_interpolate_"+Process+"_"+Initial+"_"+Target+"_"+valuetype

    canvas.SaveAs(outputFileName+".pdf")
    canvas.SaveAs(outputFileName+".eps")
    canvas.SaveAs(outputFileName+".png")
    
# done function

# run
for valuetype in list_valuetype:
    do_plot(list_jettype,valuetype,debug)
