package fun


func IndexOf(data []int, value int, start int) int {
	for i, v := range data[start:] {
		if v == value {
			return i + start
		}
	}
	return -1
}

func TwoSum(nums []int, target int) (bool, [2]int) {
	for idx_0, val_0 := range nums {
		idx_1 := IndexOf(nums, target - val_0, idx_0 + 1)
        if idx_1 >= 0 {
			return false, [2]int{idx_0, idx_1}
        }
	}
	return true, [2]int{}
}
