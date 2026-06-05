import json
import os
import sys
from serial.tools import list_ports

DEFAULT_CONFIG = {
    "port": None,
    "baudrate": 9600,
    "bits": 8,
    "parity": "None",
    "stopbits": 1,
    "timeout": 5
}


def get_config_path():
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "config.json")


def load_config():
    path = get_config_path()
    try:
        with open(path, 'r') as f:
            cfg = json.load(f)
            for k in DEFAULT_CONFIG:
                cfg.setdefault(k, DEFAULT_CONFIG[k])
            return cfg
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()


def save_config(config):
    path = get_config_path()
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"Configuración guardada en: {path}")


def list_available_ports():
    all_ports = list(list_ports.comports())
    filtered = [p for p in all_ports if p.description and p.description != 'n/a']
    return filtered if filtered else all_ports


def auto_detect_port():
    ports = list_available_ports()
    if len(ports) == 0:
        return None, None, "ERROR 001: No se encontraron puertos seriales disponibles."
    elif len(ports) == 1:
        return ports[0].device, None, None
    else:
        return None, ports, None
