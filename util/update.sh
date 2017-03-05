git pull origin master
for FOLDER in Buzatu*; do
    echo "************************************************"
    echo "****** $FOLDER *************"
    echo "************************************************"
    cd $FOLDER
    git status
    git fetch
    git status
    git pull origin master
    git status
    cd ..
done
