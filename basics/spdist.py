import math
def spdist(lat1, lon1, lat2, lon2):
    """
    Вычисляет расстояние по дуге большой окружности, зная
    широту и долготу двух точек.
    Вход
    lat1, lon1: широта и долгота первой точки в градусах
    lat2, lon2: широта и долгота второй точки в градусах
    Выход
    d: расстояние по дуге большой окружности
    """
    D = 3959 # радиус Земли в милях
    phi1 = math.radians(lat1)
    lambda1 = math.radians(lon1)
    phi2 = math.radians(lat2)
    lambda2 = math.radians(lon2)
    dlambda = lambda2 - lambda1
    dphi = phi2 - phi1
    sinlat = math.sin(dphi/2.0)
    sinlong = math.sin(dlambda/2.0)
    alpha=(sinlat*sinlat) + math.cos(phi1)
    math.cos(phi2) * (sinlong*sinlong)
    c = 2 * math.asin(min(1, math.sqrt(alpha)))
    d = D * c
    return d

if __name__ == "__main__":
    lat1, lon1 = 40, -83 # Колумбус, штат Огайо
    lat2, lon2 = 39.91, 116.56 # Пекин
    print(spdist(lat1, lon1, lat2, lon2))