#!/bin/sh

caget pflibera02:TT:WFA | cut -d ' ' -f 3-  | sed -E 's/ /\n/g' > tmpA
caget pflibera02:TT:WFB | cut -d ' ' -f 3-  | sed -E 's/ /\n/g' > tmpB
caget pflibera02:TT:WFC | cut -d ' ' -f 3-  | sed -E 's/ /\n/g' > tmpC
caget pflibera02:TT:WFD | cut -d ' ' -f 3-  | sed -E 's/ /\n/g' > tmpD

