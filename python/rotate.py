def rightrotate(arr, n):

	length = len(arr)

    rot_arr = [0] * length
 
	index = 0 - length

	while index < 0:
		rot_arr[index + 1] = arr[index]
		index = index + 1	

	return rot_arr
	
def leftr(arr, n):
    for i in xrange(n):
		arr = leftrotate(arr)
	return arr

def leftrotate(arr):
	length = len(arr)

	rot_arr = [0] * length

    index = 0

	while index <= length-1:
		rot_arr[index-1] = arr[index]
		index = index + 1

	return rot_arr
		
