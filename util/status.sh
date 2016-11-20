for FOLDER in Buzatu*; do
    echo $FOLDER
    cd $FOLDER
    git fetch
    git status
    cd ..
done
