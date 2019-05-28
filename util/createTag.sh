#!/bin/bash

if [ $# -ne 2 ]; then
cat <<EOF
Usage: $0 TAG    TEXT
Usage: $0 r01-01 "28May2018, after I left at 28 Feb 2018 my ATLAS postdoc"
EOF
exit 1
fi 

TAG=$1
TEXT=$2

for d in Buzatu*; do
    if [ -d "${d}" ]; then
        echo "${d}"   # your processing here
	if [ "${d}" == "BuzatuProceedingICHEP2016" ]; then
	    continue
	fi
	#continue
	cd $d
	pwd
	git branch -a
	git log | head
	git tag -a ${TAG} -m "${TEXT}"
	git tag -l | head
	git show ${TAG} | head
	git push origin ${TAG}	
	cd ..
    fi 
    #git submodule add ./$d
done
