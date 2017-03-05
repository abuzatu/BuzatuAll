for FOLDER in Buzatu*; do
    echo "************************************************"
    echo "****** $FOLDER *************"
    echo "************************************************"
    cd $FOLDER

    git fetch
    git status
    cd ..
done
