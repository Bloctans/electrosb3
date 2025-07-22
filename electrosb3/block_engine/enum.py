BLOCK_HAT = 1
BLOCK_STACK = 2
BLOCK_C = 3
BLOCK_INPUT = 4

INPUT_NORMAL = 1
INPUT_BRANCH = 2

YIELD_NONE = 1 # Dont yield, continue to run blocks
YIELD = 2 # Yield and call the same block next frame
YIELD_TILL_NEXT_FRAME = 3 # Yield for a single frame