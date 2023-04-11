def main():
    args = int(input())
    arr = []
    for _ in range(args):
        f,l = input().split(" ")
        arr.append((f,l))
    canSort,status = [],True
    order = list(map(int,input().split(" ")))
    order.reverse()
    while order:
        first,last = arr[order.pop()-1]
        if not canSort:
            if first > last:
                canSort.append(last)
            else:
                canSort.append(first)
            continue
        if not (first > canSort[-1] or last > canSort[-1]):
            status = False
            break
        if first > canSort[-1] and last > canSort[-1]:
            if first > last:
                canSort.append(last)
            else:
                canSort.append(first)
            continue
        if first > canSort[-1]:
            canSort.append(first)
        else:
            canSort.append(last)
    if status:
        print("YES")
    else:
        print("NO")
	
 
if __name__ == "__main__":
	main()