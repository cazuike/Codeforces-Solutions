from collections import Counter

def main():
    args = int(input())
    for _ in range(args):
        strl,swaps = map(int, input().split(" "))
        s = input()
        count = Counter(s)
        res = 0
        alphabet = [chr(value) for value in range(ord('a'), ord('a') + 26)]
        for c in alphabet:
            while count[c] > 0 and count[c.upper()] > 0:
                count[c] -= 1
                count[c.upper()] -= 1
                res += 1
            while count[c] >= 2 and swaps > 0:
                count[c] -= 2
                swaps -=1
                res += 1
        print(res)
    return True


	
 
if __name__ == "__main__":
	main()