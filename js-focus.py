import math

#Run the python file and paste input into terminal or command line
def main(): 
    x,y,dir = input().split()
    x,y = int(x), int(y) #int casting since input is str
    obstacles = set() #quicker to check if item is in set vs list
    commands = []
    while True: #process input line
        curr = input().split()
        if not curr:
            break
        if curr[0] in ["M","L","R"]:
            #casts int to the number of steps if M is first, otherwise the same
            curr = (curr[0],int(curr[1])) if curr[0] == "M" else curr
            commands.append(curr)
        else:
            #maps int to the string of two numbers and then casts tuple onto the map
            obstacles.add(tuple(map(int,curr)))
    ans = robot_turtles(x,y,dir,obstacles,commands) #computes max euclidean distance
    print(ans)
    return True
	
def robot_turtles(x,y,dir,obstacles,commands): # if input doesnt need processing or
    #want to test custom input, then use this function
    max_dist = round(math.dist((x,y),(0,0)),2) #math module has euclidean dist function
    direction_conversion = {"N":("W","E"),"E":("N","S"),"S":("E","W"),"W":("S","N")}
    def travel(x, y, dir, steps):
        parity = 1 if dir in ["N", "E"] else -1 # to travel in positive or negative dir
        nonlocal max_dist
        new_x, new_y = x, y 
        for i in range(1, steps + 1):
            if dir in ["W", "E"]:
                temp_x = x + i * parity
                if (temp_x, y) not in obstacles:
                    new_x = temp_x #update x
                else:
                    break
            if dir in ["N", "S"]:
                temp_y = y + i * parity
                if (x, temp_y) not in obstacles:
                    new_y = temp_y #update y
                else:
                    break
        new_dist = round(math.dist((new_x, new_y), (0, 0)), 2)
        max_dist = max(max_dist, new_dist)
        return new_x, new_y
    for c in commands:
        if c[0] != "M":
            #for the dictionary, if rotate is 0, then we are rotating left otherwise right
            rotate = 0 if c[0] == "L" else 1
            #change dir to next direction
            dir = direction_conversion[dir][rotate]
        else:
            x,y = travel(x,y,dir,c[1])
    return max_dist
    


if __name__ == "__main__":
	main()