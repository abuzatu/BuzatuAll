Type="Response"
Folder="${outputroot}/local/histo_PerJet${Type}/readPaul_1_0_2BTag+TruthGENWZ_1_perjet"
XAxisScaleName="GENWZ"
Variables="mean,rms,rmsovermean"
#Scales="EM,EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
#Scales="EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
#Scales="EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
#Scales="EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
#Scales="EMJES,EMJESGS"
#Scales="EMJESGS,EMJESGSMu"
#Scales="EMJESGSMu,EMJESGSMuPt"
#Scales="EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
#Scales="EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
Scales="EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3"
EventSelections="All,0Muon,1Muon"
Debug=0

FolderOutput="${outputroot}/local/histo_overlayHistogramPtRecoOrResponse/$(basename ${Folder})"
mkdir -p ${FolderOutput}
command="python ${BuzatuWH}/overlayHistogramPtRecoOrResponse/overlayHistogramPerProcess.py ${Folder} ${Type} ${XAxisScaleName} ${Variables} ${Scales} ${EventSelections} ${FolderOutput} ${Debug}"
echo ${command}
`echo ${command}`  


