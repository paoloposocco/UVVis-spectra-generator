#!/usr/bin/env python
import sys, math
import numpy as np
import matplotlib.pyplot as plt

##############
##  PARSER  ##
##############
try:
    infilename = sys.argv[1]; fwhm = sys.argv[2] #outfilename = sys.argv[3];
except:
    print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)
ifile = open( infilename, 'r') # open file for reading
##ofile = open('out.txt', 'w') # open file for writing
##ofile = open(outfilename, 'w') # open file for writing
def lorentz(x_current, x_center, fwhm, height):
    return height/(1.0+((x_current-x_center)/fwhm)**2.0)
lines = ifile.readlines()
x = []; y = [] # start with empty lists
dentrosezione = False
for line in lines:
    print "input= " + line
    try:
        xval, cestino = line.split(None, 1)
        if xval=="Interatomic": dentrosezione = False
    except ValueError:
            print 'errore in lettura file'
    if dentrosezione == True:
        try:
            c1, c2, xval, c3, yval = line.split()
            if int(c1) == 1 or 2 or 3:
                x.append(float(xval)); y.append(float(yval))
            else:
                print 'non e" una riga interessante'
        except ValueError:
                print 'errore in lettura file'
    else:
        try:
            xval, cestino = line.split(None, 1)
            if xval=="Oscillator":
                dentrosezione = True
                print "dentro la sezione interessante"       
        except ValueError:
                print 'errore in lettura file'

####################################
##  STAMPA DIAGNOSTICA DELL'INPUT ##
####################################
print 'x= ' + str(x)
print 'y= ' + str(y)

###################################################
##  COSTRUZIONE LISTE SPETTRO E RELATIVO CALCOLO ##
###################################################
spettro_finestra = np.arange(0, 10, 0.01) ## TO DO: si potrebbe settare un set o in input o comunque piu' sensato

spettro = []
for i in range(0, len(spettro_finestra), 1):
    spettro.append(0.0)
##print spettro
for i in range(0, len(x), 1):
##    print 'sono al giro numero=' + str(i)
##    print 'spettro='
##    print spettro
    for n in range(0, len(spettro_finestra), 1):
        spettro[n]=spettro[n]+lorentz(spettro_finestra[n], x[i], float(fwhm), y[i])


plt.plot(spettro_finestra, spettro)
plt.show()
