#echo $PWD
export All="${PWD}"
export ATLAS="${All}/BuzatuATLAS"
export L="${All}/BuzatuATLAS/LaTex"
export Bash="${All}/BuzatuBash"
#export CPP="${All}/BuzatuCPP"
#export Portfolio="${All}/BuzatuPortfolio"
#export Note="${All}/BuzatuNoteBJetEnergyCorrectionsRunII"
export Python="${All}/BuzatuPython"
#export Proceeding="${All}/BuzatuProceedingICHEP2016"
#export Research="${All}/BuzatuResearch"
#export RivetHbbBFatJet="${All}/BuzatuRivetHbbBFatJet"
#export RivetHbbBJets="${All}/BuzatuRivetHbbBJets"
#export ROOT="${All}/BuzatuROOT"
#export Teaching="${All}/BuzatuTeaching"
#export Tree="${All}/BuzatuTree"
export VH="${All}/BuzatuVH"
export LD_LIBRARY_PATH="${Tree}/lib:${LD_LIBRARY_PATH}"
export PYTHONPATH=${Python}:$PYTHONPATH
test_login_shell=$(shopt | grep login_shell)
test_login_shell_result=`echo ${test_login_shell} | cut -d" " -f2`

if [ ${test_login_shell_result} == "on" ]; then
    echo 'Login shell'
    echo "New LD_LIBRARY_PATH=${LD_LIBRARY_PATH}"
    echo "New PYTHONPATH=${PYTHONPATH}"
else 
    :
    #echo 'Not login shell' but it would not continue to do a scp if we use echo
fi

