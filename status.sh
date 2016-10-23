for FOLDER in Buzatu*; do
    echo $FOLDER
    cd $FOLDER
    git status
    cd ..
done
