lista=[]

if len(lista)==0:
    resp = True
    while resp == "si":
        lista.append(input("Dame una palabra o frase: ")).upper()
        resp = input("Deseas solicitar otra frase? Si/No").lower().strip()
    print(lista)