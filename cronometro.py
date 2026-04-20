import time
import os

print("Cronômetro Iniciado!")

def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')

def formatar_tempo(segundos):
  minutos, segs = divmod(segundos, 60)
  return f"{minutos:02d}:{segs:02d}"

def iniciar_cronometro():
  segundos = 0
  rodando = True
  while True:
      try:
        if rodando:
          limpar_tela()
          print("=== CRONÔMETRO DEVOPS ===")
          print(f"Tempo: {formatar_tempo(segundos)}")
          print("=========================")
          print("Pressione CTRL+C para PAUSAR / OPÇÕES")
          time.sleep(1)
          segundos += 1
        else:
          limpar_tela()
          print("=== CRONÔMETRO PAUSADO ===")
          print(f"Tempo parado em: {formatar_tempo(segundos)}")
          print("=========================")
          opcao = input("Escolha: (V)oltar, (R)esetar ou (S)air e Pressione ENTER para confirmar").upper()
          if opcao == 'V':
            rodando = True
          elif opcao == 'R':
            segundos = 0
            rodando = True
          elif opcao == 'S':
            print("Encerrando...!")
            break
      except KeyboardInterrupt:
        rodando = False
    

if __name__ == "__main__":
    input("Pressione ENTER para iniciar a contagem...")
    iniciar_cronometro()
