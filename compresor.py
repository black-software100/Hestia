from patoolib import extract_archive, create_archive
import os
from  shutil import make_archive


def Descompresor():
    file = input("Arraste aqui el archivo a descomprimir: ")
    extract_archive(file)



def Descomprimir(file):
    extract_archive(file)