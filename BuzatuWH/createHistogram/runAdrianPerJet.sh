WhereToRun="batch"  # "batch" # "local"
QUEUE="long5"
Input="AllWithMJ" #"Test" #"AllWithMJ" #"Minimum"
NrEventStart=1
NrEventEnd=0
#InputFolders="batch/readPaul_1_500000_J1Pt45+2BTag+TruthGENWZ_1_perjet"
#InputFolders="batch/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perjet"
InputFolders="batch/readPaul_1_0_J1Pt45+2BTag+PtV200inf+TruthGENWZ_1_perjet"
InputTree="perjet"
#EventSelections="All"
#EventSelections+=",0Muon"
#EventSelections+=",1Muon"
EventSelections+="1Muon"
#EventSelections+=",2T"
#EventSelections+=",2T_0Muon"
#EventSelections+=",2T_1Muon"
ApplyEventWeights="1" #"1,0"
Option="PerJet"
Debug=0


for InputFolder in `echo "${InputFolders}" | awk -v RS=, '{print}'`
do
    echo "InputFolder=${InputFolder}"
    command="${BuzatuWH}/createHistogram/run.sh ${WhereToRun} ${Input} ${NrEventStart} ${NrEventEnd} ${InputFolder} ${InputTree} ${EventSelections} ${ApplyEventWeights} ${Option} ${Debug} ${QUEUE}"
    echo ${command}
    `echo ${command}`  
done
