from abaqus import * 
from abaqusConstants import * 
import regionToolset

session.viewports['Viewport: 1'].setValues(displayedObject=None)

#------------------------------------------------------------------------
# Create the model 

mdb.models.changeKey(fromName='Model-1', toName='Truss Structure') 
trussModel = mdb.models['Truss Structure'] 
# mdb.Model(name='Truss Structure', modelType=STANDARD_EXPLICIT)
#------------------------------------------------------------------------
# Create the part 

import sketch 
import part 

trussSketch = trussModel.ConstrainedSketch(name='2D Truss Sketch', sheetSize=9000.0) 
trussSketch.Line(point1=(0, 0), point2=(3000, 0)) 
trussSketch.Line(point1=(3000, 0), point2=(3000, 3000)) 
trussSketch.Line(point1=(0, 0), point2=(3000, 3000)) 
trussSketch.Line(point1=(3000, 0), point2=(6000, 0)) 
trussSketch.Line(point1=(3000, 0), point2=(6000, 3000)) 
trussSketch.Line(point1=(3000, 3000), point2=(6000, 3000)) 
trussSketch.Line(point1=(6000, 0), point2=(6000, 3000)) 
trussSketch.Line(point1=(6000, 0), point2=(9000, 0)) 
trussSketch.Line(point1=(6000, 3000), point2=(9000, 0)) 

trussPart = trussModel.Part(name='Truss', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY) 
trussPart.BaseWire(sketch=trussSketch)

#------------------------------------------------------------------------ 
# Create material 

import material 

# Create material Steel by assigning mass density, youngs modulus 
# and poissons ratio 
trussMaterial = trussModel.Material(name='Steel') 
trussMaterial.Elastic(table=((200000, 0.3), ))

#-------------------------------------------------------------------------------
#Create a section and assign the truss to it 
import section 

trussSection = trussModel.TrussSection(name='Truss Section', 
                                       material='Steel', 
                                       area=300)
                                       
edges_for_section_assignment = trussPart.edges.findAt(((1500.0, 0.0, 0.0), ), 
                                                       ((3000.0, 1500.0, 0.0),  ), 
                                                       ((1500.0, 1500.0, 0.0), ), 
                                                       ((4500.0, 0.0, 0.0), ), 
                                                       ((4500.0, 1500.0, 0.0), ), 
                                                       ((4500.0, 3000.0, 0.0), ), 
                                                       ((6000.0, 1500.0, 0.0), ), 
                                                       ((7500.0, 0.0, 0.0), ), 
                                                       ((7500.0, 1500.0, 0.0), )) 
                                                       
truss_region = regionToolset.Region(edges=edges_for_section_assignment) 
trussPart.SectionAssignment(region=truss_region, sectionName='Truss Section')

# -----------------------------------------------------------------------
# Create the assembly 

import assembly 

#  create the part instance 
trussAssembly = trussModel.rootAssembly 
trussInstance = trussAssembly.Instance(name='Truss Instance', part=trussPart, 
                                                              dependent=ON) 

#------------------------------------------------------------------------------

# Create the step

import  step

# Create a static general step
trussModel.StaticStep(name='Loading Step', previous='Initial', 
                      description='Loads are applied to the truss in this step')

#-------------------------------------------------------------------------------------------- 
# Create the field output request 

# Change the name of field output request 'F-Output-1' to  'Selected Field outputs' 
trussModel.fieldOutputRequests.changeKey(fromName='F-Output-1',
                                         toName='Selected Field Outputs') 

# Since F-Output-1 is applied at the 'Loading Step' step by defaU1t, 
# 'Selected Field Outputs' will be too 
# We only need to set the required variables 
trussModel.fieldOutputRequests['Selected Field Outputs'].setValues(variables=('S',
                                                                'U' , 'RF', 'CF'))
#---------------------------------------------------------------------------- 
# Create the history output request
# We want the defaU1ts so we'll leave this section blank

#------------------------------------------------------------------------
# Apply loads

# Concentrated load of 20kN on first node 

vertex_coords_for_first_force = (3000.0, 0.0, 0.0) 
vertex_for_first_force = trussInstance.vertices \
                                    .findAt((vertex_coords_for_first_force,)) 
trussModel.ConcentratedForce(name='Force1', createStepName='Loading Step', 
                            region=(vertex_for_first_force,), cf2=-20000.0, 
                            distributionType=UNIFORM) 

# Concentrated load of 20kN on second node 
vertex_coords_for_second_force = (6000.0, 0.0, 0.0) 
vertex_for_second_force = trussInstance.vertices \
                                       .findAt((vertex_coords_for_second_force,)) 
trussModel.ConcentratedForce(name='Force2', createStepName='Loading Step', 
                             region=(vertex_for_second_force,), cf2=-20000.0,
                             distributionType=UNIFORM)

#------------------------------------------------------------------------------
# Apply boundary conditions 

# Pin left 0nd of upper member 
vertex_coords_for_first_pin = (0.0, 0.0, 0.0) 
vertex_for_first_pin = trussInstance.vertices \
                                          .findAt((vertex_coords_for_first_pin,)) 
trussModel.DisplacementBC(name='Pinl', createStepName='Initial', 
                          region=(vertex_for_first_pin,),
                          u1=SET, u2=SET, ur3=UNSET, 
                          amplitude=UNSET, distributionType=UNIFORM)
                          
# Pin left 0nd of lower member 
vertex_coords_for_second_pin = (9000.0, 0.0, 0.0) 
vertex_for_second_pin = trussInstance.vertices \
                                        .findAt((vertex_coords_for_second_pin,)) 
trussModel.DisplacementBC(name='Pin2', createStepName='Initial', 
                          region=(vertex_for_second_pin,), 
                          u1=SET, u2=SET, ur3=UNSET,
                          amplitude=UNSET, distributionType=UNIFORM)

#------------------------------------------------------------------------------
# Create the mesh

import mesh 

truss_mesh_region = truss_region 
edges_for_meshing = edges_for_section_assignment 

mesh_element_type = mesh.ElemType(elemCode=T2D2, elemLibrary=STANDARD)
trussPart.setElementType(regions=truss_mesh_region,
                         elemTypes=(mesh_element_type, )) 
trussPart.seedEdgeByNumber(edges=edges_for_meshing, number=1) 
trussPart.generateMesh()
