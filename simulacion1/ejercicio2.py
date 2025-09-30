registrando = True

viviana, constanza, jennifer = 0, 0, 0
total_votos = 0
eliminada = ""

while registrando:
  cant_votos = int(input("Cantidad de votos: "))
  if cant_votos == -1:
    registrando = False
  else:
    nombre = input("Votar eliminado (NOMBRE 3331): ").lower()
    if " 3331" in nombre:
      voto_name = nombre.split(" ")[0]
      if voto_name == "viviana": viviana += cant_votos
      elif voto_name == "constanza": constanza += cant_votos
      elif voto_name == "jennifer": jennifer += cant_votos

      if viviana > (constanza and jennifer): eliminada = "viviana"
      elif constanza > (viviana and jennifer): eliminada = "constanza"
      elif jennifer > (viviana and constanza): eliminada = "jennifer"

      total_votos += cant_votos
    else:
      print("VOTO NO REGISTRADO: Se necesita el formato NOMBRE 3331 para que voto sea válido!")

print(f'''
Placa de eliminación:
Viviana: {viviana} {(viviana/total_votos)*100}%
Constanza: {constanza} {(constanza/total_votos)*100}%
Jennifer: {jennifer} {(jennifer/total_votos)*100}%
Eliminada: {eliminada}
''')