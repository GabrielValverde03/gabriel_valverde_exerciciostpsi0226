segundos = int(input("Insira o número de segundos: "))

horas = segundos // 3600
resto_segundos = segundos % 3600

minutos = resto_segundos // 60
seg = resto_segundos % 60

if horas > 0 and minutos > 0 and seg > 0:
    print(f"{horas} hora(s), {minutos} minuto(s) e {seg} segundo(s)")
elif horas <= 0 and minutos > 0 and seg > 0:
    print(f"{minutos} minuto(s) e {seg} segundo(s)")
elif horas <= 0 and minutos <= 0 and seg > 0:
    print(f"{seg} segundo(s)")
elif horas <= 0 and minutos > 0 and seg <= 0:
    print(f"{minutos} minuto(s)")
elif horas > 0 and minutos > 0 and seg <= 0:
    print(f"{horas} hora(s) e {minutos} minuto(s)")
elif horas > 0 and minutos <= 0 and seg <=0:
    print(f"{horas} hora(s)")
else:
    print(f"{horas} hora(s) e e {seg} segundo(s)")