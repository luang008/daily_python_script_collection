import heapq
def topk(aim_dict,k):
    '''
        This script is used to find the top k frequent names in a dict
        One thing that makes it cumbersome is that heapq only support min heap
    '''

    myheap = [(-x[1],x[0]) for x in aim_dict.items()] # To make elements sorted in descending order
    
    heapq.heapify(myheap) # (name,count) --> (count,name)
    
    topk = []
    
    for i in range(k):
        temp = heapq.heappop(myheap)
        topk.append((temp[1],-temp[0]))
    return topk
    #return heapq.nlargest(k,myheap) # Elements in this build-in function is (count,name) rather than (name,count)

if __name__ == '__main__':
    s = "abcdefghijklmn"
    test_dict = {}
    for i,c in enumerate(s):
        test_dict[c] = i
    print topk(test_dict,5)

    for i,c in enumerate(s):
        test_dict[c] = 20 - i
    print topk(test_dict,5)