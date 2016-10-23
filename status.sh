for FOLDER in Buzatu*; do
    echo $FOLDER
    svn status $FOLDER
done
