def interval_scheduling_coving(n, u, v, intervals):
    # Please write your algorithm here:
    intervals.sort(key= lambda x: x[1])
    
    #Interval Scheduling:
    maximum = 0
    end = 0
    for s, f in intervals:
        if s >= end:
            maximum = maximum + 1
            end = f
    
    #Interval Covering:
    intervals.sort(key = lambda x: x[0])
    
    current = u
    minimum = 0
    i = 0
    
    while current < v:
        path = -1
        while i < n and intervals[i][0]<=current:
            path = max(path, intervals[i][1])
            i = i + 1
        if path == -1:
            return maximum, "no"
            
        current = path
        minimum = minimum + 1
            
    # .................................
    return maximum, minimum


def read_input():
    n, u, v = map(int, input().split())
    intervals = []
    for i in range(n):
        s, f = map(int, input().split())
        intervals.append((s, f))
    return n, u, v, intervals


if __name__ == "__main__":
    n, u, v, intervals = read_input()
    maximum, minimum = interval_scheduling_coving(n, u, v, intervals)
    print(maximum)
    print(minimum)
