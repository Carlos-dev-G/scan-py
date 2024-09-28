from Scan import Scan

# Cambia la IP por la que desees escanear
scanner = Scan('45.33.32.156', print_result=False)  # close_port=False para no incluir cerrados
scanner.range_scan(max_port=1500, save_json=True)

# Accediendo a los resultados
print("Puertos abiertos:",scanner.resultado['OPEN'])  # Solo se imprimen los puertos abiertos
