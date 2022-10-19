w=dict()
w1=dict()
q=(input("Введіть назву країни :"))
w[q]='Населення'+q
w1[q]='Площа'+q
w['Germany']='Населення:83млн'
w1['Germany']='Площа :357,588 km^2'
w['Poland']='Населення:37,95mln'
w1['Poland']='Площа:322,575 km^2'
w['Slovakia']='Населення:5,459mln'
w1['Slovakia']='Площа:49,035 km^2'
if q=='Poland':
    print(w['Poland']+' '+w1['Poland'])
elif q=='Germany':
    print(w['Germany']+' '+w1['Germany'])
elif q=='Slovakia':
    print(w['Slovakia']+' '+w1['Slovakia'])



