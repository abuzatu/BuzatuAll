Type="Response"
Folder="${outputroot}/local/histo_PerJet${Type}/readPaul_1_0_2BTag+TruthGENWZ_1_perjet"
XAxisScaleName="GENWZ"
Scales="EM,EMJES"
EventSelections="All,0Muon,1Muon"
Debug=1

FolderOutput="${outputroot}/local/histo_overlayHistogramPtRecoOrResponse/$(basename ${Folder})"
mkdir -p ${FolderOutput}
command="python ${BuzatuWH}/overlayHistogramPtRecoOrResponse/overlayHistogram.py ${Folder} ${Type} ${XAxisScaleName} ${Scales} ${EventSelections} ${FolderOutput} ${Debug}"
echo ${command}
`echo ${command}`  


