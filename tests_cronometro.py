# Testes de Formatação de Tempo do Cronômetro

import cronometro

def teste_tempo_zero():
  assert cronometro.formatar_tempo(0) == "00:00"

def teste_tempo_segundos():
  assert cronometro.formatar_tempo(30) == "00:30"

def teste_tempo_minuto():
  assert cronometro.formatar_tempo(60) == "01:00"

def teste_tempo_misto():
  assert cronometro.formatar_tempo(90) == "01:30"

def teste_tempo_grande():
  assert cronometro.formatar_tempo(600) == "10:00"
