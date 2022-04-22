


def solution(n, word):
    answer = []
    overlap = []

    signal = True
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            print(overlap)
            if (word[i] in overlap) or (word[j] in overlap):
                print('중복데스웅치')
                if (i + 1) % n != 0: 
                    answer.append((i + 1) % n + 1)
                    answer.append((i + 1) // n + 1)
                else:
                    answer.append(n + 1)
                    answer.append((i + 1) // n)
                signal = False
                break
            else:
                overlap.append(word[i])

            print(i, j)
            print(word[i])
            print(word[j])
            if word[i][-1] == word[j][0]:
                i += 1
                continue
            else:
                if (i + 1) % n != 0: 
                    answer.append((i + 1) % n + 1)
                    answer.append((i + 1) // n + 1)
                else:
                    answer.append(n + 1)
                    answer.append((i + 1) // n)
                signal = False
                break
                break
        if signal == False:
            break

    if answer == []:
        answer = [0,0]
    
    return answer


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

answer = []
n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))

answer = []
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))