Folders="${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag_1_perevent"
#Folders+=",${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perevent"
HistogramPrefix="M"
#HistogramSuffixes="j1j2_All_1_100_160_4"
HistogramSuffixes="j1j2_All_1_0_300_4"
#HistogramSuffixes="j1j2_All_1_0_300_5"
#HistogramSuffixes="j1j2_All_1_100_150_5"
#HistogramSuffixes+=",j1j2_100_150_1"
#HistogramSuffixes+=",j1j2_0_500_25"
Debug=0

for Folder in `echo "${Folders}" | awk -v RS=, '{print}'`
do
    for HistogramSuffix in `echo "${HistogramSuffixes}" | awk -v RS=, '{print}'`
    do
	FolderOutput="${outputroot}/local/histo_fit/$(basename ${Folder})"
	mkdir -p ${FolderOutput}
	command="python ${BuzatuWH}/fitHistogram/fitHistogram.py ${Folder} ${HistogramPrefix} ${HistogramSuffix} ${FolderOutput} ${Debug}"
	echo ${command}
	`echo ${command}`  
    done
done

