# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:07:07 2024

@author: Rosendo Fazzari
"""

import argparse
from library import get_Reout, get_Tout


def main():
    parser = argparse.ArgumentParser(description='Verificar si tres números tienen el mismo signo.')
    
    # Agregar argumentos
    parser.add_argument('--P', type=float, required=True, help='Presión [barg]')
    parser.add_argument('--T_in', type=float, required=True, help='Temperatura entrada °C')
    parser.add_argument('--Q', type=float, required=True, help='Potencia [kW]')
    parser.add_argument('--mp', type=float, required=True, help='Caudal Másico [kg/s]')
    parser.add_argument('--T_out', action='store_true',
                        help='Devolver la temperatura de salida en °C')
    parser.add_argument('--Re_out', action='store_true',
                        help='Devolver el nro de Reynolds a la salida')
    # Parsear los argumentos
    args = parser.parse_args()

    T_out = get_Tout(args.Q, args.T_in, args.P, args.mp, fluid = 'R134a' )
    Re_out = get_Reout(args.P, T_out, args.mp, fluid = 'R134a' )
    # Verificar si los números tienen el mismo signo
    if args.T_out and args.Re_out:
        print(f'T_out = {T_out} °C\nRe_out = {Re_out}')
    elif args.T_out:
        print(f'T_out = {T_out} °C')
    elif args.Re_out:
        print(f'Re_out = {Re_out}')
        
if __name__ == '__main__':
    main()
    
