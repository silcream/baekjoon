if __name__=='__main__':

    # for k in range(5):
    #     words = list(input())
    words = [input() for i in range(5)]

    for j in range(15):
        for i in range(5):
            if j < len(words[i]):
                print(words[i][j], end='')

