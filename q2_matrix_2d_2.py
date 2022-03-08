# given a 2D matrix such that all the rows are sorted
# and all the columns are sorted
# find the key in the matrix

# m1 brute force
# complexity - N * M, 1

def search_m2(matrix, key):
	# m2 search in every row using binary search
	# complexity N * log(M), 1
	def binary_sc(arr, i):
		st = 0
		end = len(arr) - 1
		ans = None
		while st <= end:
			mid = (st+end)//2
			if arr[mid] > key:
				end = mid - 1
			elif arr[mid] < key:
				st = mid + 1
			elif arr[mid] == key:
				ans = (i, mid)
				break
		return ans 

	for i in range(len(matrix)):
		ans = binary_sc(matrix[i], i)
		if ans:
			return ans
	return "Not found"


def search_m3(matrix, key):
	# m3 search in every col using binary search
	# complexity M * log(N), 1
	def binary_sc(matrix, col):
		st = 0
		end = len(matrix) - 1
		ans = None
		while st <= end:
			mid = (st+end)//2
			if matrix[mid][col] > key:
				end = mid - 1
			elif matrix[mid][col] < key:
				st = mid + 1
			elif matrix[mid][col] == key:
				ans = (mid, col)
				break
		return ans 

	for col in range(len(matrix[0])):
		ans = binary_sc(matrix, col)
		if ans:
			return ans
	return "Not found"

def search_m4(matrix, key):
	# m2 search in every row using binary search
	# complexity N * log(M), 1
	def binary_sc(arr, i):
		st = 0
		end = len(arr) - 1
		ans = None
		while st <= end:
			mid = (st+end)//2
			if arr[mid] > key:
				end = mid - 1
			elif arr[mid] < key:
				st = mid + 1
			elif arr[mid] == key:
				ans = (i, mid)
				break
		return ans 

	for row in range(len(matrix)):
		ans = None
		if key >= matrix[row][0] and key <= matrix[row][-1]: 
			ans = binary_sc(matrix[row], row)
		if ans:
			return ans
	return "Not found"


def search_m5(matrix, key):
	# m2 search in every row using binary search
	# complexity N * log(M), 1
	def binary_sc(arr, i):
		st = 0
		end = len(arr) - 1
		ans = None
		while st <= end:
			mid = (st+end)//2
			if arr[mid] > key:
				end = mid - 1
			elif arr[mid] < key:
				st = mid + 1
			elif arr[mid] == key:
				ans = (i, mid)
				break
		return ans 

	st = 0
	end = len(matrix) - 1
	row_ans = None
	while st <= end:
		mid = (st + end)//2
		if key >= matrix[mid][0] and key <= matrix[mid][-1]:
			row_ans = mid
			break
		elif key < matrix[mid][0]:
			end = mid - 1
		elif key > matrix[mid][-1]:
			st = mid + 1
	if row_ans:
		return binary_sc(matrix[row_ans], row_ans)
	else:
		return row_ans


def search_m6(matrix, key):
	# m4 search in RT method
	# complexity N + M, 1
	r, c = 0, len(matrix) - 1
	while r < len(matrix) and c >= 0:
		if matrix[r][c] == key:
			return r, c
		elif matrix[r][c] < key:
			r += 1
		elif matrix[r][c] > key:
			c -= 1
	return "Not Found"


def search_m7(matrix, key):
	# m7 - whole 2 dimentional array can be imagined as 1 d array of length = (len(matrix) * len(matrix[0]))
	# take st as matrix[0,0] and end as matrix[-1[-1]
	# use the binary search on the 1 d array to find the key
	# index of 1 d array can be converted in to rows and columns of 2 d array.
	st = 0
	end = (len(matrix) * len(matrix[0])) - 1

	while st <= end:
		mid = (st + end)//2
		r = mid // len(matrix[0])
		c = mid % len(matrix[0])
		if matrix[r][c] == key:
			return r, c
		elif matrix[r][c] < key:
			st = mid + 1
		elif matrix[r][c] > key:
			end = mid - 1 
	return "Not Found"

if __name__ == '__main__':
	matrix = [
		[-12, -9, -6, 3, 5, 7],
		[8, 12, 15, 19, 21, 23],
		[25, 28, 30, 32, 35, 41],
		[43, 45, 51, 53, 58, 60],
		[62, 71, 73, 85, 93, 97]
	]
	print(search_m2(matrix, 50))
	print(search_m3(matrix, 50))
	print(search_m4(matrix, 50))
	print(search_m5(matrix, 50))
	print(search_m6(matrix, 50))
	print(search_m7(matrix, 50))
