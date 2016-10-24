Folders="${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perevent"
Prefixes="GENWZ_1"
#Suffixes="M-j1j2_v_0_300_4"
Suffixes+=",M-j1j2_r_50_200_2"
Debug=0

for Folder in `echo "${Folders}" | awk -v RS=, '{print}'`
do
    for Prefix in `echo "${Prefixes}" | awk -v RS=, '{print}'`
    do
	for Suffix in `echo "${Suffixes}" | awk -v RS=, '{print}'`
	do
	    FolderOutput="${outputroot}/local/histo_overlay/$(basename ${Folder})"
	    mkdir -p ${FolderOutput}
	    command="python ${BuzatuWH}/overlayHistogram/overlayHistogram.py ${Folder} ${Prefix} ${Suffix} ${FolderOutput} ${Debug}"
	    echo ${command}
	    `echo ${command}`  
	done
    done
done

