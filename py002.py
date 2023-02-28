def main():
    args = int(input())
    for _ in range(args):
        a,b = map(int, input().split())
        res = []
        for i in range(a,b,-1):
            res.append(i)
        for j in range(b,a,1):
            res.append(j)
        print(len(res))
        print(*res)
    return True
	
 
if __name__ == "__main__":
	main()