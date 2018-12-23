#!/usr/bin/gnuplot

set pm3d map
set size square

set xlabel offset 0,-1
set ylabel offset -2,0

set xlabel 'K3 Angle [mrad]' font 'times,14'
set ylabel 'k4 Angle [mrad]' font 'times,14'
set zlabel 'Objecive value [a.u.]'

#set xrange [2:4]
#set yrange [2:4]

splot 'meas.dat'

pause 10
#reread 
