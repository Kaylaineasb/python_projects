frase = 'O python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'
i=0
apareceu_mais_vezes=0
letra_apareceu_mais_vezes=''
while i<len(frase):
    letra_atual=frase[i]
    if letra_atual==' ':
        i+=1
        continue
    qtd = frase.count(letra_atual)
    if apareceu_mais_vezes<qtd:
        apareceu_mais_vezes=qtd
        letra_apareceu_mais_vezes=letra_atual
    i+=1
print(
    'A letra que apareceu mais vezes foi'
      f' "{letra_apareceu_mais_vezes}" que apareceu'
      f' {apareceu_mais_vezes}x'
)