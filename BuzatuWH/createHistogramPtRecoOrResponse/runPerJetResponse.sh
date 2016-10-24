InputFolder="${outputroot}/local/histo_PerJet_batch/readPaul_1_0_2BTag+TruthGENWZ_1_perjet"
Input="Minimum"
InputList="${BuzatuWH}/config/input${Input}.list" # or input.list or inputWithMJ.list or inputTest.list or inputMinimum.list
echo "InputList=${InputList}"
Suffix="_1_0"
EventSelections="All"
EventSelections+=",0Muon"
EventSelections+=",1Muon"
#EventSelections+=",2T"
#EventSelections+=",2T_0Muon"
#EventSelections+=",2T_1Muon"
ApplyEventWeights="1" #"1,0"
Fits="None" # "None,Gauss,Bukin"
Quantities="mean,rms,meanwithrms,rmsovermean"
PhysicsMeaning="r"
Corrections="EM,EMJES,EMJESGS,EMJESGSMu,EMJESGSMuPt,EMJESGSMuPt3,EMJESGSMuPt3NNJ1"
ListAllBins="Type_lep-1.5-C"
ListAllBins+="+PtV-90,120,160,200-C"
ListAllBins+="+Pt_GENWZ-20,30,40,50,60,70,80,100,120,140,160,180,200,240,280-A"
Option="PerJetResponse"
Debug=0

COUNTER=0
while IFS=$'\ ' read -r -a myArray
do
    Process=${myArray[0]}
    File=${myArray[1]}
    Tree=${myArray[2]}

    Initial="$(echo ${Process} | head -c 1)"
    # echo "File=${File} Initial=${Initial}"
    if [ ${Initial} == "#" ]; then
       continue
    fi

    let COUNTER+=1
    echo "***************************************************************************************"
    echo "*************** Start ${COUNTER}: process=${Process} **********************************"
    echo "***************************************************************************************"

    echo "InputFolder=${InputFolder}"
    FolderOutput="${outputroot}/local/histo_${Option}/$(basename ${InputFolder})"
    mkdir -p ${FolderOutput}
    command="python ${BuzatuWH}/createHistogramPtRecoOrResponse/create.py ${InputFolder} ${Process} ${Suffix} ${EventSelections} ${ApplyEventWeights} ${Fits} ${Quantities} ${PhysicsMeaning} ${Corrections} ${ListAllBins} ${FolderOutput} ${Debug}"
    echo ${command}
    `echo ${command}`

done < ${InputList}
# end looping over the trees
