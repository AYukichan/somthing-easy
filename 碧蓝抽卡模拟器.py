while True:
    t=int(input("Please input the cycle times."))
    b=1
    count={'SSR':0,'SR':0,'R':0,'N':0}
    while b<=t:
        import random
        a=random.uniform(1,1000)
        if a<=70:
            print("It's SSR!You are so lucky")
            count["SSR"]+=1
        if 70<a<=190:
            print("It's SR!Maybe you can use it?")
            count["SR"]+=1
        if 190<a<=700:
            print("It's R!Eh...Do you want to take it again?")
            count["R"]+=1
        if 700<a<=1000:
            print("It's N!How funcking unlucky you are!")
            count["N"]+=1
        b+=1
    print(f'SSR-->{count["SSR"]}\nSR-->{count["SR"]}\nR-->{count["R"]}\nN-->{count["N"]}\n')
