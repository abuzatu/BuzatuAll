#!/bin/bash

if [ $# -ne 2 ]; then
cat <<EOF
Usage: $0 testHelloWorld testReadFromFile
EOF
exit 1
fi

Old=$1
New=$2

echo "Old=${Old}"
echo "New=${New}"

cp -r ${Old} ${New}
rm -rf ${New}/.svn
mv ${New}/${Old}.h ${New}/${New}.h
mv ${New}/${Old}.cxx ${New}/${New}.cxx
cat ${New}/${New}.cxx | sed -e 's/'${Old}'/'${New}'/g' > temp  && mv temp ${New}/${New}.cxx
cat ${New}/${New}.h | sed -e 's/'${Old}'/'${New}'/g' > temp && mv temp ${New}/${New}.h
