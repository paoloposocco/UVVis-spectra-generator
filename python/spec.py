#!/usr/bin/env python
import sys, math
try:
    infilename = sys.argv[1]; outfilename = sys.argv[2];
except:
    print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)
ifile = open( infilename, 'r') # open file for reading
ofile = open(outfilename, 'w') # open file for writing
def lorentz2(x_current, x_center, fwhm, height):
    return height/(1.0+((x_current-x_center)/fwhm)**2.0)
lines = ifile.readlines()
x = []; y = [] # start with empty lists
for line in lines:
    print "input= " + line
    xval, yval = line.strip().split()
    x.append(int(xval)); y.append(float(yval))
print 'x= ' + str(x)
print 'y= ' + str(y)
spectrum={}
for i in range(100, 350, 1):
    spectrum[i]=0.0
print spectrum
for i in range(0, len(x), 1):
    #print 'x(i)= ' + str(x[i]) + 'y(i)= ' + str(y[i])
    for x_current, height in spectrum.items():
        #print 'x_current= ' +  str(x_current)
        print str(x_current) + "    " + str(x[i]) + "    " + str(y[i])
        spectrum[x_current]=spectrum[x_current]+lorentz2(x_current, x[i], 15.0, y[i])
        #spectrum.values=float(height)
        print str(lorentz2(x_current, i, 15, y[i])) + " " + str(height)
        #ofile.write('%g %g\n' % (x_current, height))
for x_current, height in spectrum.iteritems():
    ofile.write('%g %18.11f\n' % (x_current, height))

print spectrum

import subprocess
plot = subprocess.Popen(['gnuplot', '-p'], shell=True, stdin=subprocess.PIPE)
##plot.stdin.write('set xrange [0:10]; set yrange [-2:2]\n')
##plot.stdin.write('plot sin(x)\n')
##plot.stdin.write('quit\n')
plot.communicate("""
plot 'out.txt' u 1:2
pause 20
""")
##plot.stdin.write("plot '%s' u 1:2 " % (outfilename))
##plot.stdin.write("pause 6")
#plot.communicate("set terminal jpeg\n")
#plot.communicate("set output '%s'\n" % (outjpgname))
#plot.communicate("plot '%s' u 1:2\n" % (outfilename))
