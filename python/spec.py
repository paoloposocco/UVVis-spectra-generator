#!/usr/bin/env python
import sys, math
try:
    infilename = sys.argv[1]; #outfilename = sys.argv[2];
except:
    print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)
ifile = open( infilename, 'r') # open file for reading
ofile = open('out.txt', 'w') # open file for writing
##ofile = open(outfilename, 'w') # open file for writing
def lorentz2(x_current, x_center, fwhm, height):
    return height/(1.0+((x_current-x_center)/fwhm)**2.0)
lines = ifile.readlines()
x = []; y = [] # start with empty lists
dentrosezione = False
for line in lines:
    #if line == "                               Oscillator strengths": print "arrivato all'oscil"
    print "input= " + line
##    xval, yval = line.strip().split()
    try:
            xval, cestino = line.split(None, 1)
            if xval=="Interatomic":
                dentrosezione = False
                print "uscito di nuovo"       
    except ValueError:
    ##        try
        print 'ops'
    if dentrosezione == True:
        try:
            c1, c2, xval, c3, yval = line.split()
            if int(c1) == 1 or 2 or 3:
                x.append(float(xval)); y.append(float(yval))
            else:
                print 'non e" una riga interessante'
        except ValueError:
            print 'opsdentrosezione'
    else:
        try:
            xval, cestino = line.split(None, 1)
            if xval=="Oscillator":
                dentrosezione = True
                print "QUI!!"       
        except ValueError:
    ##        try
            print 'ops'
    


print 'x= ' + str(x)
print 'y= ' + str(y)
x_nm=[]
for i in range(0,len(x), 1):
    x_nm.append(1239.84187/x[i])
spectrum={}
print 'x_nm= ' + str(x_nm)
for i in range(100, 350, 1):
    spectrum[i]=0.0
print spectrum
for i in range(0, len(x_nm), 1):
    #print 'x(i)= ' + str(x[i]) + 'y(i)= ' + str(y[i])
    for x_current, height in spectrum.items():
        #print 'x_current= ' +  str(x_current)
##        print str(x_current) + "    " + str(x_nm[i]) + "    " + str(y[i])
        spectrum[x_current]=spectrum[x_current]+lorentz2(x_current, x_nm[i], 7.0, y[i])
        #spectrum.values=float(height)
##        print str(lorentz2(x_current, i, 15, y[i])) + " " + str(height)
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
pause 60
""") #usare vairabile ofile
##plot.stdin.write("plot '%s' u 1:2 " % (outfilename))
##plot.stdin.write("pause 6")
#plot.communicate("set terminal jpeg\n")
#plot.communicate("set output '%s'\n" % (outjpgname))
#plot.communicate("plot '%s' u 1:2\n" % (outfilename))
