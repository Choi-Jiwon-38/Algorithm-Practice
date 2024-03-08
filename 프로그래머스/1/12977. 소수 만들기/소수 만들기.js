function checkPrime(num) {    
    for (let i = 2; i < parseInt(num / 2) + 1; i++) {
        if (num % i === 0) {
          return  false;
        }
    }
    return true;
}


function solution(nums) {
    var answer = 0;
    
    let sumNum = 0;
        
    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                sumNum = nums[i] + nums[j] + nums[k];
                if (checkPrime(sumNum)) {
                    answer++;
                }
            }
        }
    }
    
    return answer;
}