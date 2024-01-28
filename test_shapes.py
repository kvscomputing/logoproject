#!/usr/bin/env python3

from PIL import Image
import matplotlib.testing.compare as mpcompare
import unittest
import shapes
import tempfile
import os.path
import svg_turtle
import inspect

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

CANVAS_SIZE = (719, 608) #so that image size match the actual size

class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename, override_tmpdir=None):
        ''' compares the current canvas to an expected file.
        Returns None if and only if the files are identical.
        
        If override_tmpdir is set, use that directory for temporary files 
        (useful for generating known good testdata images.
        '''

        TOLERANCE = 5.0 # somewhere between 0 and 255, higher is more lax.

        with tempfile.TemporaryDirectory() as tmp_dirname:
            calling_function = inspect.stack()[1][3]
            tmp_dirname = tmp_dirname if not override_tmpdir else override_tmpdir

            actual_svg = os.path.join(tmp_dirname, '%s.svg' % calling_function)
            actual_png = os.path.join(tmp_dirname, '%s.png' % calling_function)
            self._turtle.save_as(actual_svg)
            
            # canvas generates a svg file, but we have to convert it to a png in
            # order to compare it using matplotlib's library
            drawing = svg2rlg(actual_svg)
            renderPM.drawToFile(drawing, actual_png, fmt="PNG")
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)


    def setUp(self):
        # this is run before every test
        self._turtle = svg_turtle.SvgTurtle(*CANVAS_SIZE)
        

    def house(self):
        shapes.house_outline(self._turtle, 300, 600, -600, -400)
        shapes.garage_door(self._turtle, 100, 175, -550, -400)
        shapes.garage_door(self._turtle, 100, 175, -325, -400)
        shapes.front_door(self._turtle, 75, 50, -100, -400)
        shapes.square_window(self._turtle, 50, -525, -175)
        shapes.square_window(self._turtle, 50, -325, -175)
        shapes.square_window(self._turtle, 50, -125, -175)
        shapes.round_window(self._turtle, 25, -300, -75)
        shapes.tree(self._turtle, 25, 75, 150, -400)
        shapes.tree(self._turtle, 25, 75, 450, -400)
        shapes.cloud(self._turtle, 100, -400, 300)
        shapes.cloud(self._turtle, 100, 0, 300)
        # shapes.sun(self._turtle, 200, -screen.window_width()/2, screen.window_height()/2-200)

        # compare this 20,20,20 turtle against the well-known turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/House_final.png'))


    # def test_house_fail(self):
    #     # test that a badly sized circle fails to compare as equal
    #     shapes.house_outline(self._turtle, 300, 600, -600, 400)
    #     shapes.garage_door(self._turtle, 100, 175, -550, -400)
    #     shapes.garage_door(self._turtle, 100, 175, -325, -400)
    #     shapes.front_door(self._turtle, 75, 50, -100, -400)
    #     shapes.square_window(self._turtle, 50, -525, -175)
    #     shapes.square_window(self._turtle, 50, -325, -175)
    #     shapes.square_window(self._turtle, 50, -125, -175)
    #     shapes.round_window(self._turtle, 25, -300, -75)
    #     shapes.tree(self._turtle, 25, 75, 150, -400)
    #     shapes.tree(self._turtle, 25, 75, 450, -400)
    #     shapes.cloud(self._turtle, 100, -400, 300)
    #     shapes.cloud(self._turtle, 100, 0, 300)
    #     # shapes.sun(self._turtle, 200, -screen.window_width()/2, screen.window_height()/2-200)

    #     # this should not match, therefore should be not none.
    #     self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='testdata/House_final.png'))


if __name__ == '__main__':
    unittest.main()
