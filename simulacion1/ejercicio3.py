working = True
archivo = open("invocador.txt", "r", encoding="utf-8")

normal, solo, flex = 0, 0, 0
top, mid, jg, adc, supp = 0, 0, 0, 0, 0
asesinatos = 0
muertes = 0
asistencias = 0
victorias = 0
derrotas = 0

while working:
  print('''
    -------------------
          MENU
    -------------------
      1) Cantidad de partidas jugadas
      2) Carril preferido
      3) KDA
      4) Porcentaje de victorias en Clasificatorias
      5) Salir
  ''')

  opcion = int(input("Ingresa una opción: "))

  linea = archivo.readline().strip()
  while linea != "":
      tipo_partida = linea.split(",")[0]
      resultado = linea.split(",")[6]
      if tipo_partida == "NORMAL": normal += 1
      elif tipo_partida == "SOLO":
        solo += 1
        if resultado == "VICTORIA": victorias += 1
        elif resultado == "DERROTA": derrotas += 1
      elif tipo_partida == "FLEX":
        flex += 1
        if resultado == "VICTORIA": victorias += 1
        elif resultado == "DERROTA": derrotas += 1

      carril = linea.split(",")[1]
      if carril == "TOP": top += 1
      elif carril == "MID": mid += 1
      elif carril == "JG": jg += 1
      elif carril == "ADC": adc += 1
      elif carril == "SUPP": supp += 1

      asesinatos += int(linea.split(",")[3])
      muertes += int(linea.split(",")[4])
      asistencias += int(linea.split(",")[5])

      linea = archivo.readline().strip()

  if opcion == 1:
      print(f'''
      Partidas Jugadas:
        Normales: {normal}
        Clasificatorias Solo/Duo: {solo}
        Clasificatorias Flexibles: {flex}
      ''')
  elif opcion == 2:
    most_used, name = top, "Superior"
    if mid > most_used: most_used, name = mid, "Central"
    if jg > most_used: most_used, name = jg, "Jungla"
    if adc > most_used: most_used, name = adc, "Tirador"
    if supp > most_used: most_used, name = supp, "Soporte"

    print(f'Carril preferido: {name}')
  elif opcion == 3:
    kda = (asesinatos/muertes)+(asistencias/muertes)
    print(f'KDA: {kda}')
  elif opcion == 4:
    porcentaje_victorias = ((victorias/(victorias+derrotas))*100)
    print(f'Victorias en Clasificatorias: {porcentaje_victorias}%')
  elif opcion == 5:
    working = False
  else:
    opcion = int(input("Ingrese una opción válida: "))