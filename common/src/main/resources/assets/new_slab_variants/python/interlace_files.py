def interlace_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

        max_lines = max(len(lines1), len(lines2))

        for i in range(max_lines):
            if i < len(lines1):
                output_file.write(lines1[i])
            if i < len(lines2):
                output_file.write(lines2[i])


if __name__ == "__main__":
    file1_path = "0GEN.txt"  # Replace with the path to your first input file
    file2_path = "1GEN.txt"  # Replace with the path to your second input file
    output_file_path = "output.txt"  # Replace with the desired output file path

    interlace_files(file1_path, file2_path, output_file_path)





# 65 elements
bases = ["podzol", "mycelium", "dirt_path", "coarse_dirt", "rooted_dirt", "mud", "clay", "gravel",
         "sand", "sandstone", "red_sand", "red_sandstone", "ice", "packed_ice", "blue_ice", "snow_block",
         "moss_block", "stone", "granite", "diorite", "andesite", "crimson_nylium",
         "warped_nylium", "soul_sand", "soul_soil", "bone_block", "blackstone",
         "calcite", "tuff", "dripstone_block", "prismarine", "magma_block",
         "obsidian", "crying_obsidian", "budding_amethyst", "brown_mushroom_block",
         "red_mushroom_block", "nether_wart_block", "warped_wart_block", "glowstone", "shroomlight",
         "dried_kelp_block", "tube_coral_block", "brain_coral_block", "bubble_coral_block",
         "fire_coral_block", "horn_coral_block", "dead_tube_coral_block", "dead_brain_coral_block",
         "dead_bubble_coral_block", "dead_fire_coral_block", "dead_horn_coral_block", "sponge",
         "wet_sponge", "melon", "pumpkin", "hay_bale", "honeycomb_block", "slime_block", "honey_block",
         "ochre_froglight", "verdant_froglight", "pearlescent_froglight", "sculk", "bedrock"]

# 161 elements
old_bases = ["oak_log", "oak_wood", "stripped_oak_log", "stripped_oak_wood",
             "spruce_log", "spruce_wood", "stripped_spruce_log", "stripped_spruce_wood",
             "birch_log", "birch_wood", "stripped_birch_log", "stripped_birch_wood",
             "jungle_log", "jungle_wood", "stripped_jungle_log", "stripped_jungle_wood",
             "acacia_log", "acacia_wood", "stripped_acacia_log", "stripped_acacia_wood",
             "dark_oak_log", "dark_oak_wood", "stripped_dark_oak_log", "stripped_dark_oak_wood",
             "mangrove_log", "mangrove_wood", "stripped_mangrove_log", "stripped_mangrove_wood",
             "cherry_log", "cherry_wood", "stripped_cherry_log", "stripped_cherry_wood",
             "bamboo_block", "stripped_bamboo_block",
             "crimson_stem", "crimson_hyphae", "stripped_crimson_stem", "stripped_crimson_hyphae",
             "warped_stem", "warped_hyphae", "stripped_warped_stem", "stripped_warped_hyphae",
             "cracked_stone_bricks", "chiseled_stone_bricks",
             "deepslate", "chiseled_deepslate", "cracked_deepslate_bricks", "cracked_deepslate_tiles",
             "reinforced_deepslate", "packed_mud", "chiseled_sandstone", "chiseled_red_sandstone",
             "netherrack", "cracked_nether_bricks", "chiseled_nether_bricks",
             "basalt", "smooth_basalt", "polished_basalt", "gilded_blackstone", "chiseled_polished_blackstone",
             "cracked_polished_blackstone_bricks", "end_stone", "purpur_pillar",
             "coal_block", "iron_block", "gold_block", "redstone_block", "emerald_block", "lapis_block",
             "diamond_block", "netherite_block", "chiseled_quartz_block", "quartz_bricks", "quartz_pillar",
             "amethyst_block", "copper_block", "exposed_copper_block", "weathered_copper_block",
             "oxidized_copper_block",
             "white_wool", "light_gray_wool", "gray_wool", "black_wool",
             "brown_wool", "red_wool", "orange_wool", "yellow_wool",
             "lime_wool", "green_wool", "cyan_wool", "light_blue_wool",
             "blue_wool", "purple_wool", "magenta_wool", "pink_wool",
             "terracotta",
             "white_terracotta", "light_gray_terracotta", "gray_terracotta", "black_terracotta",
             "brown_terracotta", "red_terracotta", "orange_terracotta", "yellow_terracotta",
             "lime_terracotta", "green_terracotta", "cyan_terracotta", "light_blue_terracotta",
             "blue_terracotta", "purple_terracotta", "magenta_terracotta", "pink_terracotta",
             "white_concrete", "light_gray_concrete", "gray_concrete", "black_concrete",
             "brown_concrete", "red_concrete", "orange_concrete", "yellow_concrete",
             "lime_concrete", "green_concrete", "cyan_concrete", "light_blue_concrete",
             "blue_concrete", "purple_concrete", "magenta_concrete", "pink_concrete",
             "white_concrete_powder", "light_gray_concrete_powder", "gray_concrete_powder", "black_concrete_powder",
             "brown_concrete_powder", "red_concrete_powder", "orange_concrete_powder", "yellow_concrete_powder",
             "lime_concrete_powder", "green_concrete_powder", "cyan_concrete_powder", "light_blue_concrete_powder",
             "blue_concrete_powder", "purple_concrete_powder", "magenta_concrete_powder", "pink_concrete_powder",
             "white_glazed_terracotta", "light_gray_glazed_terracotta", "gray_glazed_terracotta",
             "black_glazed_terracotta",
             "brown_glazed_terracotta", "red_glazed_terracotta", "orange_glazed_terracotta", "yellow_glazed_terracotta",
             "lime_glazed_terracotta", "green_glazed_terracotta", "cyan_glazed_terracotta",
             "light_blue_glazed_terracotta",
             "blue_glazed_terracotta", "purple_glazed_terracotta", "magenta_glazed_terracotta", "pink_glazed_terracotta"
             ]

# original = ["public static RegistryObject<Block> DIRT_SLAB = SLABS.register(\"dirt_slab\", () -> new SlabBlock(BlockBehaviour.Properties.of().mapColor(MapColor.WOOD).instrument(NoteBlockInstrument.BASS).strength(2.0F, 3.0F).sound(SoundType.WOOD).ignitedByLava()));",
#             "public static RegistryObject<Item> DIRT_SLAB_ITEM = SLAB_ITEMS.register(\"dirt_slab\", () -> new BlockItem(DIRT_SLAB.get(), new Item.Properties()));"]
#
# file = open("1GEN.txt", "w+")
# for item in bases:
#     # file.write(original[0].replace("DIRT", item.upper()).replace("dirt", item).replace("DIRT", item.upper()) + '\n')
#     file.write(original[1].replace("DIRT", item.upper()).replace("dirt", item).replace("DIRT", item.upper()) + '\n')
# file.close()

# for item in bases:
#     file = open(item + "_slab.json", "w+")
#     file.write(r'{ "type": "minecraft:crafting_shaped", "category": "building", "group": "wooden_slab", "key": { "#": { "item": "minecraft:acacia_wood" } }, "pattern": [ "###" ], "result": { "count": 6, "item": "newslabvariants:acacia_wood_slab" }, "show_notification": true }'.replace("acacia_wood", item))
#     file.close()

# original  = r'{ "parent": "minecraft:block/slab", "textures": { "bottom": "minecraft:block/acacia_log", "side": "minecraft:block/acacia_log", "top": "minecraft:block/acacia_log" } }'
# original2 = r'{ "parent": "minecraft:block/slab_top", "textures": { "bottom": "minecraft:block/acacia_log", "side": "minecraft:block/acacia_log", "top": "minecraft:block/acacia_log" } }'
#
# for item in bases:
#     file = open(item + "_slab.json", "w+")
#     file2 = open(item + "_slab_top.json", "w+")
#     file.write(original.replace("acacia_log", item))
#     file2.write(original2.replace("acacia_log", item))
#     file.close()
#     file2.close()




# Blockstate Generation
# original = [
#     "{ \"variants\": {",
#     "    \"type=bottom\": { \"model\": \"newslabvariants:block/acacia_wood_slab\" },",
#     "    \"type=double\": { \"model\": \"minecraft:block/acacia_wood\" },",
#     "    \"type=top\": { \"model\": \"newslabvariants:block/acacia_wood_slab_top\" } } }"
# ]
#
# for item in bases:
#     file = open(item+"_slab.json", "w+")
#     file.write(original[0]+'\n')
#     file.write(original[1].replace("acacia_wood", item)+'\n')
#     file.write(original[2].replace("acacia_wood", item)+'\n')
#     file.write(original[3].replace("acacia_wood", item))
#     file.close()

# make sure we're not generating more than we need :P
# for item in bases:
#     for item2 in old_bases:
#         if item == item2:
#             print("matching: " + item + " " + item2)

# for item in bases:
#     file = open(item + "_slab.json", "w+")
#     file.write(
#         r'{ "type": "minecraft:crafting_shaped", "category": "building", "group": "wooden_slab", "key": { "#": { "item": "minecraft:acacia_log" } }, "pattern": [ "###" ], "result": { "count": 6, "item": "newslabvariants:acacia_log_slab" }, "show_notification": true }'.replace(
#             "acacia_log", item))
#     file.close()

# Generating translations
# file = open("0GEN.txt", "w+")
# for item in bases:
#     file.write("  \"block.newslabvariants.dirt_slab\": \"Dirt Slab\",".replace("dirt_", item+"_").replace("Dirt ", item.replace("_", " ").title()+" ")+"\n")
# file.close()


# for item in bases:
#     file = open(item+"_slab.json", "w+")
#     # file2 = open(item+"_slab_top.json", "w+")
#
#     file.write(r'{ "parent": "newslabvariants:block/dirt_slab" }'.replace("dirt", item))
#     # file2.write(r'{ "parent": "minecraft:block/slab_top", "textures": { "bottom": "minecraft:block/dirt", "side": "minecraft:block/dirt", "top": "minecraft:block/dirt" } }'.replace("dirt", item))
#     file.close()
#     # file2.close()

# original_lines = [
#     "{ \"variants\": {",
#     "    \"type=bottom\": { \"model\": \"newslabvariants:block/dirt_slab\" },",
#     "    \"type=double\": { \"model\": \"minecraft:block/dirt\" },",
#     "    \"type=top\": { \"model\": \"newslabvariants:block/dirt_slab_top\" } } }"
# ]
#
# for item in bases:
#     file = open(item + "_slab.json", "w+")
#     new_lines = [
#         original_lines[0].replace("dirt", item),
#         original_lines[1].replace("dirt", item),
#         original_lines[2].replace("dirt", item),
#         original_lines[3].replace("dirt", item)
#     ]
#     file.write("\n".join(new_lines) + "\n")
# file.close()
