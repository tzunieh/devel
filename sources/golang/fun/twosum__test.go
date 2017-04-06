package fun

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestSortedTwoSum(t *testing.T) {
	var res [2]int

	res = TwoSum([]int{2, 7, 11, 15}, 9)
	assert.Equal(t, res, [2]int{0, 1},  "they should be equal")

	res = TwoSum([]int{2, 7, 11, 15}, 18)
	assert.Equal(t, res, [2]int{1, 2},  "they should be equal")
}

func TestUnsortedTwoSum(t *testing.T) {
	var res [2]int

	res = TwoSum([]int{3, 2, 9, 11, 7, 4}, 5)
	assert.Equal(t, res, [2]int{0, 1},  "they should be equal")

	res = TwoSum([]int{3, 2, 9, 11, 7, 4}, 20)
	assert.Equal(t, res, [2]int{2, 3},  "they should be equal")

	res = TwoSum([]int{3, 22, 9, 11, 7, 4}, 15)
	assert.Equal(t, res, [2]int{3, 5},  "they should be equal")
}

func TestDuplicatedTwoSum(t *testing.T) {
	var res [2]int

	res = TwoSum([]int{3, 3, 5, 7, 9}, 6)
	assert.Equal(t, res, [2]int{0, 1},  "they should be equal")
}

func TestZeroTwoSum(t *testing.T) {
	var res [2]int

	res = TwoSum([]int{0, 4, 3, 0}, 0)
	assert.False(t, err, false,  "error should be dalse")
	assert.Equal(t, res, [2]int{0, 3},  "they should be equal")
}

func TestNegativeTwoSum(t *testing.T) {
	var res [2]int

	res = TwoSum([]int{0, 4, 3, -2}, 2)
	assert.False(t, err, false,  "error should be dalse")
	assert.Equal(t, res, [2]int{1, 3},  "they should be equal")
}
