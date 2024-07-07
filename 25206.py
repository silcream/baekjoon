def mains():
    sumscore = 0
    sumscore2 = 0
    for i in range(20):
        name, time, score = list(input().split())
        if score == 'A+':
            score2 = 4.5
        elif score == 'A0':
            score2 = 4.0
        elif score == 'B+':
            score2 = 3.5
        elif score == 'B0':
            score2 = 3.0
        elif score == 'C+':
            score2 = 2.5
        elif score == 'C0':
            score2 = 2.0
        elif score == 'D+':
            score2 = 1.5
        elif score == 'D0':
            score2 = 1.0
        elif score == 'P':
            score2 = 0
            time = 0
        elif score == 'F':
            score2 = 0
        # print(type(time), type(score2))
        avscore = float(time) * score2
        sumscore += avscore
        sumscore2 += float(time)
    print(sumscore/sumscore2)

if __name__=='__main__':
    mains()