#!/bin/bash
#Adrian Oct 2012
#make a tarball and copy it on my public space

if [ $# -ne 0 ]; then
    cat<<EOF
Usage: $0  
Usage: $0 
EOF
    exit 1
fi

PACKAGE=$(basename $PWD)
echo ${PACKAGE}
#exit

mkdir -p ../temp
cd ../temp

if [[ -d ${PACKAGE} ]]; then
    echo "${PACKAGE} exists, so we remove it"
    rm -rf ${PACKAGE}
fi
if [[ -f ${PACKAGE}.tgz ]]; then
    echo "${PACKAGE}.tgz exists, so we remove it"
    rm -f ${PACKAGE}.tgz
fi
mkdir -p ${PACKAGE}
# copy the folders
cp -r ../${PACKAGE}/* ${PACKAGE}
# uncompile
make clean -C ${PACKAGE}
# for each folder we remove the .svn inside
for dir in ${PACKAGE}/*/
do
    dir=${dir%*/}
    folder=${dir##*/}
    echo ${folder}
    rm -rf ${folder}/.svn
done
# now ready to tar it
tar cvzf ${PACKAGE}.tgz ${PACKAGE}
rm -rf ${PACKAGE}
mv ${PACKAGE}.tgz ../.
cd ..
rm -rf temp
scp ${PACKAGE}.tgz ppelogin1.ppe.gla.ac.uk:~/public_html/BuzatuCode/.
rm -f ${PACKAGE}.tgz
cd ${PACKAGE}
