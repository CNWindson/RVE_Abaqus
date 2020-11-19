# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='RVE_Model', kernelModule='Random_Short_Fiber', kernelFunction='main', includeApplyBtn=False, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgTabBook(name='TabBook_3', p='DialogBox', layout='0')
RsgTabItem(name='TabItem_7', p='TabBook_3', text='Random_Short_Fiber')
RsgTextField(p='TabItem_7', fieldType='Float', ncols=12, labelText='length:', keyword='length', default='0')
RsgTextField(p='TabItem_7', fieldType='Float', ncols=12, labelText='width:', keyword='width', default='0')
RsgTextField(p='TabItem_7', fieldType='Float', ncols=12, labelText='height:', keyword='height', default='0')
RsgTextField(p='TabItem_7', fieldType='Float', ncols=12, labelText='fiber_length:', keyword='fiber_length', default='0')
RsgTextField(p='TabItem_7', fieldType='Float', ncols=12, labelText='fiber_diameter:', keyword='fiber_diameter', default='0')
RsgTextField(p='TabItem_7', fieldType='Float', ncols=12, labelText='fiber_content:', keyword='fiber_content', default='0')
RsgTabItem(name='TabItem_8', p='TabBook_3', text='Tab')
RsgTabItem(name='TabItem_6', p='TabBook_3', text='Tab')
RsgIcon(p='DialogBox', fileName=r'515.png')
RsgGroupBox(name='GroupBox_3', p='DialogBox', text='Title', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y')
dialogBox.show()