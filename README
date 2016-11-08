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
for lxplus, you must do first the next two lines
setupATLAS
lsetup git
now start the lines for all platforms
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

********************************************************************************
***** How to create a flat tree with bjets from CxAOD local or on eos **********
********************************************************************************

First you have to have checked out the CxAODFramework and compiled it.
You must also have access to the CxAOD file on the same machine, which can big as big as 4 GB.
The CxAOD can also be run from /eos
You may run from your institute if it allows /afs and /eos access to CERN.
If not, the surest bet is to be on lxplus an check out the package there following the above rules. Then.
cd ../CxAODFramework_r26-01

Set up RootCore for this package, so that we know the Jet class how to retrieve the info from the CxAOD
source $All/BuzatuATLAS/CxAODFramework/setup.sh 

Go to our code
cd $All/BuzatuATLAS/CxAODFramework/createTree 
ls

We want to process a very recent file for 2-lep AZh->llbb in CxAODTag26-01, copied in Adrian's public space at CERN.
ls -lh /afs/cern.ch/user/a/abuzatu/data/CxAOD/r26-00/AZh500

We create a new file processes_r26-01.list following the example of processes_r26-00.list.
You can add new processes in the file, the code will loop over them.
You can comment out each line, the code will ignore those files.

cp processes_r26-00.list processes_r26-01.list
emacs -nw processes_r26-01.list
first argument is the name of the process that we choose, say AZh500llbb
the second is the location of the folder /afs/cern.ch/user/a/abuzatu/data/CxAOD/r26/AZh500
it could be on eos, for this we would do in the folder
eosmount eos
and the we would put the full path starting with /afs, as it would interpret eos as a local folder
the third argument is what sort of b-tagging we want, we say btag, as we can also ask for ctag, for VHcc studies
the fourth argument is if we want to force our jets stored in the CxAOD to have a bParton matched to them, we set to 0, to not reduce statistics, as JetEtMiss group cares only about a TruthWZ, so we force only a TruthWZ to be matched to both jets
the fifth argument is the tag of the CxAOD, just the first number (26 would be ok for both 26-00 and 26-01) which tells us what PtReco was stored and in what way, so here we have CxAODTag26.

Now we can run.
./run.sh
Will give you the options to give, which are self explained: the output folder, which tag (to create the name of the processes file, but also the output folder suffix), on how many events (-1 means all), and if we want to print debug information (if do not want, use 0).
It's a good practice to store the data separately from the code, so I have my own data folder, in which I have a Tree (for the flat tree), already created, and then I just choose the date (and the folder will be created for me).
Let's run only on 100 events for now to test it. 
./run.sh /afs/cern.ch/user/a/abuzatu/data/Tree/161108_1   r26-01    100       0
Then you can run for full stats
./run.sh /afs/cern.ch/user/a/abuzatu/data/Tree/161108_1   r26-01    -1        0 >& run_fullstats.log & 

Now you can check your file
root.exe /afs/cern.ch/user/a/abuzatu/data/Tree/161108_1/tree_AZh500llbb.root
There is a perjet and a perevent tree.
Only events with 2jets of 20 GeV, of good quality, b-tagged, and each matched in DR to TruthWZ jet are stored.
So we can do per-jet pt and per-event mbb response and resolution studies relative to TruthWZ. The corrections stored are
Nominal (GSC)
OneMu (muon-in-jet)
PtReco
Regression 

********************************************************************************
***** How to create mbb overlay plots from this flat tree             **********
********************************************************************************

cd $All/BuzatuVH/createMbb
emacs -nw createMbb.py
emacs -nw runCreate.sh
in the for loop to have overlayHisto.py off and createMbb.py oon.
change 
INPUT_FOLDER="161107_3_CxAOD_24_7"
PROCESSes="ZZ"
NR_EVENTS=-1
OPTIONS="inclusive,2hadronic,1hadronic1semileptonic,2semileptonic"
OUTPUT_FOLDER="161107_3"
DEBUG="0"

The output will come in ~/data/histos_mbb. Once you have this folder, it will create 161107_3 there automatically.
To overlay the corrections, edit again 
emacs -nw runCreate.sh
In overlayHisto.py you can choose what histograms you want plotted, in what order, with what color, if you want to fit or not, if you want the fit value on the plot or not.
The plots appear in the same folder.
To visualize them easily, we create an index.html with then. 
/afs/cern.ch/user/a/abuzatu/data/histos_mbb/161107_3
$All/BuzatuBash/make_html.sh .
You can now make this webpage public to your cern ~/www webpage by copying the folder there. 
/afs/cern.ch/user/a/abuzatu/www/mbb/ZZ
In browser put 
https://abuzatu.web.cern.ch/abuzatu/mbb/ZZ/
use your $USER instead of abuzatu

