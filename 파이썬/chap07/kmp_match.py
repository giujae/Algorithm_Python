def LPS(pat, lps):
    leng = 0
    
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng -1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    
    lps = [0] * M
    
    LPS(pat, lps)
    
    i = 0
    j = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            print("찾았다" + str(i-j))
            j = lps[j-1]
        
KMPSearch('ABBA', 'ABABAAAABBBAABABBABAABAAB')