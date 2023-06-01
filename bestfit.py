# Python3 implementation of the Best fit
# sit memory management algorithm
# using linked list

# Two global counters
g = 0; k = 0

# Structure for free list
class free:
	def __init__(self):
		self.tag=-1
		self.size=0
		self.next=None
free_head = None; prev_free = None

# Structure for allocated list
class alloc:
	def __init__(self):
		self.block_id=-1
		self.tag=-1
		self.size=0
		self.next=None

alloc_head = None;prev_alloc = None

# Function to create free
# list with given sizes
def create_free(c):
	global g,prev_free,free_head
	p = free()
	p.size = c
	p.tag = g
	p.next = None
	if free_head is None:
		free_head = p
	else:
		prev_free.next = p
	prev_free = p
	g+=1


# Function to print free list which
# prints free blocks of given sizes
def print_free():
	p = free_head
	print("Tag\tSize")
	while (p != None) :
		print("{}\t{}".format(p.tag,p.size))
		p = p.next
	


# Function to print allocated list which
# prints allocated blocks and their block ids
def print_alloc():
	p = alloc_head
	print("Tag\tBlock ID\tSize")
	while (p is not None) :
		print("{}\t{}\t{}\t".format(p.tag,p.block_id,p.size))
		p = p.next
	


# Function to allocate memory to
# blocks as per First fit algorithm
def create_alloc(c):
	global k,alloc_head
	# create node for process of given size
	q = alloc()
	q.size = c
	q.tag = k
	q.next = None
	p = free_head

	# Iterate to find first memory
	# block with appropriate size
	while (p != None) :
		if (q.size <= p.size):
			break
		p = p.next
	

	# Node found to allocate
	if (p != None) :
		# Adding node to allocated list
		q.block_id = p.tag
		p.size -= q.size
		if (alloc_head == None):
			alloc_head = q
		else :
			prev_alloc = alloc_head
			while (prev_alloc.next != None):
				prev_alloc = prev_alloc.next
			prev_alloc.next = q
		
		k+=1
	
	else: # Node found to allocate space from
		print("Block of size {} can't be allocated".format(c))

# Function to delete node from
# allocated list to free some space
def delete_alloc(t):
	global alloc_head
	# Standard delete function
	# of a linked list node
	p = alloc_head; q = None

	# First, find the node according
	# to given tag id
	while (p != None) :
		if (p.tag == t):
			break
		q = p
		p = p.next
	
	if (p == None):
		print("Tag ID doesn't exist")
	elif (p == alloc_head):
		alloc_head = alloc_head.next
	else:
		q.next = p.next
	temp = free_head
	while (temp != None) :
		if (temp.tag == p.block_id) :
			temp.size += p.size
			break
		
		temp = temp.next
	


# Driver Code
if __name__ == '__main__':
	blockSize = [100, 500, 200]
	processSize = [417, 112, 426, 95]
	m = len(blockSize)
	n = len(processSize)

	for i in range(m):
		create_free(blockSize[i])

	for i in range(n):
		create_alloc(processSize[i])

	print_alloc()

	# Block of tag id 0 deleted
	# to free space for block of size 426
	delete_alloc(0)

	create_alloc(426)
	print("After deleting block with tag id 0.")
	print_alloc()
