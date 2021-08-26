import random

file_domande = open("scegli_file.txt", "r").read()
var_lettura = open(file_domande + ".txt", "r").readlines()

n_domande = 0
for i in var_lettura:
    if i == "\n":
        n_domande += 1

domande_fatte = []
print("*********")

while True:
    cmd = input("")
    if cmd == "q":
        break
    else:
        prossima_domanda = random.randint(0, n_domande)
        ok = False
        while ok:
            prossima_domanda = random.randint(0, n_domande)
            for j in domande_fatte:
                if j == prossima_domanda:
                    ok = True
        c = 0
        for i in var_lettura:
            if c == prossima_domanda:
                print(i)
            if i == "\n":
                c += 1
            if c > prossima_domanda:
                break
        print("*********")
        domande_fatte.append(prossima_domanda)