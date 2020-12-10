def Pass_sort(l):
    # for last in range(len(l)-1,-1,-1):
    #     swapped=False
    #     for i in range(last):
    #         min_index = i
    #         if l[i]<0:
    #             continue
    #         for j in range(i+1,len(l)):
    #             if l[j]<l[min_index] and l[j]>=0:
    #                 min_index = j
    #         l[min_index],l[i] = l[i],l[min_index]
    #         swapped=True
    #     if not swapped:
    #          break
    # return l
    for i in range(len(l)):
        min_indx=i
        if l[i]<0:
            continue
        for j in range(i+1,len(l)):
            if l[j]<l[min_indx] and l[j]>=0:
                min_indx=j
        l[min_indx],l[i]=l[i],l[min_indx]
    print(*l,sep=' ')


inp = [int(a) for a in input("Enter Input :").split()]
Pass_sort(inp)


# if __name__ == "__main__":
#     inp = list(map(int, input("Enter Input : ").split()))
#     for i in range(len(inp)):
#         min_idx = i
#         print("min",end='-->')
#         print(type(min_idx))
#         print("i",end='-->')
#         print(type(i))
#         print("inp[]",end='-->')
#         print(type(inp[i]))
#         if inp[i] < 0:
#             continue
#         for j in range(i+1, len(inp)):
#             #print("compare ", inp[j], inp[min_idx])
#             if inp[j] < inp[min_idx] and inp[j] >= 0:
#                 #print("change idx", min_idx,j)
#                 min_idx = j
#         inp[min_idx], inp[i] = inx]
#     print(*inp)