def con_utf8(vetor):
    texto_utf8 = ""
    for i in range(0, len(vetor)):
        if vetor[i] <= 127:
            aux = hex(vetor[i])
        elif vetor[i] > 127 and vetor[i] <= 191:
            aux = hex(vetor[i])
            texto_utf8 += "C2 "
        elif vetor[i] > 191:
            aux = hex(vetor[i]-64)
            texto_utf8 += "C3 "
        aux = str(aux)
        aux = aux[2:]
        aux = aux.upper()
        texto_utf8 += aux
        if i < len(vetor)-1:
            texto_utf8 += " "
    return texto_utf8

def con_ecma94(vetor):
    texto_ecma94 = ""
    for i in range(0, len(vetor)):
        aux = hex(vetor[i])
        aux = str(aux)
        aux = aux[2:]
        aux = aux.upper()
        texto_ecma94 += aux
        if i < len(vetor)-1:
            texto_ecma94 += " "
    return texto_ecma94
    


# Aqui se espera uma entrada com o caminho relativo ou absoluto do arquivo.
via = input("nome do arquivo: ")
arc = open(via, 'rb') # isso talvez de errado
scr = arc.read()

# Converte o texto em um vetor de inteiros com os respectivos códigos de cada carácter
vetor = []
for i in range(0, len(scr)):
    aux = scr[i]
    vetor.append(aux)
#print(vetor)

texto_utf8 = con_utf8(vetor)
#print(texto_utf8)
texto_ecma94 = con_ecma94(vetor)
#print(texto_ecma94)
fil = open("saída.txt", 'w')
fil.write("UTF-8: " + texto_utf8 + "\n\nECMA-94: " + texto_ecma94)


arc.close()
fil.close()