#!/usr/bin/perl

#Poor man's version of beeper
#Helpful to include this at the end of script running
#To let you know when it finises so that you can look at the result
#It is included in the makeFilelists.cc    
for ($i=0;$i<200;$i++)
{
    for($j=0;$j<200;$j++){
	#print ".";
	print $_;    
	print "\007";
    }
}
