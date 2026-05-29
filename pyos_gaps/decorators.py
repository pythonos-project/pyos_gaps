import os


def verify_pyos_dir_errorlevel():
    """
    Verifica se esiste la cartella 'pythonos'.

    Ritorna:
    0 = cartella esiste
    1 = cartella non esiste
    """

    if is_dir("pythonos"):
        return 0
    else:
        return 1


def verify_pyos_dir():
    verification = verify_pyos_dir_errorlevel()

    if verification == 0:
        print("", end="")
    else:
        raise Exception("Cartella 'pythonos' non trovata!")
