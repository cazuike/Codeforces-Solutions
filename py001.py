def main():
    def check(a,b,c,d):
        if a < b and a < c and d > c and d > b:
            return True
        return False
    args = int(input())
    for _ in range(args):
        a,b = map(int, input().split()) 
        c,d = map(int, input().split())
        if check(a,b,c,d) or check(c,a,d,b) or check(d,c,b,a) or check (b,d,a,c):
            print("YES")
        else:
            print("NO")
    return True
	
 
if __name__ == "__main__":
	main()