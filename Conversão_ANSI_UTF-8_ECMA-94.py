def con_utf8(vetor):
    win1252ex = [128,130,131,132,133,134,135,136,137,138,139,140,142,145,146,147,148,149,150,151,152,153,154,155,156,158,159]
    win1252utf8 = ["E2 82 AC","E2 80 9A","C6 92","E2 80 9E","E2 80 A6","E2 80 A0","E2 80 A1","CB 86","E2 80 B0","C5 A0","E2 80 B9","C5 92","C5 BD","E2 80 98","E2 80 99","E2 80 9C","E2 80 9D","E2 80 A2","E2 80 93","E2 80 94","CB 9C","E2 84 A2","C5 A1","E2 80 BA","C5 93","C5 BE","C5 B8"]
    texto_utf8 = ""
    for i in range(0, len(vetor)):
        if vetor[i] <= 127:
            aux = hex(vetor[i])
        elif vetor[i] > 127 and vetor[i] < 160:
            for j in range(0, len(win1252ex)):
                if vetor[i] == win1252ex[j]:
                    texto_utf8 += win1252utf8[j] + " "
                    aux = ""
                    break
        elif vetor[i] > 159 and vetor[i] <= 191:
            aux = hex(vetor[i])
            texto_utf8 += "C2 "
        elif vetor[i] > 191:
            aux = hex(vetor[i]-64)
            texto_utf8 += "C3 "
        aux = str(aux)
        aux = aux[2:]
        aux = aux.upper()
        texto_utf8 += aux
        if i < len(vetor)-1 and (vetor[i]<=127 or vetor[i]>159):
            texto_utf8 += " "
    return texto_utf8

def con_ecma94(vetor):
    texto_ecma94 = ""
    for i in range(0, len(vetor)):
        if chr(vetor[i]) in """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ""":
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
#print(len(vetor)) TESTE

texto_utf8 = con_utf8(vetor)
#print(texto_utf8)
texto_ecma94 = con_ecma94(vetor)
#print(texto_ecma94)
fil = open("saída.txt", 'w')
fil.write("UTF-8: " + texto_utf8 + "\n\nECMA-94: " + texto_ecma94)


arc.close()
fil.close()
