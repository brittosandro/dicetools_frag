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
from matplotlib.patches import ConnectionPatch
import seaborn as sns


def datas_steps_angles(file, step):
    '''Essa função recebe um arquivo contendo os ângulos da simulação MC em
    formato .dat e o número de passos em que os dados foram salvos na simulação
    e retorna uma tupla, cujos elementos são listas com ângulos e passos da
    simulação.'''

    # read data and prepare the lists
    angles = []
    with open(file, 'r') as f:
      for line in f:
        angles.append(float(line.strip()))

    stepmult = int(step)
    steps = [x * stepmult for x in range(1, len(angles)+1)]

    return steps, angles

def plot_torsion(steps, angles, nome):
    ''' This function receives a file containing the dihedral angles of the MC
    simulation, the number of steps the data was saved. Returns a picture in .pdf
    and .png format.'''

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
    plt.savefig(nome + ".pdf", bbox_inches='tight')
    plt.savefig(nome + ".png", dpi=300, orientation='portrait',
                transparent = True, format='png')

def plot_short_twist(steps, angles, nome):
    '''Essa função recebe um arquivo .dat e número de steps em que os dados
    foram armazenados na simulação Monte Carlo. A função salva duas figuras no
    diretório corrente, uma em formato .pdf e outra em formato .png com um zoom
    em um intervalo. '''

    if find_executable('latex') and find_executable('dvipng'):
      mpl.rcParams.update({'font.size':18, 'text.usetex':True, 'font.family':
                           'serif', 'ytick.major.pad':4})
    else:
      mpl.rcParams.update({'font.size':18, 'font.family':'serif',
                           'ytick.major.pad':4})

    sns.set(style="ticks")
    # Criando um container principal
    fig = plt.figure(figsize=(7, 5))
    fig.subplots_adjust(left = 0.125, right = 0.955, bottom = 0.135, top = 0.970,
                        hspace = 0.250, wspace = 0.205)


    # Eixos principais
    sub1 = fig.add_subplot(2, 2, 1) # 2 linhas, 2 colunas, somente uma célula
    sub1.scatter(steps, angles, s=2.5, color = '#7da8a9')
    #sub1.plot(steps, angles, color = 'green')
    sub1.set_xlim(100000, 250000)
    sub1.set_ylim(75, 95)
    sub1.ticklabel_format(axis="x", style='scientific', scilimits=(0,0))
    #sub1.set_ylabel(r"$\phi$ ($^\circ$)", labelpad = 16)

    # Segundo eixo, plot em cima a esquerda
    sub2 = fig.add_subplot(2, 2, 2) # 2 linhas, 2 colunas, segunda célula
    sub2.scatter(steps, angles, s=2, color = '#c7033d')
    sub2.set_xlim(350000, 500000)
    sub2.ticklabel_format(axis="x", style='scientific', scilimits=(0,0))
    sub2.set_ylim(75, 95)

    # Terceiro eixo, combinando primeira e segunda célula
    sub3 = fig.add_subplot(2, 2, (3, 4)) # 2 linhas, 2 colunas, Combinando terceira e quarta célula
    sub3.scatter(steps, angles, s=2.5, color = '#6f64c6', alpha = .7)
    sub3.set_xlim(0, 500000)
    sub3.ticklabel_format(axis="x", style='scientific', scilimits=(0,0))
    sub3.set_ylim(-125, 125)
    sub3.set_yticks([-120, -90, -60, 0, 60, 90, 120])
    #sub3.set_xlabel(r"Ciclo Monte Carlo", labelpad = 18)
    #sub3.set_ylabel(r"$\phi$ ($^\circ$)", labelpad = 18)

    fig.text(
          0.5,                      # Ordena posição x
          0.04,                     # Ordena posição y
          'Ciclo Monte Carlo',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large')

    fig.text(
          0.03,
          0.5,
          r"$\phi$ ($^\circ$)",
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large',
          rotation = 'vertical')

    # Criando blocos para Zoom
    sub3.fill_between((100000, 210000), -125, 125, facecolor='#7da8a9', alpha=0.3)
    sub3.fill_between((350000, 460000), -125, 125, facecolor='#d70641', alpha=0.25)

    # Linha da esquerda que se conecta do sub3 com sub1
    con1 = ConnectionPatch(xyA=(100000, 75), coordsA=sub1.transData,
                           xyB=(100000, 60), coordsB=sub3.transData, mutation_scale=100,
                           color = '#7da8a9', fc="w")
    # adicionando linha na figura
    fig.add_artist(con1)

    # linha da direita que se conecta entre sun3 e sub1
    con2 = ConnectionPatch(xyA=(248000, 75), coordsA=sub1.transData,
                           xyB=(210000, 60), coordsB=sub3.transData, color = '#7da8a9')
    # adicionando linha na figura
    fig.add_artist(con2)

    # Linha da esquerda que se conecta do sub3 com sub2
    con3 = ConnectionPatch(xyA=(350000, 75), coordsA=sub2.transData,
                           xyB=(350000, 60), coordsB=sub3.transData, color = '#d70641')
    # adicionando linha na figura
    fig.add_artist(con3)

    # Linha da esquerda que se conecta do sub3 com sub2
    con4 = ConnectionPatch(xyA=(500000, 75), coordsA=sub2.transData,
                           xyB=(460000, 60), coordsB=sub3.transData, color = '#d70641')
    # adicionando linha na figura
    fig.add_artist(con4)

    # salvando figuras com boa margem
    plt.savefig(nome + ".pdf", bbox_inches='tight')
    plt.savefig(nome + ".png", dpi=300, orientation='portrait',
                transparent = True, format='png', bbox_inches = 'tight', pad_inches = .1)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Receives a '.dat' file containing angles to plot the evolution with the steps.")
  parser.add_argument("fangles", help="path to the file containing the angles, one angle per line.")
  parser.add_argument("stepmult", nargs='?', help="step multiplier, the number of steps between each saved configuration (each angle)."
                      "Default is 1 and can changed to have an x-axis with the total number of steps", default=1)
  parser.add_argument("--shorttwist", help="prints a short twist graph with a range of interest.", action="store_true")
  #parser.add_argument("-I", "--interphi", type=int, help="range angle (default = 20)", default=20)
  args = parser.parse_args()

  dados = datas_steps_angles(args.fangles, args.stepmult)
  nome = os.path.splitext(args.fangles)[0]

  if args.shorttwist:
      plot_short_twist(dados[0], dados[1], nome)
  else:
      plot_torsion(dados[0], dados[1], nome)
