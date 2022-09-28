const maxProfit = function(prices) {
    let res = 0
    let l = 0
    for (let r = 1; r < prices.length; r++) {
        if (prices[r] < prices[l]) {
            l = r
        }
        res = Math.max(res, prices[r] - prices[l])
    }
    return res
}

// Example 1:
prices1 = [7,1,5,3,6,4]
//---> Output 1: 5

// Example 2:
prices2 = [7,6,4,3,1]
//---> Output 2: 0

console.log('Output 1: ', maxProfit(prices1))
console.log('Output 2: ', maxProfit(prices2))