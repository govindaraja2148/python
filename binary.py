pos=-1
def binary(list,n):
              l=0
              u=len(list)-1
              while l<=u:
                            mid=(l+u)//2
                            if list[mid]==n:
                                          globals()['pos']=mid
                                          return True
                            else:
                                          if list[mid]<=n:
                                                        l=mid+1
                                          else:
                                                        u=mid-1
list=[2,3,4,5,6]
n=5
if binary(list,n):
              print("element is found",pos+1)
else:
              print("element is not found")
              
