#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
from ConfigWH import *
from HelperWH import *

print "Start Python"
time_start=time()

####################################################
##### Start                                 ########
####################################################

total = len(sys.argv)
# number of arguments plus 1
if total!=11:
    print "You need some arguments, will ABORT!"
    print "Ex : python computeSignificance.py Folder Prefix Suffix WhatToCompute IncludeUnderflowOverflowBins AddInQuadrature Signal Background FolderOutput Debug"
    print "Ex : python computeSignificance.py ${outputroot}/local/histo_batch/readPaul_1_0_J1Pt45+2BTag_1_perevent GENWZ_1 M-j1j2_v_0_300_4 significance 0 1 Signal Background ${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent 1"
    youran="phyton"
    for element in sys.argv:
        youran+=" "+element
    print "You: ",youran
    assert(False)
# done if

Folder=sys.argv[1]
Prefix=sys.argv[2]
Suffix=sys.argv[3]
WhatToCompute=sys.argv[4]
IncludeUnderflowOverflowBins=bool(int(sys.argv[5]))
AddInQuadrature=bool(int(sys.argv[6]))
SignalName=sys.argv[7]
BackgroundName=sys.argv[8]
FolderOutput=sys.argv[9]
Debug=bool(int(sys.argv[10]))

debug=Debug

if debug:
    print "Folder",Folder
    print "Prefix",Prefix
    print "Suffix",Suffix
    print "WhatToCompute",WhatToCompute
    print "IncludeUnderflowOverflowBins",IncludeUnderflowOverflowBins
    print "AddInQuadrature",AddInQuadrature
    print "FolderOutput",FolderOutput
    print "Debug",Debug

list_Suffix=Suffix.split("-")
Variable=list_Suffix[0]
Suffix=list_Suffix[1]

if debug:
    print "list_corrections",list_corrections

# bins of criteria

inclusive_bin=(float("-inf"),float("inf"))

string_LepBins="1.5"
list_LepBins=get_list_intervals(string_LepBins,debug)
list_LepBins=[]
list_LepBins.insert(0,inclusive_bin)


#string_PtVBins="90,120,160,200"
#string_PtVBins="200"
#list_PtVBins=get_list_intervals(string_PtVBins,debug)
#list_PtVBins=[]
#list_PtVBins.insert(0,inclusive_bin)
list_PtVBins=[(200,float("inf"))]

string_QBins="20,30,40,50,60,70,80,100,120,140,160,180,200,240,280"
#string_QBins="60"
list_QBins=get_list_intervals(string_QBins,debug)
list_QBins=[]
list_QBins.insert(0,inclusive_bin)

if debug:
    print "list_LepBins",list_LepBins
    print "list_PtVBins",list_PtVBins
    print "list_QBins",list_QBins

#exit()

list_bin=[]
list_bin.append(("Type_lep",list_LepBins))
list_bin.append(("PtV",list_PtVBins))
list_bin.append(("M_GENWZ_j1j2",list_QBins))

if debug:
    print "list_bin",list_bin

list_binname=concatenate_all_collections(list_bin,debug)
if debug:
    print "list_binname",list_binname
    print "len(list_binname)",len(list_binname)


LepPrefix=list_bin[0][0]
PtVPrefix=list_bin[1][0]
QPrefix=list_bin[2][0]

string_corrections="GENWZ"
string_corrections+=",EM,EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt2,EMJESGSMuPt3,EMJESGSMuPt4"
string_corrections+=",EMJESGSMuPt4Nu000,EMJESGSMuPt4Nu005,EMJESGSMuPt4Nu010,EMJESGSMuPt4Nu015,EMJESGSMuPt4Nu020,EMJESGSMuPt4Nu025,EMJESGSMuPt4Nu030,EMJESGSMuPt4Nu035,EMJESGSMuPt4Nu040,EMJESGSMuPt4Nu045,EMJESGSMuPt4Nu050,EMJESGSMuPt4Nu055,EMJESGSMuPt4Nu060,EMJESGSMuPt4Nu065,EMJESGSMuPt4Nu070,EMJESGSMuPt4Nu075,EMJESGSMuPt4Nu080,EMJESGSMuPt4Nu085,EMJESGSMuPt4Nu090,EMJESGSMuPt4Nu095,EMJESGSMuPt4Nu100,EMJESGSMuPt4Nu105,EMJESGSMuPt4Nu110"
string_corrections+=",EMJESGSMuNu000,EMJESGSMuNu005,EMJESGSMuNu010,EMJESGSMuNu015,EMJESGSMuNu020,EMJESGSMuNu025,EMJESGSMuNu030,EMJESGSMuNu035,EMJESGSMuNu040,EMJESGSMuNu045,EMJESGSMuNu050,EMJESGSMuNu055,EMJESGSMuNu060,EMJESGSMuNu065,EMJESGSMuNu070,EMJESGSMuNu075,EMJESGSMuNu080,EMJESGSMuNu085,EMJESGSMuNu090,EMJESGSMuNu095,EMJESGSMuNu100,EMJESGSMuNu105,EMJESGSMuNu110"
string_corrections+=",EMJESGSMuNu000Pt4,EMJESGSMuNu005Pt4,EMJESGSMuNu010Pt4,EMJESGSMuNu015Pt4,EMJESGSMuNu020Pt4,EMJESGSMuNu025Pt4,EMJESGSMuNu030Pt4,EMJESGSMuNu035Pt4,EMJESGSMuNu040Pt4,EMJESGSMuNu045Pt4,EMJESGSMuNu050Pt4,EMJESGSMuNu055Pt4,EMJESGSMuNu060Pt4,EMJESGSMuNu065Pt4,EMJESGSMuNu070Pt4,EMJESGSMuNu075Pt4,EMJESGSMuNu080Pt4,EMJESGSMuNu085Pt4,EMJESGSMuNu090Pt4,EMJESGSMuNu095Pt4,EMJESGSMuNu100Pt4,EMJESGSMuNu105Pt4,EMJESGSMuNu110Pt4"

list_corrections=string_corrections.split(",")

if debug:
    print "list_corrections",list_corrections

#
for LepBin in list_LepBins:
    Lep=get_bin_string(LepBin,debug)
    # find the lepton category for the 
    if Lep=="inf_2":
        LepChannel="El"
    elif Lep=="2_inf":
        LepChannel="Mu"
    elif Lep=="inf_inf":
        LepChannel="All"
    else:
        print "Neither lep_inf_2 (meaning El), nor lep_2_inf (meaning Mu), nor lep_inf_inf (meaning All) are found in Lep",Lep,". Will ABORT!!!"
        assert(False)
    # done if 

    for QBin in list_QBins:
        Q=get_bin_string(QBin,debug)
        # create a new file
        fileOutputName=FolderOutput+"/"+WhatToCompute+"_"+Prefix+"_"+LepPrefix+"_"+Lep+"_"+QPrefix+"_"+Q+"_"+Variable+"_"+Suffix+"_"+SignalName+"_"+BackgroundName
        if IncludeUnderflowOverflowBins:
            fileOutputName+="_all_bins"
        else:
            fileOutputName+="_main_bins"
            if AddInQuadrature:
                fileOutputName+="_with_shape"
            else:
                fileOutputName+="_no_shape"
        fileOutputName+=".tex"
        f = open(fileOutputName,'w')
        f.write('\\documentclass{beamer}\n')
        f.write('\\usepackage{tabularx}\n')
        f.write('\\usepackage{adjustbox}\n')
        f.write('\\usepackage{pdflscape}\n')
        f.write('\\begin{document}\n')
        f.write('\\begin{frame}{'+WhatToCompute+' for '+LepChannel+' channel}\n')
        f.write('\\begin{center}\n')
        f.write('\\begin{landscape} \n')
        f.write('\\adjustbox{max height=\\dimexpr\\textheight-6.0cm\\relax,max width=\\textwidth}\n')
        f.write('{\n')
        f.write('\\begin{tabular}{|l|l|l|l|l|l|l|l|}\n')
        f.write('\hline\hline \n') 
        f.write('Correction & $p_{T}^{V}$ inclusive & $p_{T}^{V} < 90$ GeV & $90 < p_{T}^{V} < 120$ GeV & $120 < p_{T}^{V} < 160$ GeV & $160 < p_{T}^{V} < 200$ GeV & $p_{T}^{V} > 200$ GeV \\\\ \hline\hline \n')
        # loop over all corrections
        for correction in list_corrections:
            f.write(correction)
            for PtVBin in list_PtVBins:
                PtV=get_bin_string(PtVBin,debug)
                fileName=Folder+"/h_"+Prefix+"_"+LepPrefix+"_"+Lep+"_"+PtVPrefix+"_"+PtV+"_"+QPrefix+"_"+Q+"_"+Variable+"_"+correction+"_"+Suffix+".root"
                #
                h_S=retrieveHistogram(fileName,"",SignalName,"",debug).Clone()
                h_B=retrieveHistogram(fileName,"",BackgroundName,"",debug).Clone()
                NbinsX=h_S.GetNbinsX()
                # what is my range of bins I run on?
                if IncludeUnderflowOverflowBins:
                    myrange=[0,NbinsX+1+1]
                else:
                    # we want to run excluding the underflow (bin 0)
                    # and overflow bin NbinsX+1
                    myrange=[1,NbinsX+1]
                if debug:
                    print "myrange",myrange
                if AddInQuadrature:
                    total_squared=0.0
                    # need to loop over the bins first
                    # done if about my range of bins 
                    for i in xrange(myrange[0],myrange[-1]):
                        S=h_S.Integral(i,i)
                        B=h_B.Integral(i,i)
                        if debug:
                            print "i",i,"S","%-.2f" % S,"B","%-.2f" % B
                        if WhatToCompute=="signaloverbackground":
                            current=ratio(S,B)
                        elif WhatToCompute=="sensitivity":
                            current=sensitivity(S,B)
                        elif WhatToCompute=="significance":
                            current=significance(S,B)
                        else:
                            print "WhatToCompute",WhatToCompute,"now known. Choose between signaloverbackground, sensitivity, significance. Will ABORT!!!"
                            assert(False)
                        # done if on WhatToCompute
                        # add in quadrature
                        total_squared+=current*current
                    # done loop over all the bins in the histogram
                    if debug:
                        print "total_squared",total_squared
                    total=math.sqrt(total_squared)
                    if debug:
                        print "total",total
                else:
                    # not add in quadrature
                    S=h_S.Integral(*myrange)
                    B=h_B.Integral(*myrange)
                    if WhatToCompute=="signaloverbackground":
                        total=significance(S,B)
                    elif WhatToCompute=="sensitivity":
                        total=sensitivity(S,B)
                    elif WhatToCompute=="significance":
                        total=significance(S,B)
                    else:
                        print "WhatToCompute",WhatToCompute,"now known. Choose between signaloverbackground, sensitivity, significance. Will ABORT!!!"
                        assert(False)
                    # done if on WhatToCompute
                # done if AddInQuadrature, so let's write the total
                # which was able to be computed in two ways
                f.write(" & "+"%-.3f" % (total))
            # done over PtV
            f.write(" \\\\ \\hline \n")
        # done loop over all corrections
        f.write('\\end{tabular}\n')
        f.write('}\n')
        f.write('\\end{landscape} \n')
        f.write('\\end{center}\n')
        f.write('\\end{frame}\n')
        f.write('\\end{document}\n')
        f.close()
    # done loop over QBins    
# done loop over LepBins

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
