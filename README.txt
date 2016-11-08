Connect to CERN's lxplus, or to your institute machine, or to your own local lepton. We assume you can setup Root, including PyRoot, on either of these. For lxplus, the code below would just work with copy paste. 

For CERN it's better to work in your work area, as you have a larger disk space available. This is a workspace where you can have up to 100 GB, while in your home area you can have maximum 10 GB. Therefore we will run there, so that we can store the data, the output, etc.
ssh -X lxplus.cern.ch
Update the one below for your username, by replacing "a" with the first letter of your "username"
ln -s /afs/cern.ch/work/a/$USER work
Check
ls -lh work
cd work
ls

On lxplus, I work on
/afs/cern.ch/user/a/abuzatu/work/public
At Glasgow I work on
/afs/phas.gla.ac.uk/user/a/abuzatu/code
On my laptop I work on 
/Users/abuzatu/Work/ATLAS/Analyses

In your ~/.zshrc (lxplus), ~/.bashrc (linux), or ~/.profile (Mac laptop) set the environment variable Analyses to point to this folder. In the code below, we only use $Analyses, and thus is independent on the folder you are actually on.

To be able to check out the packages from the Git at CERN (gitlab.ch), make sure you create the ssh keys and you copy in your ~/.ssh the files id_rsa and id_rsa.pub.

cd $Analyses
pwd

In your browser, open the package that can check out all the other packages. 
https://gitlab.cern.ch/abuzatu/BuzatuAll/
At the bottom there is the README.txt file that tells you what to do (in fact you are reading this file right now). 

You can see the "Files" and click through the folder structure, see the content of the files, click on the line number to the left, if you want to send a url with that line number to someone, to take a look easily at some code, for example.
https://gitlab.cern.ch/abuzatu/BuzatuAll/blob/master/setup.sh#L4

You can see the latest commits and you can compare between two versions.

Click on "KRB5", switch to "SSH" and copy in the clipboard the value "ssh://git@gitlab.cern.ch:7999/abuzatu/BuzatuAll.git"

Checkout the package
git clone ssh://git@gitlab.cern.ch:7999/abuzatu/BuzatuAll.git
ls -lrt
cd BuzatuAll 

There is a file ChangeLog with the history of the changes to this package.

There is a file README.txt that tells you want to do next. In fact, you are reading this file right now. It is visible also directly from GitLab. 

And there is an util folder that has the scripts to check out the other packages, update them and many more. Explore it at your leasure.

You are supposed to run everything from this main folder.

Check out the outher packages
./util/checkout.sh 
It will tell you what arguments it needs.
Usage: ./util/checkout.sh packages_file        FORCE_CHECKOUT
Usage: ./util/checkout.sh ./util/packages.txt  0
If you want to get only a subset of the packages available to you, remove them from ./util/packages.txt, for example the Rivet ones may not be interesting for you at this point.
./util/checkout.sh ./util/packages.txt  0

You have now a list of packages, all starting with "Buzatu". To be easy to access them in the future, we want to make an environment variable to point to each of them. This also sets to the LD_LIBRARY_PATH the lib of the BuzatuTree, if we want to compile and run it, and to the PYTHONPATH the BuzatuPython, that help with PyRoot, especially the pearl of the crown, the script that overlays as many histograms as we want, after it does or not, depending on your desire, a fit with several options (Gauss, Bukin) and prints or not the fit values in the legend, including showing a ratio plot down or not.
source ./util/setup.sh

When you close the terminal, and you come back you do
cd $Analyses
cd BuzatuAll
source ./util/setup.sh
Wherever you are, now
cd $All
will bring you back to BuzatuAll, from where you can go to any inside package.


