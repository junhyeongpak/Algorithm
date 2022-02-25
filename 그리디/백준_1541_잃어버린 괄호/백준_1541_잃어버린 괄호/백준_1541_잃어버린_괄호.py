str1 = input()


if '-' not in str1:
    print(sum(map(int, str1.split('+'))))

else:
    str1 = str1.split('-')

    res = 0
    ban = 0
    for i in str1:
        if '+' not in i:
            if ban == 0:
                res += int(i)
                ban += 1
            else:
                res += int(i) * -1
        else:          
            a = map(int, i.split('+'))
            b = sum(a)
            if ban == 0:
                res += (b)
                ban += 1
            else:
                res += (b * -1)
    print(res)