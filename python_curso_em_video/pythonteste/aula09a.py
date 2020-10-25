frase = 'Curso em Vídeo Python'
fraseDois = '   Aprenda Python  '
fraseTres = ['Curso', 'em', 'Vídeo', 'HTML', 'e', 'CSS']
print("""Lorem ipsum dolor sit amet consectetur, adipisicing elit.
Necessitatibus placeat incidunt debitis officia a eum tenetur sed
corporis doloremque accusantium, reiciendis repellendus labore
asperiores fuga modi tempore impedit, eaque cum. Autem recusandae
facilis est accusamus accusantium, provident possimus ex dolores
aspernatur, temporibus ipsam quod quas ut, reiciendis aliquid
similique tenetur quos. Quae molestias expedita aut perferendis
repudiandae aliquid ullam! Repudiandae!.""")

print('=>   a posição 9: ', frase[9])
print('=>   de uma posição até a posição anterior:', frase[9:13])
print('=>   de uma posição até o anterior, de dois em dois: ', frase[9:21:2])
print('=>   iniciais, até o anterior: ', frase[:5])
print('=>   de uma posição até o fim: ', frase[9:])
print('=>   saltando de dois em dois', frase[::2])
print('=>   de uma posição até o fim, de três em três: ', frase[9::3])
print('=>   quantidade / comprimento: ', len(frase))
print('=>   quantidade desse caractere: ', frase.count('o'))
print('=>   quantidade desse caractere, dentro do intervalo, até o anterior: ', frase.count('o', 0, 13))
print('=>   posição onde se inicia esse trecho:', frase.find('deo'))
print('=>   retorna True ou False para o trecho:', 'Curso' in frase)
print('=>   substitui o trecho:', frase.replace('Python', 'HTML / CSS'))
print('=>   transforma para uppercase:', frase.upper())
print('=>   transforma para lowercase:', frase.lower())
print('=>   transforma só o primeiro caractere para uppercase:', frase.capitalize())
print('=>   transforma o primeiro caractere de cada palavra para upppercase:', frase.title())
print('=>   remove os espaços externos:', fraseDois.strip())
print('=>   remove só os espaços vazios da direita:', fraseDois.rstrip())
print('=>   remove só os espaços vazios da esquerda:', fraseDois.lstrip())
print('=>   converte em lista, podendo definir o seperador e numero de índices:', frase.split(' ', 3))
print('=>   converte a lista em string, com um separador:', (' - '.join(fraseTres)))
