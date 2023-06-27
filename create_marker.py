from pyx import *
import argparse
import sys

import math
import numpy as np


def generateCheckerboard(canvas, n_cols, n_rows, tsize):
    size_cols = tsize*10    # 放大倍数 10
    size_rows = tsize*10    # 放大倍数 10
    #draw boxes
    up_left_x = 0*size_cols
    up_left_y = 0*size_rows

    c.fill(path.rect(up_left_x, up_left_y, size_cols, size_rows),[color.rgb.black])  

    up_left_x = 1*size_cols
    up_left_y = 1*size_rows

    c.fill(path.rect(up_left_x, up_left_y, size_cols, size_rows),[color.rgb.black]) 

    up_left_x = 2*size_cols
    up_left_y = 2*size_rows

    c.fill(path.rect(up_left_x, up_left_y, size_cols, size_rows),[color.rgb.black]) 

    #write to file
    c.writePDFfile("target.pdf")

if __name__ == "__main__":
    usage=""
    #open a new canvas
    c = canvas.canvas()    
    n_cols = 4
    n_rows = 20
    chessSz = 1
    generateCheckerboard(c, n_cols, n_rows, chessSz)