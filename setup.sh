CODE_STEM="/data06/abuzatu/code"
DATA_STEM="/data06/abuzatu/data"
#CODE_CXAOD="CxAODFramework_tag_r32-07"
CODE_CXAOD="CxAODFramework_branch_master_21.2.60_11"
#CODE_CXAOD="CxAODFramework_branch_master_21.2.61_1"
DATA_CXAOD="190208_32-07"
cd ${CODE_STEM}/${CODE_CXAOD}/run
source ../source/CxAODOperations_VHbb/scripts/setupLocal.sh
source ../source/CxAODOperations_VHbb/scripts/setupGrid.sh Higgs 1
pushd ${DATA_STEM}/CxAOD/${DATA_CXAOD}
ls -lrt
