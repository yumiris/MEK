from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef


cfxs_meta_def = BlockDef("cfxs",
    Bool16("flags",
        "disable_brightness",
        ("disable_overexposure", 1 << 2),
        ),
    SInt16("unknown"),
    Float("overexposure_amount"),
    Float("overexposure_unknown"),
    Float("overexposure_unknown_1"),
    Float("brightness_amount"),
    Float("brightness_unknown"),
    Float("brightness_unknown_1"),
    Float("brightness_unknown_2"),
    Bool16("flags_1",
        "disable",
        ),
    SInt16("unknown_1"),
    Float("unknown_2"),
    Bool16("flags_2",
        "disable",
        ),
    SInt16("unknown_3"),
    Float("unknown_4"),
    Bool16("flags_3",
        "disable",
        ),
    SInt16("unknown_5"),
    Float("base"),
    Float("min"),
    Float("max"),
    Bool16("flags_4",
        "disable",
        ),
    SInt16("unknown_6"),
    Float("base_1"),
    Float("min_1"),
    Float("max_1"),
    Bool16("flags_5",
        "disable",
        ),
    SInt16("unknown_7"),
    Float("base_2"),
    Float("min_2"),
    Float("max_2"),
    Bool16("flags_6",
        "disable",
        ),
    SInt16("unknown_8"),
    Float("red"),
    Float("green"),
    Float("blue"),
    Bool16("flags_7",
        "disable",
        ),
    SInt16("unknown_9"),
    Float("red_1"),
    Float("green_1"),
    Float("blue_1"),
    Bool16("flags_8",
        "disable",
        ),
    SInt16("unknown_10"),
    Float("red_2"),
    Float("green_2"),
    Float("blue_2"),
    Bool16("flags_9",
        "disable",
        ),
    SInt16("unknown_11"),
    Float("unknown_12"),
    Float("unknown_13"),
    Float("unknown_14"),
    Bool16("flags_10",
        "disable",
        ),
    SInt16("unknown_15"),
    Float("unknown_16"),
    Float("unknown_17"),
    Float("unknown_18"),
    Bool16("flags_11",
        "disable",
        ),
    SInt16("unknown_19"),
    Float("unknown_20"),
    Float("unknown_21"),
    Float("unknown_22"),
    SInt32("unknown_23"),
    Bool16("flags_12",
        "disable",
        ),
    SInt16("unknown_24"),
    Float("base_3"),
    Float("min_3"),
    Float("max_3"),
    Bool16("flags_13",
        "disable",
        ),
    SInt16("unknown_25"),
    Float("base_4"),
    Float("min_4"),
    Float("max_4"),
    TYPE=Struct, ENDIAN=">", SIZE=228
    )