import os

arquivo = "alunos.txt"

def cadastrar_aluno():
  nome = input("Nome do aluno: ")
  email = input("E-mail do aluno: ")
  curso = input("Curso do aluno: ")

  with open(arquivo, "a") as f:
    f.write(f"{nome},{email},{curso}\n")

def listar_alunos():
  with open(arquivo, "r") as f:
    for linha in f:
      nome, email, curso = linha.strip().split(",")
      print(f"Nome: {nome}")
      print(f"Email: {email}")
      print(f"Curso: {curso}")

def buscar_aluno():
  nome = input("Nome do aluno a ser buscado: ")

  with open(arquivo, "r") as f:
    for linha in f:
      if nome in linha:
        nome, email, curso = linha.strip().split(",")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"Curso: {curso}")
        break

while True:
  print("1. Cadastrar aluno")
  print("2. Listar alunos")
  print("3. Buscar aluno")
  print("4. Sair")

  opcao = input("Opção: ")

  if opcao == "1":
    cadastrar_aluno()
  elif opcao == "2":
    listar_alunos()
  elif opcao == "3":
    buscar_aluno()
  elif opcao == "4":
    break