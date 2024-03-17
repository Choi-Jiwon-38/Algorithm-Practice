function solution(n) {
    for (let x = 2; x <= n - 1; x++) {
        if (n % x === 1)
            return x;
    }
}