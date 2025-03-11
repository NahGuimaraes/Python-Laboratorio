def is_palindramo(texto):
    texto_limpo = '' .join(char.lower()
                           for char in texto
                           if char.isalnum())
    return texto_limpo == texto_limpo[:: -1]

frase = "A cara rajada da jacaraca"
resultado = is_palindramo(frase)

if resultado == True:
    print(f'A frase "{frase}" é um palíndromo')

else:
    print(f'A frase "{frase}" não é um palíndromo')