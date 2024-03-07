function solution(skill, skill_trees) {
    let answer = 0;
    let map = new Map();
    
    for (let i = 0; i < skill.length; i++) {
        map.set(skill[i], i);
    }
    
    for (let skill_tree of skill_trees) {
        let index = 0;
        let flag = true;
        
        for (let s of skill_tree){
            let result = map.get(s);
            
            if (result != undefined) {
                if (result > index) {
                    flag = false;
                    break;
                } else {
                    index++;
                }
            }
        }
        
        if (flag) {
            answer++;
        }
    }
    
    
    return answer;
}