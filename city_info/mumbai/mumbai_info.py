"""
:mod:`mumbai_info` -- Mumbai city information
=============================================

.. module:: mumbai_info
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
    city = "Mumbai"
    print("Welcome to the {0} city.".format(city))
    maharashtra_info.mh(city)