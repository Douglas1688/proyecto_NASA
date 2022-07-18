from num2words import num2words
valor = "123,93"
try:
    if "," in valor:
        lista = valor.split(",")
        dol = num2words(int(lista[0]), lang='es')
        cen = num2words(int(lista[1]),lang='es')
        print("{} dólares con {} centavos".format(dol.capitalize(), cen.capitalize()))
    else:
        dol = num2words(int(valor), lang='es')
        print("{} dólares con {} centavos".format(dol.capitalize()))
except Exception as e:
    print(e)