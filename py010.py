
def main():
    g,a,b = map(int, input().split(" "))
    l = 0
    r = 10**18
    while r > l:
        mid = (l+r)//2
        if mid//a + mid//b >= (g+1):
            r = mid
        else:
            l = mid+1
    print(l)
            
 
if __name__ == "__main__":
	main()