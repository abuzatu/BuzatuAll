#
# WhereToRun="local" # local or batch
# for batch
# QUEUE="medium6" #short6, medium6, long6, vlong6 
# 6 means SL6, as ppepc137
# 5 means SL5, as ppepc136
# short means 1h, medium means 6h, long means 24h and vlong 120h(5days)
# https://twiki.ppe.gla.ac.uk/bin/view/IT/BatchSystem
# if you compile on a SL5 machine, you can run on both SL5 (short5) and SL6 (short6) machines
# the jobs runs faster on SL5 and also stars faster, as Danilo and Andrea run many long and medium jobs on SL6
# so the default is to compile the C++ code on ppepc136 (SL5) and submit jobs from there
EMAIL="adrian.buzatu@glasgow.ac.uk"

#qsub commands
#o submission:
#qsub
#o check the status of the batch:
#qstat
#o check the status of your jobs:
#qstat -u $USER.
#o kill a job:
#qdel 994535
#o kill all the jobs of a user:
#qselect -u $USER | xargs qdel
