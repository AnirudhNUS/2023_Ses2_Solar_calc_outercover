# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:00:03 2023

@author: admin
"""

import csv

def write_int(tf,dhinge,h2hdist,lframe,wframe,nxy,ncp):
    Odat = open("intermediate vals.txt", "w")
    
    Odat.write(str(tf))
    Odat.write("\t: (tf) \t Frame thickness in mm\n")
    Odat.write(str(dhinge))
    Odat.write("\t: (dhinge) \t Diameter of the hinge in mm\n")
    
    for i in range(2):
        Odat.write(str(h2hdist[i]))
        Odat.write("\t: ")
    
    Odat.write("(h2hdist[0,1]) \t Hinge to hinge distance in mm\n")
    
    for i in range(3):
        Odat.write(str(lframe[i]))
        Odat.write("\t: ")
        
    Odat.write("(lframe[0,1,2]) \t Length of frame in mm\n")
    
    for i in range(3):
        Odat.write(str(wframe[i]))
        Odat.write("\t: ")
        
    Odat.write("(wframe[0,1,2]) \t Width of frame in mm\n")
    
    for i in range(3):
        for j in range(2):
            Odat.write(str(nxy[i][j]))
            Odat.write("\t: ")
        Odat.write("(nxy[")
        Odat.write(str(i))
        Odat.write("][0,1]) \t nx and ny \n")
    
    for i in range(3):
        for j in range(2):
            Odat.write(str(ncp[i][j]))
            Odat.write("\t: ")
        Odat.write("(ncp[")
        Odat.write(str(i))
        Odat.write("][0,1]) \t ncellspanel and choice \n")
    
    Odat.close()
    
##########################################
    
def write_out(ncells, ptot, vtot, mtot, lenopen, widopen):
    Odat = open("output vals.txt", "w")
    
    Odat.write(str(ncells))
    Odat.write("\t\t: (ncells) \t Total number of cells\n")
    Odat.write(str(ptot))
    Odat.write("\t\t: (ptot) \t Total power generated in W \n")
    vtot = round(vtot/1000.0,2)
    Odat.write(str(vtot))
    Odat.write("\t\t: (vtot) \t Total volume taken up in cm^3 \n")
    mtot = round(mtot/10**6,2)
    Odat.write(str(mtot))
    Odat.write("\t\t: (mtot) \t Total mass in kg \n")
    
    for i in range(2):
        lenopen[i] = round(lenopen[i]/1000.0,3)
        Odat.write(str(lenopen[i]))
        Odat.write("\t: ")
    
    Odat.write("(lenopen[0,1]) \t Length of opened assembly in m\n")
    
    for i in range(2):
        widopen[i] = round(widopen[i]/1000.0,3)
        Odat.write(str(widopen[i]))
        Odat.write("\t: ")
    
    Odat.write("(widopen[0,1]) \t Width of opened assembly in m\n")
        
    Odat.close()