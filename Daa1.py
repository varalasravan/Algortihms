import sys
import random
import time
# Function for insertion sort
def insertionSort(arr):
    # parsing through the array from first to its length
    for i in range(1,len(arr)):
        value=arr[i]
        j=i-1
        #checking whether the element is greater than the element in array
        while j>=0 and arr[j]>value:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=value


#Function to implement Selection sort
def selectionSort(arr):
    #parsing through the elements of array from first to its length
    for x in range(len(arr)):
        min_position=x
        #Parse through the pivoted elements
        for y in range(x+1, len(arr)):
            if(arr[y] < arr[min_position]):
                min_position=y
        #swap the numbers
        temp=arr[x]
        arr[x]=arr[min_position]
        arr[min_position]=temp

#defining an array
arr=[]
#if there are two arguments
if (len(sys.argv)==2):
#give the default size and random array variables
    size=1000
    arr=random.sample(range(size),size)

    if(sys.argv[1]=="G=I"):
        start_time=time.time()
        insertionSort(arr)
        end_time=time.time()
        elapsed_time=end_time-start_time
        print("elapsed_time: ", elapsed_time)
    elif(sys.argv[1]=="G=S"):
        start_time=time.time()
        selectionSort(arr)
        end_time=time.time()
        elapsed_time=end_time-start_time
        print("elapsed_time: ", elapsed_time)
    else:
        print("please check your argument")

# If there are 4 command line arguments
if (len(sys.argv)==4):
    s=sys.argv[1]
    #is to separate the string formated number from string and convert it to int
    n=s.split("N=")
    size=int(n[1])

    if(sys.argv[2]=="S=A"):
        for i in range(size):
            arr.append(i)
    elif(sys.argv[2]=="S=R"):
        arr=random.sample(range(size),size)
    elif(sys.argv[2]=="S=D"):
        for i in range(size):
            arr.append(size-i)
    else:
        print("check 2nd argument")
        sys.exit(1)

    if(sys.argv[3]=="G=I"):
        start_time=time.time()
        insertionSort(arr)
        end_time=time.time()
        elapsed_time=end_time-start_time
        print("elapsed_time: ", elapsed_time)
    elif(sys.argv[3]=="G=S"):
        start_time=time.time()
        selectionSort(arr)
        end_time=time.time()
        elapsed_time=end_time-start_time
        print("elapsed_time: ", elapsed_time)
    else:
        print("check 3rd argument")
        sys.exit(1)
