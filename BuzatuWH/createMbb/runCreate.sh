#PROCESSes="llbb,vvbb,ttbar"
#PROCESSes="llbb,ZqqZll,WqqZll"
#PROCESSes="llbb,ttbar,STopS,STopT,STopWt,ZqqZll,Zee,Zmumu,ZeeMG,ZmumuMG"
#PROCESSes="llbb,ttbar,STopWt,ZqqZll,ZeeMG,ZmumuMG"
#PROCESSes="STopWt"
#PROCESSes="WqqZll,ZqqZll,ZeeMG,ZmumuMG"
#PROCESSes="llbb"
#NR_EVENTS=-1
#PROCESSes="ttbar"
#NR_EVENTS=50000
#NR_EVENTS=111000
#PROCESSes="ggA400ToZH250,ggA600ToZH400,ggA800ToZH500"
#PROCESSes="ggA800ToZH500"
#INPUT_FOLDER="161009_4_CxAOD_24-7"
#PROCESSes="llcc,lvcc,vvcc"
#PROCESSes="llcc"
#PROCESSes="llbbctag"
#NR_EVENTS=-1  
#OPTIONS="inclusive,2hadronic,1hadronic1semileptonic,2semileptonic"
#OPTIONS="inclusive,2hadronic,1hadronic1semileptonic"
#OPTIONS="2semileptonic"
#OUTPUT_FOLDER="161010_4"
#DEBUG="0"

INPUT_FOLDER="161007_2_CxAOD_24_7"
PROCESSes="llbb,ttbar,ggA400ToZH250,ggA600ToZH400,ggA800ToZH500"
NR_EVENTS=-1
#OPTIONS="1hadronic1semileptonic"
OPTIONS="inclusive,2hadronic,1hadronic1semileptonic,2semileptonic"
OUTPUT_FOLDER="161014_1_AZH"
DEBUG="0"

mkdir -p ~/data/histos_mbb/${OUTPUT_FOLDER}
for PROCESS in `echo "${PROCESSes}" | awk -v RS=, '{print}'`
do
    echo "PROCESS=${PROCESS}"   
    ./createMbb.py ${INPUT_FOLDER} ${PROCESS} ${OPTIONS} ${NR_EVENTS} ${OUTPUT_FOLDER}
    #./overlayHisto.py ${OUTPUT_FOLDER} ${PROCESS} ${OPTIONS} ${DEBUG}
done
#$All/BuzatuBash/make_html.sh ~/data/histos_mbb/${OUTPUT_FOLDER}/.

#./overlayHisto.py llbb llbb Gauss
#./overlayHisto.py llbb llbb Bukin

#./overlayHisto.py vvbb_100k vvbb Gauss
#./overlayHisto.py vvbb_100k vvbb Bukin

#./overlayHisto.py ttbar ttbar Gauss
#./overlayHisto.py ttbar ttbar Bukin

