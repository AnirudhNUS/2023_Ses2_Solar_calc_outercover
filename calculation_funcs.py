# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:52:02 2023

@author: admin
"""

import math
import csv
import reader

#############################

def get_ncp12(A,B,tf,dhinge):
    # A is the longer dim and B is the shorter dim
    lcell, wcell, powcell = reader.read_cell_inp()
    rho, def_tf, clf, clmside, clhi, clho, clmcen, clcell = reader.read_frame_inp()
    
    nxw = math.floor((A-(tf+clcell)-2*(dhinge+clho+clhi+clf))/(wcell+clcell))
    nxl = math.floor((A-(tf+clcell)-2*(dhinge+clho+clhi+clf))/(lcell+clcell))
    
    nyl = math.floor((B-(clcell+clmside)-2*clf-4*tf)/(lcell+clcell))
    nyw = math.floor((B-(clcell+clmside)-2*clf-4*tf)/(wcell+clcell))
    
    print("nxw: ",nxw)
    print("nxl: ",nxl)
    print("nyw: ",nyw)
    print("nyl: ",nyl)
    
    print("nxw * nyl : ", nxw*nyl)
    print("nxl * nyw : ", nxl*nyw)
    
    nxy = [0,0]
    
    if(nxw*nyl>nxl*nyw):
        ncp = nxw*nyl
        choice = 1
        nxy[0] = nxw
        nxy[1] = nyl
    else:
        ncp = nxl*nyw
        choice = 2
        nxy[0] = nxl
        nxy[1] = nyw
    
    print("chosen ncp: ", ncp)
    print("choice: ", choice)
    
    return ncp, choice, nxy   # ncellspanel[i] 1 n 2

#######################################

def getncp3(tf):
    # A n B are known this time as W n H, so read directly
    lcell, wcell, powcell = reader.read_cell_inp()
    rho, def_tf, clf, clmside, clhi, clho, clmcen, clcell = reader.read_frame_inp()
    L, W, H = reader.read_body_inp()
    
    nxw = math.floor((W-clcell-2*clf)/(wcell+clcell))
    nxl = math.floor((W-clcell-2*clf)/(lcell+clcell))
    
    nyw = math.floor((H-clcell-2*clf)/(wcell+clcell))
    nyl = math.floor((H-clcell-2*clf)/(lcell+clcell))
    
    print("nxw: ",nxw)
    print("nxl: ",nxl)
    print("nyw: ",nyw)
    print("nyl: ",nyl)
    
    print("nxw * nyl : ", nxw*nyl)
    print("nxl * nyw : ", nxl*nyw)
    
    nxy = [0,0]
    
    if(nxw*nyl>nxl*nyw):
        ncp = nxw*nyl
        choice = 1
        nxy[0] = nxw
        nxy[1] = nyl
    else:
        ncp = nxl*nyw
        choice = 2
        nxy[0] = nxl
        nxy[1] = nyw
    
    print("chosen ncp: ", ncp)
    print("choice: ", choice)
    
    return ncp, choice, nxy    # ncellspanel[3]

######################################

def getframelw12(ncp, nxy, tf, dhinge):
    # calculate frame length and width (lw) for case 1 n 2
    lcell, wcell, powcell = reader.read_cell_inp()
    rho, def_tf, clf, clmside, clhi, clho, clmcen, clcell = reader.read_frame_inp()
    
    if (ncp[1] == 1):       # if choice is 1, use nxw
        lframe = nxy[0]*(wcell+clcell) +clcell +2*(dhinge+clho+clhi+clf)
        wframe = nxy[1]*(lcell+clcell) +2*clf +clcell
    else: 
        lframe = nxy[0]*(lcell+clcell) +clcell +2*(dhinge+clho+clhi+clf)
        wframe = nxy[1]*(wcell+clcell) +2*clf +clcell
    
    print("lframe individual: ", lframe)
    print("wframe individual: ", wframe)
    
    return lframe, wframe

###########################################

def getframelw3(ncp, nxy):
    # calculate frame length and width (lw) for case 1 n 2
    lcell, wcell, powcell = reader.read_cell_inp()
    rho, def_tf, clf, clmside, clhi, clho, clmcen, clcell = reader.read_frame_inp()
    
    if (ncp[1] == 1):       # if choice is 1, use nxw
        lframe = nxy[0]*(wcell+clcell) +2*clf +clcell
        wframe = nxy[1]*(lcell+clcell) +2*clf +clcell
    else: 
        lframe = nxy[0]*(lcell+clcell) +2*clf +clcell
        wframe = nxy[1]*(wcell+clcell) +2*clf +clcell
    
    print("lframe individual: ", lframe)
    print("wframe individual: ", wframe)
    
    return lframe, wframe
    
#############################################

def getlwopen(W,H,h2hdist,tf,dhinge,wframe,clmside):
    lenopen = [0,0]
    lenopen[0] = W + 4*h2hdist[0] -4*tf - dhinge
    lenopen[1] = H + 4*h2hdist[1] -4*tf - dhinge
    widopen = [0,0]
    
    for i in range(2):
        widopen[i] = wframe[i] + clmside
        
    return lenopen, widopen
        
    
    
    
    
    
    