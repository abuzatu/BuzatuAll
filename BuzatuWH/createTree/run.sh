#! /bin/bash
#if there is no parameter, it stops and it gives the instructions
if [ $# -ne 8 ]; then
cat <<EOF
You should pass one argument, and passed one as output trees. 
Run for example:
Usage: ./run.sh WhereToRun OutputTrees EventSelection Input AddTruth NrEventStart NrEventEnd QUEUE
Usage: ./run.sh local event+small+perevent+perjet J1Pt45+0BTag+LepEl Test 0 1 0 medium6
Usage: ./run.sh batch event+small+perevent+perjet J1Pt45+0BTag+LepEl+GENWZ Test 1 1 0 medium6

EOF
exit 1
fi

WhereToRun=$1
echo "WhereToRun=${WhereToRun}"
OutputTrees=$2
echo "OutputTrees=${OutputTrees}"
EventSelection=$3
echo "EventSelection=${EventSelection}"
Input=$4
echo "Input=${Input}"
AddTruth=$5
echo "AddTruth=${AddTruth}"
NrEventStart=$6
echo "NrEventStart=${NrEventStart}"
NrEventEnd=$7
echo "NrEventEnd=${NrEventEnd}"
QUEUE=$8
echo "QUEUE=${QUEUE}"

# setup batch
source ${BuzatuWH}/config/setupBatch.sh
#
do=1
# 
Folder="NoJ1Pt45Cut"
InputFolder=${initialroot}/${Folder}
InputList="${BuzatuWH}/config/input"${Input}".list" # or input.list or inputWithMJ.list or inputTest.list or inputMinimum.list
TreeType="Paul"
#NrEventStart=1
#NrEventEnd=0
#it comes from above
#EventSelection="J1Pt45+0BTag+LepEl" # "TruthAll+2TBTag+LepEl+J1Pt45+PtV120160"
#AddTruth=1
#OutputTrees="event+small+perevent+perjet" # event+small or event or small
OutputFolder="${outputroot}/${WhereToRun}/readPaul_${NrEventStart}_${NrEventEnd}_${EventSelection}_${AddTruth}_${OutputTrees}"
LogFolder=${OutputFolder}/logs
# create the folder if it doesn't exist
mkdir -p ${OutputFolder}
mkdir -p ${LogFolder}

COUNTER=0
while IFS=$'\ ' read -r -a myArray
do
    Process=${myArray[0]}
    File=${myArray[1]}
    Tree=${myArray[2]}
    MaxDiff=${myArray[3]}

    Initial="$(echo ${Process} | head -c 1)"
    #echo "File=${File} Initial=${Initial}"
    if [ ${Initial} == "#" ]; then
       continue
    fi

    let COUNTER+=1
    echo "***************************************************************************************"
    echo "*************** Start ${COUNTER}: process=${Process} file=${File} tree=${Tree}  ****"
    echo "****************************************************************************************"

    
    # for some processes the user may decide that even if we ask to run on large number of events
    # we still want to run on fewer than that
    # we do this only if MaxDiff the user gives is not 0, in which case we run on whatever the run.sh asks for
    if [ ! $MaxDiff -eq "0" ];then
	Diff=$((NrEventEnd - NrEventStart))
	if [ $NrEventEnd -eq "0" ] || [ $Diff -gt $MaxDiff ]; then
	    echo "Diff=${Diff} larger than MaxDiff=${MaxDiff}. So we replace NrEventEnd=${NrEventEnd} with:"
	    NrEventEnd=$(($NrEventStart + $MaxDiff -1))
	    echo "new NrEventEnd=${NrEventEnd}"
	fi
    fi

    # 
    InputFile=${InputFolder}/${File}
    OutputFile=${OutputFolder}/${Process}
    LogFile="${LogFolder}/run_$(basename ${OutputFile}).log"
    Command="${BuzatuTree}/bin/read.exe ${InputFile}.root ${Tree} ${TreeType} ${NrEventStart} ${NrEventEnd} ${EventSelection} ${AddTruth} ${OutputTrees} ${OutputFile}.root"
    # create script for the current tree to be run either locally on on the bash
    SCRIPT="${LogFolder}/script_${Process}.log"
    touch ${SCRIPT}
    # create the script that will be run
    (
        # first cd to the working folder
	echo "cd ${WH};"
        # then setup what you need
	if [ ${WhereToRun} != "local" ]; then
	    echo "source setup.sh;"
	fi	
	echo "echo LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
	# print current tree we are working on
	# echo "echo ${COUNTER}: ${File} ${Tree} ${Process};"
	# read
	if [ ${do} = 1 ]; then

	    echo "$Command >& ${LogFile};"
	fi 
	# beep when ended
	# echo "${BuzatuTree}/util/beeper.pl;"
    ) > "${SCRIPT}"
    # print the script file 
    echo "Start cat **** ${SCRIPT} *****"
    cat ${SCRIPT}
    echo "End   cat **** ${SCRIPT} *****"

    #    
    if [ $WhereToRun = "local" ]; then 
	echo "running locally the script ${SCRIPT}"
	source ${SCRIPT}
    elif [ $WhereToRun = "batch" ]; then
	echo "running at Glasgow batch"
	JOBNAME="tree_${Process}"
	# submit the job to the PBS batch system at Glasgow
	qsub -N ${JOBNAME} -q ${QUEUE} -M ${EMAIL} -S /bin/bash ${SCRIPT}
	# check the status of the batch: 
	# qstat
	# check the status of your jobs:
	# qstat -u $USER
	# kill a job:
	# qdel 994535
	# kill all the jobs of a user:
	# qselect -u $USER | xargs qdel
    else
	echo "Not knowing where to run. You chose ${WhereToRun}, need local or batch. Will ABORT!!"
	exit
    fi 
done < ${InputList}
# end looping over the trees

# now make a sound at the end
$BuzatuWH/util/beeper.pl



 

