from city_info.pune import pune_info
from city_info.mumbai import mumbai_info
from city_info.aurangabad import aurangabad_info

"""
.. module:: city_info
    :platform: Linux
    :synopsis: module illustrating how to document python source code
 
.. moduleauthor:: Sachin Wakle <sbwakle@hotmail.com>
"""

class CityInfoApp:
    """Class illustrating how to document python source code
 
    This class provides some basic methods for providing information
    about cities.
 
    .. note::
 
        This class does not provide any significant functionality that the
        python does not already include. It is just for illustrative purposes.
    """
    def __main__(self):
        """Method to display the information of all cities.
    
        Args:
            None
        """
        print("===========[ City Information ]===================\n")
        pune_info.city()
        print("==============================")
        mumbai_info.city()
        print("==============================")
        aurangabad_info.city()
        print("==============================")

if __name__ == "__main__":
    city = CityInfoApp()
    city.__main__()