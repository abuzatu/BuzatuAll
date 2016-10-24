# !/usr/bin/python
# Adrian Buzatu (adrian.buzatu@glasgow.ac.uk)
# 28 Jan 2015, Python functions to configure the NNs

# functions that deal with the NNs
from NeuralNetwork import *

#########################################################################################
#### get the file used in the NN training                                            ####
#########################################################################################

def get_file_NN_training_perjet(debug):
    # define the file we want to use in training
    path=os.environ['outputroot']
    if debug:
        print "path",path
    #result=path+"/local/merged_for_NN/merged_perjet_14090.root"
    #result=path+"/local/150203_1/readPaul_1_0_2BTag+TruthGENWZ+Clean_1_perevent+perjet/lvbb125.root"
    #result=path+"/local/NN/lvbb125.root"
    result=path+"/local/readPaul_1_30000_J1Pt45+2BTag+TruthGENWZ+Clean_1_perevent+perjet/lvbb125.root"
    #result="/afs/phas.gla.ac.uk/user/a/abuzatu/public_ppe/WH/BuzatuWH/runPython/NeuralNetwork/lvbb125.root"
    # check if the file needed for NN training exists
    if not os.path.isfile(result):
        print "file",result,"needed for NN training does not exist. WILL ABORT!"
        result=None
    # now ready to return
    return result
# done function

def get_file_NN_training_perevent(debug):
    # define the file we want to use in training
    path=os.environ['outputroot']
    if debug:
        print "path",path
    #result=path+"/local/150129/readPaul_1_0_2BTag+TruthGENWZ_1_perevent/lvbb125.root"
    #result=path+"/local/merged_for_NN/merged_perevent_7040.root"
    #result=path+"/local/merged_for_NN_2/merged_perevent_7044.root"
    #result=path+"/local/NN/lvbb125.root"
    result=path+"/local/readPaul_1_30000_J1Pt45+2BTag+TruthGENWZ+Clean_1_perevent+perjet/lvbb125.root"
    # check if the file needed for NN training exists
    if not os.path.isfile(result):
        print "file",result,"needed for NN training does not exist. WILL ABORT!"
        result=None
    # now ready to return
    return result
# done function

def get_list_NN_A1():
    debug=True
    initial_number=100
    random_number_variations=1
    # ex: neuron_activation_functions=["Sigmoid","Tanh","Gauss","Linear"]
    neuron_activation_functions=["Sigmoid"]
    # ex: learning_methods=["Stochastic","Batch","SteepestDescent","RibierePolak","FletcherReeves","BFGS"]
    learning_methods=["BFGS"]
    # NN structure, do not use BWeight, EMF and SvpM
    input_layers=[]
    #input_layers.append("EMJESGSCMuPt3_Pt,SumPtTrk,SumPtTrk_EMJESGSCMuPt3_Pt,JVF,EMF,hasMuon,MuEffectPt,hasSV,SVLxy,SVLxyErr,SVLxySig,NTrk,TrkWidth,FracEM3,FracTile0")
    input_layers.append("EMJESGSCMuPt3_Pt,SumPtTrk,SumPtTrk_EMJESGSCMuPt3_Pt,JVF,SVLxy,SVLxyErr,SVLxySig")
    output_layers=[]
    # ex: output_layers.append("GENWZ_EMJESGSCMuPt3_E")
    output_layers.append("GENWZ_EMJESGSCMuPt3_Pt")
    hidden_layers="" # ":3:
    dict_tree_epoch={}
    dict_tree_epoch["perjet"]=100
    use_defaults_if_wrong_values=True
    # get the fileName hard coded in the function below (described above)
    fileName=get_file_NN_training_perjet(debug)
    result=get_list_NN(initial_number,random_number_variations,neuron_activation_functions,learning_methods,
                       input_layers,output_layers,hidden_layers,dict_tree_epoch, use_defaults_if_wrong_values, 
                       fileName,debug)
    # done
    return result
# done definition function


def get_list_NN_B1():
    debug=True
    initial_number=200
    random_number_variations=1
    # ex: neuron_activation_functions=["Sigmoid","Tanh","Gauss","Linear"]
    neuron_activation_functions=["Sigmoid"]
    # ex: learning_methods=["Stochastic","Batch","SteepestDescent","RibierePolak","FletcherReeves","BFGS"]
    learning_methods=["BFGS"]
    # NN structure, do not use BWeight, EMF and SvpM
    input_layers=[]
    #input_layers.append("j1_EMJESGSCMuPt3_Pt,j2_EMJESGSCMuPt3_Pt,j1_SumPtTrk,j2_SumPtTrk,j1_SVLxy,j2_SVLxy,j1_MuEffectPt,j2_MuEffectPt,j1j2_EMJESGSC_dR,j1j2_EMJESGSCMuPt3_Pt")
    input_layers.append("j1_EMJESGSCMuPt3_Pt,j2_EMJESGSCMuPt3_Pt,j1j2_EMJESGSC_dR,j1j2_EMJESGSCMuPt3_Pt")
    output_layers=[]
    # ex: output_layers.append("GENWZ_EMJESGSCMuPt3_E")
    output_layers.append("j1_GENWZ_EMJESGSCMuPt3_Pt,j2_GENWZ_EMJESGSCMuPt3_Pt")
    hidden_layers="" # "" or ":3:"
    dict_tree_epoch={}
    dict_tree_epoch["perevent"]=100
    use_defaults_if_wrong_values=True
    # get the fileName hard coded in the function below (described above)
    fileName=get_file_NN_training_perevent(debug)
    result=get_list_NN(initial_number,random_number_variations,neuron_activation_functions,learning_methods,
                       input_layers,output_layers,hidden_layers,dict_tree_epoch, use_defaults_if_wrong_values, 
                       fileName,debug)
    # done
    return result
# done definition function

#########################################################################################
#### get the final (all) list we will use                                            ####
#########################################################################################

def get_list_NN_all(name):
    # ex: result=get_list_NN_1()+get_list_NN_2()
    # ex: #list_names_to_reject="n100,n102".split(",")
    # ex: result=get_sublist_NN_to_reject(get_list_NN_1(),list_names_to_reject)
    # ex: list_names=[]
    # ex: for i in xrange(8513,8584): # if you want from A to B inclusive you write xrange(A,B+1) 
    # ex: list_names.append("n"+str(i))
    # ex: print "list_names",list_names
    # ex: get_sublist_NN_to_keep(result,list_names)
    if name=="A1":
        result=get_list_NN_A1()
    elif name=="B1":
        result=get_list_NN_B1()
    else:
        print "Name",name,"not known. Will ABORT!"
        assert(False)
    #result=get_list_NN_B()
    #result=get_list_NN_C()
    #result=get_list_NN_A()+get_list_NN_B()
    # done
    return result
# done definition function

