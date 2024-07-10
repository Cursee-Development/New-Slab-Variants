import os
from typing import List

def print_filenames(directory: str) -> None:
    for filename in os.listdir(directory):
        file_path: str = os.path.join(directory, filename)

        slab_id = filename.replace(".json", "")

        if os.path.isfile(file_path):
            # print("public static final Item " + slab_id.upper() + " = Registry.register(BuiltInRegistries.ITEM, ResourceLocation.fromNamespaceAndPath(Constants.MOD_ID, \"" + slab_id + "\"), new BlockItem(Registry.register(BuiltInRegistries.BLOCK, ResourceLocation.fromNamespaceAndPath(Constants.MOD_ID, \"" + slab_id + "\"), new SlabBlock(BlockBehaviour.Properties.ofFullCopy(Blocks." + slab_id.replace("_slab", "").upper() + "))), new Item.Properties()));")
            print("                output.accept(" + slab_id.upper() + ");")

# Set the directory
directory: str = 'recipe'

# Call the function
print_filenames(directory)
