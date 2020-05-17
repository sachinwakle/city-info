"""
:mod:`pune_info` -- Pune city information
=========================================

.. module:: pune_info
   :platform: Linux, Windows
   :synopsis: Provide the details of the city.

.. moduleauthor:: sachinwakle <sbwakle@hotmail.com>

"""
from city_info.maharashtra import maharashtra_info

def city():
    """The city function provide the details of the city
    
    Args:
        city (str): name of the city
        
    Returns:
        None:
    """
    city = "Pune"
    print("Welcome to the {0} city.".format(city))
    maharashtra_info.mh(city)