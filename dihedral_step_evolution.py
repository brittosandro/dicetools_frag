#!/usr/bin/env python3
"""
Receives a '.dat' file containing dihedrals to plot them across a step axis.

Author: Henrique Musseli Cezar
Date: FEB/2017
"""

import argparse
import os
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from distutils.spawn import find_executable



def plot_torsion(file, step):
    ''' This function receives a file containing the dihedral angles of the MC
    simulation, the number of steps the data was saved. Returns a picture in .pdf
    and .png format.'''

    # read data and prepare the lists
    angles = []
    with open(file, 'r') as f:
      for line in f:
        angles.append(float(line.strip()))

    stepmult = int(step)
    steps = [x * stepmult for x in range(1, len(angles)+1)]

    if find_executable('latex') and find_executable('dvipng'):
      mpl.rcParams.update({'font.size':18, 'text.usetex':True, 'font.family':
                           'serif', 'ytick.major.pad':4})
    else:
      mpl.rcParams.update({'font.size':18, 'font.family':'serif',
                           'ytick.major.pad':4})

    fig, ax = plt.subplots(figsize=(7, 5))
    fig.subplots_adjust(left = 0.135, right = 0.945, bottom = 0.125, top = 0.955,
                        hspace = 0.24, wspace = 0.23)

    ax.scatter(steps, angles, s=2)
    ax.set_xlabel(r"MC Cycle")
    ax.set_ylabel(r"$\phi$ ($^\circ$)")
    ax.set_xlim([0, steps[-1]])
    ax.set_ylim([-180, 180])
    ax.set_yticks([-180, -120, -60, 0, 60, 120, 180])
    plt.savefig(os.path.splitext(file)[0] + ".pdf", bbox_inches='tight')
    plt.savefig(os.path.splitext(file)[0] + ".png", dpi=300, orientation='portrait',
                transparent = True, format='png')



if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Receives a '.dat' file containing angles to plot the evolution with the steps.")
  parser.add_argument("fangles", help="path to the file containing the angles, one angle per line.")
  parser.add_argument("stepmult", nargs='?', help="step multiplier, the number of steps between each saved configuration (each angle)."
                      "Default is 1 and can changed to have an x-axis with the total number of steps", default=1)
  parser.add_argument("--shorttwist", help="prints a short twist graph with a range of interest.", action="store_true")
  parser.add_argument("-I", "--interphi", type=int, help="range angle (default = 20)", default=20)
  args = parser.parse_args()

  if args.shorttwist:
      print("Aqui!")
      
  else:
      print("Bem Aqui!")
      plot_torsion(args.fangles, args.stepmult)
