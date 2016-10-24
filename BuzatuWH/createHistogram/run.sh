#! /bin/bash
#if there is no parameter, it stops and it gives the instructions
if [ $# -ne 11 ]; then
cat <<EOF
You should pass one argument, and passed one as output trees. 
Run for example:
Usage: ./run.sh WhereToRun Input NrEventStart NrEventEnd InputFolder InputTree EventSelections ApplyEventWeights Option Debug QUEUE
Usage: ./run.sh local Test 1 100 readPaul_1_300_J1Pt45+2BTag+TruthGENWZ_1_perevent perevent All+GENWZ 1+0 PerJetPtReco 0 medium6

EOF
exit 1
fi

WhereToRun=${1}
echo "WhereToRun=${WhereToRun}"
Input=${2}
echo "Input=${Input}"
NrEventStart=${3}
echo "NrEventStart=${NrEventStart}"
NrEventEnd=${4}
echo "NrEventEnd=${NrEventEnd}"
InputFolderShort=${5}
echo "InputFolderShort=${InputFolderShort}"
InputTree=${6}
echo "InputTree=${InputTree}"
EventSelections=${7}
echo "EventSelections=${EventSelections}"
ApplyEventWeights=${8}
echo "ApplyEventWeights=${ApplyEventWeights}"
Option=${9}
echo "Option=${Option}"
Debug=${10}
echo "Debug=${Debug}"
QUEUE=${11}
echo "QUEUE=${QUEUE}"

# setup batch
source ${BuzatuWH}/config/setupBatch.sh

#
do=1
# 
InputFolder="${outputroot}/${InputFolderShort}"
echo "InputFolder=${InputFolder}"
InputList="${BuzatuWH}/config/input${Input}.list" # or input.list or inputWithMJ.list or inputTest.list or inputMinimum.list
echo "InputList=${InputList}"
OutputFolder="${outputroot}/${WhereToRun}/histo_${Option}_${InputFolderShort}"
echo "OutputFolder=${OutputFolder}"
LogFolder="${OutputFolder}/logs"
echo "LogFolder=${LogFolder}"
# create the folder if it doesn't exist
mkdir -p ${OutputFolder}
mkdir -p ${LogFolder}

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
    echo "*************** Start ${COUNTER}: process=${Process} file=${File} tree=${Tree}  *******"
    echo "***************************************************************************************"

    # 
    InputFile="${InputFolder}/${Process}"
    # OutputFile="${OutputFolder}/${Process}_${NrEventStart}_${NrEventEnd}_${EventSelections}_${ApplyEventWeights}"
    OutputFile="${OutputFolder}/${Process}_${NrEventStart}_${NrEventEnd}"
    # LogFile="${LogFolder}/run_$(basename ${OutputFile}).log"
    LogFile="${LogFolder}/run_${Process}.log"
    Command="python ${BuzatuWH}/createHistogram/createHistogram${Option}.py ${InputFile}.root ${InputTree} ${NrEventStart} ${NrEventEnd} ${EventSelections} ${ApplyEventWeights} ${OutputFile}.root ${Debug}"
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
	echo "echo LD_LIBRARY_PATH=${LD_LIBRARY_PATH}"
	# print current tree we are working on
	# echo "echo ${COUNTER}: ${File} ${Tree} ${Process};"
	# read
	if [ ${do} = 1 ]; then

	    echo "${Command} >& ${LogFile};"
	fi 
	# beep when ended
	# echo "${BuzatuTree}/util/beeper.pl;"
    ) > "${SCRIPT}"
    # print the script file 
    echo "Start cat **** ${SCRIPT} *****"
    cat ${SCRIPT}
    echo "End   cat **** ${SCRIPT} *****"

    #    
    if [ ${WhereToRun} == "local" ]; then 
	echo "running locally the script ${SCRIPT}"
	source ${SCRIPT}
    elif [ ${WhereToRun} == "batch" ]; then
	echo "running at Glasgow batch"
	JOBNAME="histo_${Process}"
	# submit the job to the PBS batch system at Glasgow
	qsub -N ${JOBNAME} -q ${QUEUE} -M ${EMAIL} -S /bin/bash ${SCRIPT}
	# check the status of the batch: 
	# qstat
	# check the status of your jobs:
	# qstat -u ${USER}
	# kill a job:
	# qdel 994535
	# kill all the jobs of a user:
	# qselect -u ${USER} | xargs qdel
    else
	echo "Not knowing where to run. You chose ${WhereToRun}, need local or batch. Will ABORT!!"
	exit
    fi 
done < ${InputList}
# end looping over the trees

# now make a sound at the end
${BuzatuWH}/util/beeper.pl



 

