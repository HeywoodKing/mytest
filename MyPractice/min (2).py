# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    # write your code in Python 3.6
    def get_min(t):
        if t:
            low,high = min(t),max(t)
            return abs(high - low)
        else:
            return 0
        
    if T:
        ele_count = int(len(T) / 4)
        wint = T[0:ele_count]
        spri = T[ele_count:2*ele_count]
        summ = T[2*ele_count:3*ele_count]
        autu = T[3*ele_count:4*ele_count]
        
        wint_res = get_min(wint)
        spri_res = get_min(spri)
        summ_res = get_min(summ)
        autu_res = get_min(autu)
        
        res = [wint_res, spri_res, summ_res, autu_res]
        
        list_res = ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']
        
        return list_res[res.index(max(res))]
        
    