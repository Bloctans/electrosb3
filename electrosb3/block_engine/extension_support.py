# General extension related stuff.

BLOCK_HAT = 1
BLOCK_STACK = 2
BLOCK_C = 3

block_sets = {}
def register_extension(extension_name: str, extension): block_sets.update({extension_name:extension})