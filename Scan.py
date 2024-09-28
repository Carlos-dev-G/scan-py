import socket
import json
from concurrent.futures import ThreadPoolExecutor


class Scan:
    __slots__ = ['IP', 'WORKERS', 'close_port', 'resultado', 'print_result']

    def __init__(self, IP: str = None, WORKERS: int = 1000, close_port: bool = False, print_result: bool = False) -> None:
        """
        Inicializa la clase Scan.

        :param IP: Dirección IP a escanear. Si no se proporciona, se usa '127.0.0.1'.
        :param WORKERS: Número máximo de hilos para el escaneo. Por defecto es 1000.
        :param close_port: Indica si se deben mostrar los puertos cerrados. Por defecto es False.
        """
        self.IP = IP if IP else '127.0.0.1'
        self.WORKERS = WORKERS
        self.close_port = close_port
        self.print_result = print_result
        self.resultado = {
            "OPEN": [],
            "CLOSE": []
        }

    def __json_save(self) -> None:
        """Guarda los resultados en un archivo JSON."""
        with open('result.json', 'w') as resultados_json:
            json.dump(self.resultado, resultados_json)

    def __scan_port(self, puerto: int) -> None:
        """
        Escanea un puerto específico.

        :param puerto: Número del puerto a escanear.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)  # Reducir el tiempo de espera para acelerar
            resultado_conexion = sock.connect_ex((self.IP, puerto))

            if resultado_conexion == 0:
                if self.print_result:
                    print(f"OPEN: {puerto}")
                self.resultado['OPEN'].append(puerto)
            elif self.close_port:
                if self.print_result:
                    print(f"CLOSE: {puerto}")
                self.resultado['CLOSE'].append(puerto)

    def full_scan(self, save_json: bool = True) -> None:
        """
        Escanea todos los puertos del 1 al 65535.
        Utiliza ThreadPoolExecutor para paralelizar el escaneo.
        """
        with ThreadPoolExecutor(max_workers=self.WORKERS) as executor:
            executor.map(self.__scan_port, range(1, 65536))

        # Ordenar resultados
        self.resultado['OPEN'].sort()
        if self.close_port:
            self.resultado['CLOSE'].sort()

        if save_json:
            self.__json_save()

    def range_scan(self, max_port: int, save_json: bool = True) -> None:
        """
        Escanea un rango específico de puertos.

        :param max_port: Número máximo de puerto hasta donde se desea escanear.
        """
        with ThreadPoolExecutor(max_workers=self.WORKERS) as executor:
            executor.map(self.__scan_port, range(1, max_port + 1))

        # Ordenar resultados
        self.resultado['OPEN'].sort()
        if self.close_port:
            self.resultado['CLOSE'].sort()

        if save_json:
            self.__json_save()
