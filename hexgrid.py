
import bpy

# first need to append path so we can import my other scripts
import os
import sys

# this is a temp solution until i can figure out how to do relative path
dir = '/home/kcw/code/blender-turtleshell'
if not dir in sys.path:
    sys.path.append(dir)
print(dir)

from hex import hexagon
from mathutils import Vector
from math import *
import random


side_length = 5
height = 10
deviation = 6

basis_a = Vector((2*side_length*cos(radians(30)), 0, 0))
basis_b = Vector((side_length*cos(radians(30)), 3/2 *side_length, 0))


name = 'hexagon'
for x in range(5):
    for y in range(2):
        h = height + ((random.random() - 0.5) * deviation * 2)
        mesh = hexagon(name, side_length, h)

        # now create object, add to blender database and make it accessible to editor
        obj = bpy.data.objects.new(name, mesh)

        # by default object is placed at origin
        # put object in its place on the grid
        obj.location += x * basis_a + y * basis_b

        col = bpy.data.collections[0]
        col.objects.link(obj)