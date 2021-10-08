# dicetools_frag

Neste repositório serão armazenados scripts que resolvem problemas específicos de rotação em moléculas. 
Os scripts são casos particulares do repositório https://github.com/hmcezar/dicetools, Henrique M. Cezar, Clustering Traj, (2020), GitHub repository. 

## plot_eff_tors.py

Originalmente esse script é utilizado para calcular o perfil de energia devido a rotação "livre" em moléculas, ou seja leva em consideração a rotação nos intervalos [0,360) ou [-180,180). Em nosso caso desejamos utilizar o script para rotacionar a molécula em ângulos específicos, como por exemplo (-25, 25) graus, portanto em um intervalo (-i, i). Logo, foram realizadas pequenas modificações no script para que essa funcionalidade fosse adicionada. 
