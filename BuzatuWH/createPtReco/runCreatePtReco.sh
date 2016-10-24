#./createPtReco.py 160525_1/From-CxAOD-Elisabeth ZHll125   ZHll125      -1        OneMu   Parton 
#./overlayPtReco.py ZHll125 OneMu Parton inclusive Bukin,None,Gauss,GaussMedian,BukinMedian

#./createPtReco.py 160525_1/From-CxAOD-Moriond ZHll125   ZHll125      -1        OneMu   Parton False,True
#./createPtReco.py 160525_1/From-CxAOD-Moriond ZHll125   ZHll125      -1        OneMu   Parton True
#./overlayPtReco.py ZHll125 OneMu Parton inclusive Bukin True
#./overlayPtReco.py ZHll125 OneMu Parton inclusive Bukin False,True
#./overlayPtReco.py ZHll125 OneMu Parton inclusive Bukin,None,Gauss,GaussMedian,BukinMedian True
#./overlayPtReco.py ZHll125 OneMu Parton hadronic Bukin,None,Gauss,GaussMedian,BukinMedian True
#./overlayPtReco.py ZHll125 OneMu Parton muon Bukin,None,Gauss,GaussMedian,BukinMedian True
#./overlayPtReco.py ZHll125 OneMu Parton electron Bukin,None,Gauss,GaussMedian,BukinMedian True
#./overlayPtReco.py ZHll125 OneMu Parton inclusive,hadronic,muon,electron Bukin True
#./overlayPtReco.py ZHll125 OneMu Parton inclusive Bukin True,False
#./overlayPtReco.py ZHll125 OneMu Parton hadronic Bukin True,False
#./overlayPtReco.py ZHll125 OneMu Parton muon Bukin True,False
#./overlayPtReco.py ZHll125 OneMu Parton electron Bukin True,False

#nrEvents=-1
#./createPtReco.py 160603_1 llbb llbb      ${nrEvents}       OneMu   Parton,TruthWZ True,False
#nrEvents=-1
#./createPtReco.py      llbb    ${nrEvents}       OneMu   Parton,TruthWZ True,False 0
#./interpolatePtReco.py llbb                      OneMu   Parton,TruthWZ True,False

nrEvents=-1
#./createPtReco.py      ggA400ToZH250    ${nrEvents}       OneMu   TruthWZ True 0
#./createPtReco.py      ggA600ToZH400    ${nrEvents}       OneMu   TruthWZ True 0
#./createPtReco.py      ggA800ToZH500    ${nrEvents}       OneMu   TruthWZ True 0

#./interpolatePtReco.py  ggA800ToZH500                    OneMu   TruthWZ True
#./interpolatePtReco.py  llbb                    OneMu   TruthWZ True

FOLDER_INPUT="161009_4_CxAOD_24-7"
PROCESS="llcc"
NREVENTS=-1
FOLDER_OUTPUT="161010_2"
DEBUG="0"
mkdir -p ~/data/histos_PtReco/${FOLDER_OUTPUT}
./createPtReco.py ${FOLDER_INPUT} ${PROCESS} ${NREVENTS} OneMu TruthWZ True ${FOLDER_OUTPUT} ${DEBUG}
