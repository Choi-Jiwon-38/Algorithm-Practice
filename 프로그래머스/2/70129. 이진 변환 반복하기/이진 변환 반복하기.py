def solution(s):
    bin_convert_count = 0
    removed_zero_count = 0
    
    while s != '1':
        # step 1
        zero_count = s.count('0')
        removed_zero_count += zero_count

        # step 2
        c = len(s) - zero_count
        s = bin(c)[2:]
        bin_convert_count += 1

    
    return [bin_convert_count, removed_zero_count]