#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
import numpy
import sys


####################################################
##### Start                                 ########
####################################################

print "Start Python"

total = len(sys.argv)
# number of arguments plus 1
if total!=4:
    print "You need two arguments, will ABORT!"
    print "python runPerJet.py PtReco over AllJets"
    print "Response, PtReco"
    print "over, minus"
    print "AllJets, WithMuon, NoMuon"
    exit()

Variable=str(sys.argv[1])
Type=str(sys.argv[2])
MuonInJet=str(sys.argv[3])

if Variable!="Response" and Variable!="PtReco":
    print "Variable",Variable,"must be Response, PtReco. Will ABORT!"
    exit()

if Type!="over" and Type!="minus":
    print "Type",Type,"must be over, minus. Will ABORT!"
    exit()

if MuonInJet!="AllJets" and MuonInJet!="NoMuon" and MuonInJet!="WithMuon":
    print "MuonInJet",MuonInJet,"must be AllJets, NoMuon, or WithMuon. Will ABORT!"
    exit()

if Type=="over":
    type_bins=(300,0,3)
elif Type=="minus":
    type_bins=(300,-150,-150)
    
if Variable=="Response":
    if Type=="over":
        current_xaxis_title="Ratio of each correction to GENWZ for jet pT"
    elif Type=="minus":
        current_xaxis_title="Difference of each correction to GENWZ jet pT [GeV/c]"
elif Variable=="PtReco":
    if Type=="over":
        current_xaxis_title="Ratio of GENWZ to each correction for jet pT"
    elif Type=="minus":
        current_xaxis_title="Difference of GENWZ to each correction for jet pT [GeV/c]" 

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

debug=False
Folder="local"
ApplyEventWeight=False

NrEvents=-1
Test=False
do=True
if do:
    CreateH1DPrimary=True
    PlotH1DPrimary=True
    OverlayH1DPrimary=True
    CreateH1DSecondary=True
    OverlayH1DSecondary=True
else:
    CreateH1DPrimary=False
    PlotH1DPrimary=False
    OverlayH1DPrimary=False
    CreateH1DSecondary=False
    OverlayH1DSecondary=False

# initial input file
pathName=os.environ['outputroot']
initialFileName="150124/readPaul_1_0_2BTag+TruthGENWZ_1_perevent+perjet/lvbb125.root"
treeName="perjet"
initialFileNameFull=pathName+"/"+Folder+"/"+initialFileName

# for bins we have a tuple, for now we can split the analysis only in bins of one variable
if MuonInJet=="AllJets" or MuonInJet=="NoMuon":
    bins=("EMJESGSCMuPt6_Pt","20,30,40,50,60,70,80,100,120,140,160,180,200,240,280",("Reco jet pT at EMJESGSCMuPt6 [GeV]",0.045,0.90),("Arbitrary units",0.035,0.95))
elif MuonInJet=="WithMuon":
    bins=("EMJESGSCMuPt6_Pt","20,40,50,60,70,80,100,120,160",("Reco jet pT at EMJESGSCMuPt6 [GeV]",0.045,0.90),("Arbitrary units",0.035,0.95))
else:
    print "MuonInJet",MuonInJet,"should be AllJets,WithMuon,NoMuon. Will ABORT!"
    exit()
if Test==True:
    bins=("EMJESGSCMuPt6_Pt","20,280",("Reco jet pT at EMJESGSCMuPt6 [GeV]",0.045,0.90),("Arbitrary units",0.035,0.95))
    NrEvents=10000
bins_name=bins[0]
bins_string=bins[1]
bins_xaxis=bins[2]
bins_yaxis=bins[3]
list_bin=get_list_intervals(bins_string,debug)
array_bin=get_array_values(bins_string,debug)
numpyarray_bin=numpy.asarray(array_bin)

# for 1D histograms we have a list of tuples
list_h1D=[]
# first is the name of the variable in the tree
# then comes a tuple describing number of bins, low bin and high bin
# then comes a tuple describing attributes for plotting (color,markerstyle,fillstyle)
# then comes a tuple describing the x axis (title,size,offset)
if True:
    #corrections="EMJESGSC,EMJESGSCMu,EMJESGSCMuPt"
    #corrections="EMJESGSCMuPtB,EMJESGSCMuPt,EMJESGSCMu,EMJESGSC,EMJES,EM"
    #corrections="EMJESGSCMuPt,EMJESGSCMu,EMJESGSC,EMJES,EM,GENWZ"
    #corrections="EMJESGSCMuPt"
    corrections="EMJESGSCMuPt6"
    #corrections="EMJESGSC,EMJESGSCMu"
    for i,correction in enumerate(corrections.split(",")):
        if Variable=="Response":
            current_variable=correction+"_"+Type+"_GENWZ_Pt"
        elif Variable=="PtReco":
            current_variable="GENWZ_"+Type+"_"+correction+"_Pt"
        list_h1D.append((current_variable,type_bins,(i+1,20,0,1),(current_xaxis_title,0.045,0.90),("Arbitrary Units",0.035,0.90),correction))
    # done for


# these will be saved in a file that remembers the bins_name and a suffix we choose
prefix=""
suffix=Variable+"_"+Type+"_"+MuonInJet
# primary
h1D_primary_fileName="./plots/histos_"+prefix+"_"+bins_name+"_"+suffix+".root"
h1D_primary_rebin=1
h1D_primary_plot_fits="Bukin" #"None,Gauss,Bukin"
h1D_primary_plot_option=""
# primary overlay
h1D_primary_overlay_plot_min=-1
h1D_primary_overlay_plot_max=-1
h1D_primary_overlay_plot_path="./plots/"
h1D_primary_overlay_plot_extensions="pdf"
h1D_primary_overlay_plot_option=""
h1D_primary_overlay_plot_legend_info=[0.45,0.70,0.90,0.90,72,0.04,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
h1D_primary_overlay_options="histo+Bukin" # "histo,Bukin,histo+Bukin,Gauss,histo+Gauss"
# secondary
h1D_secondary_fileName="./plots/allbins_"+prefix+"_"+bins_name+"_"+suffix+".root"
h1D_secondary_plot_fits="None,Bukin"
h1D_secondary_quantities="mean,rms,meanwithrms,rmsovermean"
h1D_secondary_quantity_yaxistitle={}
h1D_secondary_quantity_yaxistitle["mean"]="Response (mean)"
h1D_secondary_quantity_yaxistitle["rms"]="Resolution (rms)"
h1D_secondary_quantity_yaxistitle["meanwithrms"]="Response as marker, resolution as as bars"
h1D_secondary_quantity_yaxistitle["rmsovermean"]="Incorrect resolution (rms over mean)"
h1D_secondary_rebin=1
# secondary overlay
h1D_secondary_overlay_plot_quantity={}
h1D_secondary_overlay_plot_quantity["mean"]=(-1,1.3)
h1D_secondary_overlay_plot_quantity["rms"]=(-1,0.3)
h1D_secondary_overlay_plot_quantity["meanwithrms"]=(-1,1.35)
h1D_secondary_overlay_plot_quantity["rmsovermean"]=(-1,0.3)
h1D_secondary_overlay_quantity_legend_info={}
h1D_secondary_overlay_quantity_legend_info["mean"]=[0.65,0.12,0.89,0.32,72,0.030,0]
h1D_secondary_overlay_quantity_legend_info["rms"]=[0.65,0.68,0.89,0.88,72,0.030,0]
h1D_secondary_overlay_quantity_legend_info["meanwithrms"]=[0.65,0.12,0.89,0.32,72,0.030,0]
h1D_secondary_overlay_quantity_legend_info["rmsovermean"]=[0.65,0.68,0.89,0.88,72,0.030,0]
h1D_secondary_overlay_plot_legend_info=[0.65,0.70,0.90,0.88,72,0.035,0] # x_low,y_low,x_high,y_high,text_font,text_size,fill_color
h1D_secondary_overlay_options="histo"
h1D_secondary_overlay_plot_path="./plots/"
h1D_secondary_overlay_plot_extensions="pdf"
h1D_secondary_overlay_plot_option="E3"
h1D_secondary_overlay_plot_fits="None,Bukin" # "None,Gauss,Bukin"

# create the name of a bin, used in h1D overlay
def get_name_bins_quantity(prefix,bins_name,quantity,fit,suffix):
    return "h_"+prefix+"_allbins_"+bins_name+"_"+quantity+"_"+fit+"_"+suffix
# done function

# create the name of a bin, used in h1D overlay
def get_name_bin_h1D_quantity_fit(prefix,bins_name,name,quantity,fit,suffix):
    return "h_"+prefix+"_"+bins_name+"_"+name+"_"+quantity+"_"+fit+"_"+suffix
# done function

# create the name of a histogram for a certain bin and a variable
def get_name_h1D(prefix,bins_name,bin,h1D_name,suffix):
    return "h_"+prefix+"_"+bins_name+"_"+str(bin[0])+"_"+str(bin[-1])+"_"+h1D_name+"_"+suffix
# done function

# create the name of a bin, used in h1D overlay
def get_name_bin(prefix,bins_name,bin,suffix):
    return "h_"+prefix+"_"+bins_name+"_"+str(bin[0])+"_"+str(bin[-1])+"_"+suffix
# done function

# create the dictionary of a h1D name vs a h1D for all the bins and variables
def get_dict_name_h1D(list_bin,list_h1D,debug):
    result={}
    # loop over list_bins
    for bin in list_bin:
        # loop over list_h1D
        for h1D in list_h1D:
            name=h1D[0]
            fullname=get_name_h1D(prefix,bins_name,bin,name,suffix)
            if debug:
                print "fullname",fullname
            title=fullname
            #
            binning=h1D[1]
            result[fullname]=TH1F(fullname,title,*binning)
        # done loop over list_h1D
    # done loop over list_bin
    if debug:
        print "dict_name_h1D",result
    # ready
    return result
# done function

#     
def test_dict_name_h1D(debug):
    if debug:
        print "test"
    dict_name_h1D=get_dict_name_h1D(bins,list_h1D,debug)
# done function

# 
def get_value(entry,name,debug):
    if debug:
        print "test"
    list_name=name.split("_")
    if debug:
        print list_name
    if len(list_name)==3:
        if debug:
            print "We have only one variable, so we read it directly"
        result=getattr(entry,name)
    elif len(list_name)==4:
        if debug:
            print "We have a ratio or difference of two variables, so we compute it"
        name_value_1=list_name[0]+"_"+list_name[3]
        name_value_2=list_name[2]+"_"+list_name[3]
        value_1=getattr(entry,name_value_1)
        value_2=getattr(entry,name_value_2)
        if list_name[1]=="over":
            result=value_1/value_2
        elif list_name[1]=="minus":
            result=value_1-value_2
        else:
            print "Not known what type, choose between over or minus. Will ABORT!!!"
            exit()
    else:
        print "We don't know this case, we ABORT!!"
        exit()
    if debug:
        print "result=",result
    # read to return
    return result
# done function

#
def create_h1D_primary(fileOutputName,debug):
    if debug:
        print "initialfileNameFull",initialFileNameFull
    # open the desied file
    file=TFile(initialFileNameFull,"READ")
    # check that the file was open correctly and if not, abort
    exists(file,debug)
    # retrieve the desired tree from the file
    tree=file.Get(treeName)
    # check that the tree exists and if not, abort
    # but this does not abort even if the treeName is wrong
    exists(tree,debug)
    if debug:
        print type(tree),tree

    # create output file
    if debug:
        print "fileOutputName",fileOutputName
    fileOutput=TFile(fileOutputName,"recreate")

    # the dictionary that holds histograms
    dict_name_h1D=get_dict_name_h1D(list_bin,list_h1D,debug)

    # loop over the events in the tree
    # for each event compute the x and y variables needed
    # then fill the histograms

    # loop over all the entries in the tree
    for i,entry in enumerate(tree):
        if debug:
            if i>9:
                continue
        if debug:
            print "************* next tree entry *************"

        if NrEvents>0:
            if i>NrEvents:
                continue

        if MuonInJet=="AllJets":
            None
        elif MuonInJet=="WithMuon":
            MuEffectPt=getattr(entry,"MuEffectPt")
            if MuEffectPt==0.0:
                continue
        elif MuonInJet=="NoMuon":
            MuEffectPt=getattr(entry,"MuEffectPt")
            if MuEffectPt!=0.0:
                continue
        else:
            print "MuonInJet",MuonInJet,"should be AllJets,WithMuon,NoMuon. Will ABORT!"
            exit()
        #

        if ApplyEventWeight==True:
            eventWeight=getattr(entry,"eventWeight")
        else:
            eventWeight=1.0
        if debug:
            print "eventWeight",eventWeight
            
        # check in which bin falls the current event
        bin_value=getattr(entry,bins_name)
        if debug:
            print get_string_value("bin:",bins_name,bin_value)
        # only for the bin interval in which the current bin_value falls
        # we fill the histograms for each desired h1D variable
        for bin in list_bin:
            if debug:
                print "bin",bin
            if bin[0]<bin_value<bin[-1]:
                if debug:
                    print "The bin_value",bin_value,"is in the interval",bin
                for h1D in list_h1D:
                    name=h1D[0]
                    fullname=get_name_h1D(prefix,bins_name,bin,name,suffix)
                    if debug:
                        print "name",name, "fullname",fullname
                    value=get_value(entry,name,debug)
                    if debug:
                        print get_string_value("h1D:",name,value)
                    # fill the histograms
                    dict_name_h1D[fullname].Fill(value,eventWeight)
                # done loop over list_h1D
        # done for over list_bin
    # done loop over tree entries

    # save the file with all the histograms created
    fileOutput.Write()
    fileOutput.Close()
# done function

#
def plot_h1D_primary(fileInputName,fits,plot_option,debug):
    # open file
    fileInput=TFile(fileInputName,"read") 
    # loop over list_bin
    for bin in list_bin:
        if debug:
            print "bin",bin
        # loop over list_h1D
        for h1D in list_h1D:
            name=h1D[0]
            fullname=get_name_h1D(prefix,bins_name,bin,name,suffix)
            if debug:
                print "fullname",fullname
            # loop over fits
            for fit in fits.split(","):
                gStyle.SetOptFit()
                c=TCanvas("c","c",600,400)
                h=fileInput.Get(fullname).Clone()
                h.Rebin(1)
                update_h1D_characteristics(h,h1D_primary_rebin,h1D[2],h1D[3],h1D[4],debug)
                h.Draw()
                f,result_fit=fit_hist(h,fit,plot_option,debug)
                if debug:
                    print get_string_distribution(fit,name,result_fit[0],result_fit[1],result_fit[2])
                c.Print("./plots/"+fullname+"_"+fit+".pdf")
            # end loop over fits
        # done loop list_h1D
    # done loop list_bin
    fileInput.Close()
# done function

#
def overlay_h1D_primary(fileInputName,plot_option,debug):
    # open file
    fileInput=TFile(fileInputName,"read") 
    # loop over list_bin
    for bin in list_bin:
        if debug:
            print "bin",bin
        binname=get_name_bin(prefix,bins_name,bin,suffix)+"_overlay"
        if debug:
            print "binname",binname
        list_tuple_h1D=[]
        # loop over list_h1D
        for h1D in list_h1D:
            name=h1D[0]
            shortname=h1D[5]
            fullname=get_name_h1D(prefix,bins_name,bin,name,suffix)
            if debug:
                print "fullname",fullname
            h=fileInput.Get(fullname).Clone()
            update_h1D_characteristics(h,h1D_primary_rebin,h1D[2],h1D[3],h1D[4],debug)
            list_tuple_h1D.append([h,shortname])
        # done loop list_h1D
        # we loop over all the options for overlaying
        for h1D_primary_overlay_option in h1D_primary_overlay_options.split(","):
            overlayHistograms(h1D_primary_overlay_option,list_tuple_h1D,h1D_primary_overlay_plot_min,h1D_primary_overlay_plot_max,h1D_primary_overlay_plot_legend_info,h1D_primary_overlay_plot_option,h1D_primary_overlay_plot_path,binname,h1D_primary_overlay_plot_extensions,debug)
    # done loop list_bin
    fileInput.Close()
# done function

#
def create_h1D_secondary(fileInputName,fileOutputName,fits,quantities,debug):
    # open file
    fileInput=TFile(fileInputName,"read")
    dict_bin_h1D_fit_meanrms={}
    # loop over list_bin
    for bin in list_bin:
        if debug:
            print "bin",bin
        dict_h1D_fit_meanrms={}
        # loop over list_h1D
        for h1D in list_h1D:
            name=h1D[0]
            fullname=get_name_h1D(prefix,bins_name,bin,name,suffix)
            if debug:
                print "fullname",fullname
            dict_fit_meanrms={}
            # loop over fits
            for fit in fits.split(","):
                gStyle.SetOptFit()
                c=TCanvas("c","c",600,400)
                h=fileInput.Get(fullname).Clone()
                update_h1D_characteristics(h,h1D_primary_rebin,h1D[2],h1D[3],h1D[4],debug)
                h.Draw()
                f,result_fit=fit_hist(h,fit,"O",debug)
                dict_fit_meanrms[fit]=(result_fit[1],result_fit[2])
                if debug:
                    print get_string_distribution(fit,name,result_fit[0],result_fit[1],result_fit[2])
                #c.Print("./plots/"+fullname+"_"+fit+".pdf")
            # end loop over fits
            dict_h1D_fit_meanrms[name]=dict_fit_meanrms
        # done loop list_h1D
        dict_bin_h1D_fit_meanrms[bin]=dict_h1D_fit_meanrms
    # done loop list_bin
    if debug:
        print "dict_bin_h1D_fit_meanrms",dict_bin_h1D_fit_meanrms
    fileInput.Close()

    # now that we have the values, we can create the new histograms in a new root file
    # will loop over all things that can differ, and we will create and fill the histograms
    # in the same place
    # create histograms of rms/mean in bins of x
    fileOutput=TFile(fileOutputName,"recreate")

    dict_name_h1D={}
    # loop over list_h1D
    for h1D in list_h1D:
        name=h1D[0]
        if debug:
            print "name",name
        # loop over quantities
        for quantity in quantities.split(","):
            if debug:
                print "quantity",quantity
            # loop over fits
            for fit in fits.split(","):
                if debug:
                    print "fit",fit
                fullname=get_name_bin_h1D_quantity_fit(prefix,bins_name,name,quantity,fit,suffix)
                if debug:
                    print "fullname",fullname,len(numpyarray_bin)-1,numpyarray_bin
                dict_name_h1D[fullname]=TH1F(fullname,fullname,len(numpyarray_bin)-1,numpyarray_bin)
                #
                # loop over list_bin and for each bin set the value and the error
                for i,bin in enumerate(list_bin):
                    if debug:
                        print "bin",bin
                    mean,rms=dict_bin_h1D_fit_meanrms[bin][name][fit]
                    if quantity=="mean":
                        value=mean
                        error=0.0
                    elif quantity=="rms":
                        value=rms
                        error=0.0
                    elif quantity=="meanwithrms":
                        value=mean
                        error=rms
                    elif quantity=="rmsovermean":
                        if mean!=0:
                            value=rms/mean
                        else:
                            value=0.0
                        error=0.0
                    else:
                        print "Quantity",quantity,"not known. Choose between mean, rms, meanwithrms, rmsovermean. Will ABORT!"
                        exit()
                    # done if over quantity
                    if debug:
                        print fullname,"bin",i,"value",value,"error",error
                    dict_name_h1D[fullname].SetBinContent(i,value)
                    dict_name_h1D[fullname].SetBinError(i,error)
    # done all loops
    if debug:
        print "dict_name_h1D",dict_name_h1D

    # save the file with all the histograms created thanks to the histograms being in the dictionary
    fileOutput.Write()
    fileOutput.Close()

# done function

#
def overlay_h1D_secondary(fileInputName,quantities,fits,debug):
    # open file
    fileInput=TFile(fileInputName,"read") 
    # loop over list_bin
    for quantity in quantities.split(","):
        if debug:
            print "quantity",quantity
        h1D_secondary_overlay_plot_min=h1D_secondary_overlay_plot_quantity[quantity][0]
        h1D_secondary_overlay_plot_max=h1D_secondary_overlay_plot_quantity[quantity][1]
        for fit in fits.split(","):
            if debug:
                print "fit",fit
            plotname=get_name_bins_quantity(prefix,bins_name,quantity,fit,suffix)
            if debug:
                print "plotname",plotname
            list_tuple_h1D=[]
            # loop over list_h1D
            for h1D in list_h1D:
                name=h1D[0]
                shortname=h1D[5]
                fullname=get_name_bin_h1D_quantity_fit(prefix,bins_name,name,quantity,fit,suffix)
                if debug:
                    print "fullname",fullname
                h=fileInput.Get(fullname).Clone()
                bins_yaxis_current=(h1D_secondary_quantity_yaxistitle[quantity],bins_yaxis[1],bins_yaxis[2])
                update_h1D_characteristics(h,h1D_secondary_rebin,h1D[2],bins_xaxis,bins_yaxis_current,debug)
                list_tuple_h1D.append([h,shortname])
            # done loop list_h1D
            # we loop over all the options for overlaying
            for h1D_secondary_overlay_option in h1D_secondary_overlay_options.split(","):
                overlayHistograms(h1D_secondary_overlay_option,list_tuple_h1D,h1D_secondary_overlay_plot_min,h1D_secondary_overlay_plot_max,h1D_secondary_overlay_quantity_legend_info[quantity],h1D_secondary_overlay_plot_option,h1D_secondary_overlay_plot_path,plotname,h1D_secondary_overlay_plot_extensions,debug)
    # done loop list_bin
    fileInput.Close()
# done function

# run 
if Test:
    test_dict_name_h1D(debug)
# 
if CreateH1DPrimary:
    create_h1D_primary(h1D_primary_fileName,debug)

if PlotH1DPrimary:
    plot_h1D_primary(h1D_primary_fileName,h1D_primary_plot_fits,h1D_primary_plot_option,debug)

if OverlayH1DPrimary:
    overlay_h1D_primary(h1D_primary_fileName,h1D_primary_overlay_plot_option,debug)

if CreateH1DSecondary:
    create_h1D_secondary(h1D_primary_fileName,h1D_secondary_fileName,h1D_secondary_plot_fits,h1D_secondary_quantities,debug)

if OverlayH1DSecondary:
    overlay_h1D_secondary(h1D_secondary_fileName,h1D_secondary_quantities,h1D_secondary_overlay_plot_fits,debug)

print "End Python"

####################################################
##### End                                   ########
####################################################



