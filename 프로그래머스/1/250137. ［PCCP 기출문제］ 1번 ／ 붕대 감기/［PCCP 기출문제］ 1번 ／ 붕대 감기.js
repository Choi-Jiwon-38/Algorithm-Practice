function solution(bandage, health, attacks) {
    let currTime = 0; // 첫 시작 시간
    
    let castingTime = bandage[0]; // 시전 시간
    let healPerSec = bandage[1]; // 초당 회복량
    let bonusHeal = bandage[2]; // 추가 회복량
    
    let currHealth = health; // 현재 체력 <- 처음에는 최대 체력과 동일

    while (attacks.length > 0) {
        let attackTime = attacks[0][0];
        let attackDamage = attacks[0][1];
        
        let timeDiff = attackTime - currTime - 1;
        
        currHealth += healPerSec * timeDiff // 기본 초당 회복
        currHealth += parseInt(timeDiff / castingTime) * bonusHeal // 추가 회복
        
        if (currHealth > health)
            currHealth = health; // 최대 체력 이상 회복 불가능
        
        currHealth -= attackDamage;
        
        if (currHealth <= 0)
            return -1; // 캐릭터 사망
        
        attacks.shift();
        
        currTime = attackTime;
        
        
        
    }
    
    
    
    return currHealth;
}