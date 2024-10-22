import heapq

def LIFO_FF(k, n, m, requests):
    # Please write your algorithm here:
    
    #LIFO:
    lcache = []
    lmiss = 0
    for i in requests:
        if i in lcache:
            continue
        elif len(lcache)>=k:
            lcache.pop()
        lcache.append(i)
        lmiss = lmiss + 1
    
    #Farthest in Future:
    next = {}
    last = {}
    next_occur = [-1] * m
    
    #Precomputing next occurence of each element
    for i in range(m-1,-1,-1):
        p = requests[i]
        if p in last:
            next_occur[i] = last[p]
        else:
            next_occur[i] = float('inf')
        last[p] = i
    
    fcache = []
    fmiss = 0
    heap = []
    
    for i in range(m):
        p = requests[i]
        if p in fcache:
            next_ind = next_occur[i]
            heapq.heappush(heap,(-next_ind,p))
            continue
        if len(fcache)>=k:
            while heap:
                far_dist, far_page = heapq.heappop(heap)
                far_dist = -far_dist
                if far_page in fcache and far_dist>=i:
                    fcache.remove(far_page)
                    break
        fcache.append(p)
        fmiss = fmiss + 1
        next_ind = next_occur[i]
        heapq.heappush(heap,(-next_ind,p))
        
    sum = lmiss + fmiss
    dif = lmiss - fmiss
                
    # .................................
    return sum, dif

#You are allowed to use some built-in functions, such as the Python heap library, including heapq.heapify(). 

def read_input():
    k, n, m = map(int, input().split())
    requests = []
    for _ in range(m):
        request = int(input())
        requests.append(request)
    return k, n, m, requests


if __name__ == "__main__":
    k, n, m, requests = read_input()
    sum, dif = LIFO_FF(k, n, m, requests)
    print(sum, dif)
