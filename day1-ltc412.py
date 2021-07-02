from typing import List

class Solution:
    def fizzbuzz(self, n: int) -> List[str]:
        res = []

        # range over the numbers from 1 to n. +1 due to it starting at 0
        for i in range(1, n+1):
            # order of these is important, the 15 case has to go first or it doesn't work
            if i%15==0:
                res.append("FizzBuzz")
            elif i%5==0:
                res.append("Buzz")
            elif i%3==0:
                res.append("Fizz")
            else:
                # set the int values to string
                res.append(str(i))

        # return the result
        return res
