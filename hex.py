'''
create a regular 3d hexagon prism mesh
maybe we'll make it less regular in future
'''
import bpy
import bmesh
from math import *
from mathutils import Vector


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

# create the mesh
name = 'hexagon'
mesh = bpy.data.meshes.new(name)
mesh.from_pydata(vertices, edges, faces)

# now extrude into a 3d hex prism
bm = bmesh.new()
bm.from_mesh(mesh)

bm.faces.ensure_lookup_table()
bottom = bm.faces[0] # the bottom of the prism

top = bmesh.ops.extrude_face_region(bm, geom=[bottom])
print(top)
bmesh.ops.translate(bm, vec=Vector((0,0,height)),
    verts = [v for v in top['geom'] if isinstance(v, bmesh.types.BMVert)])

bm.normal_update()

bm.to_mesh(mesh)
bm.free()

# now create object, add to blender database and make it accessible to editor
obj = bpy.data.objects.new(name, mesh)
col = bpy.data.collections[0]
col.objects.link(obj)