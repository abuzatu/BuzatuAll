git pull origin master
for FOLDER in Buzatu*; do
    echo $FOLDER
    cd $FOLDER
    git pull origin master
    cd ..
done
