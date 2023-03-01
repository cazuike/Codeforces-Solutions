import heapq

def main():
    args = int(input())
    for _ in range(args):
        n,c = map(int,input().split())
        tp = list(map(int, input().split(" ")))
        tp = heapq.heapify([tp[i] + i for i in range(len(tp))])
        count = 0
        while tp:
            curr = heapq.heappop(tp)
            print(curr)
            if curr+1 > c:
                break
            count += 1
            c -= (curr+1)
        print(count)
            
    return True
 
if __name__ == "__main__":
	main()