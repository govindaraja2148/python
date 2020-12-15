pos =-1

def liner(list,n):
              i=0
              
              while i<len(list):
                            if list[i]==n:
                                          globals()['pos'] = i
                                          return True
                            i=i+1
              return False
list=[2,3,5,6,7,8]
n=2
if liner(list,n):
              print("element is found",pos+1)
else:
              print("element is not found")
