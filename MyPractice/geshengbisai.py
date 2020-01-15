# -*- coding: UTF-8 -*-



def inputscore(num):
    i = True
    while i:
        try:
            print('评委%d' % num)
            score = float(raw_input('请输入一个成绩（1-100）：'))
            if score > 100 or score < 0:
                print('输入错误，请重新输入')
                i = True
            else:
                i = False
        except:
            print('输入错误，请重新输入')
            i = True

    return score


if __name__ == '__main__':
    sumscore = 0
    maxscore = 0
    minscore = 100
    for i in range(10):
        intscore = inputscore(i + 1)
        sumscore += intscore
        if intscore > maxscore:
            maxscore = intscore
        elif intscore < minscore:
            minscore = intscore

    averagescore = (sumscore - maxscore - minscore) / 8.0
    print('去掉一个最高分%f，去掉一个最低分%f，本选手的最后得分是%f' % (maxscore,minscore,averagescore))





