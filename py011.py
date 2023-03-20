def main():
    args = int(input())
    for _ in range(args):
        L = int(input())
        arr = list(map(int, input().split(" ")))
        abs_sum = 0
        rsum = 0
        ngc = 0 
        for i in range(L):
            if arr[i] < 0:
                ngc += 1
            abs_sum += abs(arr[i])
            rsum += arr[i]

        if L == 2:
            print(max(abs_sum,rsum))
            continue
        if ngc % 2 == 0:
            print(abs_sum)
            continue
        res = rsum
        for i in range(L):
            res = max(res,abs_sum-2*abs(arr[i]))
        print(res)
    return True
	
 
if __name__ == "__main__":
	main()