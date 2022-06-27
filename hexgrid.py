
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

# create materials so we can assign random materials to hexagons
base_mat = bpy.data.materials.new('mat')
base_mat.use_nodes = False
base_mat.diffuse_color = (1, 0.5, 0.5, 1)

materials = [base_mat, base_mat.copy(), base_mat.copy()]
materials[1].diffuse_color = (0.5, 1, 1, 1)
materials[2].diffuse_color = (0.5, 1, 0.5, 1)


# create hexagon objects and add them to a grid collection
name = 'hexagon'
col = bpy.data.collections.new('hexgrid')
bpy.data.collections[0].children.link(col)
for x in range(15):
    for y in range(13):
        h = height + ((random.random() - 0.5) * deviation * 2)
        mesh = hexagon(name, side_length, h)

        # now create object, add to blender database and make it accessible to editor
        obj = bpy.data.objects.new(name, mesh)

        # by default object is placed at origin
        # put object in its place on the grid
        obj.location += x * basis_a + y * basis_b
        
        # assign random material to object
        mat = random.choice(materials)
        obj.data.materials.append(mat)

        col.objects.link(obj)