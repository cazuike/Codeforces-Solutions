def main():
    args = int(input())
    for _ in range(args):
        c = int(input())
        monsters = list(map(int, input().split(" ")))
        monsters.sort()
        diff = 0
        for i in range(len(monsters)):
            if i == 0:
                if monsters[i] == 1:
                    continue
                diff += abs(1-monsters[i])
                monsters[i] = 1
            elif monsters[i] == monsters[i-1] or monsters[i] == monsters[i-1]+1:
                continue
            else:
                diff += abs((monsters[i-1]+1)-monsters[i])
                monsters[i] = monsters[i-1]+1
        print(diff)
    return True

	
if __name__ == "__main__":
	main()