Folders="${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag+PtV200inf+TruthGENWZ_1_perevent"
#Folders="${outputroot}/local/histo_merged/readPaul_1_500000_J1Pt45+2BTag+TruthGENWZ_1_perevent"
#Folders="${outputroot}/local/histo_merged/readPaul_1_2000000_J1Pt45+2BTag+TruthGENWZ_1_perevent"
#Folders="${outputroot}/local/histo_merged/readPaul_1_0_J1Pt45+2BTag+TruthGENWZ_1_perevent"
Prefixes="All_1,0Muon_1,1Muon_1,2Muon_1" # Event Selection and if weights are applied
#Prefixes="2Muon_1" # Event Selection and if weights are applied
#Suffixes="M-j1j2_v_0_300_4"
Suffixes="M-j1j2_v_0_300_10"
#WhatToComputes="signaloverbackground"
#WhatToComputes+=",sensitivity"
WhatToComputes+=",significance"
IncludeUnderflowOverflowBinss="0" #"0,1"
AddInQuadratures="1" #"0,1"
Signals="Signal" # "Signal,WH,ZH"
Backgrounds="Background"
#Backgrounds="Background,VV,TopPair,SingleTop,Whf,Wcl,Wl,Zhf,Zcl,Zl"
Debug=0

for Folder in `echo "${Folders}" | awk -v RS=, '{print}'`
do
    for Prefix in `echo "${Prefixes}" | awk -v RS=, '{print}'`
    do
	for Suffix in `echo "${Suffixes}" | awk -v RS=, '{print}'`
	do
	    for WhatToCompute in `echo "${WhatToComputes}" | awk -v RS=, '{print}'`
	    do
		for IncludeUnderflowOverflowBins in `echo "${IncludeUnderflowOverflowBinss}" | awk -v RS=, '{print}'`
		do
		    for AddInQuadrature in `echo "${AddInQuadratures}" | awk -v RS=, '{print}'`
		    do
			for Signal in `echo "${Signals}" | awk -v RS=, '{print}'`
			do
			    for Background in `echo "${Backgrounds}" | awk -v RS=, '{print}'`
			    do	
				FolderOutput="${outputroot}/local/${WhatToCompute}/$(basename ${Folder})"
				mkdir -p ${FolderOutput}
				command="python ${BuzatuWH}/computeSignificance/computeSignificance.py ${Folder} ${Prefix} ${Suffix} ${WhatToCompute} ${IncludeUnderflowOverflowBins} ${AddInQuadrature} ${Signal} ${Background} ${FolderOutput} ${Debug}"
				echo ${command}
			`echo ${command}`  
			    done
			done
		    done
		done
	    done 
	done
    done
done
