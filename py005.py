from collections import defaultdict
def main():
    count = int(input())
    tree = defaultdict(list)
    for _ in range(count):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    print(sum([(len(v)*(len(v)-1))//2 for k,v in tree.items()]))
    return True

if __name__ == "__main__":
	main()