rm -f *~
rm -f \#*
rm -f ./util/*~
rm -f *.tgz
#for each folder in our package, remove the *~ files
for dir in ./*/
do
    dir=${dir%*/}
    folder=${dir##*/}
    echo $folder
    rm -f $folder/*~
done
# end for loop
