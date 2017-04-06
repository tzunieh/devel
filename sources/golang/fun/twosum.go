package fun


func TwoSum(nums []int, target int) [2]int {
	var reversed_data map[int]int

	reversed_data = make(map[int]int)
	for i, v := range nums {
		if j, ok := reversed_data[v]; ok {
			return [2]int{j, i}
		} else {
			reversed_data[target - v] = i
		}
	}
	return [2]int{-1, -1}
}
