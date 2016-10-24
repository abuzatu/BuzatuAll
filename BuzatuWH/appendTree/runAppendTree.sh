# for test
#DEBUG=1
#PROCESSes="llbb"
#NR_ENTRIES=100
# for run
#DEBUG=0
#PROCESSes="llbb"
#NR_ENTRIES=-1
#PROCESSes="llbb,ttbar,STopS,STopT,STopWt,ZqqZll,Zee,Zmumu,ZeeMG,ZmumuMG"
#PROCESSes="ZqqZll,WqqZll,ZeeMG,ZmumuMG,STopWt,llbb"
#NR_ENTRIES=111000
#PROCESSes="ttbar"
#NR_ENTRIES=50000
#DEBUG=1
#PROCESSes="ggA800ToZH500"
#NR_ENTRIES=-1
DEBUG=0
#PROCESSes="llcc"
PROCESSes="llbbctag"
NR_ENTRIES=-1

#
for PROCESS in `echo "${PROCESSes}" | awk -v RS=, '{print}'`
do
    echo "PROCESS=${PROCESS}"   
    ./appendTree.py ${PROCESS} ${NR_ENTRIES} ${DEBUG}
done

