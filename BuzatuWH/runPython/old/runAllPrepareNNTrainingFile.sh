if [ $# -ne 2 ]; then
cat <<EOF
Usage: ./runAllPrepareNNTrainingFile.sh cleanTreeName cleanedNrEvents
Usage: ./runAllPrepareNNTrainingFile.sh perevent 100
Usage: ./runAllPrepareNNTrainingFile.sh perjet 100
EOF
exit 1
fi

cleanedTreeName=$1
cleanedNrEvents=$2

PROCESSes="WZ+lvbb100+lvbb105+lvbb110+lvbb115+lvbb120+lvbb125+lvbb130+lvbb135+lvbb140+lvbb145+lvbb150"
#PROCESSes="lvbb125"
#PROCESSes="lvbb105+lvbb110"

doClean=1
doCount=1
doThin=1
doMerge=1

EventSelection="J1Pt45+2BTag+TruthGENWZ+Clean"

initialDate="150201_4"
initialTreeName="perevent+perjet"
initialNrEvents="25000"
inputFilePath="${outputroot}/local/${initialDate}/readPaul_1_${initialNrEvents}_${EventSelection}_1_${initialTreeName}"

# clean the files for all processes
cleanedDate="150201_5"
#cleanedTreeName="perevent"
#cleanedNrEvents="100"
cleanedFilePath="${outputroot}/local/${cleanedDate}/readPaul_1_${cleanedNrEvents}_${EventSelection}_1_${cleanedTreeName}_cleaned"
if [ "${doClean}" -eq 1 ]; then
    mkdir -p ${cleanedFilePath}
    for PROCESS in `echo "${PROCESSes}" | awk -v RS=+ '{print}'`
    do
	echo "PROCESS=${PROCESS}"
	inputFileName="${inputFilePath}/${PROCESS}.root" 
	cleanedFileName="${cleanedFilePath}/${PROCESS}.root" 
	commandClean="python runCleanTree.py ${inputFileName} ${cleanedTreeName} ${cleanedNrEvents} ${cleanedFileName}"
	echo "${commandClean}"
	`echo ${commandClean}`
    done
fi


# count the minimum number of events
minNrEvents=99999999999
if [ "${doCount}" -eq 1 ]; then
    for PROCESS in `echo "${PROCESSes}" | awk -v RS=+ '{print}'`
    do
	echo "PROCESS=${PROCESS}"
	cleanedFileName="${cleanedFilePath}/${PROCESS}.root" 
	currentNrEvents=$(python runCountEventsInTree.py ${cleanedFileName} ${cleanedTreeName})
	echo "before: currentNrEvents=${currentNrEvents}, minNrEvents=${minNrEvents}"
	if [ "$minNrEvents" -ge "$currentNrEvents" ]; then
	    minNrEvents=${currentNrEvents}
	fi
	echo "after: currentNrEvents=${currentNrEvents}, minNrEvents=${minNrEvents}"
    done
    echo "minNrEvents=${minNrEvents}"
    # if odd number, remove 1 as we need even number for training
    if [ $((minNrEvents%2)) -eq 1 ]; then
	echo "odd number, so removing 1"
	minNrEvents=$[${minNrEvents}-1]
    fi
    echo "minNrEvents=${minNrEvents}"
fi

# thin the files for all processes to that number and hadd 
# to have equal contributions from all processes when training the NN
thinnedDate=${cleanedDate}
thinnedTreeName=${cleanedTreeName}
thinnedNrEvents=${minNrEvents}
thinnedFilePath="${outputroot}/local/${thinnedDate}/readPaul_1_${thinnedNrEvents}_${EventSelection}_1_${thinnedTreeName}_cleaned"
if [ "${doThin}" -eq 1 ]; then
    mkdir -p ${thinnedFilePath}
    for PROCESS in `echo "${PROCESSes}" | awk -v RS=+ '{print}'`
    do
	echo "PROCESS=${PROCESS}"
	cleanedFileName="${cleanedFilePath}/${PROCESS}.root" 
	thinnedFileName="${thinnedFilePath}/${PROCESS}.root" 
	commandThin="python runThinTree.py ${cleanedFileName} ${thinnedTreeName} ${thinnedNrEvents} ${thinnedFileName}"
	echo "${commandThin}"
	`echo ${commandThin}`
    done
fi

# thin the files for all processes to that number and hadd 
# to have equal contributions from all processes when training the NN
mergedFilePath="${outputroot}/local/${thinnedDate}"
mergedFileName=${mergedFilePath}"/merged_${thinnedTreeName}_${thinnedNrEvents}.root"
commandMerged="hadd -f ${mergedFileName} "
if [ "${doMerge}" -eq 1 ]; then
    for PROCESS in `echo "${PROCESSes}" | awk -v RS=+ '{print}'`
    do
	commandMerged+="${thinnedFileName} " 
    done
    echo "${commandMerged}"
    `echo ${commandMerged}`
fi



