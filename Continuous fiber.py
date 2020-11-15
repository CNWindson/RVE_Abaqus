# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-5.27, -9.128), 
    point2=(5.27, 9.128))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=2.635, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.06, name='__profile__', 
    sheetSize=42.48, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges[7], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 2.635)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(0.0, 3.5))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    5.27, 9.128), point1=(8.77, 9.128))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -5.27, 9.128), point1=(-8.77, 9.128))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -5.27, -9.128), point1=(-8.77, -9.128))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    5.27, -9.128), point1=(9.77, -9.128))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], ))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    5.27, -9.128), point1=(8.77, -9.128))
mdb.models['Model-1'].parts['Part-1'].PartitionCellBySketch(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], sketchPlane=
    mdb.models['Model-1'].parts['Part-1'].faces[4], sketchUpEdge=
    mdb.models['Model-1'].parts['Part-1'].edges[7])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[5], 
    mdb.models['Model-1'].parts['Part-1'].edges[11], 
    mdb.models['Model-1'].parts['Part-1'].edges[12]), line=
    mdb.models['Model-1'].parts['Part-1'].edges[19], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[19], 
    mdb.models['Model-1'].parts['Part-1'].edges[21], 
    mdb.models['Model-1'].parts['Part-1'].edges[22]), line=
    mdb.models['Model-1'].parts['Part-1'].edges[29], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[21], 
    mdb.models['Model-1'].parts['Part-1'].edges[26], 
    mdb.models['Model-1'].parts['Part-1'].edges[30]), line=
    mdb.models['Model-1'].parts['Part-1'].edges[22], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[14], 
    mdb.models['Model-1'].parts['Part-1'].edges[33], 
    mdb.models['Model-1'].parts['Part-1'].edges[38]), line=
    mdb.models['Model-1'].parts['Part-1'].edges[15], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[39], ), line=
    mdb.models['Model-1'].parts['Part-1'].edges[28], sense=REVERSE)
mdb.models['Model-1'].Material(name='Fiber')
mdb.models['Model-1'].materials['Fiber'].Elastic(table=((241000.0, 0.2), ))
mdb.models['Model-1'].Material(name='Matrix')
mdb.models['Model-1'].materials['Matrix'].Elastic(table=((3120.0, 0.38), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Fiber', name='Fiber', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Matrix', name='Matrix', 
    thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#3d ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName='Fiber', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), name='Set-2')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-2'], sectionName='Matrix', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-1', previous=
    'Initial')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-2', previous=
    'Step-1')
del mdb.models['Model-1'].steps['Step-1']
del mdb.models['Model-1'].steps['Step-2']
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-1', previous=
    'Initial')
mdb.models['Model-1'].FieldOutputRequest(createStepName='Step-1', name=
    'F-Output-2', variables=('S', 'E', 'U', 'IVOL'))
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#400a000 ]', ), ), name='Set-1')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=UNSET, 
    u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#1000210 ]', ), ), name='Set-2')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-2', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'], u1=UNSET, 
    u2=0.0, u3=18.256, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#2821120 ]', ), ), name='XXXXXXXXXX')
mdb.models['Model-1'].XsymmBC(createStepName='Step-1', localCsys=None, name=
    'BC-3', region=mdb.models['Model-1'].rootAssembly.sets['XXXXXXXXXX'])
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#87c0000 ]', ), ), name='m_Set-4')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#1001088a ]', ), ), name='s_Set-4')
mdb.models['Model-1'].Tie(adjust=OFF, master=
    mdb.models['Model-1'].rootAssembly.sets['m_Set-4'], name='Constraint-1', 
    positionTolerance=2.635, positionToleranceMethod=SPECIFIED, slave=
    mdb.models['Model-1'].rootAssembly.sets['s_Set-4'], thickness=ON, 
    tieRotations=OFF)
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].setMeshControls(regions=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#3f ]', 
    ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#3f ]', 
    ), ), ))
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-UT3747N', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-4_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SET-4_CNS_,ASSEMBLY_M_SET-4_CNS_) MAY RESULT IN UNREALISTIC DEFORMATION BETWEEN THE SURFACES OR LARGE STRESSES BECAUSE THE MASTER IS NODE-BASED AND NO ADJUSTMENT IS SPECIFIED. DEFINE A SURFACE-BASED MASTER SURFACE OR ADJUST=YES TO AVOID THIS PROBLEM.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY_S_SET-4_CNS_,ASSEMBLY_M_SET-4_CNS_) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'Boundary conditions are specified on inactive dof of 47 nodes. The nodes have been identified in node set WarnNodeBCInactiveDof.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '77 nodes have dof on which incorrect boundary conditions may have been specified. The nodes have been identified in node set WarnNodeBCIncorrectDof.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'E:\\abaqus\\temp\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-UT3747N', 'handle': 3528, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 85.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16334.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 23.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': 1, 
    'timeIncrement': 2.22e-16, 'increment': 1, 'stepTime': 2.22e-16, 'step': 1, 
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Sat Nov 14 19:49:53 2020', 
    'jobName': 'Job-1'})
# Save by Yi on 2020_11_14-20.23.30; build 2018 2017_11_08-01.21.41 127140
