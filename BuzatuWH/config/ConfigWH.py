#!/usr/bin/python
# if a .py you want to import is in the current folder, you would have to add
# the full path of the folder to the PYTHONPATH
# for example, if the NNs are in their own folder called NN:
# ex: export PYTHONPATH=$jer/PyROOT/NN:$PYTHONPATH
from HelperPyRoot import *
from HelperWH import *
import numpy
import sys

debug=False

# each process should know if its signal, background or data
dict_type_process={}
dict_type_process["Signal"]=["lvbb125","llbb125","llbb125gg","vvbb125","VH","WH","ZH"]
dict_type_process["Background"]=["WW","WZ","ZZ","TTbar","STopS","STopT","STopWt","Wll","Wcl","Wbb","Wbl","Wcc","Zll","Zcl","Zbb","Zbl","Zcc","VV","TopPair","SingleTop","Wl","Wcl","Whf","Zl","Zcl","Zhf","MJ"]
dict_type_process["Data"]=["DataEl","DataMu"]
dict_type_process["BackgroundMJ"]=["WWMJ","WZMJ","ZZMJ","TTbarMJ","STopSMJ","STopTMJ","STopWtMJ","WllMJ","WclMJ","WbbMJ","WblMJ","WccMJ","ZllMJ","ZclMJ","ZbbMJ","ZblMJ","ZccMJ"]
dict_type_process["DataMJ"]=["DataElMJ","DataMuMJ"]

# how to group processes
dict_name_processes={}
dict_name_processes["WH"]=["lvbb125"]
dict_name_processes["ZH"]=["llbb125","llbb125gg","vvbb125"]
dict_name_processes["VV"]=["WW","WZ","ZZ"]
dict_name_processes["TopPair"]=["TTbar"]
dict_name_processes["SingleTop"]=["STopS","STopT","STopWt"]
dict_name_processes["Wl"]=["Wll"]
dict_name_processes["Wcl"]=["Wcl"]
dict_name_processes["Whf"]=["Wbb","Wbl","Wcc"]
dict_name_processes["Zl"]=["Zll"]
dict_name_processes["Zcl"]=["Zcl"]
dict_name_processes["Zhf"]=["Zbb","Zbl","Zcc"]
dict_name_processes["MJ"]=["DataElMJ","DataMuMJ","WWMJ","WZMJ","TTbarMJ","STopSMJ","STopTMJ","STopWtMJ","WllMJ","WclMJ","WbbMJ","WblMJ","WccMJ","ZllMJ","ZclMJ","ZbbMJ","ZblMJ","ZccMJ"] # not included ZZMJ
dict_name_processes["Data"]=["DataEl","DataMu"]


# the order in which we want them to appear in the table
list_names=["WH","ZH","Signal","VV","TopPair","SingleTop","Wl","Wcl","Whf","Zl","Zcl","Zhf","MJ","Background","Data"]

# the SF from the QCD fit for the MC backgrounds
# values computed by Tom
dict_bkg_lep_SF={}
# regular MC backgrounds
dict_lep_SF={}
dict_lep_SF["El"]=1.09902
dict_lep_SF["Mu"]=0.949032
dict_lep_SF["All"]=1.0
dict_bkg_lep_SF["Background"]=dict_lep_SF
# MJ background from data
dict_lep_SF={}
dict_lep_SF["El"]=0.0482946
dict_lep_SF["Mu"]=0.115172
dict_lep_SF["All"]=0.10 # dummy
dict_bkg_lep_SF["DataMJ"]=dict_lep_SF
# MJ background from MC
# to be subtractd from MJ background from data
# therefore the negative sign
dict_lep_SF={}
dict_lep_SF["El"]=-0.0482946
dict_lep_SF["Mu"]=-0.115172
dict_lep_SF["All"]=-0.10 # dummy
dict_bkg_lep_SF["BackgroundMJ"]=dict_lep_SF
# regular MC signal
dict_lep_SF={}
dict_lep_SF["El"]=1.0
dict_lep_SF["Mu"]=1.0
dict_lep_SF["All"]=1.0
dict_bkg_lep_SF["Signal"]=dict_lep_SF
# regular data
dict_lep_SF={}
dict_lep_SF["El"]=1.0
dict_lep_SF["Mu"]=1.0
dict_lep_SF["All"]=1.0
dict_bkg_lep_SF["Data"]=dict_lep_SF
#
if debug:
    print "dict_bkg_lep_SF",dict_bkg_lep_SF

# pentru overlay PtReco or Response
list_process="lvbb125,llbb125,llbb125gg,vvbb125,WW,WZ,ZZ,TTbar,STopS,STopT,STopWt,Wbb,Wbl,Wcc,Wcl,Wll,Zbb,Zbl,Zcc,Zcl,Zll".split(",")
#list_process="lvbb125,TTbar,Wbb,Wll".split(",")
list_list_process=[]
list_list_process.append("lvbb125,llbb125,llbb125gg".split(","))
list_list_process.append("lvbb125,WW,WZ,ZZ".split(","))
list_list_process.append("lvbb125,TTbar".split(","))
list_list_process.append("lvbb125,STopS".split(","))
list_list_process.append("lvbb125,STopT".split(","))
list_list_process.append("lvbb125,STopWt".split(","))
list_list_process.append("lvbb125,Wbb,Wbl,Wcc,Wcl,Wll".split(","))
list_list_process.append("lvbb125,Zbb,Zbl,Zcc,Zcl,Zll".split(","))

string_corrections="GENWZ"
string_corrections+=",EM,EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt2,EMJESGSMuPt3,EMJESGSMuPt4"
string_corrections+=",EMJESGSMuPt4Nu000,EMJESGSMuPt4Nu005,EMJESGSMuPt4Nu010,EMJESGSMuPt4Nu015,EMJESGSMuPt4Nu020,EMJESGSMuPt4Nu025,EMJESGSMuPt4Nu030,EMJESGSMuPt4Nu035,EMJESGSMuPt4Nu040,EMJESGSMuPt4Nu045,EMJESGSMuPt4Nu050,EMJESGSMuPt4Nu055,EMJESGSMuPt4Nu060,EMJESGSMuPt4Nu065,EMJESGSMuPt4Nu070,EMJESGSMuPt4Nu075,EMJESGSMuPt4Nu080,EMJESGSMuPt4Nu085,EMJESGSMuPt4Nu090,EMJESGSMuPt4Nu095,EMJESGSMuPt4Nu100,EMJESGSMuPt4Nu105,EMJESGSMuPt4Nu110"
string_corrections+=",EMJESGSMuNu000,EMJESGSMuNu005,EMJESGSMuNu010,EMJESGSMuNu015,EMJESGSMuNu020,EMJESGSMuNu025,EMJESGSMuNu030,EMJESGSMuNu035,EMJESGSMuNu040,EMJESGSMuNu045,EMJESGSMuNu050,EMJESGSMuNu055,EMJESGSMuNu060,EMJESGSMuNu065,EMJESGSMuNu070,EMJESGSMuNu075,EMJESGSMuNu080,EMJESGSMuNu085,EMJESGSMuNu090,EMJESGSMuNu095,EMJESGSMuNu100,EMJESGSMuNu105,EMJESGSMuNu110"
string_corrections+=",EMJESGSMuNu000Pt4,EMJESGSMuNu005Pt4,EMJESGSMuNu010Pt4,EMJESGSMuNu015Pt4,EMJESGSMuNu020Pt4,EMJESGSMuNu025Pt4,EMJESGSMuNu030Pt4,EMJESGSMuNu035Pt4,EMJESGSMuNu040Pt4,EMJESGSMuNu045Pt4,EMJESGSMuNu050Pt4,EMJESGSMuNu055Pt4,EMJESGSMuNu060Pt4,EMJESGSMuNu065Pt4,EMJESGSMuNu070Pt4,EMJESGSMuNu075Pt4,EMJESGSMuNu080Pt4,EMJESGSMuNu085Pt4,EMJESGSMuNu090Pt4,EMJESGSMuNu095Pt4,EMJESGSMuNu100Pt4,EMJESGSMuNu105Pt4,EMJESGSMuNu110Pt4"

#string_corrections="EMJESGSMuPt4"


list_corrections=string_corrections.split(",")
