times = ('BOTAFOGO','Palmeiras','Red Bull Bragantino','Fluminense','Grêmio','Flamengo',
         'Fortaleza','Athletico-PR','Atlético-MG','Cuiabá','Cruzeiro','Internacional',
         'São Paulo','Corinthians','Goiás','Bahia','Santos','Vasco','América-MG','Coritiba')
print(f'Aqui estão os 5 primeiros colocados: {times[0:5]}')
print(20 * '=-')
print(f'Aqui estão os 5 primeiros colocados: {times[-4:]}')
print(20 * '=-')
print(sorted(times))
print(20 * '=-')
time = 'Internacional'
pos = times.index(time) + 1
print(f'O Internacional está na posição {pos}')