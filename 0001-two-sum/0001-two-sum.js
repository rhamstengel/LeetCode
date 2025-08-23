/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = (nums, target, map = new Map()) => {
    for (let index = 0; index < nums.length; index++) {
        /* Time O(N) */
        const num = nums[index];
        const complement = target - num;  // Fixed: was "compliment"
        const sumIndex = map.get(complement);  // Now this works

        const isTarget = map.has(complement);  // Fixed: was "complement"
        if (isTarget) return [sumIndex, index];  // Fixed order

        map.set(num, index); /* Space O(N) */
    }

    return [-1, -1];
};
