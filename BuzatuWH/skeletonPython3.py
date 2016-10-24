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


#################################################################
################### Functions##### ##############################
#################################################################

# http://ipl.physics.harvard.edu/wp-uploads/2013/03/PS3_Error_Propagation_sp13.pdf
# https://en.wikipedia.org/wiki/Propagation_of_uncertainty



#################################################################
################### Run #########################################
#################################################################

#print "ratio",ratioError(25.88,0.0115,47167,1.43)
#print "sensitivity",sensitivityError(25.88,0.0115,47167,1.43)
#print "significance",significanceError(25.88,0.0115,47167,1.43)

dict_category_values={
"2jet1tag<":(25.88,0.0115,47167,1.43),
"2jet2tag<":(20.00,0.0142,8626,2.11),
"3jet1tag<":(37.79,0.00766,74103,1.49),
"3jet2tag<":(29.38,0.00889,21055,2.1),
"2jet1tag>":(6.313,0.0183,2885.6,2.94),
"2jet2tag>":(4.756,0.0222,321.94,3.11),
"3jet1tag>":(14.85,0.0108,8397.9,1.35),
"3jet2tag>":(12.32,0.012,1689.2,1.86),
}

dict_category_ratio={}
dict_category_sensitivity={}
dict_category_significance={}
for category in dict_category_values:
    values=dict_category_values[category]
    s=values[0]
    se=values[1]
    b=values[2]
    be=values[3]
    print "category",category, "s",s,"se",se,"b",b,"be",be
    dict_category_ratio[category]=ratioError(s,se,b,be)[0]
    dict_category_sensitivity[category]=sensitivityError(s,se,b,be)[0]
    dict_category_significance[category]=significanceError(s,se,b,be)[0]
    #print "ratio S/B",ratioError(s,se,b,be)
    #print "sensitivity S/sqrt(B)",sensitivityError(s,se,b,be)
    #print "significance math.sqrt(2*((s+b)*math.log(1+s/b)-s))",significanceError(s,se,b,be)


print ""
list_figureofmerit="ratio,sensitivity,significance".split(",")
for figureofmerit in list_figureofmerit:
    print "***",figureofmerit,"***"
    if figureofmerit=="ratio":
        x=dict_category_ratio
    elif figureofmerit=="sensitivity":
        x=dict_category_sensitivity
    elif figureofmerit=="significance":
        x=dict_category_significance
    for category in sorted(x, key=x.get, reverse=True):
        print "%-10s %-.3f" % (category,x[category])

#################################################################
################### Finished ####################################
#################################################################
