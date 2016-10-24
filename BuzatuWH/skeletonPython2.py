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

#################################################################
################### Functions##### ##############################
#################################################################


#################################################################
################### Run #########################################
#################################################################

#h=retrieveHistogram("/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_hadronic_Bukin","",debug)
#h=retrieveHistogram("/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_Parton_True.root","","PtReco_semileptonic_Bukin","",debug)
#h=retrieveHistogram("/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_TruthWZ_True.root","","PtReco_hadronic_None","",debug)
#h=retrieveHistogram("/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_TruthWZ_True.root","","PtReco_semileptonic_None","",debug)
#h=retrieveHistogram("/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_TruthWZ_True.root","","PtReco_hadronic_BukinMedian","",debug)
#h=retrieveHistogram("/Users/abuzatu/data/histos_PtReco/PtRecoNow/PtReco_histos_llbb_OneMu_TruthWZ_True.root","","PtReco_semileptonic_Bukin","",debug)
getBinValues(h,debug)

#################################################################
################### Finished ####################################
#################################################################
