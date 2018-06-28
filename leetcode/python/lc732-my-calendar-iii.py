# coding=utf-8
import unittest

"""732. My Calendar III
https://leetcode.com/problems/my-calendar-iii/description/

Implement a `MyCalendarThree` class to store your events. A new event can
**always** be added.

Your class will have one method, `book(int start, int end)`. Formally, this
represents a booking on the half open interval `[start, end)`, the range of
real numbers `x` such that `start <= x < end`.

A _K-booking_ happens when **K** events have some non-empty intersection (ie.,
there is some time that is common to all K events.)

For each call to the method `MyCalendar.book`, return an integer `K`
representing the largest integer such that there exists a `K`-booking in the
calendar.

Your class will be called like this: `MyCalendarThree cal = new
MyCalendarThree();` `MyCalendarThree.book(start, end)`

**Example 1:**  

    
    
    MyCalendarThree();
    MyCalendarThree.book(10, 20); // returns 1
    MyCalendarThree.book(50, 60); // returns 1
    MyCalendarThree.book(10, 40); // returns 2
    MyCalendarThree.book(5, 15); // returns 3
    MyCalendarThree.book(5, 10); // returns 3
    MyCalendarThree.book(25, 55); // returns 3
    **Explanation:** 
    The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
    The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
    The remaining events cause the maximum K-booking to be only a 3-booking.
    Note that the last event locally causes a 2-booking, but the answer is still 3 because
    eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
    

**Note:**

* The number of calls to `MyCalendarThree.book` per test case will be at most `400`.
* In calls to `MyCalendarThree.book(start, end)`, `start` and `end` are integers in the range `[0, 10^9]`.


Similar Questions:
  My Calendar I (my-calendar-i)
  My Calendar II (my-calendar-ii)
"""


class MyCalendarThree(object):

    def __init__(self):
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
