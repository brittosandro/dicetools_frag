# dicetools_frag

Neste repositório serão armazenados scripts que resolvem problemas específicos de rotação em moléculas. 
Os scripts são casos particulares do repositório https://github.com/hmcezar/dicetools, Henrique M. Cezar, dicetools, (2018), GitHub repository. 

## plot_eff_tors.py

Originalmente esse script é utilizado para calcular o perfil de energia devido a rotação "livre" em moléculas, ou seja leva em consideração a rotação nos intervalos [0,360) ou [-180,180). Em nosso caso desejamos utilizar o script para rotacionar a molécula em ângulos específicos, como por exemplo (-25, 25) graus, portanto em um intervalo (-i, i). Logo, foram realizadas pequenas modificações no script para que essa funcionalidade fosse adicionada. 

## dihedral_step_evolution.py

Esse script plota a evolução de um diedro de interesse a medida que a simulação ocorre. Adicionamos uma funcionalidade para que seja plotada um zoom em um certo intervalo de evolução do diedro. É necessário que se leia o código e modifique o zoom no próprio script, neste primeiro momento.
