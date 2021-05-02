def selection_sort(arr):
	"""选择排序"""
	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] > arr[j]:
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp

	return arr
