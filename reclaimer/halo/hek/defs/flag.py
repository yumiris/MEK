from ...common_descriptors import *
from supyr_struct.defs.tag_def import TagDef


attachment_point = Struct("attachment point",
    BSInt16("height to next attachment"),
    Pad(18),
    StrLatin1("marker name", SIZE=32),
    )

flag_body = Struct("Data",
    Pad(4),
    BSEnum16("trailing edge shape",
        "flat",
        "concave triangular",
        "convex triangular",
        "trapezoid short top",
        "trapezoid short bottom",
        ),

    BSInt16("trailing edge shape offset"),
    BSEnum16("attached edge shape",
        "flat",
        "concave triangular",
        ),
    Pad(2),
    BSInt16("width"),
    BSInt16("height"),

    BFloat("cell width"),
    BFloat("cell height"),

    TagIndexRef("red flag shader", INCLUDE=Tag_Index_Ref_Struct),
    TagIndexRef("physics",         INCLUDE=Tag_Index_Ref_Struct),

    BFloat("wind noise"),
    Pad(8),
    TagIndexRef("blue flag shader", INCLUDE=Tag_Index_Ref_Struct),

    Reflexive("attachment points",
        INCLUDE=Reflexive_Struct,

        CHILD=Array("attachment points array", MAX=4,
            SIZE=".Count", SUB_STRUCT=attachment_point ),
        ),
    SIZE=96,
    )



def get():
    return flag_def

flag_def = TagDef(
    com( {1:{DEFAULT:"flag" }}, Tag_Header),
    flag_body,
    
    NAME="flag",
    
    ext=".flag", def_id="flag", endian=">"
    )
