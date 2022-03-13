# given numbers till from 1 to N find the first missing number
# eg -  
# -1, 3, 5, 2, -6, 1, 8, 1
# ans = 4 
# explanation 1, 2, 3, are present therefore, first missing number is 4

# 5, 3, 1, 4, 2
# ans = 6
# explanation 1,2,3,4,5 all the present therefore, return N + 1 = 6


def sol_m1(arr):
	# iterate from 1 to N
	# for each iteration check of the number is present in the arr.
	# if not present return that number
	# complexity = N * N, 1

	for i in range(1, len(arr)+1):
		if not i in arr:
			return i
	return len(arr) + 1

# def sol_m2(arr, N):
# 	# sort the array and use binary search to find the first missing number
# 	# complexity = N * log(N) + log(N), N
# 	# this method will not work in case of duplicates
# 	arr.sort()

# 	def find_st_ind():
# 		st = 0
# 		end = len(arr) - 1
# 		ans = N+1
# 		while st<=end:
# 			mid = (st+end)//2

# 			if arr[mid] >= 1:
# 				ans = mid
# 				end = mid - 1
# 			else:
# 				st = mid + 1
# 		return ans

# 	def find_end_ind():
# 		st = 0
# 		end = len(arr) - 1
# 		ans = N+1
# 		while st<=end:
# 			mid = (st+end)//2

# 			if arr[mid] > N:
# 				end = mid - 1
# 			else:
# 				st = mid + 1
# 				ans = mid
# 		return ans
	
# 	def binary_sc(st, end):
# 		if arr[st] == 1:
# 			diff = st - arr[st]
# 		else:
# 			return 1
# 		ans = None
# 		while st <= end:
# 			mid = (st+end)//2
# 			if mid - arr[mid] == diff:
# 				ans = mid
# 				st = mid + 1
# 			else:
# 				end = mid - 1
# 		return ans + 1 if ans else None

# 	st = find_st_ind()
# 	end = find_end_ind()
# 	print(arr)
# 	print(st, end)
# 	if st<=end:
# 		return binary_sc(st, end)
# 	return N + 1


def sol_m3(arr):
	# sort the array and use linear search to find the first missing number
	# complexity = N * log(N) + log(N), N
	arr.sort()
	st = 0
	for i in range(0, len(arr)):
		if arr[i] <= 0:
			continue
		else:
			st = i
			break
	i = st
	counter = 1
	for i in range(st, len(arr)):
		if arr[i]>counter and counter<=len(arr):
			return counter
		if arr[i] == counter:
			counter = counter + 1
	return len(arr) + 1


def sol_m4(arr, N):
	# use hash maps
	# complexity = N + N, N
	hash = [0] * (len(arr) + 1)
	for i in range(0, N):
		if arr[i] > 0 and arr[i] < N+1:
			hash[arr[i]] += 1
	for j in range(1, len(hash)):
		if hash[j] == 0:
			return j
	return N + 1


def sol_m5(arr):
	# convert less than 1 to N + 1000
	# now mark indices of elements to be preset if elements are from 1 to N
	# find the first Non negative index
	# return first Non negative index + 1
	for i in range(0, len(arr)):
		if arr[i] > len(arr) or arr[i] <=0:
			arr[i] = len(arr) + 1000000 

	for i in range(0, len(arr)):
		if abs(arr[i]) == len(arr) + 1000000:
			continue
		else:
			arr[abs(arr[i]) - 1] = -1 * abs(arr[abs(arr[i]) - 1])

	for i in range(0, len(arr)):
		if arr[i] > 0:
			return i + 1
	return len(arr) + 1


if __name__ == '__main__':
	arr = [-1, 3, 5, 2, -6, 1, 8, 1]
	# arr = [5, 10, 1, 4, 2]
	print(sol_m1(arr))
	# print(sol_m2(arr, len(arr)))
	print(sol_m4(arr, len(arr)))
	print(sol_m3(arr))
	print(sol_m5(arr))



