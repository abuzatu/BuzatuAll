#PROCESSes="llbb,ttbar,vvbb"
#PROCESSes="llbb"
#PROCESSes="llbb,ZqqZll,WqqZll"
#PROCESSes="llbb,ZqqZll"
#PROCESSes="ttbar"
#PROCESSes="llbb,Zee,Zmumu,ZqqZll,ttbar"
#PROCESSes="llbb,ttbar,STopS,STopT,STopWt,ZqqZll,Zee,Zmumu,ZeeMG,ZmumuMG"
#PROCESSes="llbb,ttbar,STopWt,ZqqZll,ZeeMG,ZmumuMG"
#PROCESSes="ttbar"
#PROCESSes="ggA400ToZH250"
#PROCESSes="ggA400ToZH250,ggA600ToZH400,ggA800ToZH500"
#PROCESSes="ggA800ToZH500"
FOLDER="161010_1"
PROCESSes="llcc"
OPTIONS="inclusive,2hadronic,1hadronic1semileptonic,2semileptonic"
#OPTIONS="inclusive"
DEBUG=0
for PROCESS in `echo "${PROCESSes}" | awk -v RS=, '{print}'`
do
    echo "PROCESS=${PROCESS}"   
    ./overlayHisto.py ${FOLDER} ${PROCESS} ${OPTIONS} ${DEBUG}
done
$All/BuzatuBash/make_html.sh ~/data/histos_mbb/${FOLDER}/.
