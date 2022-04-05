from numpy import pi, cos, sin, radians, degrees, sqrt

def opt_theta(lat, verbose=False):
    """
    Находит оптимальное значение тета методом Ньютона–Рафсона.
    Вход
    lat: значение широты
    verbose: True, если нужна промежуточная печать
    Выход
    theta
    """
    lat1 = radians(lat)
    theta = lat1
    while True:
        dtheta = -(theta+sin(theta)-
        pi*sin(lat1))/(1.0+cos(theta))
        if verbose:
            print ("theta =", degrees(theta))
            print ("delta =", degrees(dtheta))
        if int(1000000*dtheta) == 0:
            break
        theta = theta+dtheta
    return theta/2.0

def transform2(lon, lat, lon0=0, R=1.0):
    """
    Возвращает результат преобразования lon и lat
    в проекцию Мольвейде.
    Вход
    lon: долгота
    lat: широта
    lon0: средний меридиан
    R: радиус глобуса
    Выход
    x: координат x (начало координат в точке 0,0)
    y: координат y (начало координат в точке 0,0)
    """
    lon1 = lon-lon0
    if lon0 != 0:
        if lon1>180:
            lon1 = -((180+lon0)+(lon1-180))
        elif lon1<-180:
            lon1 = (180-lon0)-(lon1+180)
    theta = opt_theta(lat)
    x = sqrt(8.0)/pi*R*lon1*cos(theta)
    x = radians(x)
    y = sqrt(2.0)*R*sin(theta)
    return x, y