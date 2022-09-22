/*
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    const prevMap = {}

    nums.forEach((value, index) => {
        prevMap[value] = index
    })

    for (let index = 0; index < nums.length; index++) {
        const diff = target - nums[index]

        if (prevMap[diff] !== undefined && prevMap[diff] !== index) {
            return [prevMap[diff], index]
        }
    }
};

// Example 1:
const nums1 = [2,7,11,15]
const target1 = 9
//---> Output: [0,1]

// Example 2:
const nums2 = [3,2,4]
const target2 = 6
//---> Output: [1,2]

// Example 3:
const nums3 = [3,3]
const target3 = 6
//---> Output: [0,1]

console.log("Output 1: ", twoSum(nums1, target1));
console.log("Output 2: ", twoSum(nums2, target2));
console.log("Output 3: ", twoSum(nums3, target3));