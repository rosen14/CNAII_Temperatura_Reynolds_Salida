# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:07:07 2024

@author: Rosendo Fazzari
"""

import argparse
from library import get_Reout, get_Tout


def main():
    parser = argparse.ArgumentParser(description='Cálculo de temperatura y \
                                     Reynolds a la salida de la sección.')
    
    # Argumentos a ingresar por consola
    parser.add_argument('--P', type=float, required=True, help='Presión [barg]')
    parser.add_argument('--T_in', type=float, required=True, help='Temperatura entrada °C')
    parser.add_argument('--Q', type=float, required=True, help='Potencia [kW]')
    parser.add_argument('--mp', type=float, required=True, help='Caudal Másico [kg/s]')
    parser.add_argument('--fluid', type=str, required=False,
                        default = 'R134a', choices = ['R134a', 'Water'])
    
    parser.add_argument('--T_out', action='store_true',
                        help='Devolver la temperatura de salida en °C')
    parser.add_argument('--Re_out', action='store_true',
                        help='Devolver el nro de Reynolds a la salida')
    
    # Parseo los argumentos
    args = parser.parse_args()
    
    # Cálculos
    T_out = get_Tout(args.Q, args.T_in, args.P, args.mp, fluid = args.fluid)
    Re_out = get_Reout(args.P, T_out, args.mp, fluid = args.fluid)
    
    # Impresión de resultados
    if args.T_out and args.Re_out:
        print(f'T_out = {round(T_out,2)} °C\nRe_out = {round(Re_out,0)}')
    elif args.T_out:
        print(f'T_out = {round(T_out,2)} °C')
    elif args.Re_out:
        print(f'Re_out = {round(Re_out,0)}')
        
if __name__ == '__main__':
    main()
    
