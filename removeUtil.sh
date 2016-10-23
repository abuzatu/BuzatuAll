#!/bin/bash
if [ $# -ne 1 ]; then
    cat<<EOF
Usage: $0 do   
Usage: $0 1 
Usage: $0 0 
EOF
    exit 1
fi

do_command=$1

source packages.sh

echo "${ARRAY_PACKAGE[@]}"

for elementpackage in "${ARRAY_PACKAGE[@]}" ;
do
echo " "
KEY="${elementpackage%%:*}"
VALUE="${elementpackage##*:}"
#printf "%s in %s.\n" "$KEY" "$VALUE"
PACKAGE=${KEY}
PACKAGETAG=${VALUE}
COMMAND="svn remove ${SVNUSR}/${PACKAGE}/trunk/util -m \"Remove Util folder from all packages. Will use that from BuzatuAll.\""
echo ${COMMAND}

echo ${COMMAND} > ${RUN}
if [ ${do_command} == 1 ]; then
    echo "Doing it"
    source ${RUN}
else
    echo "Not doing it, it was just printing for testing"
fi

done
