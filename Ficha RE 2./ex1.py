import re
texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

def iso_8601(texto):
  return re.sub(r"(\d{2})/(\d{2})/(\d{4})",r"\3-\2-\1",texto)

print(iso_8601(texto))