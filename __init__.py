bl_info = {
    "name" : "ATblend",
    "author" : "Adwait.R.K",
    "description" : "Adwait 2D 's Blender addon for 2D animation",
    "blender" : (2,91,0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
    }

import bpy

from . Centcur import Test_OT_Operator
from . test_panel import Test_PT_Panel


classes = (Test_OT_Operator, Test_PT_Panel,)

register, unregister = bpy.utils.register_classes_factory(classes)
