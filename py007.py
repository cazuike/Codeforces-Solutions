import math

def main():
    args = int(input())
    arr = []
    unique = set()
    total = 0
    for i in range(args):
        arr.append((int(input()),i+1))
        unique.add(arr[i][0])
        total += arr[i][0]
    if len(arr) == 2 and len(unique) == 2 and sum([j[0] for j in arr])%2 == 0:
        if arr[1][0] > arr[0][0]:
            div = arr[1][0]//2 
            a,b = arr[0][1],arr[1][1]
        else:
            div = arr[0][0]//2
            a,b = arr[1][1],arr[0][1]
        print("{} ml. from cup #{} to cup #{}.".format(div,a,b))
        return True
    arr.sort(key = lambda x:x[0])
    if len(unique) == 1:
        print("Exemplary pages.")
    elif len(unique) != 3 or total%len(arr) != 0:
        print("Unrecoverable configuration.")
    else:
        print("{} ml. from cup #{} to cup #{}.".format(arr[-1][0]-arr[1][0],arr[0][1],arr[-1][1]))
    return True
	
 
if __name__ == "__main__":
	main()