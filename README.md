# Mini Librería de Escaneo de Puertos

Esta librería permite escanear puertos en una dirección IP específica y guardar los resultados en un archivo JSON. Utiliza `ThreadPoolExecutor` para realizar escaneos de manera concurrente.

## Instalación

No es necesario instalar paquetes adicionales, ya que esta librería utiliza solo módulos estándar de Python.

## Uso

### Clase `Scan`

La clase `Scan` es la principal de esta librería. Permite escanear puertos abiertos y cerrados en una dirección IP.

#### Constructor

```python
Scan(IP: str = None, WORKERS: int = 1000, close_port: bool = False, print_result: bool = False)
```

- **Parámetros**:
  - `IP` (str): Dirección IP a escanear. Si no se proporciona, se usa `'127.0.0.1'`.
  - `WORKERS` (int): Número máximo de hilos para el escaneo. Por defecto es `1000`.
  - `close_port` (bool): Indica si se deben mostrar los puertos cerrados. Por defecto es `False`.
  - `print_result` (bool): Indica si se deben imprimir los resultados en la consola. Por defecto es `False`.

#### Métodos

## (Método 1) `full_scan(save_json: bool = True) -> None`

Escanea todos los puertos del 1 al 65535 y guarda los resultados en un archivo JSON.

- **Parámetros**:
  - `save_json` (bool): Indica si se deben guardar los resultados en un archivo JSON. Por defecto es `True`.

**Ejemplo**:

```python
from scanner import Scan

scanner = Scan('192.168.1.1', print_result=True, close_port=True)
scanner.full_scan()
```

## (Método 2) `range_scan(max_port: int, save_json: bool = True) -> None`

Escanea un rango específico de puertos.

- **Parámetros**:
  - `max_port` (int): Número máximo de puerto hasta donde se desea escanear.
  - `save_json` (bool): Indica si se deben guardar los resultados en un archivo JSON. Por defecto es `True`.

**Ejemplo**:

```python
from scanner import Scan

scanner = Scan('192.168.1.1', print_result=True, close_port=False)
scanner.range_scan(max_port=1000)
```

#### Resultados

Los resultados se almacenan en un diccionario dentro de la clase `Scan` y se pueden acceder a través del atributo `resultado`. Los resultados se dividen en dos listas:

- `resultado['OPEN']`: Lista de puertos abiertos.
- `resultado['CLOSE']`: Lista de puertos cerrados (si `close_port` es `True`).

### Guardar Resultados en JSON

Los resultados del escaneo se guardan automáticamente en un archivo llamado `result.json`, a menos que se indique lo contrario al llamar a los métodos `full_scan` o `range_scan`.

### Ejemplo Completo

Aquí tienes un ejemplo completo que muestra cómo utilizar la librería para escanear puertos:

```python
from Scan import Scan

# Cambia la IP por la que desees escanear
scanner = Scan('45.33.32.156', print_result=False)  # close_port=False para no incluir cerrados
scanner.range_scan(max_port=1500, save_json=True)

# Accediendo a los resultados
print("Puertos abiertos:", scanner.resultado['OPEN'])  # Solo se imprimen los puertos abiertos
print("Puertos cerrados:", scanner.resultado['CLOSE']) # Solo se imprimen los puertos cerrados
```

## Conclusión

Esta librería proporciona una forma sencilla y eficiente de escanear puertos en una dirección IP específica. Puedes personalizar el comportamiento del escaneo mediante los parámetros del constructor y los métodos disponibles.

Para más información, consulta el código fuente y la implementación.