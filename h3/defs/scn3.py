############# Credits and version info #############
# Definition autogenerated from Assembly XML tag def
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: DarkShallFall
# 	Widgets, Bitmaps, Animations, Y and X offsets, layers, blending, and model.
# revision: 3		author: -DeToX-
# 	X and Y Scale
# revision: 4		author: Lord Zedd
# 	Fixed up, added flags and types
# revision: 5		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef

scn3_group_widget_bitmap_widget_blend_method = (
    "standard",
    "unknown_0",
    "unknown_1",
    "alpha",
    "overlay",
    "unknown_2",
    "lighter_color",
    "unknown_3",
    "unknown_4",
    "unknown_5",
    "inverted_alpha",
    "unknown_6",
    "unknown_7",
    "unknown_8",
    )

unknown_flags_32 = tuple("bit_%s" % i for i in range(32))


scn3_data_source = Struct("data_source", 
    dependency("data_source"),
    ENDIAN=">", SIZE=16
    )


scn3_group_widget_list_widget_list_widget_item = Struct("list_widget_item", 
    Bool32("flags", *unknown_flags_32),
    string_id_meta("name"),
    SInt16("unknown", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_offset"),
    SInt16("widescreen_x_offset"),
    SInt16("widescreen_y_unknown"),
    SInt16("widescreen_x_unknown"),
    SInt16("standard_y_offset"),
    SInt16("standard_x_offset"),
    SInt16("standard_y_unknown"),
    SInt16("standard_x_unknown"),
    dependency("animation"),
    string_id_meta("target"),
    ENDIAN=">", SIZE=48
    )


scn3_group_widget_list_widget = Struct("list_widget", 
    dependency("ancestor"),
    Bool32("flags", 
        ("horizontal", 1 << 4),
        "loops",
        ),
    string_id_meta("name"),
    SInt16("unknown", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_offset"),
    SInt16("widescreen_x_offset"),
    SInt16("widescreen_y_unknown"),
    SInt16("widescreen_x_unknown"),
    SInt16("standard_y_offset"),
    SInt16("standard_x_offset"),
    SInt16("standard_y_unknown"),
    SInt16("standard_x_unknown"),
    dependency("animation"),
    string_id_meta("data_source_name"),
    dependency("skin"),
    SInt32("row_count"),
    reflexive("list_widget_items", scn3_group_widget_list_widget_list_widget_item),
    dependency("up_arrow_bitmap"),
    dependency("down_arrow_bitmap"),
    ENDIAN=">", SIZE=128
    )


scn3_group_widget_text_widget = Struct("text_widget", 
    dependency("ancestor"),
    Bool32("flags", 
        ("left_alignment", 1 << 3),
        "right_alignment",
        ("all_caps", 1 << 6),
        ("wrap_at_bounds", 1 << 13),
        ),
    string_id_meta("name"),
    SInt16("unknown_0", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_bounds_min"),
    SInt16("widescreen_x_bounds_min"),
    SInt16("widescreen_y_bounds_max"),
    SInt16("widescreen_x_bounds_max"),
    SInt16("standard_y_bounds_min"),
    SInt16("standard_x_bounds_min"),
    SInt16("standard_y_bounds_max"),
    SInt16("standard_x_bounds_max"),
    dependency("animation"),
    string_id_meta("data_source_name"),
    string_id_meta("text_string"),
    string_id_meta("text_color"),
    SInt16("text_font"),
    SInt16("unknown_1", VISIBLE=False),
    ENDIAN=">", SIZE=76
    )


scn3_group_widget_bitmap_widget = Struct("bitmap_widget", 
    dependency("ancestor"),
    Bool32("flags", 
        ("scale_to_bounds", 1 << 3),
        "replace_with_blur",
        ("replace_with_white", 1 << 10),
        "replace_with_black",
        ),
    string_id_meta("name"),
    SInt16("unknown_0", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_bounds_min"),
    SInt16("widescreen_x_bounds_min"),
    SInt16("widescreen_y_bounds_max"),
    SInt16("widescreen_x_bounds_max"),
    SInt16("standard_y_bounds_min"),
    SInt16("standard_x_bounds_min"),
    SInt16("standard_y_bounds_max"),
    SInt16("standard_x_bounds_max"),
    dependency("animation"),
    dependency("bitmap"),
    dependency("unknown_1"),
    SEnum16("blend_method", *scn3_group_widget_bitmap_widget_blend_method),
    SInt16("unknown_2", VISIBLE=False),
    SInt16("sprite_index"),
    SInt16("unknown_3", VISIBLE=False),
    string_id_meta("data_source_name"),
    string_id_meta("sprite_data_source_name"),
    ENDIAN=">", SIZE=108
    )


scn3_group_widget_model_widget_camera_refinement_zoom_data_1 = Struct("zoom_data_1", 
    rawdata_ref("unknown", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=20
    )


scn3_group_widget_model_widget_camera_refinement_zoom_data_2 = Struct("zoom_data_2", 
    rawdata_ref("unknown", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=20
    )


scn3_group_widget_model_widget_camera_refinement = Struct("camera_refinement", 
    string_id_meta("biped", VISIBLE=False),
    Array("unknown_array", SUB_STRUCT=Float("unknown"), SIZE=8, VISIBLE=False),
    reflexive("zoom_data_1", scn3_group_widget_model_widget_camera_refinement_zoom_data_1),
    reflexive("zoom_data_2", scn3_group_widget_model_widget_camera_refinement_zoom_data_2),
    VISIBLE=False,
    ENDIAN=">", SIZE=60
    )


scn3_group_widget_model_widget = Struct("model_widget", 
    dependency("ancestor"),
    Bool32("flags", *unknown_flags_32),
    string_id_meta("name"),
    SInt16("unknown", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_bounds_min"),
    SInt16("widescreen_x_bounds_min"),
    SInt16("widescreen_y_bounds_max"),
    SInt16("widescreen_x_bounds_max"),
    SInt16("standard_y_bounds_min"),
    SInt16("standard_x_bounds_min"),
    SInt16("standard_y_bounds_max"),
    SInt16("standard_x_bounds_max"),
    dependency("animation"),
    reflexive("camera_refinement", scn3_group_widget_model_widget_camera_refinement),
    ENDIAN=">", SIZE=72
    )


scn3_group_widget = Struct("group_widget", 
    dependency("ancestor"),
    Bool32("flags", 
        ("initially_hidden", 1 << 3),
        ),
    string_id_meta("name"),
    SInt16("unknown", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_offset"),
    SInt16("widescreen_x_offset"),
    SInt16("widescreen_y_unknown"),
    SInt16("widescreen_x_unknown"),
    SInt16("standard_y_offset"),
    SInt16("standard_x_offset"),
    SInt16("standard_y_unknown"),
    SInt16("standard_x_unknown"),
    dependency("animation"),
    reflexive("list_widgets", scn3_group_widget_list_widget),
    reflexive("text_widgets", scn3_group_widget_text_widget),
    reflexive("bitmap_widgets", scn3_group_widget_bitmap_widget),
    reflexive("model_widgets", scn3_group_widget_model_widget),
    ENDIAN=">", SIZE=108
    )


scn3_button_key_legend = Struct("button_key_legend", 
    dependency("legend"),
    ENDIAN=">", SIZE=16
    )


scn3_meta_def = BlockDef("scn3", 
    Bool32("flags", *unknown_flags_32),
    string_id_meta("name"),
    SInt16("unknown_0", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_bounds_min"),
    SInt16("widescreen_x_bounds_min"),
    SInt16("widescreen_y_bounds_max"),
    SInt16("widescreen_x_bounds_max"),
    SInt16("standard_y_bounds_min"),
    SInt16("standard_x_bounds_min"),
    SInt16("standard_y_bounds_max"),
    SInt16("standard_x_bounds_max"),
    dependency("animation"),
    dependency("strings"),
    dependency("ancestor"),
    string_id_meta("default_key_legend_string"),
    reflexive("data_sources", scn3_data_source),
    reflexive("group_widgets", scn3_group_widget),
    reflexive("button_key_legends", scn3_button_key_legend),
    dependency("ui_sounds"),
    ascii_str32("script_title"),
    SInt16("script_index"),
    SInt16("unknown_1", VISIBLE=False),
    TYPE=Struct, ENDIAN=">", SIZE=168
    )