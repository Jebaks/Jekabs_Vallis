krasas = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
for atslega in sorted(krasas):
    print(atslega,'-',krasas[atslega]) #sakārtots pēc atslēgas augošā secībā
for atslega in sorted(krasas):
    print(krasas[atslega])
veikals = {
    'banāni':12,
    'apelsīni':32,
    'arbūzi':21,
    'mandarīni':17,
    'vīnogas':15
}
kartots=sorted(veikals,key=veikals.get)
for vertiba in kartots:
    print(vertiba,veikals[vertiba])

    kartots = sorted(veikals,key=veikals.get)
kartota_vardnica = {}

for key in kartots:
    kartota_vardnica[key] = veikals[key]
print(kartota_vardnica)