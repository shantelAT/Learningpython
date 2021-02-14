
#find if two words are anagram

def anagram2(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for x in s1:
        if x in count:
            count[x]+= 1
        else:
            count[x] = 1
        print(count)

    for x in s2:
        if x in count:
            count[x] -= 1
        else:
            count[x] =1
        print(count)

    for k in count:
        if count[k] != 0:
            return False

    return True

ana = anagram2("D OG", "God")
print(ana)


#crete subarray so that the elements add up to k

def pair_sum(array, k):
    if len(array)< 2:
        return array


    seen = set()
    output = set()

    for num in array:
        target = k - num
        if target is not seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n' .join(map(str,list(output))), "yes")

pair_sum([1,3,2,2], 4)


# TakeTake on array with positive and a negative
#integers and find the maximum some of that array

def largest(arr):
     if len(arr) == 0:
         return None

     max_sum = current_sum = arr[0]

     for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

     return max_sum

print(largest([7, 10, 2,-20,3,4,10,-12 ,3, 21, -19]))

#Recurrsion
def sequence(n):
     if n == 1:
        return 1
     elif n == 2:
        return 1
     elif n > 2:
        return sequence(n-1) + sequence(n-2)

for n in range(1, 11):
    print(sequence(n))


# find the sum of a list with element [32, 55, 710, 1]

listt = [32, 55, 710, 1]
count = 0
for i in listt:
    count = i + count
    #return count

print(count)



given_array = [2,9,11,7,2]

largest == 0

for x in given_array:
    if largest == 0:
        largest = x
    elif x > largest:
        largest = x
        print(largest)
#--- FIND OUT OF THE STRING IS EQUQAL TTO THE REVERSE OF A STRING

def are_reverse(astring, bstring):
    for i in range(len(astring)):
        i2 = len(bstring)-i -1
        if astring[i] != bstring[i2]:
            return False
        return True

        print(i2)
print(are_reverse("ABC", "BCA"))


#Kadanes ALgorithm

def Kadanes(arra):
    max_now = 0
    max_sofar = 0

    for x in arra:
        max_now = max_now + arra[i]
        if max_now < arra[i]:
            max_now=arra[i]
        if max_sofar < max_now:
            max_sofar = max_now
    return max_sofar

print(Kadanes([-2,-3,4,-1,-2,3,1,5,-3]))


#Binary Search

def binarySearch(listData, Value):
    mini = 0
    max = len(listData)-1
    while (min <= max):
        mid = (min+max)/2
        if listData[mid] == Value:
            return mid
        elif listData[mid] < Value:
            max = mid - 1
        else:
            min = mid + 1
    return -1
print(binarySearch([1,2,4,5,7,8], 7) )
