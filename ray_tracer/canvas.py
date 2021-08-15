from ray_tracer import data_structures

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[data_structures.Color(0,0,0) for y in range(height)] for x in range(width)]

    def write_pixel(self, x, y, color):
        self.canvas[x][y] = color

    def pixel_at(self, x, y):
        return self.canvas[x][y]

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield self.canvas[j][i]

def canvas_to_ppm(canvas):
    ppm_string = "P3\n"
    ppm_string += "{} {}\n".format(canvas.width, canvas.height)
    ppm_string += "255\n"
    
    line_length = 70
    width = canvas.width
    i = 0
    for y in range(canvas.height):
        for x in range(width):
            pixel = canvas.canvas[x][y]
            red, green, blue = pixel.norm_convert_255()
            ppm_string += "{} {} {} ".format(red, green, blue)
        ppm_string += "\n" 
    return ppm_string
