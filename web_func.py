def make_appropriate_scale(result_tmp_response):
    size_information = result_tmp_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['boundedBy']
    low_corner = size_information['Envelope']['lowerCorner'].split()
    upper_corner = size_information['Envelope']['upperCorner'].split()
    x_size = abs(float(upper_corner[0]) - float(low_corner[0]))
    y_size = abs(float(upper_corner[1]) - float(low_corner[1]))
    return f'{x_size},{y_size}'