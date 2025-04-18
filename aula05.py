def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
            if entrada.lower() == 'fim':
                break

            nota = float(entrada)
            if 0 <= nota <=10:
                notas.append(nota)

            else:
                print("Nota invalida. Digite um valor de 0 a 10.")
        
        except ValueError:
            print("Entrada Inválida. Por favor digite um numero ou 'fim'.")

            if notas:
                media = sum(notas) / len(notas)
                print(f"\nMédia da turma: {media:2f}")
                print(f"Total de notas validas registradas: {len(notas)}")

            else:
                print("Nenhuma nota válida registrada")

registrar_notas()