WhereToRun="batch" # "batch" # "local"
QUEUE="long5"
Input="AllWithMJ" #"Test" #"AllWithMJ" #"Minimum"
NrEventStart=1
NrEventEnd=0
#InputFolders="batch/readPaul_1_500000_J1Pt45+2BTag+TruthGENWZ_1_perevent"
#InputFolders="batch/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perevent"
InputFolders="batch/readPaul_1_0_J1Pt45+2BTag+PtV200inf+TruthGENWZ_1_perevent"
InputTree="perevent"
EventSelections="All"
EventSelections+=",0Muon"
EventSelections+=",1Muon"
EventSelections+=",2Muon"
#EventSelections+="1Muon,2Muon"
#EventSelections+=",GENWZ_2L"
#EventSelections+=",GENWZ_2L_0Muon"
#EventSelections+=",GENWZ_2L_1Muon"
#EventSelections+=",GENWZ_2L_2Muon"
#EventSelections+=",GENWZ_2M"
#EventSelections+=",GENWZ_2M_0Muon"
#EventSelections+=",GENWZ_2M_1Muon"
#EventSelections+=",GENWZ_2M_2Muon"
#EventSelections+=",GENWZ_2T"
#EventSelections+=",GENWZ_2T_0Muon"
#EventSelections+=",GENWZ_2T_1Muon"
#EventSelections+=",GENWZ_2T_2Muon"
ApplyEventWeights="1" #"1,0"
Option="PerEvent"
Debug=0


for InputFolder in `echo "${InputFolders}" | awk -v RS=, '{print}'`
do
    echo "InputFolder=${InputFolder}"
    command="${BuzatuWH}/createHistogram/run.sh ${WhereToRun} ${Input} ${NrEventStart} ${NrEventEnd} ${InputFolder} ${InputTree} ${EventSelections} ${ApplyEventWeights} ${Option} ${Debug} ${QUEUE}"
    echo ${command}
    `echo ${command}`  
done
