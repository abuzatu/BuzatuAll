#!/bin/bash
#Adrian Oct 2012
#Commit a tag version to SVN
#computes automatically what was the latest version
#adds 1
#and commits with that
#this does not require us to check manually what was the latest tag
#also it allows us to tag automatically all the packages in BuzatuAll

if [ $# -lt 1 ]; then
    cat<<EOF
Usage: $0 do_tag comment
Usage: $0 1      bla  
Usage: $0 0      bla  
EOF
    exit 1
fi

PACKAGE=$(basename $PWD)
echo " ***** Start tagging a new version in SVN for ${PACKAGE} *******"

TEMP="temp.list"
RUN="tag.sh"
#exit

do_tag=$1
comment=$2

echo "do_tag=${do_tag}"
echo "comment=${comment}"

#exit


path="${SVNUSR}/${PACKAGE}"
trunk="${path}/trunk"
echo "trunk=${trunk}"
tags="${path}/tags"
echo "tags=${tags}"

command_list="svn ls ${tags}"
echo ${command_list}

`echo ${command_list}` | tail -1 > ${TEMP}
value=`cat ${TEMP}`
echo "value=${value}"
rm -f ${TEMP}
stem=${value:0:$(expr ${#value} - 3)}
echo "stem=${stem}"
versionslash=${value:(-3)}
echo "versionslash=${versionslash}"
version=${versionslash:0:2}
echo "version=${version}"
echo "Removing the 0 in front of number if present"
version=`echo $version | sed 's/^0*//'`
echo "version=${version}"
newversion=$((version +1))
echo "newversion=${newversion}"
if [ "${newversion}" -lt "10" ]; then
    newversionstring="0${newversion}"
else
    newversionstring="${newversion}"
fi
echo "newversionstring=${newversionstring}"
tag="${tags}/${PACKAGE}-00-00-${newversionstring}"
echo "tag=${tag}"
command_tag="svn cp ${trunk} ${tag} -m \"tag ${newversionstring} ${comment}\" "
echo ${command_tag}
echo ${command_tag} > ${RUN}
if [ ${do_tag} == 1 ]; then
    echo "Doing it"
    source ${RUN}
else
    echo "Not doing it, it was just printing for testing"
fi
rm -f ${RUN}

echo " ***** End    tagging a new version in SVN for ${PACKAGE} *******"
