skaitli = [i for i in range (41)]
for j in skaitli:
    if j/4 ==int(j/4) and j/2 == int(j/2):#pārbauda vai skaitlis dalās gan ar 2 gan ar 4
        print(j,'Dalos gam ar 2, gan ar 4')
    elif j/2 == int(j/2):#pārbauda vai skaitlis dalās ar 2
        print(j,'Dalos ar 2')
    elif j/4 == int(j/4):
        print(j,'Dalos ar 4')
    else:
        print(j)#izvada skaitli, kas dalās ne ar 2, ne ar 4