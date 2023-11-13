# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:03:34 2023

@author: admin
"""
import csv

def read_cell_inp():
    with open("cell char input.txt") as inp_dat:
        tsv_reader = csv.reader(inp_dat, delimiter=":")
        row = next(tsv_reader) # get the values from each row
        lcell = float(row[0])          # length of cell
        row = next(tsv_reader) # get the values from the next row
        wcell = float(row[0])       # width of cell
        row = next(tsv_reader) # get the values from the next row
        powcell = float(row[0])     # power generate by each cell
    inp_dat.close()     # close the file after done reading
    
    return lcell, wcell, powcell

def read_frame_inp():
    with open("frame dimz input.txt") as inp_dat:
        tsv_reader = csv.reader(inp_dat, delimiter=":")
        row = next(tsv_reader) # get the values from each row
        rho = float(row[0])        # density of the frame
        row = next(tsv_reader) # get the values from each row
        tf = float(row[0])          # frame thickness
        row = next(tsv_reader) # get the values from the next row
        clf = float(row[0])       # frame clearance
        row = next(tsv_reader) # get the values from the next row
        clmside = float(row[0])     # side mechanism clearance
        row = next(tsv_reader) # get the values from the next row
        clhi = float(row[0])     # side mechanism clearance
        row = next(tsv_reader) # get the values from the next row
        clho = float(row[0])     # side mechanism clearance
        row = next(tsv_reader) # get the values from the next row
        clmcen = float(row[0])     # side mechanism clearance
        row = next(tsv_reader) # get the values from the next row
        clcell = float(row[0])     # side mechanism clearance
    inp_dat.close()     # close the file after done reading
    
    return rho, tf, clf, clmside, clhi, clho, clmcen, clcell

def read_body_inp():
    with open("body size inputs.txt") as inp_dat:
        tsv_reader = csv.reader(inp_dat, delimiter=":")
        row = next(tsv_reader) # get the values from each row
        L = float(row[0])          # length of craft
        row = next(tsv_reader) # get the values from the next row
        W = float(row[0])       # width of craft
        row = next(tsv_reader) # get the values from the next row
        H = float(row[0])     # height of craft
    inp_dat.close()     # close the file after done reading
    
    return L, W, H