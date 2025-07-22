# General extension utilities.

block_sets = {}

# Register an extension as a block set.
def register_extension(extension_name: str, extension): 
    block_sets.update({extension_name:extension})

# Run a block function itself.
def run_block_func(block, args, script):
    return block.info["function"](args, script)

# Get a block set itself.
def get_block_set(set: str): return block_sets[set]

# Get a block sets map.
def get_block_map(set: str): return get_block_set(set).block_map

# Grab the block data from a set.
def get_raw_block(opcode: str):
    split = opcode.split("_")

    block_set = split[:1][0]
    block_map = get_block_map(block_set)
    block_opcode = "_".join(split[1:])

    return block_map[block_opcode],block_opcode,block_set