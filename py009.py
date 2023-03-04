
def main():
    w,h,n = map(int, input().split(" "))
    volume = w*h*n
    l = 0
    r = 10**20
    while r > l:
        mid = (l+r)//2
        if mid**2 - volume >= 0 and (n <= (mid//w)*(mid//h)):
            r = mid
        else:
            l = mid+1
    print(l)
            
 
if __name__ == "__main__":
	main()