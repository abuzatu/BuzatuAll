#!/bin/sh
#if there is no parameter, it stops and it gives the instructions
if [ $# -ne 0 ]; then
cat <<EOF
Usage: $0 
EOF
exit 1
fi

#PACKAGEes="BuzatuROOT,BuzatuResearch,BuzatuRivetHbbBFatJet,BuzatuRivetHbbBJets,BuzatuTTbarDilepton,BuzatuTree"
PACKAGEes="BuzatuTeachingPortofolio,BuzatuWH"
SVNPATH="/Users/abuzatu/Work/ATLAS/Analyses/fromSVN/BuzatuAll"
GITPATH="/Users/abuzatu/Work/ATLAS/Analyses/BuzatuAll"

for PACKAGE in `echo "${PACKAGEes}" | awk -v RS=, '{print}'`
do
    echo $PACKAGE
    cd ${SVNPATH}/${PACKAGE}
    rm -rf .svn
    rm -rf .DS_Store
    rm -rf *.aux
    rm -rf *.toc
    rm -rf *.out
    rm -rf *.log
    rm -rf *.blg
    rm -rf *.bbl
    rm -rf \#*
    rm -rf *~
    cp -r * ${GITPATH}/${PACKAGE}/.
    cd ${GITPATH}/${PACKAGE}
    git status
    git add .
    git status
    git commit -m "First version from SVN"
    git status
    #git push origin master
    #cd ${GITPATH}
done

exit

