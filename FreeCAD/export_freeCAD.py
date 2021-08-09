import os
import sys
import scipy.io

#FREECADPATH = 'C:/Program Files/FreeCAD 0.19/bin/'
FREECADPATH = '/home/rboshra/miniconda3/envs/fcenv/lib'
sys.path.append(FREECADPATH)
import FreeCAD
import Sketcher
import Part

data = scipy.io.loadmat('Generic Circular.mat', simplify_cells = True)

x_mm = data['strctGridModel']['m_afGridHolesX']
y_mm = data['strctGridModel']['m_afGridHolesY']
hole_radius = data['strctGridModel']['m_strctGridParams']['m_fGridHoleDiameterMM'] / 2

FreeCAD.openDocument('grid_template.FCStd')

App.getDocument('grid_template').getObject('Body').newObject('Sketcher::SketchObject','Sketch003')
App.getDocument('grid_template').getObject('Sketch003').Support = (App.getDocument('grid_template').getObject('Pocket'),['Face3',])
App.getDocument('grid_template').getObject('Sketch003').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

holeNum = 0
for x, y in zip(x_mm, y_mm):
    App.getDocument('grid_template').getObject('Sketch003').addGeometry(Part.Circle(App.Vector(x,y,0),App.Vector(0,0,1),hole_radius),False)
    holeNum += 1
    print('Added hole x: %.2f, y: %.2f'%(x,y))

App.ActiveDocument.recompute()
App.getDocument("grid_template").save()

App.getDocument('grid_template').getObject('Body').newObject('PartDesign::Pocket','Pocket002')
App.getDocument('grid_template').getObject('Pocket002').Profile = App.getDocument('grid_template').getObject('Sketch003')
App.getDocument('grid_template').getObject('Pocket002').Length = 5.0
App.getDocument('grid_template').getObject('Sketch003').Visibility = False
App.ActiveDocument.recompute()

App.getDocument('grid_template').getObject('Pocket002').ViewObject.ShapeColor=getattr(App.getDocument('grid_template').getObject('Pocket').getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument('grid_template').getObject('Pocket002').ViewObject.ShapeColor)
App.getDocument('grid_template').getObject('Pocket002').ViewObject.LineColor=getattr(App.getDocument('grid_template').getObject('Pocket').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('grid_template').getObject('Pocket002').ViewObject.LineColor)
App.getDocument('grid_template').getObject('Pocket002').ViewObject.PointColor=getattr(App.getDocument('grid_template').getObject('Pocket').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('grid_template').getObject('Pocket002').ViewObject.PointColor)
App.getDocument('grid_template').getObject('Pocket002').ViewObject.Transparency=getattr(App.getDocument('grid_template').getObject('Pocket').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('grid_template').getObject('Pocket002').ViewObject.Transparency)
App.getDocument('grid_template').getObject('Pocket002').ViewObject.DisplayMode=getattr(App.getDocument('grid_template').getObject('Pocket').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('grid_template').getObject('Pocket002').ViewObject.DisplayMode)

__objs__=[]
__objs__.append(FreeCAD.getDocument("grid_template").getObject("Body"))
import Mesh
Mesh.export(__objs__,"Grid_to_print.stl")
App.closeDocument('grid_template')
