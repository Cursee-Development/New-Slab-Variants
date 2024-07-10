package com.cursee.new_slab_variants;

import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.SlabBlock;
import net.minecraft.world.level.block.state.BlockBehaviour;

import java.util.function.Supplier;

public class NewSlabVariants {

    public static void init() {}

//    public static final Item ACACIA_LOG_SLAB = Registry.register(BuiltInRegistries.ITEM, ResourceLocation.fromNamespaceAndPath(Constants.MOD_ID, "acacia_log_slab"), new BlockItem(Registry.register(BuiltInRegistries.BLOCK, ResourceLocation.fromNamespaceAndPath(Constants.MOD_ID, "acacia_log_slab"), new SlabBlock(BlockBehaviour.Properties.ofFullCopy(Blocks.ACACIA_LOG))), new Item.Properties()));
//
//    public static final CreativeModeTab SLAB_TAB = Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB, ResourceLocation.fromNamespaceAndPath(Constants.MOD_ID, "slab_tab"), CreativeModeTab.builder(CreativeModeTab.Row.TOP, 0)
//            .title(Component.translatable("itemGroup.newSlabVariants"))
//            .icon(() -> new ItemStack(ACACIA_LOG_SLAB))
//            .displayItems((context, output) -> {
//                output.accept(ACACIA_LOG_SLAB);
//            })
//            .build());
}