# Exercícios
# Ex2 e Ex3: Definição de hora.

class Hora

# AM: Ante Meridiem (antes do meio-dia)
# PM: Post Meridiem (depois do meio-dia)

  def __init__(self, hora, periodo):

    self.hora = hora
    self.periodo = periodo

  def tempo(self, tempo):

    r = tempo % 12
    p = tempo // 12

    if p % 2 == 0:
      # A parâmetro período não sel altera
    else:
      # O parâmetro período se altera.

    Teste de github 
