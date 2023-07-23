import colorgram

colors = colorgram.extract('hirst.jpg', 30)


def list_colors():
    colour_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colour_list.append((r, g, b))

    return colour_list
