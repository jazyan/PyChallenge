from PIL import Image

def check_bounds(pos):
	return pos[0] >= 0 and pos[0] <= 99 and pos[1] >= 0 and pos[1] <= 99

# original image
orig_im = Image.open('wire.png')
orig_pix = orig_im.load()

# where we'll store our spiralled image
new_im = Image.new('RGB', (100, 100))
new_pix = new_im.load()

new_pix[0, 0] = orig_pix[0, 0]
curr_pos = (0, 0)
curr_ind = 0
visited = set()
visited.add((0, 0))
# 0 = east, 1 = south, 2 = west, 3 = north
direction = {0: [1, 0], 1: [0, 1], 2: [-1, 0], 3: [0, -1]}
curr_direction = 0

while curr_ind < 9999:
	# get the corresponding increment vector
	inc_vector = direction[curr_direction]
	# get a new position
	new_pos = (curr_pos[0] + inc_vector[0], curr_pos[1] + inc_vector[1])
	# if the new position is in bounds and we haven't visited it yet
	if check_bounds(new_pos) and new_pos not in visited:
		# move forward in spiral
		new_pix[new_pos[0], new_pos[1]] = orig_pix[curr_ind, 0]
		curr_ind += 1
		visited.add(new_pos)
		# update curr_pos
		curr_pos = new_pos
	else:
		# rotate 90 deg right and keep curr_pos
		curr_direction = (curr_direction + 1) % 4

new_im.show()