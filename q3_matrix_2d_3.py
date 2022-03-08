def sol_m1(matrix):
	# at each row count the total no of ones and maintain the max
	# complexity = N * M, 1
	maxa = 0
	for r in range(len(matrix)):
		maxa = max(maxa, sum(matrix[r]))
	return maxa


def sol_m2(matrix):
	# iterate through each row
	# use binary search at each row to find total no of ones
	# complexity - N log(M), 1

	def binary_sc(arr, row):
		st = 0
		end = len(arr)
		ans = len(arr)
		while st <= end:
			mid = (st + end)//2

			if arr[mid] == 1:
				ans = mid
				end = mid - 1
			else:
				st = mid + 1
		return len(arr) - ans

	maxa = 0
	for r in range(len(matrix)):
		maxa = max(maxa, binary_sc(matrix[r], r))
	return maxa


def rt_solve(matrix):
	# use RT approach-
	# start a pointer at top right cornor of the matrix.
	# move to the left if one is present 
	# move downwards othervise
	# complexity = N + M, 1
	r, c = 0, len(matrix[0]) - 1
	while r<len(matrix) and c>0:
		if c-1>=0 and matrix[r][c-1] == 1:
			c-=1
		else:
			r+=1
	return len(matrix[0]) - c



if __name__ == '__main__':
	matrix = [
		[0, 0, 0, 0, 1, 1, 1, 1],
		[0, 0, 0, 0, 1, 1, 1, 1],
		[0, 0, 1, 1, 1, 1, 1, 1],
		[0, 0, 0, 1, 1, 1, 1, 1],
		[0, 0, 0, 1, 1, 1, 1, 1],
		[0, 0, 0, 1, 1, 1, 1, 1],
	]
	print(sol_m1(matrix))
	print(sol_m2(matrix))
	print(rt_solve(matrix))
