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
  try:
    while True:
        limpar_tela()
        print("=== CRONÔMETRO DEVOPS ===")
        print(f"Tempo: {formatar_tempo(segundos)}")
        print("=========================")
        print("Pressione CTRL+C para parar.")
        time.sleep(1)
        segundos += 1
  except KeyboardInterrupt:
    print("\nCronômetro Pausado!")
