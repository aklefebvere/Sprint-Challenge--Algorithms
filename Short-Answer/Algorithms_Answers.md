#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
a = 0 O(1)
while (a < n * n * n): O(n^3)
a = a + n * n O(n^2)

O(n^3) / O(n^2) = O(n)

the while loop iterates through n and since n is in there
three times, it would be n^3. Since a inside the while loop
is modifying the result of the while loop, its considered n^2 because there are two n's. We can then cancel out the exponents by diving the exponents (n * n * n) / (n * n) =
O(n).

b)
sum = 0 O(1)
for i in range(n): O(n)
    j = 1 O(1)
    while j < n: O(log n)
        j *= 2 O(1)
        sum += 1 O(1)

O(n * (1 + (log n))) = O(n log n)

The for loop iterates thorugh the range which is O(n). The while loop runs if the condition is true and the line below it multiplys the incremeter by 2 and thus cutting the number of incriments by half which would make that while loop O(log n). Multipling the for loop and while loop time complexity would make O(n log n)


c)
def bunnyEars(bunnies):
    if bunnies == 0: O(1)
        return 0 O(1)

    return 2 + bunnyEars(bunnies-1) O(2 + n)

O(1 + 1 + 2 + n) = O(n)

The if statement just checks a condition which would be O(1) and the first return just returns a value which is also O(1). The second return is calling the function recursively 2 + n times so it can be considered O(n).
You add all the time complexitys together and take the fastest growing term which would be O(n).

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.


If all was given was the amount of floors, the best thing we could do is create a binary search function. Since we already know that floors are organized in chronological order (floor 1, floor 2, floor 3, floor 4 etc...). we can utilize a binary search function since they can only accept sorted data. Since we don't know what the value of f is, we can cut our chances of dropping an egg and cracking it in half by cutting the amount of floors in half and dropping it on the bottom half rather than the top half since we can assume that the top half has a higher chance of cracking an egg.

def egg(arr, target = None):
    # first_floor = 0
    # last_floor = len(arr) - 1
    # middle_floor = (first_floor + last_floor) // 2
    # return middle_floor - 1

O(log n)




