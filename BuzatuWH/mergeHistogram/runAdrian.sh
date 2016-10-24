InputFolders="${outputroot}/batch/histo_PerEvent_batch/readPaul_1_0_J1Pt45+2BTag+PtV200inf+TruthGENWZ_1_perevent"
#InputFolders="${outputroot}/batch/histo_PerEvent_batch/readPaul_1_500000_J1Pt45+2BTag+TruthGENWZ_1_perevent"
#InputFolders="${outputroot}/batch/histo_PerEvent_batch/readPaul_1_2000000_J1Pt45+2BTag+TruthGENWZ_1_perevent"
#InputFolders="${outputroot}/batch/histo_PerEvent_batch/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perevent"
#InputFolders="${outputroot}/local/histo_PerEvent_batch/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perevent"
Suffix="_1_0" #"_1_1000"  #"_1_0"
EventSelections="All,0Muon,1Muon,2Muon"
#EventSelections="1Muon"
#EventSelections="GENWZ,GENWZ_0Muon,GENWZ_1Muon,GENWZ_2Muon"
#EventSelections="All,GENWZ"
#EventSelections="All"
#EventSelections="2L,2M,2T"
ApplyEventWeights="1" # "1,0"
Quantity="M"
Object="j1j2"
#NewXs="r-0.5-2.0-0.02"
#NewXs+=",v-0.0-300.0-4.0"
NewXs+=",v-0.0-300.0-10.0"
Debug=0

for InputFolder in `echo "${InputFolders}" | awk -v RS=, '{print}'`
do
    FolderOutput="${outputroot}/local/histo_merged/$(basename ${InputFolder})"
    mkdir -p ${FolderOutput}
    for NewX in `echo "${NewXs}" | awk -v RS=, '{print}'`
    do
	command="python ${BuzatuWH}/mergeHistogram/mergeHistogram.py ${InputFolder} ${Suffix} ${EventSelections} ${ApplyEventWeights} ${Quantity} ${Object} ${Type} ${NewX} ${FolderOutput} ${Debug}"
	echo ${command}
	`echo ${command}`  
done
done






