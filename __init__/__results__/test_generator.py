#제너레이터

def sqaures(n=10): # 10까지 자승하는 놈을 리턴
    for i in range(n+1):
        yield i**2 # 리턴은 1번전달 일드는 루프끝날때까지 값을 계속전달


for x in sqaures(10): #자승한 값을 리스트로 받음
    print(x)