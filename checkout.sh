#!/bin/bash
#Adrian 19 Sept 2014
#Commit a tag version to SVN

if [ $# -ne 2 ]; then
    cat<<EOF
Usage: $0 trunk checkout   
Usage: $0 1     0 
Usage: $0 0     0 
Usage: $0 1     1 
Usage: $0 0     1 
EOF
    exit 1
fi

trunk=$1
checkout=$2

source packages.sh

echo "${ARRAY_PACKAGE[@]}"

#exit

for elementpackage in "${ARRAY_PACKAGE[@]}" ;
do
echo " "
KEY="${elementpackage%%:*}"
VALUE="${elementpackage##*:}"
#printf "%s in %s.\n" "$KEY" "$VALUE"
PACKAGE=${KEY}
if [ $trunk = 1 ]; then
    PACKAGETAG="trunk"
else
    PACKAGETAG=${VALUE}
fi
echo "${PACKAGE} Tag=${PACKAGETAG}"
COMMAND="svn co ${SVNUSR}/${PACKAGE}/${PACKAGETAG} ${PACKAGE}"
echo ${COMMAND}
if [ $checkout = 1 ]; then
    `echo ${COMMAND}`
fi
done
