'''
create a regular 3d hexagon prism mesh
maybe we'll make it less regular in future
'''

import bpy
from math import *


# temp for now, will make this configurable
a = 10 # the side length
height = 10

vertices = []
edges = [] #doesn't really need to be defined
faces = []

# create the vertices

# first let's keep our initial hex on a flat plane z=0
# our hexagon center will be at origin
# put first point at bottom left (negative x and y) and move clockwise
angle = 30
for i in range(6):
    vertices.append([-a*cos(radians(angle)), -a*sin(radians(angle)), 0])
    print(vertices[-1])
    angle += 60


# create 6gon face
faces.append([0,1,2,3,4,5])

# now add the object to the blender database and make it visible
name = 'hexagon'
mesh = bpy.data.meshes.new(name)
obj = bpy.data.objects.new(name, mesh)

col = bpy.data.collections[0]
col.objects.link(obj)
#bpy.context.view_layer.objects.active = obj
mesh.from_pydata(vertices, edges, faces) #switch to bmesh