# Usage: ./run.sh WhereToRun OutputTrees EventSelection Input AddTruth NrEventStart NrEventEnd

WhereToRun="batch"  #"batch" #"local"
QUEUE="medium6"

#$BuzatuWH/createTree/run.sh ${WhereToRun} perjet   J1Pt45+2BTag+TruthGENWZ Minimum 1 1 0 ${QUEUE}
#$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+TruthGENWZ Minimum 1 1 0 ${QUEUE}

$BuzatuWH/createTree/run.sh ${WhereToRun} perjet   J1Pt45+2BTag+PtV200inf+TruthGENWZ AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+PtV200inf+TruthGENWZ AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perjet   J1Pt45+2BTag+TruthGENWZ AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+TruthGENWZ AllWithMJ 1 1 0 ${QUEUE}


#$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+TruthGENWZ Test 1 1 1000 ${QUEUE}
