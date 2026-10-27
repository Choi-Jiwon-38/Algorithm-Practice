def solution(bandage, health, attacks):
    time = 0
    t, x, y = bandage
    max_health = health
    
    for attack_time, damage in attacks:
        time_diff = attack_time - time - 1
        
        heal = time_diff * x
        bonus_heal = (time_diff // t) * y
        health = min(health + heal + bonus_heal, max_health)
        
        health -= damage
        time = attack_time
        
        if health <= 0:
            return -1
    
    return health