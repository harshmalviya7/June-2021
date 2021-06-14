def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]

        merge(l)
        merge(r)
        i=j=k=0
        while(i<len(l) and j<len(r)):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while(i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
        while (j < len(r)):
            arr[k] = r[j]
            j += 1
            k += 1

arr=[12, 11, 13, 5, 6, 7]
merge(arr)
print(arr)  #[5, 6, 7, 11, 12, 13]
