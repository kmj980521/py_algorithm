
def LCS(list1,list2):

    lcs_list=[[0 for col in range(len(list2)+1)] for row in range(len(list1)+1)]

    list1=' '+list1
    list2=' '+list2

    for a in range(1,len(list1)):
        for b in range(1,len(list2)):
            if list1[a]==list2[b]:
                lcs_list[a][b] = lcs_list[a-1][b-1] +1
            else:
                lcs_list[a][b] = max(lcs_list[a-1][b],lcs_list[a][b-1])
    print(lcs_list[1][2])

list1= "ABCBDAB"

list2= "BDCABA"

LCS(list1,list2)



