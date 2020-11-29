import bpy

class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "Test_PT_Panel"
    bl_label = "AdwAddon"
    bl_category = "Adw_Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout=self.layout
        row=layout.row()
        row.operator('view3d.cursor_center', text="Center 3D Cursor")
        ob = bpy.context.object
        col = flow.column()
        col.prop(ob, "parent")
        sub = col.column()
        sub.prop(ob, "parent_type")
        parent = ob.parent
