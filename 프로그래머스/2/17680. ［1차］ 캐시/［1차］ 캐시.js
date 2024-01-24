function solution(cacheSize, cities) {
    var answer = 0;
    let cacheList = [];
    
    if (cacheSize === 0)
        return answer = cities.length * 5;
    
    
    for (let city of cities) {
        city = city.toUpperCase();
        if (cacheList.includes(city)) { // cache hit
            const index = cacheList.indexOf(city);
            cacheList.splice(index, 1);
            answer++; 
        } else { // cache miss
            if (cacheList.length === cacheSize) {
                cacheList.shift();
            }
            answer += 5;
        }
        cacheList.push(city);
    }

    return answer;
}