#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
#from ConfigWH import *
#from HelperWH import *

import copy

print "Start Python"
time_start=time()

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=1:
    print "You need some arguments, will ABORT!"
    print "Ex: ./findWindow.py %"
    print "Ex: ./findWindow.py 90"
    assert(False)
# done if

debug=False
dict_corr_window={}
dict_corr_window["Nominal"]=[115.6,17.75]
dict_corr_window["OneMu"]=[116.4,15.86]
dict_corr_window["PtRecollbbOneMuPartonBukinNew"]=[122.3,14.65]
dict_corr_window["Regression"]=[129.26,14.84]

list_corr="Nominal,OneMu,PtRecollbbOneMuPartonBukinNew,Regression".split(",")
#list_corr="Nominal".split(",")


histoPath=""
histoName="qqZllH125_2tag2jet_0_150ptv_SR_mBB"
name=""

def integral(h,xmin,xmax,debug):
    result=0.0
    NBins=h.GetNbinsX()
    for i in xrange(NBins+1):
        value=h.GetBinContent(i)
        low=h.GetBinLowEdge(i)
        high=h.GetBinLowEdge(i)+h.GetBinWidth(i)
        if not (low >= xmin and high <= xmax):
            continue
        if debug:
            print i,low,high,value
        result+=value
    return result
# done

def print_corr_integral(corr,h,low,high,debug):
    integralAll=h.Integral()
    integralCurrent=integral(h,low,high,debug)
    ratio=integralCurrent/integralAll
    print "mBB_dict_correction_subRange[\""+corr+"\"]=["+str(low)+","+str(high)+"] # signal efficiency "+str(ratio)
# done

def range_integral(h,Nr,debug):
    for i in xrange(Nr):
        low=125.0-i
        high=125.0+i
        print_integral(h,low,high,debug)

# done

def find_bin_edge(central=125.0,binwidth=5.0,option="low",target=80.1,nrBins=20,debug=False):
    if debug:
        print "central",central,"binwidth",binwidth,"option",option,"target",target,"nrBins",nrBins
    for i in xrange (nrBins):
        if option=="low":
            current=central-binwidth*(0.5+i)
            if debug:
                print "i",i,"current",current
            if current<target:
                return current
        elif option=="high":
            current=central+binwidth*(0.5+i)
            if debug:
                print "i",i,"current",current
            if current>target:
                return current
        else:
            print "option",option,"not known. Choose low or high. Will ABORT!"
            assert(false)
    # done for
# done function
        

def print_integral_peak_width(h,peak,width,debug):
    low=peak-width
    high=peak+width
    if debug:
        print "peak,width",peak,width
    newlow=find_bin_edge(125.0,5.0,"low",low,20,debug)
    newhigh=find_bin_edge(125.0,5.0,"high",high,20,debug)
    print "peak,width",peak,width,"low,high",low,high,"newlow,newhigh",newlow,newhigh
    #print_corr_integral(h,low,high,debug)
    print_corr_integral(corr,h,newlow,newhigh,debug)



for corr in list_corr:
    print "corr",corr
    fileName="~/data/Reader/151212/submitDir_"+corr+"/hist-ZHll125.root"
    h=retrieveHistogram(fileName,histoPath,histoName,name,debug)
    window=dict_corr_window[corr]
    peak=window[0]
    width=window[1]
    #print_integral_peak_width(h,peak,width,debug) # close to 68%
    print_integral_peak_width(h,peak,2*width,debug) # close to 95%
    print_corr_integral(corr,h,95.0,140.0,debug)
    print_corr_integral(corr,h,105.0,145.0,debug)

if False:
    range_integral(h,40,debug)
    print_integral(h,95,140,debug)
    print_integral(h,93,134,debug) #68%
    print_integral(h,74,146,debug) #90%
    print_integral(h,104,146,debug) #90%
    
    
    c=TCanvas("c","c",600,300)
    h.Draw()
    c.Print("mBB_"+corr+".pdf")
    
