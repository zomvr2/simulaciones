file = open("datos.txt", "r", encoding="utf-8")

linea = file.readline().strip()

# Estadisticas
total_contagios = 0
america_mayor_name, europa_mayor_name, asia_mayor_name = "", "", ""
america_mayor, europa_mayor, asia_mayor = 0, 0, 0
america_menor_name, europa_menor_name, asia_menor_name = "", "", ""
america_menor, europa_menor, asia_menor = 9999999999, 9999999999, 9999999999
max_recuperados, recuperados_name = 0, ""
min_deaths, min_deaths_country = 9999999999, ""

while linea != "":
  continente, paises = "", 0
  es_continente = len(linea.split(",")) == 2
  recuperados_continente = 0

  if es_continente:
    partes = linea.split(",")
    continente, paises = partes[0], int(partes[1])
    for i in range(paises):
      linea = file.readline().strip()
      pais_parts = linea.split(",")

      total_contagios += int(pais_parts[1])
      contagios_pais = int(pais_parts[1])
      recuperados_continente += int(pais_parts[3])

      if recuperados_continente > max_recuperados: max_recuperados, recuperados_name = recuperados_continente, continente
      if int(pais_parts[4]) < min_deaths: min_deaths, min_deaths_country = int(pais_parts[4]), pais_parts[0]

      if continente == "America":
        if contagios_pais > america_mayor:
          america_mayor = contagios_pais
          america_mayor_name = pais_parts[0]
        elif contagios_pais < america_menor:
          america_menor = contagios_pais
          america_menor_name = pais_parts[0]
      elif continente == "Europa":
        if contagios_pais > europa_mayor:
          europa_mayor = contagios_pais
          europa_mayor_name = pais_parts[0]
        elif contagios_pais < europa_menor:
          europa_menor = contagios_pais
          europa_menor_name = pais_parts[0]
      elif continente == "Asia":
        if contagios_pais > asia_mayor:
          asia_mayor = contagios_pais
          asia_mayor_name = pais_parts[0]
        elif contagios_pais < asia_menor:
          asia_menor = contagios_pais
          asia_menor_name = pais_parts[0]

  linea = file.readline().strip()

print(f'''
América:
  Mayor Contagio: {america_mayor_name} ({america_mayor})
  Menor Contagio: {america_menor_name} ({america_menor})
Europa:
  Mayor Contagio: {europa_mayor_name} ({europa_mayor})
  Menor Contagio: {europa_menor_name} ({europa_menor})
Asia:
  Mayor Contagio: {asia_mayor_name} ({asia_mayor})
  Menor Contagio: {asia_menor_name} ({asia_menor})
Cantidad total de contagios: {total_contagios}
Pais con mayor cantidad de contagios por millon de habitantes:
Continente con mayor cantidad de recuperados: {recuperados_name} ({max_recuperados})
Pais con menor cantidad de victimas fatales: {min_deaths_country} ({min_deaths})
''')