Folders="${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent"
Prefix="GENWZ_1"
Histogram="M_EMJESGSMuPt_j1j2_v_0_300_4"
Debug=0

for Folder in `echo "${Folders}" | awk -v RS=, '{print}'`
do
    FolderOutput="${outputroot}/local/yield/$(basename ${Folder})"
    mkdir -p ${FolderOutput}
    command="python ${BuzatuWH}/computeYield/computeYield.py ${Folder} ${Prefix} ${Histogram} ${FolderOutput} ${Debug}"
    echo ${command}
    `echo ${command}`  
done






