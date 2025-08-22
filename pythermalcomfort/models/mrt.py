from typing import List, Union, Optional
import numpy as np
from dataclasses import dataclass

# from pythermalcomfort.utilities import units_converter
# from .sky_radiation import calculate_sky_radiation
# from .ground_radiation import calculate_ground_radiation
# from .surface_radiation import calculate_surface_longwave_radiation

class mrt_assumptions: #remae this to more something like a defaults, or assuptions class
    ak: float = 0.7  # shortwave absorption coeff.
    fp: float = 0.5  # projected area factor
    al: float = 0.95  # longwave absorption coeff.
    ground_emissivity: float = 0.95


#FROM: http://dx.doi.org/10.1016/j.buildenv.2014.05.019  Tmrt is the uniform temperature of an imaginary enclosure that cannot be measured directly. Tmrt can be expressed
#by Formula 1 as the fourth root of the integration of individual
# radiation components, each weighted by the view factor from the
# source to a person. --> MRT is the fourth-root of the weighted sum of the surrounding surface temperatures raised to the fourth power, weighted by their respective view factors.

def mean_radiant_temperature() -> float:
    return 0.0





# Globe Temperature clauclation, if wanted? But explain the issues
# MRT Direct SOlar Radiation calculation
# Six-Direction Method
# Surface Temperature + View Factors
    # V1 Provides Typical Environments, with a basic setup?
    # V2 You can provide View Factors?
    # V3 We can calculate View Factors?

# one basic function?
def mean_radiant_temperature_simple(temperatures, view_factors) -> float:
    """
    Calculate Mean Radiant Temperature (MRT).
    
    Parameters:
    temperatures (list or array): Surface temperatures in Celsius.
    view_factors (list or array): Corresponding view factors (sum should be <= 1).
    
    Returns:
    float: MRT in Celsius.
    """
    # Convert Celsius to Kelvin
    temps_k = [t + 273.15 for t in temperatures]
    
    # Calculate weighted sum of T^4
    numerator = sum(f * (T ** 4) for f, T in zip(view_factors, temps_k))
    denominator = sum(view_factors)
    
    # Calculate MRT in Kelvin
    mrt_k = (numerator / denominator) ** 0.25
    
    # Convert back to Celsius
    return mrt_k - 273.15

# Example usage
#temps = [25, 30, 28]        # temperatures of surfaces in °C
#view_factors = [0.3, 0.4, 0.3]

#mrt = calculate_mrt(temps, view_factors)
#print(f"Mean Radiant Temperature: {mrt:.2f} °C")