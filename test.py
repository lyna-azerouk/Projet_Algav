#creation de l'arbre exemple (figure 1 de l'enonce)

trueGGD=Arbre('TrueGGD')
trueGGD.mot_luka="True"
falseGGG=Arbre('FalseGGG')
falseGGG.mot_luka="False"
x1GG=Arbre('x1GG')
x1GG.mot_luka="x1(False)(True)"
x1GG.G=falseGGG
x1GG.D=trueGGD

trueGDG=Arbre('TrueGDG')
trueGDG.mot_luka="True"
falseGDD=Arbre('FalseGDD')
falseGDD.mot_luka="False"
x1GD=Arbre('x1GD')
x1GD.mot_luka="x1(True)(False)"
x1GD.G=trueGDG
x1GD.D=falseGDD

trueDGD=Arbre('TrueDGD')
trueDGD.mot_luka="True"
falseDGG=Arbre('FalseDGG')
falseDGG.mot_luka="False"
x1DG=Arbre('x1DG')
x1DG.mot_luka="x1(False)(True)"
x1DG.G=falseDGG
x1DG.D=trueDGD

falseDDG=Arbre('FalseDDG')
falseDDG.mot_luka="False"
falseDDD=Arbre('FalseDDD')
falseDDD.mot_luka="False"
x1DD=Arbre('x1DD')
x1DD.mot_luka="x1(False)(False)"
x1DD.G=falseDDG
x1DD.D=falseDDD

x2G=Arbre('x2G')
x2G.mot_luka="x2(x1(False)(True))(x1(True)(False))"
x2G.G=x1GG
x2G.D=x1GD
x2D=Arbre('x2D')
x2D.mot_luka="x2(x1(False)(True))(x1(False)(False))"
x2D.G=x1DG
x2D.D=x1DD
root=Arbre('rootx3')
root.mot_luka="x3(x2(x1(False)(True))(x1(True)(False)))(x2(x1(False)(True))(x1(False)(False)))"
root.G=x2G
root.D=x2D