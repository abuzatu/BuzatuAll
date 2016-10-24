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
    print "Ex: python fitHistogram.py Folder HistogramPrefix HistogramSuffix FolderOutput Debug"
    print "Ex: python fitHistogram.py ${outputroot}/local/histo_batch/readPaul_1_0_J1Pt45+2BTag_1_perevent M_ _j1j2_100_150_5 ${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent 1"
    assert(False)
# done if

Folder=sys.argv[1]
HistogramPrefix=sys.argv[2]
HistogramSuffix=sys.argv[3]
FolderOutput=sys.argv[4]
Debug=bool(int(sys.argv[5]))

debug=Debug

if debug:
    print "Folder",Folder
    print "HistogramPrefix",HistogramPrefix
    print "HistogramSuffix",HistogramSuffix
    print "FolderOutput",FolderOutput
    print "Debug",Debug

# to run in batch mode
import ROOT
ROOT.gROOT.SetBatch(True)

list_LepBinsUse="all".split(",")
list_PtVBinsUse="all".split(",")
list_names="WH".split(",")
fit="Bukin" # "None" # "Gauss" # "Bukin"
list_corrections="GENWZ,EM,EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3".split(",")
#list_corrections="GENWZ,EMJESGSMuPt,EMJESGSMuPt3".split(",")



if debug:
    print "list_LepBinsUse",list_LepBinsUse
# loop over Lep
for Lep in list_LepBinsUse:
    if debug:
        print "Lep",Lep
        print "list_names",list_names
    options_fit="histo" #"histo,Bukin,histo+Bukin"
    # loop over process
    for process in list_names:
        if debug:
            print "process",process
            print "list_corrections",list_corrections
        fileOutputNameTex="h_"+Lep+"_"+HistogramPrefix+"_"+HistogramSuffix+"_"+process+"_"+fit
        frameName=deepcopy(fileOutputNameTex)
        frameName = frameName.replace("_"," ")
        f=open(FolderOutput+"/"+fileOutputNameTex+".tex",'w')
        f.write('\\documentclass{beamer} \n')
        f.write('\\usepackage{tabularx} \n')
        f.write('\\usepackage{adjustbox} \n')
        f.write('\\usepackage{pdflscape}\n')
        f.write('\\begin{document} \n')
        f.write(' \n')
        f.write('\\begin{frame}{Mbb fits for '+Lep+' channel}\n')
        f.write('\\begin{center}\n')
        f.write('\\adjustbox{max height=\\dimexpr\\textheight-6.0cm\\relax,max width=\\textwidth}\n')
        f.write('{\n')
        f.write('\\begin{tabular}{|l|l|l|l|l|l|l|l|}\n')
        f.write('\hline\hline \n') 
        f.write('Correction & $p_{T}^{V}$ inclusive & $p_{T}^{V} < 90$ GeV & $90 < p_{T}^{V} < 120$ GeV & $120 < p_{T}^{V} < 160$ GeV & $160 < p_{T}^{V} < 200$ GeV & $p_{T}^{V} > 200$ GeV \\\\ \hline\hline \n')
        f.write('\hline\hline \n') 
        # loop over correction
        for correction in list_corrections:
            if debug:
                print "correction",correction
            f.write(correction)
            if debug:        
                print "list_PtVBinsUse",list_PtVBinsUse
            # loop over PtV
            for PtV in list_PtVBinsUse:
                if debug:
                    print "PtV",PtV
                plot_option=""
                gStyle.SetOptFit()
                c=TCanvas("c","c",600,400)
                fileName=Folder+"/h_"+Lep+"_"+PtV+"_"+HistogramPrefix+"_"+correction+"_"+HistogramSuffix+".root"
                h=retrieveHistogram(fileName,"",process,"",debug).Clone()
                if debug:
                    print process,correction,h.Integral()
                h.Draw()
                # add ATLAS
                setupTextOnPlot("#bf{#it{#bf{ATLAS } Simulation Internal}}",0.05,13,0.50,0.30,0.09)
                function,result_fit=fit_hist(h,fit,plot_option,debug)
                if debug:
                    print get_string_distribution(fit,correction,result_fit[0],result_fit[1],result_fit[2])
                fileOutputNamePdf="h_"+Lep+"_"+PtV+"_"+HistogramPrefix+"_"+HistogramSuffix+"_"+process+"_"+fit
                c.Print(FolderOutput+"/"+fileOutputNamePdf+"_"+correction+".pdf")
                f.write(" & %-.1f/%-.1f " % (result_fit[1],result_fit[2]))
            # done loop over PtV
            f.write(" \\\\ \\hline \n")
        # done loop over correction
        f.write('\\hline\n')
        f.write('\\end{tabular}\n')
        f.write('}\n')
        f.write('\\end{center}\n')
        f.write('\\end{frame}\n')
        f.write(' \n')
        f.write('\\end{document}\n')
        f.close()
        # done loop over process
# done loop over Lep


####################################################
##### End                                   ########
####################################################

time_end = time()
s=time_end-time_start
m=s/60.0
h=m/60.0
print 'Code took to run: %-.0f seconds %-.1f minutes %-.3f hours.' %(s,m,h)
print "End Python"
