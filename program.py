#!/usr/bin/env python3

with open('codes.csv') as file:
    content = file.readlines()

    codeInput = input('Introduce el código de área telefónica: ')

    if '+' in codeInput:
        codeInput = codeInput.replace('+', '')

    for line in content:
        code, country = line.strip().split(',')

        if code == codeInput:
            print(f'El código de área telefónica +{code} es de {country}.')
