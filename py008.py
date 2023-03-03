from collections import defaultdict
def main():
    a,b = map(int, input().split()) 
    strs = []
    for _ in range(a):
        strs.append(input())
    ls = list(map(int, input().split(" ")))
    rem = [strs[i] for i in range(a) if i+1 in ls]
    key = defaultdict(set)
    length = set()
    for i in range(len(rem)):
        li = len(rem[i])
        length.add(li)
        for j in range(li):
            if len(length) > 1:
                print("No")
                return True
            key[j].add(rem[i][j])
    res = ""
    for k,v in key.items():
        if len(v) != 1:
            res += "?"
        else:
            res += next(iter(v)) 
    for i in range(len(strs)):
        if strs[i] in rem or len(strs[i]) != len(res):
            continue
        for j in range(len(res)):
            if j == len(res)-1 and (res[j] == strs[i][j] or res[j] == "?"):
                print("No")
                return True
            if not (res[j] == strs[i][j] or res[j] == "?"):
                break
    print("Yes")
    print(res)
 
if __name__ == "__main__":
	main()