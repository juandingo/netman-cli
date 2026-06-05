# netman-cli

Herramienta CLI para administración de equipos de red (switches, routers, firewalls) vía puerto serial.

## Características actuales

- Conexión serial a switches (Cisco, HP, Dell, Juniper, etc.)
- Auto-detección de puertos disponibles
- Envío interactivo de comandos
- Obtención de `show version`, `show running-config`
- Exportación de datos a Excel (marca, modelo, firmware, MAC, IP, etc.)
- Reinicio a fábrica (borrado de flash, `write erase`, `reload`)
- Test de puertos con detección de enlace

## Requisitos

- Python 3.8+
- `pyserial`
- `openpyxl`

## Instalación

```bash
pip install -r requirements.txt
python main.py
```

## Uso

Al ejecutar, el menú principal ofrece:

1. Conectar al dispositivo
2. Enviar comando
3. Ver configuración actual
4. Información del dispositivo
5. Configuración serial
6. Exportar datos a Excel
7. Reinicio a fábrica
8. Testear puertos del switch

## Roadmap / A futuro

- [ ] Soporte para routers y firewalls
- [ ] Conexión vía SSH y Telnet
- [ ] Backup automatizado de configuraciones
- [ ] Soporte para más marcas y sistemas operativos de red
- [ ] Mejorar el menú principal (navegación, submenús, atajos)
