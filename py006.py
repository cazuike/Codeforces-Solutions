def main():
    args = int(input())
    tp = list(map(int, input().split(" ")))
    count = 0
    n = 0
    arr = []
    for i in range(len(tp)):
        if tp[i] == n+1:
            n+=1
            arr.append(2000+i+1)
    print(n)
    print(*arr) 
    return True
	
 
if __name__ == "__main__":
	main()