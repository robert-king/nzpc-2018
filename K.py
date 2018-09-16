
def read_vals():
    return [int(x) for x in input().strip().split()]


while True:
    w,h,f,p = read_vals()
    if w == 0:
        break
    
    R = [[1,h]]
    C = [[1,w]]

    
    def find(R, cm):
        seg = 0
        x = 0
        #print("find", cm , "in",R)
        while True: #x <= cm:
            t,L = R[seg]
            if x + L > cm:
                #print("got:", seg, x)
                return seg, x
            seg += 1
            x += L
        assert False

    def fold(R, cm):
        seg,x = find(R,cm)
        t,L = R[seg]
        if x == cm:
            R1 = R[seg:]
            R2 = R[seg-1::-1]
        else:
            R1 = [[t, L - (cm-x)]] + R[seg+1:]
            R2 = [[t, (cm-x)]]
            if seg > 0:
                R2 += R[seg-1::-1]

        #merge:
        ret = []
        i1 = 0
        i2 = 0
        #print("merging", R1, R2)
        
        while i1 < len(R1) or i2 < len(R2):
            if i1 >= len(R1):
                t1,L1 = 0,1e9
            else:
                t1,L1 = R1[i1]
            if i2 >= len(R2):
                t2,L2 = 0,1e9
            else:
                t2,L2 = R2[i2]
            #print (i1,i2, L1, L2)
            
            if L1==L2:
                ret.append([t1+t2, L1])
                i1 += 1
                i2 += 1
            elif L1 < L2:
                ret.append([t1+t2, L1])
                i1 += 1
                if i2 < len(R2):
                    R2[i2][1] -= L1
            elif L1 > L2:
                ret.append([t1+t2, L2])
                i2 += 1
                if i1 < len(R1):
                    R1[i1][1] -= L2
        #print("MERGED:", ret)
        return ret
    for _ in range(f):
        lin = input().strip()
        ch  =lin[0]
        cm = int(lin[1:])
        #print(ch, cm)
        if ch == 'T':
            R = fold(R,cm)
        elif ch == 'B':
            R = fold(R[::-1],cm)[::-1]
        elif ch == 'L':
            C = fold(C,cm)
        elif ch == 'R':
            C = fold(C[::-1],cm)[::-1]
    #print("final", R, C)
    for _ in range(p):
        ret = 1
        rr,cc = read_vals()
        rr -= 1
        cc -= 1
        #print("CHEC",rr,cc)
        seg,x = find(R, rr)
        #print("R: ", seg,x)
        ret *= R[seg][0]
        seg,x = find(C, cc)
        ret *= C[seg][0]
        print(ret)
    
