# Usage: ./run.sh WhereToRun OutputTrees EventSelection Input AddTruth NrEventStart NrEventEnd QUEUE

WhereToRun="batch"
QUEUE="medium6"

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+0BTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+0BTag+TruthGENWZ+LepMu AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+0BTag+TruthGENWZ+LepAll AllWithMJ 1 1 0 ${QUEUE}

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+1BTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+1BTag+TruthGENWZ+LepMu AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+1BTag+TruthGENWZ+LepAll AllWithMJ 1 1 0 ${QUEUE}

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+TruthGENWZ+LepMu AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2BTag+TruthGENWZ+LepAll AllWithMJ 1 1 0 ${QUEUE}

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2LBTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2LBTag+TruthGENWZ+LepMu AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2LBTag+TruthGENWZ+LepAll AllWithMJ 1 1 0 ${QUEUE}

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2MBTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2MBTag+TruthGENWZ+LepMu AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2MBTag+TruthGENWZ+LepAll AllWithMJ 1 1 0 ${QUEUE}

$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2TBTag+TruthGENWZ+LepEl AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2TBTag+TruthGENWZ+LepMu AllWithMJ 1 1 0 ${QUEUE}
$BuzatuWH/createTree/run.sh ${WhereToRun} perevent J1Pt45+2TBTag+TruthGENWZ+LepAll AllWithMJ 1 1 0 ${QUEUE}
