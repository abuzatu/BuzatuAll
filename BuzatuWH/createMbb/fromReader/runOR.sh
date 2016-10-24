INPUT_PATH="${HOME}/data/Reader/160323_1"
list_OPTIONS="0,1+0,2+0,3+0,4+0,5+0,6+0,7+0,8+0,9+0,10+9,10"
#list_OPTIONS="9,10"
VARIABLES="mBB,pTB1,pTB2,EtaB1,EtaB2,pTL1,pTL2,pTM1,pTM2,pTE1,pTE2,EtaL1,EtaL2,EtaM1,EtaM2,EtaE1,EtaE2"
#VARIABLES="mBB"
DEBUG="0"

#OUTPUT_STEM="${HOME}/public_html/OR/forHbb/160325_3" # Glasgow
OUTPUT_STEM="${HOME}/data/histos_OR_fromReader/forHbb/160326_mBB" # Mac

for OPTIONS in `echo "${list_OPTIONS}" | awk -v RS=+ '{print}'`
do
    echo ${OPTIONS}
    FOLDER="${OUTPUT_STEM}_${OPTIONS}"
    CURRENT="OR_SimpleMerge500"
    rm -rf ${CURRENT}
    mkdir -p ${CURRENT}/plots
    ./overlayOR.py ${INPUT_PATH} ${OPTIONS} ${VARIABLES} ${OUTPUT_STEM} ${DEBUG}
    mkdir -p ${FOLDER}
    rm -rf ${FOLDER}/${CURRENT}
    cp -r ${CURRENT} ${FOLDER}/.
    $All/BuzatuBash/make_html.sh ${FOLDER}/${CURRENT}/plots
done
