"""
:mod:`aurangabad_info` -- Aurangabad city information
=====================================================

.. module:: aurangabad_info
   :platform: Linux, Windows
   :synopsis: Provide the details of the city.

.. moduleauthor:: sachinwakle <sbwakle@hotmail.com>

"""
from city_info.maharashtra import maharashtra_info

def city():
    """The city function provide 
    the details of the city

    Args:
        city (str): name of the city
        
    Returns:
        None:
    
    """
    city = "Aurangabad"
    print("Welcome to the {0} city.".format(city))
    maharashtra_info.mh(city)