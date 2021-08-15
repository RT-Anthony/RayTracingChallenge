import unittest
from ray_tracer import canvas
from ray_tracer import data_structures

class TestCanvas(unittest.TestCase):

    def test_create_canvas(self):
        c = canvas.Canvas(10, 20)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)
        for pixel in c:
            self.assertEqual(pixel, data_structures.Color(0, 0, 0))

    def test_write_pixel(self):
        c = canvas.Canvas(10, 20)
        red = data_structures.Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertEqual(c.pixel_at(2, 3), red)

    def test_canvas_ppm_header(self):
        c = canvas.Canvas(5, 3)
        ppm = canvas.canvas_to_ppm(c)
        i = 0
        for line in iter(ppm.splitlines()):
            if i == 0:
                self.assertEqual (line, "P3")
            elif i == 1:
                self.assertEqual(line, "5 3")
            elif i == 2:
                self.assertEqual(line, "255")
            else:
                break
            i += 1

    def test_canvas_pixel_data(self):
        c = canvas.Canvas(5, 3)
        c1 = data_structures.Color(1.5, 0, 0)
        c2 = data_structures.Color(0, 0.5, 0)
        c3 = data_structures.Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = canvas.canvas_to_ppm(c)
        i = 0
        for line in iter(ppm.splitlines()):
            if i == 3:
                self.assertEqual (line.strip(), "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
            elif i == 4:
                self.assertEqual(line.strip(),  "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0")
            elif i == 5:
                self.assertEqual(line.strip(),  "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255")
            i += 1
        self.assertEqual(i, 6)