for FOLDER in Buzatu*; do
    echo $FOLDER
    svn update $FOLDER
done
