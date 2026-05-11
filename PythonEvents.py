"""
Alternating Threads with Python Event
Ref : https://leetcode.com/problems/print-foobar-alternately/

Why this is interesting:
This is a very small concurrency example, but it demonstrates a real coordination protocol between two threads.
The interesting part is not printing "foo" and "bar"; the interesting part is how synchronization creates ordering.

What it covers:
- thread coordination
- shared synchronization state
- signaling with `Event`
- enforced alternation between concurrent execution paths

Why I want to keep this:
This feels like one of those tiny examples that opens a much deeper systems rabbit hole.
I want to understand it not just as Python code, but all the way down to runtime, OS, and CPU behavior.

TODO:
- inspect CPython `Event`
- reimplement with semaphore / condition variable
- trace blocking and wakeup behavior
- study memory ordering and scheduling underneath
"""

from threading import Event, Thread

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_printed = Event()
        self.bar_printed = Event()
        self.bar_printed.set() # Start in lock state



    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_printed.wait()
            self.bar_printed.clear()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_printed.set()



    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_printed.wait()
            self.foo_printed.clear()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_printed.set()

def main():
    n = 5
    foobar = FooBar(n)

    def printFoo():
        print("foo", end="")

    def printBar():
        print("bar", end="")

    t1 = Thread(target=foobar.foo, args=(printFoo,))
    t2 = Thread(target=foobar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()


"""
Another Semophore example
# https://leetcode.com/problems/building-h2o/
from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar_assembling = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.bar_assembling.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.bar_assembling.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()

"""
