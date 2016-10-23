Connect to CERN, but similarly it can be done on your laptop
ssh -X lxplus.cern.ch

Update the one below for your username, by replacing "a" with the first letter of your "username"
ln -s /afs/cern.ch/work/a/$USER work
Check
ls -lh work

This is a workspace where you can have up to 100 GB, while in your home area you can have maximum 10 GB. Therefore we will run there, so that we can store the data, the output, etc.

Go there
cd work
ls

We have a "public" folder. All you put there can be read by others. Anything that is not there can not be read by others. This is why we put here the data we have to share with others, files we want to share with others, etc.

We have a "private" folder. Typically we put the code there.

In the "public" folder we create a structure of initial, output and PtReco folders. We copy the data files from Adrian for initial and PtReco. The output contains batch and local.

cd public
mkdir forVH
cd forVH
ls
mkdir initial
cd initial
[there are 14 GB of data files to copy, so it can take a few minutes]
cp -r ~abuzatu/work/public/forVH/initial/NoJ1Pt45Cut .
[if you are not on a CERN machine, you can copy with]
scp -r lxplus.cern.ch:~abuzatu/work/public/WH/initial/NoJ1Pt45Cut .
cd ..
mkdir output
cd output
mkdir batch
mkdir local
cd ..
[we copy the PtReco, just very small files]
cp -r ~abuzatu/work/public/forVH/PtReco .
[if you are not on a CERN machine, you can copy with]
scp -r lxplus.cern.ch:~abuzatu/work/public/WH/PtReco .

Now we decide the location where we check out the code, the WH package. From this package we will check out other package, BuzatuTree, BuzatuWH, BuzatuPython, NoteWH. For all these, we need to define some environment variables. Add this to your .bashrc, .zshrc, .profile or the equivalent.

export SVNUSR="svn+ssh://$USER@svn.cern.ch/reps/atlas-abuzatu"
export SVN_EDITOR="emacs -nw"
export initialroot="$HOME/work/public/WH/initial"
export outputroot="$HOME/work/public/WH/output"
export Analyses="$HOME/work/private"
export WH="${Analyses}/WH"

If you are not on a CERN machine, replace $USER, the username on that machine, with the username you have at CERN. Once you start you a new window, these environment variables are defined. Or if not, do
source ~/.zshrc [or equivalent]

Now we will checkout the code, the tag 19.

cd $Analyses
svn co $SVNUSR/WH/tags/WH-00-00-19 WH
cd WH
[every time you start a new window, you need to setup, which will set up more environement variables and update the LD_LIBRARY_PATH and the PYTHONPATH.]
source setup.sh

The WH package is just a package that allows us to check out the other packages. We will retrieve the tagged packages.
./checkout.sh
We see the examples, since we want the tag (not the trunk)
./checkout.sh 0 1
All the packages are checked out automatically. If you are not on a CERN machine, you will have to put your CERN password for each package.

Now we compile the code BuzatuTree
cd BuzatuTree
[for the NN, every time we need to do this]
cd NN && ./merge.sh && make && cd ..
[now we compile everything]
make

Now we can run the tree for testing
./bin/read.exe
[this will give us the examples of the arguments]
./bin/read.exe ${initialroot}/NoJ1Pt45Cut/Signal.root WlvH125 Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_WH.root
[to test the file]
root.exe test1_WH.root

perjet->Show()
[distributions]
perjet->Draw("GENWZ_Pt")
perjet->Draw("EMJESGSCMuPt2_Pt")
perjet->Draw("EMJESGSCMuPt3_Pt")
perjet->Draw("EMJESGSCMuPt3NNJ1_Pt")
perjet->Draw("EMJESGSCMuPt3NNE1_Pt")
perjet->Draw("EMJESGSCMuPt3NNE2_Pt")

[correction factors needed]
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt_Pt")
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt2_Pt")
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3_Pt")
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3NNJ1_Pt")
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3NNE1_Pt")
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3NNE2_Pt")

[response]
perjet->Draw("EMJESGSCMuPt_Pt/GENWZ_Pt")
perjet->Draw("EMJESGSCMuPt2_Pt/GENWZ_Pt")
perjet->Draw("EMJESGSCMuPt3_Pt/GENWZ_Pt")
perjet->Draw("EMJESGSCMuPt3NNJ1_Pt/GENWZ_Pt")
perjet->Draw("EMJESGSCMuPt3NNE1_Pt/GENWZ_Pt")
perjet->Draw("EMJESGSCMuPt3NNE2_Pt/GENWZ_Pt")

perevent->Show()

[distributions]
perevent->Draw("j1j2_GENWZ_M")
perevent->Draw("j1j2_EMJESGSCMuPt_M")
perevent->Draw("j1j2_EMJESGSCMuPt2_M")
perevent->Draw("j1j2_EMJESGSCMuPt3_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNJ1_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNE1_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNE2_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNE2_M")

[response]
perevent->Draw("j1j2_EMJESGSCMuPt_M/j1j2_GENWZ_M")
perevent->Draw("j1j2_EMJESGSCMuPt2_M")
perevent->Draw("j1j2_EMJESGSCMuPt3_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNJ1_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNE1_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNE2_M")
perevent->Draw("j1j2_EMJESGSCMuPt3NNE2_M")

You have examples on how to run also on electron data, muon data, or MC multijet or data MJ.
Usage: ./bin/read.exe ${initialroot}/NoJ1Pt45Cut/Signal.root WlvH125 Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_WH.root
Usage: ./bin/read.exe ${initialroot}/NoJ1Pt45Cut/Electron.root data Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_el.root
Usage: ./bin/read.exe ${initialroot}/NoJ1Pt45Cut/Muon.root data Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_mu.root
Usage: ./bin/read.exe ${initialroot}/NoJ1Pt45Cut/MCMJ.root WlvH125 Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_WHMJ.root
Usage: ./bin/read.exe ${initialroot}/NoJ1Pt45Cut/ElectronMJ.root data Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_elMJ.root
Usage: ./bin/read.exe ${initialroot}/NoJ1Pt45Cut/MuonMJ.root data Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_muMJ.root

Now that the file with low statistics looks like we want, we want to run for many processes in an automatic way. For this we have another package, BuzatuWH.

cd ../BuzatuWH
or
cd $BuzatuWH
[the advantage of the environement variables defined in source setup.sh in WH]
cd runTree
[The files input*.list enumerate the processes we want to run on]
[The file runRead.sh runs on each process at a time and can run on batch [at Glasgow so in parallel] or locally [one after the other].
[The file run.sh actually is the one we run where we call runRead.sh with different arguments]

We want now to create a signal file with low statistics to train NNs.
./run.sh
[where the line actually run is $BuzatuWH/runTree/runRead.sh local perevent+perjet J1Pt45+2BTag+TruthGENWZ+Clean Test 1 1 30000]

Once it finishes, the result is in $outputroot
cd $outputroot
ls
cd local
ls
cd readPaul_1_30000_J1Pt45+2BTag+TruthGENWZ+Clean_1_perevent+perjet
ls
[the output file is in lvbb125.root and we can open and check it as above]
[the two type of log files are in logs]
[script_*.log is the command we run]
[run_*.log is the actual output, where we can read nicely the number of initial events, the number of events that pass our event selection and the total yield. The yield is nicely rescaled if we decide to run on fewer events than the entire sample]
tail run_lvbb125.log

Now we are going to train neural networks using this file.
cd $BuzatuWH/runPython/NeuralNetwork
[the NN trainings are defined in ConfigNN.py, while the actual running is in runTrain.py]

Let's train a per-jet NN:
python runTrainNN.py
It expects arguments and it gives us suggestions, the perjet is A1
python runTrainNN.py A1

Once it finishes, in the NN folder we have:
o in the NN folder in Python (.py) and in C++ (two files, one .h, and one .cxx). Here we have n100_1_perjet NN.
o in the plot folder a .pdf for this NN. In the top left you have the train and test error as a function as the number of epochs. But at CERN it seems just the first epoch is shown. In the top right you see the structure of the NN, with the inputs, the hidden layers, the output. It is hard to read the names of the variables if they are too many. On the bottom right is the distribution of the change in the NN output if one input at a time is changed, while the others are left unchanged. The more a variable is on the right, the more it means it contributed to the result of this NN training. This is a plot that can help "guess" the most important variables. If we run for different random numbers and training methods and we see the same variables on the right and the same on the left, it means that we could remove the variables on the left to leave more statistics for those on the right. The last plot, the bottom right, is harder to read and not that useful.
o in the training folder we see a list of all the NNs trained with the option "A1". It helps us remember what are the variables used in the training and their order for the number n100_1_perjet, which are needed when we will implement this NN in our code. Also it tells us what was the epoch number for the smallest testing error. Here we trained on 100 NNs, but we see the smallest is at 77. So we could train again on only 77 epochs. This can have been done if in runTrain.py we had said step_2=True instead of step_2=False.
o in the weight folder we have the weights before the NN training, as in order to run again on step_2 with the same NN we read the weights again in.
o in the error folder we have the change in the training (learn) and the testing (test) as a function of the number of epochs: less n100_1_perjet.txt

Now we train a NN per event.
python runTrainNN.py B1
In the same folders you have the NN called "n200_1_perevent".
You can go to the folders and check.

Now we want to update the code in BuzatuTree to add these new NNs as new corrections to the jets.
cd $BuzatuTree
cd NN
[this copies all the NNs that are in the NN folder]
./copy.sh
[check that they have appeared n100_1_perjet and n200_1_perevent]
ls
[remove the old NN.h and NN.cxx and merge all the NN in the folder in NN.h and NN.cxx]
./merge.sh
[now compile]
make

The code is very modular, so what we need to change is only in Run/Run.cxx
cd ../Run
emacs Run.cxx&

The function DoAfterFillEvent() tells us what is done after the event is filled with the j1 and j2 and the truth for all the jets.
o the truth is matched to the j1 and j2
o some quantities are added
o then we add all the PtReco corrections; our NN comes on the top of the Pt3 correction that is added here, so the variable is defined already
o then we add all the per jet NNs
o then all the per event NNs
o then all the neutrino corrections

Let's go at the AddAllPerJetNN() function. We see how we loop over all the jets (j1 and j2) and for each we correct the jet. We add the n100 by commented out the line
AddPerJetNN(current_jet,"EMJESGSCMuPt3","EMJESGSCMuPt3NNJ2","n100");
It means that we apply it at the top of EMJESGSCMuPt3 and it will have the name EMJESGSCMuPt3NNJ2. How the actual correction is computed is defined based on the string "n100".

We now go at the AddPerJetNN() function.
First we retrieve the variables that we need for the input of the NN for this jet, be it either j1 or j2.
We define the correction factor. Then as a function of the string, we compute it.
If "n300" we read the NN n300_1_perjet(). The same we do for our new NN n100_1_perjet by commenting out the lines.

If you train NNs in Junior's style, you get the NN function itself and then you copy paste it here. Here he has n2 which is different if the jet has muon or not. The NNs have only PtReco as argument at the EMJESGSCMu stage. Also note how the correction also uses MOP_RecoPt because he trains to the GENWZ_Pt/MOP_RecoPt and not to the GENWZ_Pt/RecoPt as I do in the default.

That is it. Save and compile.

Now let's add the per-event NN. Let's search AddAllPerEventNN();
There we uncomment the line and we add EMJESGSCMuPt3NNE3 on the top of EMJESGSCMuPt3 with the string n200.

Then we go to the infividual correction function AddPerEventNN(). It is similar to the per-jet one, except you have two correction factors, one for j1, one for j2 and you get the j1 one by taking the 0 and the j2 by taking the 1

corr1=n20_1_perevent().Value(0,...)
corr2=n20_1_perevent().Value(1,...)

We uncomment the code for n200.
Then at the bottom the correction is added for j1 and j2 separately.

And that is all, you can compile again.

You see how every time we multiply the Pt and E by the same number. We also use that in adding the PtReco or the Neutrino correction. This is why it is all in one function,

AddNewLVByScalingAnotherLV(Obj("j2"),name_lv_reference,name_lv_NN,corr2);

You can take a look at this function to see how it is.

Now we compile again and run again locally.

make
cd ..
./bin/read.exe
./bin/read.exe ${initialroot}/NoJ1Pt45Cut/Signal.root WlvH125 Paul 1 2000 J1Pt45+2BTag+TruthGENWZ+Clean 1 perjet+perevent ./test1_WH.root

Notice the Clean which adds some cleaning cuts that remove the extemes when training. We should test the results in in the same selection as the one used for training, but then also the official analysis, without the cleaning cuts.

root.exe ./test1_WH.root
As you see, we now have added these corrections and you can quickly check if the Mbb is narrower and peaks better, if the resolutions for jets have improved, as per the code above.

perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3_Pt")
the new ones:
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3NNJ2_Pt")
perjet->Draw("GENWZ_Pt/EMJESGSCMuPt3NNE3_Pt")

Now we want to run again, for the signal and some main backgrounds, WZ, TTbar and Wbb. They are in inputMinimum.list.

cd $BuzatuWH/runTree
emacs run.sh &
We comment the line currently running and we uncomment the line:
$BuzatuWH/runTree/runRead.sh local perevent+perjet J1Pt45+2BTag+TruthGENWZ Minimum 1 1 30000
This is just 30.000 events but for all the processes and with the same event selection as the analysis.

We look at the files
cd $outputroot
ls
cd local
ls
readPaul_1_30000_J1Pt45+2BTag+TruthGENWZ_1_perevent+perjet

As you see, we have now 4 files. Let's look at the yields. They are located in the logs.
cd logs
tail run_lvbb125.log
> 104.362
tail run_WZ.log
> 295.743
tail run_TTbar.log
> 8973.47
tail run_Wbb.log
>7035.21

we can compute a quick s/b=0.006 and s/sqrt(b)=0.817
The real numbers would be smaller as we include more backgrounds that are not included here.

Now we want to make plots overlaying mbb for different corrections.
cd $BuzatuWH/runPython

We have here a lot of scripts that can use these files in order to loop over the events, fill histograms and manipulate them. We can for example compute the PtReco correction, or we can compute the Mbb. Let's focus on the Mbb. For this we have the script runHistograms.sh. At the top you say for what processes you want to run on. Then for each process we have four steps:
1. we create the Histograms. Only mbb is filled for different corrections, but we can also do mbb resolution, jet Pt, jet Pt resolution, you can just modify runCreateHistograms.py. Also add in this file new corrections once you have them.
2. we manipulate the histograms, meaning we perform the bukin fit on them and they are saved. A .tex file of the mbb peak and width for all the corrections is created. You have to add here your corrections.
3. we can overlay histograms in one style. You have to add here your corrections.
4. we can overlay histograms in another style. You have to add here your corrections.

In the future I will add a script to compute the sensitivity for the desired corrections based on the processes that we have. 
