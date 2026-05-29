from pathlib import Path


def gaps_perc():
    pathperc = Path(__file__).resolve().parent.parent.parent.parent
    return pathperc
