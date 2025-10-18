# Informações das notas do aluno
n1 = int(input('Digite a primeira nota, de 0 a 100:'))
n2 = int(input('Digite a segunda nota, de 0 a 100:'))
n3 = int(input('Digite a terceira nota, de 0 a 100:'))
n4 = int(input('Digite a quarta nota, de 0 a 100:'))

# Cálulo da media do aluno
media = (n1 + n2 + n3 + n4)/4

# Informação da aprovação ou não:
if media >= 50:
    print(f"O aluno está aprovado, com media {media}")
else:
    print(f"O aluno está reprovado, com media {media}")