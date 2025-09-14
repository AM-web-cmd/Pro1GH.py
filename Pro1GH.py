pqrs = (input("enter either the phrase 'convertor' or 'operations' "))
abc = "convertor"
don = "operations"
if pqrs == don :
    import math
    a = "+"
    b = "-"
    c = "*"
    d = "/"
    e = "**"
    percentage = "%"
    g = "sqrt"
    h = "cbrt"
    arithmetic = [a,b,c,d,e]
    roots = [g,h]
    xyz = (input(" choose between 'arithmetic' or 'percentage' or 'roots'"))
    if xyz == "arithmetic" :
        x = float(input("enter the number"))
        y = float(input("enter the number"))
        z = (input("enter the sign"))
        if z == a :
            print ("the sum is",x + y)
        elif z == b :
            print ("the difference is",x - y)
        elif z == c :
            print ("the product is ",x * y)
        elif z == d :
            if y != 0 :
                print ("the quotient is ", x / y)
                print ("the remainder is",x % y)
            else :
                print ("error. cannot be divided by 0")    
        elif z == e :
            print ("the power is", x ** y)
        else :
            print ("ERROR")
    elif xyz == "percentage" :
        p = float(input("enter the whole number"))
        q = float(input("enter the part"))
        if q <= p :
            print ("the percentage is", (q/p)*100,"%")
        else :
            print ("error.part cannot be greater")
    elif xyz == "roots" :
        r = float(input("enter the number"))
        s = (input("enter the type (sqrt or cbrt)"))
        if s == g :
            print ("the square root is",math.sqrt(r))
        elif s == h :
            if r >= 0:
                print("The cube root is", r ** (1/3))
            else:
                print("The cube root is", -((-r) ** (1/3)))
        else :
            print ("error")
    else :
        print ("Invalid choice")
# dont give unnecessary gaps during execution. orelse it will show error
elif pqrs == abc :
    ab = "mass"
    bc = "length"
    cd = "area"
    de = "volume"
    pq = (input("choose your unit convertor between mass, length, area and volume"))
    if pq == ab :
        aaa = "kg"
        bbb = "hg"
        ccc = "dag"
        ddd = "g"
        eee = "dg"
        fff = "cg"
        ggg = "mg"
        www = float(input("enter the number"))
        ppp = (input("enter the number's unit"))
        pppp = (input("enter the unit on which it is to be converted"))
        if ppp == aaa :
            if pppp == aaa :
                print ("they are equal")
            elif pppp == bbb :
                print (www*10,"hg")
            elif pppp == ccc :
                print (www*100,"dag")
            elif pppp == ddd :
                print (www*1000,"g")
            elif pppp == eee :
                print (www*10000,"dg")
            elif pppp == fff :
                print (www*100000,"cg")
            elif pppp == ggg :
                print (www*1000000,"mg")
            else:
                print ("error")
        elif ppp == bbb :
            if pppp == aaa :
                print (www*1/10,"kg")
            elif pppp == bbb :
                print ("they are equal")
            elif pppp == ccc :
                print (www*10,"dag") 
            elif pppp == ddd :
                print (www*100,"g")
            elif pppp == eee :
                print (www*1000,"dg")
            elif pppp == fff :
                print (www*10000,"cg") 
            elif pppp == ggg :
                print (www*100000,"mg") 
            else :
                print ("error")
        elif ppp == ccc :
            if pppp == aaa :
                print (www*(1/100),"kg")
            elif pppp == bbb :
                print (www*(1/10),"hg")
            elif pppp == ccc :
                print ("they are equal")
            elif pppp == ddd :
                print (www*10,"g")
            elif pppp == eee :
                print (www*100,"dg")
            elif pppp == fff :
                print (www*1000,"cg")
            elif pppp == ggg :
                print (www*10000,"mg")
            else :
                print ("error")
        elif ppp == ddd :
            if pppp == aaa :
                print (www*(1/1000),"kg")
            elif pppp == bbb :
                print (www*(1/100),"hg")
            elif pppp == ccc :
                print (www*(1/10),"dag")
            elif pppp == ddd :
                print ("they are equal")
            elif pppp == eee :
                print (www*10,"dg")
            elif pppp == fff :
                print (www*100,"cg")
            elif pppp == ggg :
                print (www*1000,"mg")
            else :
                print ("error")
        elif ppp == eee :
            if pppp == aaa:
                print (www*(1/10000),"kg")
            elif pppp == bbb :
                print (www*(1/1000),"hg")
            elif pppp == ccc :
                print (www*(1/100),"dag")
            elif pppp == ddd :
                print (www*(1/10),"g")
            elif pppp == eee :
                print ("they are equal")
            elif pppp == fff :
                print (www*10,"cg")
            elif pppp == ggg :
                print (www*100,"mg")
            else :
                print ("error")
        elif ppp == fff :
            if pppp == aaa :
                print (www*(1/100000),"kg")
            elif pppp == bbb :
                print (www*(1/10000),"hg")
            elif pppp == ccc :
                print (www*(1/1000),"dag")
            elif pppp == ddd :
                print (www*(1/100),"g")
            elif pppp == eee :
                print (www*(1/10),"dg")
            elif pppp == fff :
                print ("they are equal")
            elif pppp == ggg :
                print (www*10,"mg")
            else :
                print ("error")
        elif ppp == ggg :
            if pppp == aaa :
                print (www*(1/1000000),"kg")
            elif pppp == bbb :
                print (www*1/100000,"hg")
            elif pppp == ccc :
                print (www*1/10000,"dag")
            elif pppp == ddd :
                print (www*1/1000,"g")
            elif pppp == eee :
                print (www*1/100,"dg")
            elif pppp == fff :
                print (www*1/10,"cg")
            elif pppp == ggg :
                print ("they are equal")
            else :
                print ("error")
        else :
            print ("error")
    elif pq == bc :
        hhh = "km"
        iii = "hm"
        jjj = "dam"
        kkk = "m"
        lll = "dm"
        mmm = "cm"
        nnn = "mm"
        xxx = float(input("enter the number"))
        qqq = (input("enter the numbers unit"))
        qqqq = (input("enter the unit on which it is to be converted"))
        if qqq == hhh :
            if qqqq == hhh :
                print ("they are equal")
            elif qqqq == iii :
                print (xxx*10,"hm")
            elif qqqq == jjj :
                print (xxx*100,"dam")
            elif qqqq == kkk :
                print (xxx*1000,"m")
            elif qqqq == lll :
                print (xxx*10000,"dm")
            elif qqqq == mmm :
                print (xxx*100000,"cm")
            elif qqqq == nnn :
                print (xxx*1000000,"mm")
            else:
                print ("error")
        elif qqq == iii :
            if qqqq == hhh :
                print (xxx*1/10,"km")
            elif qqqq == iii :
                print ("they are equal")
            elif qqqq == jjj :
                print (xxx*10,"dam") 
            elif qqqq == kkk :
                print (xxx*100,"m")
            elif qqqq == lll :
                print (xxx*1000,"dm")
            elif qqqq == mmm :
                print (xxx*10000,"cm") 
            elif qqqq == nnn :
                print (xxx*100000,"mm") 
            else :
                print ("error")
        elif qqq == jjj :
            if qqqq == hhh :
                print (xxx*(1/100),"km")
            elif qqqq == iii :
                print (xxx*(1/10),"hm")
            elif qqqq == jjj :
                print ("they are equal")
            elif qqqq == kkk :
                print (xxx*10,"m")
            elif qqqq == lll :
                print (xxx*100,"dm")
            elif qqqq == mmm :
                print (xxx*1000,"cm")
            elif qqqq == nnn :
                print (xxx*10000,"mm")
            else :
                print ("error")
        elif qqq == kkk :
            if qqqq == hhh :
                print (xxx*(1/1000),"km")
            elif qqqq == iii :
                print (xxx*(1/100),"hm")
            elif qqqq == jjj :
                print (xxx*(1/10),"dam")
            elif qqqq == kkk :
                print ("they are equal")
            elif qqqq == lll :
                print (xxx*10,"dm")
            elif qqqq == mmm :
                print (xxx*100,"cm")
            elif qqqq == nnn :
                print (xxx*1000,"mm")
            else :
                print ("error")
        elif qqq == lll :
            if qqqq == hhh :
                print (xxx*(1/10000),"km")
            elif qqqq == iii :
                print (xxx*(1/1000),"hm")
            elif qqqq == jjj :
                print (xxx*(1/100),"dam")
            elif qqqq == kkk :
                print (xxx*(1/10),"m")
            elif qqqq == lll :
                print ("they are equal")
            elif qqqq == mmm :
                print (xxx*10,"cm")
            elif qqqq == nnn :
                print (xxx*100,"mm")
            else :
                print ("error")
        elif qqq == mmm :
            if qqqq == hhh :
                print (xxx*(1/100000),"km")
            elif qqqq == iii :
                print (xxx*(1/10000),"hm")
            elif qqqq == jjj :
                print (xxx*(1/1000),"dam")
            elif qqqq == kkk :
                print (xxx*(1/100),"m")
            elif qqqq == lll :
                print (xxx*(1/10),"dm")
            elif qqqq == mmm :
                print ("they are equal")
            elif qqqq == nnn :
                print (xxx*10,"mm")
            else :
                print ("error")
        elif qqq == nnn :
            if qqqq == hhh :
                print (xxx*(1/1000000),"km")
            elif qqqq == iii :
                print (xxx*1/100000,"hm")
            elif qqqq == jjj :
                print (xxx*1/10000,"dam")
            elif qqqq == kkk :
                print (xxx*1/1000,"m")
            elif qqqq == lll :
                print (xxx*1/100,"dm")
            elif qqqq == mmm :
                print (xxx*1/10,"cm")
            elif qqqq == nnn :
                print ("they are equal")
            else :
                print ("error")
        else :
            print ("error")
    elif pq == cd :
        car = "km square"
        bus = "hm square"
        bye = "dam square"
        cat = "m square"
        eye = "dm square"
        dog = "cm square"
        cow = "mm square"
        yyy = float(input("enter the number"))
        rrr = (input("enter the numbers unit"))
        rrrr = (input("enter the unit on which it is to be converted"))
        if rrr == car :
            if rrrr == car :
                print ("they are equal")
            elif rrrr == bus :
                print (yyy*100,"hm square")
            elif rrrr == bye :
                print (yyy*10000,"dam square")
            elif rrrr == cat :
                print (yyy*1000000,"m square")
            elif rrrr == eye :
                print (yyy*100000000,"dm square")
            elif rrrr == dog :
                print (yyy*10000000000,"cm square")
            elif rrrr == cow :
                print (yyy*1000000000000,"mm square")
            else:
                print ("error")
        elif rrr == bus :
            if rrrr == car :
                print (yyy*1/100,"km square")
            elif rrrr == bus :
                print ("they are equal")
            elif rrrr == bye :
                print (yyy*100,"dam square") 
            elif rrrr == cat :
                print (yyy*10000,"m square")
            elif rrrr == eye :
                print (yyy*1000000,"dm square")
            elif rrrr == dog :
                print (yyy*100000000,"cm square") 
            elif rrrr == cow :
                print (yyy*10000000000,"mm square") 
            else :
                print ("error")
        elif rrr == bye :
            if rrrr == car :
                print (yyy*(1/10000),"km square")
            elif rrrr == bus :
                print (yyy*(1/100),"hm square")
            elif rrrr == bye :
                print ("they are equal")
            elif rrrr == cat :
                print (yyy*100,"m square")
            elif rrrr == eye :
                print (yyy*10000,"dm square")
            elif rrrr == dog :
                print (yyy*1000000,"cm square")
            elif rrrr == cow :
                print (yyy*100000000,"mm square")
            else :
                print ("error")
        elif rrr == cat :
            if rrrr == car :
                print (yyy*(1/1000000),"km square")
            elif rrrr == bus :
                print (yyy*(1/10000),"hm square")
            elif rrrr == bye :
                print (yyy*(1/100),"dam square")
            elif rrrr == cat :
                print ("they are equal")
            elif rrrr == eye :
                print (yyy*100,"dm square")
            elif rrrr == dog :
                print (yyy*10000,"cm square")
            elif rrrr == cow :
                print (yyy*1000000,"mm square")
            else :
                print ("error")
        elif rrr == eye :
            if rrrr == car :
                print (yyy*(1/100000000),"km square")
            elif rrrr == bus :
                print (yyy*(1/1000000),"hm square")
            elif rrrr == bye :
                print (yyy*(1/10000),"dam square")
            elif rrrr == cat :
                print (yyy*(1/100),"m square")
            elif rrrr == eye :
                print ("they are equal")
            elif rrrr == dog :
                print (yyy*100,"cm square")
            elif rrrr == cow :
                print (yyy*10000,"mm square")
            else :
                print ("error")
        elif rrr == dog :
            if rrrr == car :
                print (yyy*(1/10000000000),"km square")
            elif rrrr == bus :
                print (yyy*(1/100000000),"hm square")
            elif rrrr == bye :
                print (yyy*(1/1000000),"dam square")
            elif rrrr == cat :
                print (yyy*(1/10000),"m square")
            elif rrrr == eye :
                print (yyy*(1/100),"dm square")
            elif rrrr == dog :
                print ("they are equal")
            elif rrrr == cow :
                print (yyy*100,"mm square")
            else :
                print ("error")
        elif rrr == cow :
            if rrrr == car :
                print (yyy*(1/1000000000000),"km square")
            elif rrrr == bus :
                print (yyy*1/10000000000,"hm square")
            elif rrrr == bye :
                print (yyy*1/100000000,"dam square")
            elif rrrr == cat :
                print (yyy*1/1000000,"m square")
            elif rrrr == eye :
                print (yyy*1/10000,"dm square")
            elif rrrr == dog :
                print (yyy*1/100,"cm square")
            elif rrrr == cow :
                print ("they are equal")
            else :
                print ("error")
        else :
            print ("error")
    elif pq == de :
        cia = "km cube"
        mos = "hm cube"
        raw = "dam cube"
        isi = "m cube"
        bia = "dm cube"
        nasa = "cm cube"
        isro = "mm cube"
        zzz = float(input("enter the number"))
        sss = (input("enter the numbers unit"))
        ssss = (input("enter the unit on which it is to be converted"))
        if sss == cia :
            if ssss == cia :
                print ("they are equal")
            elif ssss == mos :
                print (zzz*1000,"hm cube")
            elif ssss == raw :
                print (zzz*1000000,"dam cube")
            elif ssss == isi :
                print (zzz*1000000000,"m cube")
            elif ssss == bia :
                print (zzz*1000000000000,"dm cube")
            elif ssss == nasa :
                print (zzz*1000000000000000,"cm cube")
            elif ssss == isro :
                print (zzz*1000000000000000000,"mm cube")
            else:
                print ("error")
        elif sss == mos :
            if ssss == cia :
                print (zzz*1/1000,"km cube")
            elif ssss == mos :
                print ("they are equal")
            elif ssss == raw :
                print (zzz*1000,"dam cube") 
            elif ssss == isi :
                print (zzz*1000000,"m cube")
            elif ssss == bia :
                print (zzz*1000000000,"dm cube")
            elif ssss == nasa :
                print (zzz*100000000000,"cm cube") 
            elif ssss == isro :
                print (zzz*100000000000000,"mm cube") 
            else :
                print ("error")
        elif sss == raw :
            if ssss == cia :
                print (zzz*(1/1000000),"km cube")
            elif ssss == mos :
                print (zzz*(1/1000),"hm cube")
            elif ssss == raw :
                print ("they are equal")
            elif ssss == isi :
                print (zzz*1000,"m cube")
            elif ssss == bia :
                print (zzz*1000000,"dm cube")
            elif ssss == nasa :
                print (zzz*1000000000,"cm cube")
            elif ssss == isro :
                print (zzz*1000000000000,"mm cube")
            else :
                print ("error")
        elif sss == isi :
            if ssss == cia :
                print (zzz*(1/1000000000),"km cube")
            elif ssss == mos :
                print (zzz*(1/1000000),"hm cube")
            elif ssss == raw :
                print (zzz*(1/1000),"dam cube")
            elif ssss == isi :
                print ("they are equal")
            elif ssss == bia :
                print (zzz*1000,"dm cube")
            elif ssss == nasa :
                print (zzz*1000000,"cm cube")
            elif ssss == isro :
                print (zzz*1000000000,"mm cube")
            else :
                print ("error")
        elif sss == bia :
            if ssss == cia :
                print (zzz*(1/100000000000),"km cube")
            elif ssss == mos :
                print (zzz*(1/1000000000),"hm cube")
            elif ssss == raw :
                print (zzz*(1/1000000),"dam cube")
            elif ssss == isi :
                print (zzz*(1/1000),"m cube")
            elif ssss == bia :
                print ("they are equal")
            elif ssss == nasa :
                print (zzz*1000,"cm cube")
            elif ssss == isro :
                print (zzz*1000000,"mm cube")
            else :
                print ("error")
        elif sss == nasa :
            if ssss == cia :
                print (zzz*(1/10000000000000),"km cube")
            elif ssss == mos :
                print (zzz*(1/100000000000),"hm cube")
            elif ssss == raw :
                print (zzz*(1/1000000000),"dam cube")
            elif ssss == isi :
                print (zzz*(1/1000000),"m cube")
            elif ssss == bia :
                print (zzz*(1/1000),"dm cube")
            elif ssss == nasa :
                print ("they are equal")
            elif ssss == isro :
                print (zzz*1000,"mm cube")
            else :
                print ("error")
        elif sss == isro :
            if ssss == cia :
                print (zzz*(1/1000000000000000),"km cube")
            elif ssss == mos :
                print (zzz*1/10000000000000,"hm cube")
            elif ssss == raw :
                print (zzz*1/100000000000,"dam cube")
            elif ssss == isi :
                print (zzz*1/1000000000,"m cube")
            elif ssss == bia :
                print (zzz*1/1000000,"dm cube")
            elif ssss == nasa :
                print (zzz*1/1000,"cm cube")
            elif ssss == isro :
                print ("they are equal")
            else :
                print ("error")
        else :
            print ("error")
    else :
        print ("error")
else :
    print ("error")           