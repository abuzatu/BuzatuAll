#!/bin/bash

FOLDER="160525_1/From-CxAOD-Elisabeth"
PROCESSes="ZHll125"
#PROCESSes="llbb" # old style
#INITIALs="OneMu,AllMu"
INITIALs="OneMu"
#TARGETs="TruthWZ,Parton"
TARGETs="Parton"
#TARGETs="TruthWZ"
NREVENTS=-1

doCreatePtReco=1
doInterpolatePtReco=0
doOverlayPtRecoDistribution=0

for PROCESS in `echo "${PROCESSes}" | awk -v RS=, '{print}'`
do
    echo "PROCESS=${PROCESS}"
    for INITIAL in `echo "${INITIALs}" | awk -v RS=, '{print}'`
    do
	echo "INITIAL=${INITIAL}"
	for TARGET in `echo "${TARGETs}" | awk -v RS=, '{print}'`
	do
	    echo "TARGET=${TARGET}"
	    #
	    COMMAND_CREATE_PTRECO="./createPtReco.py ${FOLDER} ${PROCESS} ${PROCESS} ${NREVENTS} ${INITIAL} ${TARGET}"
	    echo ${COMMAND_CREATE_PTRECO}
	    if [ ${doCreatePtReco} == 1 ]; then
		`echo ${COMMAND_CREATE_PTRECO}`
	    fi
	    #
	    COMMAND_INTERPOLATE_PTRECO="./interpolatePtReco.py ${PROCESS} ${INITIAL} ${TARGET}"
	    echo ${COMMAND_INTERPOLATE_PTRECO}
	    if [ ${doInterpolatePtReco} == 1 ]; then
		`echo ${COMMAND_INTERPOLATE_PTRECO}`
	    fi
	    #
	    COMMAND_OVERLAY_PTRECO_DISTRIBUTION="./overlayPtRecoDistribution.py ${PROCESS} ${INITIAL} ${TARGET}"
	    echo ${COMMAND_OVERLAY_PTRECO_DISTRIBUTION}
	    if [ ${doOverlayPtRecoDistribution} == 1 ]; then
		`echo ${COMMAND_OVERLAY_PTRECO_DISTRIBUTION}`
	    fi
	done
    done
done
