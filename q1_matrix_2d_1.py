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


if __name__ == '__main__':
	matrix = [
		[-10, -8, -3, 5, 12, 17],
		[-7, -6, -1, 7, 13, 18],
		[-3, 0, 5, 10, 17, 23],
		[3, 8, 12, 15, 21, 28],
		[5, 12, 19, 25, 31, 37]
	]
	print(search_m2(matrix, 25))
	print(search_m3(matrix, 25))
	print(search_m4(matrix, 25))
