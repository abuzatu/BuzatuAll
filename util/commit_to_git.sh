#!/bin/sh
#if there is no parameter, it stops and it gives the instructions
if [ $# -ne 0 ]; then
cat <<EOF
Usage: $0 
EOF
exit 1
fi

PACKAGEes="BuzatuNoteATLASTemplate"
SVNPATH="/Users/abuzatu/Work/ATLAS/Analyses/fromSVN/BuzatuAll/"

for PACKAGE in `echo "${PACKAGEes}" | awk -v RS=, '{print}'`
do
    echo $PACKAGE
    #cd $PACKAGE
    #pushd ${SVNPATH}/${PACKAGE}
    #rm -rf .svn
    #rm -rf DS_Store
    #popd
    #cp -r pushd ${SVNPATH}/${PACKAGE}/* .
    git add .
    git commit -m "First version from SVN"
    git push origin master
    #cd ..
done

exit

