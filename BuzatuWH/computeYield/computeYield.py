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
if total!=6:
    print "You need some arguments, will ABORT!"
    print "Ex: python computeYield.py Folder Histogram FolderOutput Debug"
    print "Ex: python computeYield.py ${outputroot}/local/histo_batch/readPaul_1_0_J1Pt45+2BTag_1_perevent h_GENWZ_1 M_EMJESGSMuPt_j1j2_r_0_300_4 ${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent 1"
    assert(False)
# done if

Folder=sys.argv[1]
Prefix=sys.argv[2]
Histogram=sys.argv[3]
FolderOutput=sys.argv[4]
Debug=bool(int(sys.argv[5]))

debug=Debug

if debug:
    print "Folder",Folder
    print "Prefix",Prefix
    print "Histogram",Histogram
    print "FolderOutput",FolderOutput
    print "Debug",Debug

# run
if debug:
    print "list_LepBinsUse",list_LepBinsUse
    print "list_PtVBinsUse",list_PtVBinsUse

for Lep in list_LepBinsUse:
    if debug:
        print "list_PtVBinsUse",list_PtVBinsUse
    # create a new file
    f = open(FolderOutput+"/yield_"+Prefix+"_"+Lep+"_"+Histogram+".tex",'w')
    f.write('\\documentclass{beamer}\n')
    f.write('\\usepackage{tabularx}\n')
    f.write('\\usepackage{adjustbox}\n')
    f.write('\\usepackage{pdflscape}\n')
    f.write('\\begin{document}\n')
    f.write('\\begin{frame}{Yields for '+Lep+' channel}\n')
    f.write('\\begin{center}\n')
    f.write('\\begin{landscape} \n')
    f.write('\\adjustbox{max height=\\dimexpr\\textheight-6.0cm\\relax,max width=\\textwidth}\n')
    f.write('{\n')
    f.write('\\begin{tabular}{|l|l|l|l|l|l|l|}\n')
    f.write('\hline\hline \n') 
    f.write('Process & $p_{T}^{V}$ inclusive & $p_{T}^{V} < 90$ GeV & $90 < p_{T}^{V} < 120$ GeV & $120 < p_{T}^{V} < 160$ GeV & $160 < p_{T}^{V} < 200$ GeV & $p_{T}^{V} > 200$ GeV \\\\ \hline\hline \n')
    # we have to remember the signal and background values in each bin of PtV
    dict_PtV_name_yield={}
    for PtV in list_PtVBinsUse:
        if debug:
            print PtV
        dict_name_yield={}
        dict_name_yield["Signal"]=0.0
        dict_name_yield["Background"]=0.0
        dict_PtV_name_yield[PtV]=dict_name_yield
    # done loop over PtV
    if debug:
        print "dict_PtV_name_yield",dict_PtV_name_yield
    # loop over processes
    for process in list_names:
        if debug:
            print process
        if process=="Signal" or process=="Background":
            f.write('\\hline\n')
        f.write(process)
        for PtV in list_PtVBinsUse:
            # ex: "h_Mu_inf_90_M_EMJESGSMuPt_j1j2_100_150_5"
            fileName=Folder+"/h_"+Prefix+"_"+Lep+"_"+PtV+"_"+Histogram+".root"
            h=retrieveHistogram(fileName,"",process,"",debug)
            current_yield=h.Integral()
            if process=="Signal" or  process=="Background":
                dict_PtV_name_yield[PtV][process]=current_yield
            # done if process is signal or background
            f.write(" & "+"%-.2f" % (current_yield))
            if debug:
                print "%-10s %-.2f" % (process, current_yield)
            if debug:
                print "fileName",fileName
            if debug:
                print Lep,PtV
        # done loop over PtV
        f.write(" \\\\ \n")
        if process=="Signal" or process=="Background":
            f.write('\\hline\n')
    # done loop over processes
    #
    f.write('\\hline \n')
    # write some S vs B quantities
    #        
    f.write("S/B")
    for PtV in list_PtVBinsUse:
        S=dict_PtV_name_yield[PtV]["Signal"]
        B=dict_PtV_name_yield[PtV]["Background"]
        f.write(" & "+"%-.2f" % (ratio(S,B)))
    # done loop over PtV
    f.write(" \\\\ \n")
    f.write('\\hline \n')
    #
    f.write("Sensitivity")
    for PtV in list_PtVBinsUse:
        S=dict_PtV_name_yield[PtV]["Signal"]
        B=dict_PtV_name_yield[PtV]["Background"]
        f.write(" & "+"%-.2f" % (sensitivity(S,B)))
    # done loop over PtV
    f.write(" \\\\ \n")
    f.write('\\hline\n')
    #
    f.write("Significance")
    for PtV in list_PtVBinsUse:
        S=dict_PtV_name_yield[PtV]["Signal"]
        B=dict_PtV_name_yield[PtV]["Background"]
        f.write(" & "+"%-.2f" % (significance(S,B)))
    # done loop over PtV
    f.write(" \\\\ \n")
    f.write('\\hline\n')
    #
    f.write('\\hline\n')
    f.write('\\end{tabular}\n')
    f.write('}\n')
    f.write('\\end{landscape} \n')
    f.write('\\end{center}\n')
    f.write('\\end{frame}\n')
    f.write('\\end{document}\n')
    f.close()
# done

####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"



