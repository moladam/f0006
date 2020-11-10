évszak = input('Nyár van, vagy ősz? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if szél == 'n' and (évszak == 'ny' or (évszak == 'ő' and esik == 'n')):
    print('megyünk')
else:
    print('maradunk')