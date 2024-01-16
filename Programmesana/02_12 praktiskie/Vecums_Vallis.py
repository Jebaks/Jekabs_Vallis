vecums = input('ievadiet suņa vecumu:')
vecums = float(vecums)
if vecums < 0:
    print('nepareizs vecums')
elif vecums <= 2:
    print(vecums*10.5)
else:
    print(2*10.5+(vecums-2)*4)#izvada pirmo divu gadu reizinajumu ar 10,5 un tos 2 gadus atņem no visa vecuma, jo tos jau reizināja ar 10,5 un nevajag reizināt ar 4