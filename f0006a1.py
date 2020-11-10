évszak = input('Nyár van, vagy ősz? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if évszak == 'ny' and szél == 'n':
    print('megyünk')
if évszak == 'ő' and esik == 'n' and szél == 'n':
    print('megyünk')