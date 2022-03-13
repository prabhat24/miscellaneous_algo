
def freq_m2(arr, N):
	hash = {}
	for i in range(0, N):
		hash[arr[i]] = hash.get(arr[i], 0) + 1
	print(hash)



def freq_m3(arr, N):
	k = 1000000
	for i in range(0, N):
		if arr[i] < 1 or arr[i] > N:
			arr[i] = 0

	for i in range(0, N):
		if arr[i] % k > 0:
			arr[(arr[i] % k) - 1] += k

	for i in range(0, N):
		arr[i] = arr[i] // k
	print(arr)



if __name__ == '__main__':
	arr = [1, 7, 2, 10, 8, 1, 5, 7, 5, 8]
	freq_m2(arr, len(arr))
	freq_m3(arr, len(arr))