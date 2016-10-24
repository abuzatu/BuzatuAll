# Usage: ./run.sh WhereToRun OutputTrees EventSelection Input AddTruth NrEventStart NrEventEnd QUEUE

WhereToRun="batch"
QUEUE="medium6"

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+0BTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
