from supyr_struct.defs.tag_def import TagDef
from ..common_descriptors import *
from ..fields import *

def get(): return shop_wad_def

item_type = LUEnum32('type',
    ('exit',   0),
    ('key',    1),
    ('potion', 3),

    ('ten strength', 5),
    ('ten speed', 6),
    ('ten armor', 7),
    ('ten magic', 8),

    ('reflect shield', 9),
    ('phoenix',       10),
    ('rapid fire',    11),
    ('three way shot',    12),

    ('hammer',        13),
    ('elec shield',   14),
    ('fire shield',   15),

    ('food',     17),
    ('levitate', 18),
    ('growth',   19),

    ('fire amulet',  20),
    ('elec amulet',  21),
    ('light amulet', 22),
    ('acid amulet',  23),

    ('super shot', 24),

    ('fire breath', 25),
    ('lightning breath', 26),
    ('acid breath',  27),

    ('invisibility', 30),
    ('invulnerable', 31),
    ('x-ray',    32),
    ('gas mask', 33),

    ('anti-death', 35),
    ('hand-of-death', 36),
    ('health vampire', 37),
    ('mikey dummy', 38),

    ('unknown1', 4),
    ('unknown2', 16),
    ('unknown3', 28),
    ('unknown4', 29),
    ('unknown5', 34),
    )

item = Struct('item',
    StrLatin1('blit', GUI_NAME='icon id',     SIZE=32),
    StrLatin1('desc', GUI_NAME='description', SIZE=32),
    LFloat('scale'),
    item_type,
    LUInt32('price'),
    LUInt32('amount'),
    )

item_array = Lump('items',
    SUB_STRUCT=item, SIZE=lump_size, POINTER=lump_pointer
    )

shop_wad_def = TagDef(
    rom_header,
    lump_headers,

    #these need to be in a container to have the same index
    #ordering as their headers in the lump_headers array
    Container('lumps',
        item_array
    ),
    
    NAME='gdl shop wad',
    ext=".wad", def_id="shop"
    )
