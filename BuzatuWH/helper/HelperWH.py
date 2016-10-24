#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *

# (0.0,90,0) -> "0_90"
# (-inf, 90) -> "inf_90"
# we want to not have dots and - in the name of a histogram
# so that we can do in TBrowswer histo_name->Draw(), etc
def get_bin_string(bin,debug):
    if debug:
        print "bin",bin
    result=""
    for i,value in enumerate(bin):
        if value==float("-inf") or value==float("inf"):
            value_string="inf"
        else:
            value_string="%-.0f" % value
        if debug:
            print "i",i,"value_string",value_string
        if i!=0:
            result+="_"
        result+=value_string
    # done for loop over the two elements in the bin
    if debug:
        print "bin_string",result
    return result
# done function

# ex: list=["a","b"]
# ex: collection=["PtV",[(90.0,120.0),(120.0,160.0)]]
# ex: result=["a_PtV_90_120","a_PtV_120_160","b_PtV_90_120","b_PtV_120_160"]
def concatenate_two_collections(list,collection,debug):
    if debug:
        print "list",list
        print "collection",collection
    name=collection[0]
    bins=collection[1]
    if debug:
        print "name",name
        print "bins",bins
    result=[]
    if len(list)==0:
        for j in bins:
            result.append(name+"_"+get_bin_string(j,debug))
    # if here, it means the list is not empty
    for i in list:
        for j in bins:
            result.append(i+"_"+name+"_"+get_bin_string(j,debug))
    return result
# done function

# ex: list_criteria=[]
# ex: string_PtVBins="90,120,160,200"
# ex: list_PtVBins=get_list_intervals(string_PtVBins,debug)
# ex: inclusive_bin=(float("-inf"),float("inf"))
# ex: list_PtVBins.insert(0,inclusive_bin)
# ex: list_criteria=[]
# ex: list_criteria.append(("PtV",list_PtVBins))
def concatenate_all_collections(list_criteria,debug):
    result=[]
    for list in list_criteria:
        result=concatenate_two_collections(result,list,debug)
    return result
# done function

# ex: get_list_h1D("v","None","M","j1j2",(500,0,500),(1,0,0,1),("Dijet invariant mass [GeV]",0.045,0.90),("Entries",0.045,0.95),list_corrections,debug)
# ex: get_list_h1D("r","GENWZ","M","j1j2",(300,0,3),(1,0,0,1),("Dijet invariant mass response [GeV]",0.045,0.90),("Entries",0.045,0.95),list_corrections,debug)
# ex: get_list_h1D("f","GENWZ","M","j1j2",(300,0,3),(1,0,0,1),("Dijet invariant mass correction factor [GeV]",0.045,0.90),("Entries",0.045,0.95),list_corrections,debug)
def get_list_h1D(type_style,type_name,quantity,obj,binning,plotting,xaxis,yaxis,list_corrections,debug):
    if obj=="":
        obj_suffix=""
    else:
        obj_suffix="_"+obj
    list_h1D=[]
    for i,correction in enumerate(list_corrections):
        h1D_name=quantity+"_"+correction+obj_suffix
        if type_style=="v":
            h1D_name_r=type_name
        elif type_style=="r" or type_style=="f":
            h1D_name_r=quantity+"_"+type_name+obj_suffix
        else:
            print "Type_Style",type_style,"not known. Choose v for value, or r for response, or f for correction factor. Will ABORT!!!"
            assert(False)
        # end if for the type_style
        list_h1D.append((type_style,h1D_name,h1D_name_r,binning,plotting,xaxis,yaxis,correction))
    # done for loop
    if debug:
        print "list_h1D",list_h1D
    return list_h1D
# done function

# create the name of a histogram for a certain bin and a variable and event selection and apply event weight
# ex get_name_h1D("All","1","El",(-inf,90,0),"M_EMJESGSMuPt_j1j2","v",debug)
# ex get_name_h1D("All","1","El",(-inf,90,0),"M_EMJESGSMuPt_j1j2","r",debug)
# ex get_name_h1D("All","1","El",(-inf,90,0),"M_EMJESGSMuPt_j1j2","f",debug)
def get_name_h1D(EventSelection,ApplyEventWeight,bin_name,h1D_name,type_style,debug):
    if debug:
        print "EventSelection",EventSelection,"ApplyEventWeight",ApplyEventWeight,"bin_name",bin_name,"h1D_name",h1D_name,"type_style",type_style
    # end loop over the values
    fullname="h_"+EventSelection+"_"+ApplyEventWeight+"_"+bin_name+"_"+h1D_name+"_"+type_style
    if debug:
        print "fullname",fullname
    return fullname
# done function

# create the dictionary of a h1D name vs a h1D for all the bins and variables
def get_dict_name_h1D(list_EventSelection,list_ApplyEventWeight,list_bin_name,list_h1D,debug):
    result={}
    # loop over event selections
    for EventSelection in list_EventSelection:
        # loop over if to apply event weights
        for ApplyEventWeight in list_ApplyEventWeight:
            # loop over all the bins
            for bin_name in list_bin_name:
                if debug:
                    print "bin_name",bin_name
                # loop over list_h1D
                for h1D in list_h1D:
                    type_style=h1D[0]
                    h1D_name=h1D[1]
                    h1D_name_r=h1D[2]
                    # do 
                    fullname=get_name_h1D(EventSelection,ApplyEventWeight,bin_name,h1D_name,type_style,debug)
                    title=fullname
                    binning=h1D[3]
                    if debug:
                        print "fullname",fullname,"binning",binning
                    result[fullname]=TH1F(fullname,fullname,*binning)
                    result[fullname].SetTitle("")
                    rebin=1
                    plotting=h1D[4]
                    xaxis=h1D[5]
                    yaxis=h1D[6]
                    update_h1D_characteristics(result[fullname],rebin,plotting,xaxis,yaxis,debug)
                # done loop over list_h1D
            # done loop over list_bins   
        # done loop over list_ApplyEventWeight
    # done loop over list_EventSelection 
    if debug:
        print "dict_name_h1D",result
    # ready
    return result
# done function

def get_list_bin_name(list_bin,entry,debug):
    list_bins_passed=[]
    # loop over all the bins and if the event passes all the bins 
    # then add it to the list
    for collection in list_bin:
        name=collection[0]
        bins=collection[1]
        list_bins_values_passed=[]
        for bin_values in bins:
            if bin_values[0]<=getattr(entry,name)<bin_values[1]:
                list_bins_values_passed.append(bin_values)
        # done loop over all the bin_values
        list_bins_passed.append([name,list_bins_values_passed])
    # done loop over all the collections (criteria)
    result=concatenate_all_collections(list_bins_passed,debug)
    if debug:
        print "the bins where this event is found"
        for item in result:
            print item
    return result
# done function

def get_list_bin_numpyarray_QBins(listAllBins,debug):
    # bins of criteria
    inclusive_bin=(float("-inf"),float("inf"))
    # 
    list_bin=[]
    for element in listAllBins.split("+"):
        if debug:
            print element
        list_element=element.split("-")
        name=list_element[0]
        string_bins=list_element[1]
        option=list_element[2]
        if debug:
            print name, string_bins, option
        if option=="A":
            list_bins=get_list_intervals(string_bins,debug)
        elif option=="B":
            list_bins=get_list_intervals(string_bins,debug)
            list_bins.insert(0,inclusive_bin)
        elif option=="C":
            list_bins=[]
            list_bins.insert(0,inclusive_bin)
        else:
            print "Option",option,"not known. Choose A, B, C. Will ABORT!!!"
            assert(False)
        # done if over option
        if debug:
            print list_bins
        list_bin.append((name,list_bins))
    # done for

    if debug:
        print "list_bin",list_bin

    # the last value of string_bins is the one for Q (PtReco or Response)
    # so can use to to build the numpy array that will be used to create the bins
    # of the histograms in exactly the same values as for the PtReco or Response
    numpyarray_QBins=numpy.asarray(get_array_values(string_bins,debug))
    if debug:
        print "numpyarray_QBins",numpyarray_QBins

    # return
    return (list_bin,numpyarray_QBins)
# done function

def create_h1D_primary(inputFileName,treeName,outputFileName,list_EventSelection,list_ApplyEventWeight,list_bin,list_bin_name,list_h1D,NrEventStart,NrEventEnd,debug):

    # open the desied file
    if debug:
        print "inputFileName",inputFileName
    inputFile=TFile(inputFileName,"READ")
    if not inputFile.IsOpen():
        print "ROOT file",inputFileName,"does not exist. WILL ABORT!!!"
        assert(False)

    # read the desired tree from the file
    tree=inputFile.Get(treeName)
    if tree==None:
        print "tree",treeName,"doesn't exist in file",inputFileName
        assert(False)

    # create output file
    if debug:
        print "outputFileName",outputFileName
    outputFile=TFile(outputFileName,"RECREATE")

    # the dictionary that holds histograms
    dict_name_h1D=get_dict_name_h1D(list_EventSelection,list_ApplyEventWeight,list_bin_name,list_h1D,debug)
    
    if debug:
        for name in sorted(dict_name_h1D):
            print name,dict_name_h1D[name]

    # loop over the events in the tree
    # for each event compute the x and y variables needed
    # then fill the histograms

    # for counting time
    time_start=time()
    time_previous=time_start

    # loop over all the entries in the tree
    for i,entry in enumerate(tree):

        if i<(NrEventStart-1):
            continue
        
        #if debug:
        #    if i>9:
        #        continue
        if debug:
            print "************* next tree entry ",i,"*************"

        if NrEventEnd>0:
            if i>=NrEventEnd:
                continue

        if i%10000==0:
            time_previous,result_current=get_duration_of_run(time_start,time_previous,"current",debug)
            time_previous,result_start=get_duration_of_run(time_start,time_previous,"start",debug)
            print "*** i",i," *** since previous",result_current," *** since start",result_start

        # decide in which category the event falls
        hasGENWZ=int(getattr(entry,"hasGENWZ"))
        hasMuon=int(getattr(entry,"hasMuon"))
        bTag=int(getattr(entry,"bTag"))
        if debug:
            print "hasGENWZ",hasGENWZ,"hasMuon",hasMuon,"bTag",bTag

        # loop over event selections
        for EventSelection in list_EventSelection:
            # apply event selection
            if debug:
                print "EventSelection",EventSelection
            list_currentEventSelection=EventSelection.split("_")
            total_passed=True
            for currentEventSelection in list_currentEventSelection:
                if debug:
                    print "currentEventSelection",currentEventSelection
                if currentEventSelection=="All":
                    current_passed=True
                elif currentEventSelection=="GENWZ":
                    if treeName=="perevent":
                        # both jets need to have a jet of type truth (GENWZ) matched to them
                        current_passed=(hasGENWZ==2)
                    elif treeName=="perjet":
                        # the one jet has a truth jet matched
                        current_passed=(hasGENWZ==1)
                    else:
                        print "treeName",treeName,"not known. Will ABORT!!!"
                        assert(False)
                    # done if over treeName
                elif currentEventSelection=="0Muon":
                    current_passed=(hasMuon==0)
                elif currentEventSelection=="1Muon":
                    current_passed=(hasMuon==1)
                elif currentEventSelection=="2Muon":
                    current_passed=(hasMuon==2)
                elif currentEventSelection=="2L":
                    current_passed=(bTag==2)
                elif currentEventSelection=="2M":
                    current_passed=(bTag==3)
                elif currentEventSelection=="2T":
                    current_passed=(bTag==4)
                else:
                    print "currentEventSelection",currentEventSelection,"is not known. Choose All,GENWZ,0Muon,1Muon,2Muon,2L,2M,2T. Will ABORT!!"
                    assert(False)
                # end evaluate current_passed for currentEventSelection
                total_passed=total_passed and current_passed
                if debug:
                    print currentEventSelection,"current",current_passed,"passed",total_passed
            # end loop over currentEventSelection
            if debug:
                print "end event","passed",total_passed

            # apply the event selection
            if not total_passed:
                continue

            # find all the bin names where this event falls
            list_bin_name=get_list_bin_name(list_bin,entry,debug)
            # ex: list_bin_name=["Type_lep_inf_inf_PtV_inf_inf_Pt_EMJESGSMu_inf_inf"]
            # and for each, fill the histograms
            for bin_name in list_bin_name:
                # read and compute values for each correction:
                # loop over list_h1D
                for h1D in list_h1D:
                    type_style=h1D[0]
                    h1D_name=h1D[1]
                    h1D_name_reference=h1D[2]
                    if type_style=="v":
                        if debug:
                            print h1D_name,getattr(entry,h1D_name)
                        value=getattr(entry,h1D_name)
                    elif type_style=="r":
                        if debug:
                            print h1D_name,getattr(entry,h1D_name),h1D_name_reference,getattr(entry,h1D_name_reference)
                        value=ratio(getattr(entry,h1D_name),getattr(entry,h1D_name_reference))
                    elif type_style=="f":
                        if debug:
                            print h1D_name,getattr(entry,h1D_name),h1D_name_reference,getattr(entry,h1D_name_reference)
                        value=ratio(getattr(entry,h1D_name_reference),getattr(entry,h1D_name))           
                    else:
                        print "Type_Style",type_style," now known. Choose v for value, or r for response, or f for correction factor. Will ABORT!!!"
                        assert(False)
                    # done if over type_style
                    if debug:
                        print "type_style",type_style,"name",name,"value",value
                    # loop over if apply event weights
                    for ApplyEventWeight in list_ApplyEventWeight:
                        if debug:
                            print "ApplyEventWeight",ApplyEventWeight,
                        # event weight
                        if bool(int(ApplyEventWeight))==True:
                            eventWeight=getattr(entry,"eventWeight")
                        else:
                            eventWeight=1.0
                        if debug:
                            print "ApplyEventWeight",ApplyEventWeight,"eventWeight",eventWeight
                        # fill histogram
                        fullname=get_name_h1D(EventSelection,ApplyEventWeight,bin_name,h1D_name,type_style,debug)
                        dict_name_h1D[fullname].Fill(value,eventWeight)
                    # done loop over list_ApplyEventWeight
                # done for loop over list_h1D
            # done loop over list_bin_name
        # done loop over list_EventSelection
    # done loop over all the entries in the tree
    print "Done loop over all the entries in the jet. Start saving histograms."
    time_previous,result_current=get_duration_of_run(time_start,time_previous,"current",debug)
    time_previous,result_start=get_duration_of_run(time_start,time_previous,"start",debug)
    print "To save histograms",result_current," *** since start",result_start
    # save the file with all the histograms created
    outputFile.Write()
    outputFile.Close()
    # time at the end
    time_previous,result_start=get_duration_of_run(time_start,time_previous,"start",debug)
    print "All done. In total the code ran for",result_start
# done function

def create_PtReco_or_Response(inputFileName,outputFileName,list_EventSelection,list_ApplyEventWeight,listAllBins,fits,quantities,list_variable,physicsMeaning,debug):
    # for counting time
    time_start=time()
    time_previous=time_start

    if debug:
        print "inputFileName",inputFileName
        print "outputFileName",outputFileName
        print "list_EventSelection",list_EventSelection
        print "list_ApplyEventWeight",list_ApplyEventWeight
        print "list_AllBins",list_AllBins
        print "fits",fits
        print "quantities",quantities
        print "list_variable",list_variable
        print "physicsMeaning",physicsMeaning

    # get list_bin and numpyarray_QBins
    (list_bin,numpyarray_QBins)=get_list_bin_numpyarray_QBins(listAllBins,debug)    

    # interpret the last element of list bin as bins of Q
    # and first bins except the last as bins of analysis (Lep, PtV)
    nr_list_bin=len(list_bin)
    if debug:
        print "nr_list_bin",nr_list_bin
    # fill all elements except the last one to list_bin_analysis
    list_bin_analysis=[]
    for i in xrange(nr_list_bin-1):
        list_bin_analysis.append(list_bin[i])
    # put the last element into list_QBins
    list_all_QBin=list_bin[-1]
    QName=list_all_QBin[0]
    list_QBin=list_all_QBin[1]
    #  
    list_bin_analysisname=concatenate_all_collections(list_bin_analysis,debug)
    if debug:
        print "list_bin_analysisname",list_bin_analysisname
        print "len(list_bin_analysisname)",len(list_bin_analysisname)
        print "len(list_bin_analysis)",len(list_bin_analysis)

    # open file
    inputFile=TFile(inputFileName,"READ")
    if not inputFile.IsOpen():
        print "ROOT file",inputFileName,"does not exist. WILL ABORT!!!"
        assert(False)

    # loop over list_EventSelection
    dict_EventSelection_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms={}
    for EventSelection in list_EventSelection:
        # loop over list_ApplyEventWeight
        dict_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms={}
        for ApplyEventWeight in list_ApplyEventWeight:
            # loop over list_bin_analysisname
            dict_analysisname_variable_QBin_fit_meanrms={}
            for analysisname in list_bin_analysisname:
                # loop over list_variable
                dict_variable_QBin_fit_meanrms={}
                for variable in list_variable:
                    # loop over the list_QBin
                    dict_QBin_fit_meanrms={}
                    for QBin in list_QBin:
                        histogramName="h_"+EventSelection+"_"+ApplyEventWeight+"_"+analysisname+"_"+QName+"_"
                        if debug:
                            print QBin
                        histogramName+=get_bin_string(QBin,debug)+"_"+variable+"_"+physicsMeaning
                        if debug:
                            print "histogramName",histogramName
                        # histogramName="h_All_1_Type_lep_inf_inf_PtV_inf_inf_Pt_EMJESGSMu_40_50_Pt_EMJESGSMu_f"
                        dict_fit_meanrms={}
                        # loop over fits
                        for fit in fits.split(","):
                            gStyle.SetOptFit()
                            c=TCanvas("c","c",600,400)
                            # h=retrieveHistogram(inputFileName,"",histogramName,"",debug).Clone()
                            h=inputFile.Get(histogramName).Clone()
                            if debug:
                                print h,type(h)
                                print h.GetMean(),h.GetRMS()
                            h.Draw()
                            f,result_fit=fit_hist(h,fit,"O",debug)
                            dict_fit_meanrms[fit]=(result_fit[1],result_fit[2])
                            if debug:
                                print get_string_distribution(fit,QName,result_fit[0],result_fit[1],result_fit[2])
                        # done loop over fits
                        dict_QBin_fit_meanrms[QBin]=dict_fit_meanrms
                    # done loop over list_QBin
                    dict_variable_QBin_fit_meanrms[variable]=dict_QBin_fit_meanrms
                # done loop over list_variable
                dict_analysisname_variable_QBin_fit_meanrms[analysisname]=dict_variable_QBin_fit_meanrms
            # done loop over list_bin_analysisname
            dict_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms[ApplyEventWeight]=dict_analysisname_variable_QBin_fit_meanrms
        # done loop over list_ApplyEventWeight
        dict_EventSelection_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms[EventSelection]=dict_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms
    # done loop over list_EventSelection

    # close file
    inputFile.Close()



    # print the big dictionary
    if debug:
        print "dict_EventSelection_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms"
        print dict_EventSelection_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms

    # now that we have the values, we can create the new histograms in a new root file
    # will loop over all things that can differ, and we will create and fill the histograms
    # in the same place
    # create histograms of rms/mean in bins of x
    outputFile=TFile(outputFileName,"RECREATE")

    dict_name_h1D={}
    # loop over list_EventSelection
    for EventSelection in list_EventSelection:
        # loop over list_ApplyEventWeight
        for ApplyEventWeight in list_ApplyEventWeight:
            # loop over list_bin_analysisname
            for analysisname in list_bin_analysisname:
                # loop over list_variable:
                for variable in list_variable:
                    # loop over fits
                    for fit in fits.split(","):
                        if debug:
                            print "fit",fit
                        # loop over quantities
                        for quantity in quantities.split(","):
                            if debug:
                                print "quantity",quantity
                            histogramName="h_"+EventSelection+"_"+ApplyEventWeight+"_"+analysisname+"_"+variable+"_"+fit+"_"+quantity
                            if debug:
                                print "histogramName",histogramName
                            dict_name_h1D[histogramName]=TH1F(histogramName,histogramName,len(numpyarray_QBins)-1,numpyarray_QBins)
                            # loop over the list_QBin
                            for i,QBin in enumerate(list_QBin):
                                if debug:
                                    print "QBin",QBin
                                mean,rms=dict_EventSelection_ApplyEventWeight_analysisname_variable_QBin_fit_meanrms[EventSelection][ApplyEventWeight][analysisname][variable][QBin][fit]
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
                                    value=ratio(rms,mean)
                                    error=0.0
                                else:
                                    print "Quantity",quantity,"not known. Choose between mean, rms, meanwithrms, rmsovermean. Will ABORT!"
                                    assert(False)
                                # done if over quantity
                                if debug:
                                    print histogramName,"bin",i,"value",value,"error",error
                                dict_name_h1D[histogramName].SetBinContent(i,value)
                                dict_name_h1D[histogramName].SetBinError(i,error)

    # done all loops
    if debug:
        print "dict_name_h1D",dict_name_h1D

    # save the file with all the histograms created thanks to the histograms being in the dictionary
    outputFile.Write()
    outputFile.Close()

    # time at the end
    time_previous,result_start=get_duration_of_run(time_start,time_previous,"start",debug)
    print "All done. In total the code ran for",result_start

# done function
