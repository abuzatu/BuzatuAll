Folder="${outputroot}/local/histo_PerJetPtReco/readPaul_1_0_2BTag+TruthGENWZ_1_perjet"
Debug=0

FolderOutput="${outputroot}/local/histo_overlayHistogramPtRecoOrResponse/$(basename ${Folder})"
mkdir -p ${FolderOutput}
command="python ${BuzatuWH}/overlayHistogramPtRecoOrResponse/overlayHistogram.py ${Folder} ${FolderOutput} ${Debug}"
echo ${command}
`echo ${command}`  


