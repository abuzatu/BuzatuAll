#!/bin/bash 

# forbids an interactive shell from running this executable, in other words, do not source
if [[ $- == *i* ]] ; then
    echo "ERROR: I'm a script forcing you to execute. Don't source me!" >&2
    return 1
else
    # if I am OK to execute, force that the script stops if variables are not defined
    # this catches bugs in the code when you think a variable has value, but it is empy
    set -eu
fi

# check the number of parameters, if not stop
if [ $# -ne 2 ]; then
cat <<EOF
Usage: $0 packages_file        FORCE_CHECKOUT
Usage: $0 ./util/packages.txt  0
EOF
exit 1
fi

packages_list=$1
FORCE_CHECKOUT=$2

path_prefix=ssh://git@gitlab.cern.ch:7999/abuzatu

# start loop over CxAODFramework packages
while read line
do
    #
    package=$(echo "$line" | awk '{print $1}')
    type=$(echo "$line" | awk '{print $2}')
    tag=$(echo "$line" | awk '{print $3}')
    path=$path_prefix/$package.git
    echo "package=${package} type=${type} tag=${tag} path=${path}"

    # skip Adrian's personal packages
    if [[ $USER != "abuzatu" ]] ; then
	if [[ $type != "public" ]] ; then
	    continue
	fi
    fi

    # check if the packate is already there and if we really want to check it again
    if [[  -d $package ]] ; then
        if [[ $FORCE_CHECKOUT == "1" ]] ; then
            rm -rf $package
        else
            echo "$path already checked out, so skipping it."
            continue
        fi
    fi
    #

    # Jon suggests the entire package with "git clone $path"
    COMMAND="git clone $path"
    echo "COMAND=${COMMAND}"
    ${COMMAND}
    
    # if folder does not exist, continue
    if [ ! -d "$package" ]; then
	echo "WARNING!!! package ${package} does not have a folder! We'll skip the checkout of a tag for this package!"
	continue
    fi

    # and then if we want a particular tag we do to that folder and do "git checkout tag_version"
    COMMAND="cd $package"
    echo "COMAND=${COMMAND}"
    ${COMMAND}
    # ... and do "git checkout tag_version" and ...
    COMMAND="git checkout $tag"
    echo "COMAND=${COMMAND}"
    ${COMMAND}
    # ... and to make it easier to develop, and suggest improvements to Adrian's code using the forking workflow,
    # set up the upstream to your fork depending on the username for each package of CxAOD
    #COMMAND="echo before"
    #echo "COMAND=${COMMAND}"
    #${COMMAND}
    #COMMAND="git remote -v"
    #echo "COMAND=${COMMAND}"
    #${COMMAND}
    #COMMAND="git remote add upstream ssh://git@gitlab.cern.ch:7999/${USER}/${package}.git"
    #echo "COMAND=${COMMAND}"
    #${COMMAND}
    #COMMAND="echo after"
    #echo "COMAND=${COMMAND}"
    #${COMMAND}
    #COMMAND="git remote -v"
    #echo "COMAND=${COMMAND}"
    #${COMMAND}
    # ... and return to previous folder
    #COMMAND="cd .."
    #echo "COMAND=${COMMAND}"
    #${COMMAND}
    # done all for current package
done < $packages_list
# done loop over all the packages

echo "Done the checkout of CxAOD package from GitLab!"
