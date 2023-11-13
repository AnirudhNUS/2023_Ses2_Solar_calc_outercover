# import numpy as np
# import math
# import csv
import reader
import calculation_funcs
import writer

# inputing values

lcell, wcell, powcell = reader.read_cell_inp()
'''
print("lcell: ", lcell)
print("wcell: ", wcell)
print("powcell: ", powcell)
'''
rho, tf, clf, clmside, clhi, clho, clmcen, clcell = reader.read_frame_inp()
'''
print("rho: ", rho)
print("tf: ", tf)
print("clf: ", clf)
print("clmside: ", clmside)
print("clhi: ", clhi)
print("clho: ", clho)
print("clmcen: ", clmcen)
print("clcell: ", clcell)
'''
L, W, H = reader.read_body_inp()
'''
print("L: ", L)
print("W: ", W)
print("H: ", H)
'''

####################################################

# calculating intermediate values

if (L>300):
    tf = 0.01*L

print("new tf: ",tf)
dhinge = round(2*(tf-clhi),2)

ncellspanel = [[0,0],[0,0],[0,0]]   # array of size 3
nxy = [[0,0],[0,0],[0,0]] # array of size 3

ncellspanel[0][0], ncellspanel[0][1], nxy[0] = calculation_funcs.get_ncp12(L, W, tf, dhinge)
ncellspanel[1][0], ncellspanel[1][1], nxy[1] = calculation_funcs.get_ncp12(L, H, tf, dhinge)

ncellspanel[2][0], ncellspanel[2][1], nxy[2] = calculation_funcs.getncp3(tf)

print("ncellspanel: ", ncellspanel)
print("nxy: ", nxy)

lframe = [0,0,0]
wframe = [0,0,0]

lframe[0], wframe[0] = calculation_funcs.getframelw12(ncellspanel[0], nxy[0], tf, dhinge)
lframe[1], wframe[1] = calculation_funcs.getframelw12(ncellspanel[1], nxy[1], tf, dhinge)

lframe[2], wframe[2] = calculation_funcs.getframelw3(ncellspanel[2], nxy[2])

print("lframe: ",lframe)
print("wframe: ",wframe)

h2hdist = [0,0]

for i in range(2):
    h2hdist[i] = round(lframe[i] - 2*clho - dhinge,2)

print("hinge to hinge distance: ", h2hdist)

####################################################

# Writing in the intermediate file
writer.write_int(tf,dhinge,h2hdist,lframe,wframe,nxy,ncellspanel)

####################################################

# calculating output values

ncells = 4*(ncellspanel[0][0]+ncellspanel[1][0]) + ncellspanel[2][0]
ptot = round(powcell*ncells,2)

print("ncells: ", ncells)
print("ptot: ", ptot)

lenopen, widopen = calculation_funcs.getlwopen(W, H, h2hdist, tf, dhinge, wframe, clmside)

print("lenopen (mm): ", lenopen)
print("widopen (mm): ", widopen)

vtot = tf*(4*(lframe[0]*widopen[0] + lframe[1]*widopen[1]) +lframe[2]*wframe[2])

print("vtot (mm^3): ", vtot)

mtot = rho*tf*(lenopen[0]*widopen[0]+lenopen[1]*widopen[1] - widopen[0]*widopen[1])

print("mtot (mg): ", mtot)

################################################

# writing in output file
writer.write_out(ncells, ptot, vtot, mtot, lenopen, widopen)


''''''''''''''''''''''''''''''''''''''''''''''''
################################################

