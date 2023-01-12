import math

def distance_to_north_pole(country):
    # Use the haversine formula to calculate the distance between two latitudes and longitudes
    def haversine(lat1, lon1, lat2, lon2):
        R = 3959 # radius of earth in miles
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Coordinates of the North Pole
    north_pole = (90, 0)

    # Look up the latitude and longitude of the given country
    # You will need to provide a way to look up the coordinates of the country
    # For example, you could use a library like GeoPy or OpenCage Geocoder
    country_coord = (0,0) # replace with the coordinates of the country
    distance = haversine(north_pole[0], north_pole[1], country_coord[0], country_coord[1])
    return distance
