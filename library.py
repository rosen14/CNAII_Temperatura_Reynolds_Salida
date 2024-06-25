# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:16:27 2024

@author: Rosendo Fazzari
"""

import numpy as np
import CoolProp.CoolProp as CP

def get_Tout(Q, T_in, P, mp, fluid = 'R134a' ):
    '''
    Parameters
    ----------
    Q : [kW]
        Potencia eléctrica entregada.
    T_in : °C
        Temperatura de entrada.
    P : [barg]
        Presión de operación. Se asume como la presión a la salida de la sección
    mp : [kg/s]
        Caudal másico.
    fluid : default 'R134a' (Opciones: 'Water')
        Fluido de trabajo.
    Returns
    -------
    Temperatura a la salida en °C.

    '''
    
    # Conversión de unidades al SI (K, kg, J/kg, Pa, N/m, etc.)
    Q = Q*1e3             # [J/s]
    T_in = T_in + 273.15  # K
    P = (P + 1)*1e5       # [Pa]
    
    H_in = CP.PropsSI("H", "P", P, "T", T_in, fluid)   # Entalpía de entrada.
    H_out = Q/mp + H_in                                # Entalía a la salida.
    
    T_out = CP.PropsSI("T", "P", P, "H", H_out, fluid) # Temperatura de salida.
    
    return T_out - 273.15 # °C

def get_Reout(P, T_out, mp, fluid = 'R134a' ):
    '''
    Parameters
    ----------
    T_out : °C
        Temperatura a la salida.
    P : [barg]
        Presión de operación. Se asume como la presión a la salida de la sección
    mp : [kg/s]
        Caudal másico.
    fluid : default 'R134a' (Opciones: 'Water')
        Fluido de trabajo.
    Returns
    -------
    Temperatura a la salida en °C.

    '''
    
    # Conversión de unidades al SI (K, kg, J/kg, Pa, N/m, etc.)
    T_out = T_out + 273.15  # K
    P = (P + 1)*1e5         # [Pa]
    
    # Calculos geométricos
    #A_pasaje = 0.004359            # [m2]
    d_v = 12.9/1000                 # [m] Diametro vaina
    d_c = 108/1000                  # [m] Diametro canal 
    n_v = 37                        # numero de vainas en la seccion
    Pw = n_v*np.pi*d_v + np.pi*d_c  # [m] Perímetro mojado 
    
    mu = CP.PropsSI("V", "P", P, "T", T_out, fluid) # Dynamic viscosity [Pa-s]
    
    Re = 4*mp/(mu*Pw)
    return Re




    