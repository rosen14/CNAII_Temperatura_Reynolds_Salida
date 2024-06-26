# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:16:27 2024

@author: Rosendo Fazzari
"""

import numpy as np
import CoolProp.CoolProp as CP

def titulo_termodinamico_equilibrio(Q, mp, T_in, P, fluid = 'R134a', z = 3.0):
    '''
    Parameters
    ----------
    Q : [kW]
        Potencia eléctrica entregada.
    mp : [kg/s]
        Caudal másico.
    T_in : °C
        Temperatura de entrada.
    P : [barg]
        Presión de operación. Se asume como la presión a la salida de la sección
    z : TYPE
        Longitud calefaccionada.
        
    Returns
    -------
    título termodinámico de equilibrio a la salida (z)
    '''
    # Conversión de unidades al SI (K, kg, J/kg, Pa, N/m, etc.)
    Q = Q*1e3             # [J/s]
    T_in = T_in + 273.15  # K
    P = (P + 1)*1e5       # [Pa]
    #T de saturacion a la P de operación:
    #Tsat = CP.PropsSI('T','P',P,'Q',1,fluid)
    hf = CP.PropsSI('H','P',P,'Q',0,fluid)
    hg = CP.PropsSI('H','P',P,'Q',1,fluid)
    hfg =  hg - hf
    
    #Supongo que a la entrada tengo liquido subenfriado
    h_in = CP.PropsSI("H", "P", P, "T", T_in, fluid)
    
    #z_sat = -(h_in - hf)/hfg * mp*hfg/q
    
    return Q/(hfg*mp)*z + (h_in - hf)/hfg#, z_sat

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
    fluid : default 'R134a' (Alternativa: 'Water')
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


def viscosity_mcAdams(mu_f, mu_g, x):
    return 1/(x/mu_g + (1-x)/mu_f)

def get_Reout(Q, T_in, P, mp, T_out, fluid = 'R134a' ):
    '''
    Parameters
    ----------
    T_out : °C
        Temperatura a la salida.
    P : [barg]
        Presión de operación. Se asume como la presión a la salida de la sección
    mp : [kg/s]
        Caudal másico.
    fluid : default 'R134a' (Alternativa: 'Water')
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
    n_v = 37                        # Número de vainas en la sección
    Pw = n_v*np.pi*d_v + np.pi*d_c  # [m] Perímetro mojado 
    
    x = titulo_termodinamico_equilibrio(Q, mp, T_in, P, fluid = fluid)
    if x < 0:
        mu = CP.PropsSI("V", "P", P, "T", T_out, fluid) # Dynamic viscosity [Pa-s]
    else:
        # 
        mu_f = CP.PropsSI('V','P',P,'Q',0,fluid)
        mu_g = CP.PropsSI('V','P',P,'Q',1,fluid)
        mu = viscosity_mcAdams(mu_f, mu_g, x)
        
    Re = 4*mp/(mu*Pw)
    return Re




    