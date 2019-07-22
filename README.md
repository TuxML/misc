# misc
Misc experiments and utilities 

This repo contains the results of the two experiments we performed.
During these experiments we have compiled 100 different configurations for each.
To have a fair measure we have compiled each configuration 5 times.

	Firstly we compiled using tuxml, and we retrieved our results from the database.
We created pandas Dataframes with these results, they contain all the information needed for future analysis.

	In a second time, we recompiled these same configurations 5 times, but this time not with tuxml, just with the native method, i.e by copying the .config and then "make".
It gave us another two Dataframes which contain these results.
