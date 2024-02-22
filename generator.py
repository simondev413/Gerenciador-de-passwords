#!python3
#pw.py - um gerenciador de password
import random

class Generator:

    def generatePwd():
        char = '0123456789abcdfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#-&%$<>'
        pwd = ''
        for i in range(8):
            pwd += char[random.randint(0,len(char) -1)]
        return pwd



