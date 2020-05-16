from city_info.maharashtra import maharashtra_info

def city():
    """The city function provide 
    the details of the city
    Arg: None"""
    city = "Mumbai"
    print("Welcome to the {0} city.".format(city))
    maharashtra_info.mh(city)