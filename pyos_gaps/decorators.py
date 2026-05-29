import os
from pathlib import Path


def verify_pyos_dir_errorlevel():
    """
    Verifica se esiste la cartella 'pythonos'.

    Ritorna:
    0 = cartella esiste
    1 = cartella non esiste
    """

    base_dir = Path(__file__).parent

    if (base_dir / "pythonos").is_dir():
        return 0
    else:
        return 1


def verify_pyos_dir():
    verification = verify_pyos_dir_errorlevel()

    if verification == 0:
        print("", end="")
    else:
        raise Exception("Cartella 'pythonos' non trovata!")
