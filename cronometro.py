import time
import os

print("Cronômetro Iniciado!")

def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')

def formatar_tempo(segundos):
  minutos, segs = divmod(segundos, 60)
  return f"{minutos:02d}:{segs:02d}"
