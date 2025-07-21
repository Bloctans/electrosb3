# General extension utilities.

block_sets = {}

# Register an extension as a block set.
def register_extension(extension_name: str, extension): 
    block_sets.update({extension_name:extension})

# Run a block function itself.
def run_block_func(block, args, script):
    opcode = block.opcode

    block_map = get_block_map(block.block_set)
    return block_map[opcode]["function"](args, script)

# Get a block sets map.
def get_block_map(set: str):
    return block_sets[set].block_map

# Grab the block data from a set.
def get_raw_block(opcode: str):
    split = opcode.split("_")

    block_set = split[:1][0]
    block_map = get_block_map(block_set)
    block_opcode = "_".join(split[1:])

    return block_map[block_opcode],block_opcode,block_set