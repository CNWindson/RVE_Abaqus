# -*- coding: utf-8 -*-
# author: Jiabo Wang
# QQ: 1457912352
# E-mail : 1457912352@qq.com
from abaqus import *
from abaqusConstants import *
from caeModules import *
import math
import random
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

def main(length, width, height, fiber_length, fiber_diameter, fiber_content):
    fiber_number = (length * width * height) * fiber_content / (fiber_length * math.pi * (fiber_diameter / 2))
    print("Fiber Number", fiber_number)
    part = mdb.models[mdb.models.keys()[0]].Part('Wrie')

    def get_end_point(x1, y1, z1, i1, j1, k1):
        vector_length = ((i1 ** 2 + j1 ** 2 + k1 ** 2) ** 0.5)
        scale = fiber_length / vector_length
        i2, j2, k2 = i1 * scale, j1 * scale, k1 * scale
        return x1 + i2, y1 + j2, z1 + k2

    fiber_number_finish = 0
    while fiber_number_finish < fiber_number:
        x_1 = random.uniform(0, length)
        y_1 = random.uniform(0, width)
        z_1 = random.uniform(0, height)
        i = random.uniform(-1, 1)
        j = random.uniform(-1, 1)
        k = random.uniform(-1, 1)
        x_2, y_2, z_2 = get_end_point(x_1, y_1, z_1, i, j, k)
        if 0 < x_2 < length and 0 < y_2 < width and 0 < z_2 < height:
            part.WirePolyLine(points=(((x_1, y_1, z_1), (x_2, y_2, z_2)),))
            fiber_number_finish += 1
    session.viewports[session.viewports.keys()[0]].setValues(displayedObject=part)
    print('Successful')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
                                                           engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p = mdb.models['Model-1'].parts['Wrie']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(100.0, 50.0))
    p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D,
                                   type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-2']
    p.BaseSolidExtrude(sketch=s, depth=20.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
                                                           engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='fiber')
    mdb.models['Model-1'].materials['fiber'].Elastic(table=((214000.0, 0.3),))
    mdb.models['Model-1'].Material(name='matrix')
    mdb.models['Model-1'].materials['matrix'].Elastic(table=((7830.0, 0.28),))
    mdb.models['Model-1'].HomogeneousSolidSection(name='matrix', material='matrix',
                                                  thickness=None)
    mdb.models['Model-1'].CircularProfile(name='Profile-1', r=0.2)
    mdb.models['Model-1'].BeamSection(name='Section-2',
                                      integration=DURING_ANALYSIS, poissonRatio=0.0, profile='Profile-1',
                                      material='fiber', temperatureVar=LINEAR, consistentMassMatrix=False)
    session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-2']
    a.Instance(name='Part-2-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Wrie']
    a.Instance(name='Wrie-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=HIDDEN)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        renderStyle=WIREFRAME)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Random_fibre', instances=(
        a.instances['Part-2-1'], a.instances['Wrie-1'],),
                               keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
                                                           engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['Random_fibre']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p1 = mdb.models['Model-1'].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['Model-1'].parts['Part-2']
    p = mdb.models['Model-1'].parts['Random_fibre']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p1 = mdb.models['Model-1'].parts['Wrie']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['Model-1'].parts['Wrie']
    p = mdb.models['Model-1'].parts['Random_fibre']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    del a.features['Part-2-1']
    a = mdb.models['Model-1'].rootAssembly
    del a.features['Wrie-1']
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Random_fibre']
    p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Random_fibre']
    p.generateMesh()
if __name__ == '__main__':
    # length = float(getInput("length"))
    # width = float(getInput("width"))
    # height = float(getInput("height"))
    # fiber_length = float(getInput("fiber_length"))
    # fiber_diameter = float(getInput("fiber_diameter"))
    # fiber_content = float(getInput("fiber_content"))
    main(length, width, height, fiber_length, fiber_diameter, fiber_content)
