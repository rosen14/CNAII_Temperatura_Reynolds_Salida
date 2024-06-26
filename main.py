# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:38:27 2024

@author: Termohidraulica
"""

from library import get_Reout, get_Tout

# INGRESO DE CONDICIONES 
Q = 480.71      # [kW]   | Potencia eléctrica entregada.
T_in = 57.674   # °C     | Temperatura de entrada.
P = 18.12       # [barg] | Presión de operación (Se asume a la salida de la sección)
mp = 14.61      # [kg/s] | Caudal másico.
fluid = 'R134a' # Fluido | de trabajo.

# CÁLCULO
T_out = get_Tout(Q, T_in, P, mp, fluid)
Re_out = get_Reout(P, T_out, mp, fluid) 

# IMPRESIÓN DE RESULTADOS
print(f'T_out = {round(T_out,2)} °C\nRe_out = {round(Re_out,0)}')