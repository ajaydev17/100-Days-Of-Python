import colorgram

# extract 30 colors from the image
colors = colorgram.extract("damien_hirst.jpg", 30)
rgb_colors = []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    cols = (red, green, blue)
    rgb_colors.append(cols)

print(rgb_colors)