def main():
    args = int(input())
    for _ in range(args):
        L = int(input())
        arr = list(map(int, input().split(" ")))
        mval = list(map(abs,arr))
        
        if L == 2:
            print(max(sum(arr),-1*sum(arr)))
            continue
        res = sum(arr)
        for i in range(L):
            res = max(res,sum(mval)-2*abs(arr[i]))
        print(res)
    return True
	
 
if __name__ == "__main__":
	main()