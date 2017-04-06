package fun


func TwoSum(nums []int, target int) []int {
	var reversed_data map[string]int

	for i, v := range nums {
		if j, ok := reversed_data[v]; ok {
			return []int{j, i}
		} else {
			reversed_data[target - v] = i
		}
	}
}
