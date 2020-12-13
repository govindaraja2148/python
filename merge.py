def Merge(arr):
    if len(arr)>1:
        r = len(arr)//2
        leftarr=arr[r:]
        rightarr=arr[:r]
        Merge(leftarr)
        Merge(rightarr)
        i=j=k=0
        while i < len(leftarr) and j <len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k]=leftarr[i]
                i+=1
            else:
                arr[k]=rightarr[j]
                j+=1
            k+=1

        if i <len(leftarr):
            arr[k]=leftarr[i]
            i+=1
            k+=1
        if j<len(rightarr):
            arr[k]=rightarr[j]
            j+=1
            k+=1
def display(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
if __name__ == '__main__':
    arr=[33,44,55,66,77,88]
    print("unsortedarry")
    display(arr)
    Merge(arr)
    print("sorted arry")
    display(arr)

