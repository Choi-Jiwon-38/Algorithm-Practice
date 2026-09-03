function solution(today, terms, privacies) {
    const answer = [];
    const term_rules = new Map();
    const [y, m, d] = today.split(".").map((x) => Number(x));
    const current = (y - 1) * 12 * 28 + (m - 1) * 28 + d;
    
    for (const term of terms) {
        const [t, m] = term.split(" ");
        term_rules.set(t, m * 28);
    }
    
    let idx = 1;
    
    for (const privacy of privacies) {
        const [date, type] = privacy.split(" ")
        const [y, m, d] = date.split(".").map((x) => Number(x));
        
        const limit = (y - 1) * 12 * 28 + (m - 1) * 28 + d + term_rules.get(type);
        if (current >= limit) answer.push(idx);
        idx++;
    }

    return answer;
}