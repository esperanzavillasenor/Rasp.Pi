from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    #mc = Minecraft.create("10.183.3.25", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	

def clear_with_air_block(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)	
	
def layer (mc, x, y, z, s ,e,w, m):
	# s start , e end m material  , w width m material 
	w = int(w/2)
	print("w ",w)
	mc.setBlocks(x-w,y,z+s,x+w,y,z+e-1,m)


def body(mc,x, y, z):
	clear_with_air_up(mc, x, y, z+1,10,20,10)
	blackwool=35,15
	savey = y
	y = y; s,e,w = 2,5,1; #0 l shoe
	layer(mc, x,y,z+2,s,e,w,blackwool); #0 l shoe
	y = y; s,e,w = 6,9,1; #0 r shoe
	layer(mc, x,y,z+2,s,e,w,blackwool); #0 r shoe
	y = y+1; s,e,w = 3,5,1; #1 l shoe
	layer(mc, x,y,z+2,s,e,w,blackwool); #1 l shoe
	y = y; s,e,w = 6,8,1; #1 r shoe
	layer(mc, x,y,z+2,s,e,w,blackwool); #1 r shoe
	y = y+1; s,e,w = 1,2,1; #2 l hand
	layer(mc, x,y,z+2,s,e,w,blackwool); #2 l hand
	y = y; s,e,w = 2,9,1; #2 lower mid 
	layer(mc, x,y,z+2,s,e,w,22); #2 lower mid
	y = y; s,e,w = 9,10,1; #2 r hand
	layer(mc, x,y,z+2,s,e,w,blackwool); #2 r hand
	y = y+1; s,e,w =1,2,1; #3 l hand
	layer(mc, x,y,z+2,s,e,w,blackwool); #3 l hand
	y = y; s,e,w = 2,9,1; #3 lower mid
	layer(mc, x,y,z+2,s,e,w,22); #3 lower mid
	y = y; s,e,w = 9,10,1; #3 r hand
	layer(mc, x,y,z+2,s,e,w,blackwool); #3 r hand
	y = y+1; s,e,w = 1,2,1; #4 l arm
	layer(mc, x,y,z+2,s,e,w,41); #4 l arm
	y = y; s,e,w = 2,9,1; #4 mid section
	layer(mc, x,y,z+2,s,e,w,22); #4 mid section
	y = y; s,e,w = 9,10,1; #4 r arm
	layer(mc, x,y,z+2,s,e,w,41); #4 r arm
	y = y+1; s,e,w = 1,3,1; #5 l arm & l chest
	layer(mc, x,y,z+2,s,e,w,41); #5 l arm & l chest
	y = y; s,e,w = 3,4,1; #5 l strap
	layer(mc, x,y,z+2,s,e,w,22); #5 l strap
	y = y; s,e,w = 4,7,1; #5 mid
	layer(mc, x,y,z+2,s,e,w,42); #5 mid
	y = y; s,e,w = 7,8,1; #5 r strap
	layer(mc, x,y,z+2,s,e,w,22); #5 r strap
	y = y; s,e,w = 8,10,1; #5 r arm & r chest
	layer(mc, x,y,z+2,s,e,w,41); #5 r arm & r chest
	y = y+1; s,e,w = 1,3,1; #6 l arm & l chest
	layer(mc, x,y,z+2,s,e,w,41); #6 l arm & l chest
	y = y; s,e,w = 3,4,1; #6 l strap
	layer(mc, x,y,z+2,s,e,w,22); #6 l strap
	y = y; s,e,w = 4,7,1; #6 mid
	layer(mc, x,y,z+2,s,e,w,42); #6 mid
	y = y; s,e,w = 7,8,1; #5 r strap
	layer(mc, x,y,z+2,s,e,w,22); #5 r strap
	y = y; s,e,w = 8,10,1; #6 r arm & r chest
	layer(mc, x,y,z+2,s,e,w,41); #6 r arm & r chest
	y = y+1; s,e,w = 1,2,1; #6 l arm
	layer(mc, x,y,z+2,s,e,w,41); #6 l arm
	y = y; s,e,w = 2,9,1; #6 high mid 
	layer(mc, x,y,z+2,s,e,w,22); #6 high mid
	y = y; s,e,w = 9,10,1; #6 r arm
	layer(mc, x,y,z+2,s,e,w,41); #6 r arm
	y = y+1; s,e,w = 1,2,1; #7 l sleeve
	layer(mc, x,y,z+2,s,e,w,22); #7 l sleeve
	y = y; s,e,w = 2,9,1; #7 neck
	layer(mc, x,y,z+2,s,e,w,41); #7 neck
	y = y; s,e,w = 9,10,1; #7 r sleeve
	layer(mc, x,y,z+2,s,e,w,22); #7 r sleeve
	y = y+1; s,e,w = 1,4,1; #8 l face
	layer(mc, x,y,z+2,s,e,w,41); #8 l face
	y = y; s,e,w = 4,8,1; #8 smile
	layer(mc, x,y,z+2,s,e,w,blackwool); #8 smile
	y = y; s,e,w = 8,10,1; #8 r face
	layer(mc, x,y,z+2,s,e,w,41); #8 r face
	y = y+1; s,e,w = 1,3,1; #9 l face
	layer(mc, x,y,z+2,s,e,w,41); #9 l face
	y = y; s,e,w = 3,4,1; #9 dimple
	layer(mc, x,y,z+2,s,e,w,blackwool); #9 dimple
	y = y; s,e,w = 4,10,1; #9 r face
	layer(mc, x,y,z+2,s,e,w,41); #9 r face
	y = y+1; s,e,w = 1,10,1; # 10 mid face
	layer(mc, x,y,z+2,s,e,w,41); #9 mid face
	y = y+1; s,e,w = 1,3,1; #11 l face
	layer(mc, x,y,z+2,s,e,w,41); #11 l face
	y = y; s,e,w = 3,5,1; #11 l lower goggle
	layer(mc, x,y,z+2,s,e,w,1); #11 l lower goggle
	y = y; s,e,w = 5,6,1; #11 nose
	layer(mc, x,y,z+2,s,e,w,41); #11 nose
	y = y; s,e,w = 6,8,1; #11 r lower goggle
	layer(mc, x,y,z+2,s,e,w,1); #11 r lower goggle
	y = y; s,e,w = 8,10,1; #11 r face
	layer(mc, x,y,z+2,s,e,w,41); #11 r face
	y = y+1; s,e,w = 1,2,1; #12 l head
	layer(mc, x,y,z+2,s,e,w,41); #12 l head
	y = y; s,e,w = 2,3,1; #12 l goggle
	layer(mc, x,y,z+2,s,e,w,1); #12 l goggle
	y = y; s,e,w = 3,5,1; #12 l eye
	layer(mc, x,y,z+2,s,e,w,42); #12 l eye
	y = y; s,e,w = 5,6,1; #12 mid goggle
	layer(mc, x,y,z+2,s,e,w,1); #12 mid goggle
	y = y; s,e,w = 6,8,1; #12 r eye
	layer(mc, x,y,z+2,s,e,w,42); #12 r eye
	y = y; s,e,w = 8,9,1; #12 r goggle
	layer(mc, x,y,z+2,s,e,w,1); #12 r goggle
	y = y; s,e,w = 9,10,1; #12 r head
	layer(mc, x,y,z+2,s,e,w,41); #12 r head
	y = y+1; s,e,w = 1,2,1; #13 l head
	layer(mc, x,y,z+2,s,e,w,41); #13 l head
	y = y; s,e,w = 2,3,1; #13 l goggle
	layer(mc, x,y,z+2,s,e,w,1); #13 l goggle
	y = y; s,e,w = 3,4,1; #13 l eye
	layer(mc, x,y,z+2,s,e,w,42); #13 l eye
	y = y; s,e,w = 4,5,1; #13 l pupil
	layer(mc, x,y,z+2,s,e,w,blackwool); #13 l pupil
	y = y; s,e,w = 5,6,1; #13 mid goggle
	layer(mc, x,y,z+2,s,e,w,1); #13 mid goggle
	y = y; s,e,w = 6,7,1; #13 r eye
	layer(mc, x,y,z+2,s,e,w,42); #13 r eye
	y = y; s,e,w = 7,8,1; #13 r pupil
	layer(mc, x,y,z+2,s,e,w,blackwool); #13 r pupil
	y = y; s,e,w = 8,9,1; #13 r goggle
	layer(mc, x,y,z+2,s,e,w,1); #13 r goggle
	y = y; s,e,w = 9,10,1; #13 r head
	layer(mc, x,y,z+2,s,e,w,41); #13 r head
	y = y+1; s,e,w = 2,3,1; #14 l top head
	layer(mc, x,y,z+2,s,e,w,41); #14 l top head
	y = y; s,e,w = 3,5,1; #14 l upper goggle
	layer(mc, x,y,z+2,s,e,w,1); #14 l upper goggle
	y = y; s,e,w = 5,6,1; #14 forehead
	layer(mc, x,y,z+2,s,e,w,41); #14 forehead
	y = y; s,e,w = 6,8,1; #14 r upper goggle
	layer(mc, x,y,z+2,s,e,w,1); #14 r upper goggle
	y = y; s,e,w = 8,9,1; #14 r top head
	layer(mc, x,y,z+2,s,e,w,41); #14 r top head
	y = y+1; s,e,w = 3,8,1; #15 mid top head
	layer(mc, x,y,z+2,s,e,w,41); #15 mid top head
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.player.setPos(x, y+1, z)
	print("position ",x,y,z)
	body(mc, x,y,z+3)
	#mc.player.setPos(x-10, y, z + 10)


main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
