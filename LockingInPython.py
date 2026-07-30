"""
Concurrency Demo
================

This file demonstrates three approaches:

1. No Locking (Race Condition)
2. Pessimistic Locking
3. Optimistic Locking (Versioning)

Run each demo independently to observe the behavior.
"""

import threading
import time


# ============================================================
# 1. NO LOCKING (Race Condition)
# ============================================================

"""
Expected Output (Possible)

Purchased
Purchased
Final Quantity: -1

OR

Purchased
Purchased
Final Quantity: 0

Explanation
-----------
Both threads read quantity=1 before either updates it.
Both believe the product is available.

Race Condition!
"""

print("\n========== NO LOCKING ==========")


class ProductNoLock:
    def __init__(self):
        self.quantity = 1


product = ProductNoLock()


def buy_without_lock():
    if product.quantity > 0:
        print(f"{threading.current_thread().name} sees quantity={product.quantity}")
        time.sleep(1)  # Simulate processing delay
        product.quantity -= 1
        print(f"{threading.current_thread().name} Purchased")
    else:
        print(f"{threading.current_thread().name} Out of Stock")


threads = [
    threading.Thread(target=buy_without_lock, name="Thread-1"),
    threading.Thread(target=buy_without_lock, name="Thread-2"),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final Quantity:", product.quantity)


# ============================================================
# 2. PESSIMISTIC LOCKING
# ============================================================

"""
Expected Output

Thread-1 Purchased
Thread-2 Out of Stock
Final Quantity: 0

Explanation
-----------
Only one thread acquires the lock.
Second thread waits.
After first finishes, second checks quantity again.
"""


print("\n========== PESSIMISTIC LOCKING ==========")


class ProductPessimistic:
    def __init__(self):
        self.quantity = 1
        self.lock = threading.Lock()


product = ProductPessimistic()


def buy_with_lock():

    with product.lock:

        if product.quantity > 0:
            print(f"{threading.current_thread().name} sees quantity={product.quantity}")
            time.sleep(1)
            product.quantity -= 1
            print(f"{threading.current_thread().name} Purchased")
        else:
            print(f"{threading.current_thread().name} Out of Stock")


threads = [
    threading.Thread(target=buy_with_lock, name="Thread-1"),
    threading.Thread(target=buy_with_lock, name="Thread-2"),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final Quantity:", product.quantity)


# ============================================================
# 3. OPTIMISTIC LOCKING
# ============================================================

"""
Expected Output

Thread-1 Purchased
Thread-2 Version Changed... Retrying
Thread-2 Out of Stock
Final Quantity: 0

Explanation
-----------
No lock while reading.

Each thread remembers:
    quantity
    version

Before updating, it briefly acquires a lock
to verify the version is unchanged.

If another thread already updated,
the version changes and this thread retries.
"""

print("\n========== OPTIMISTIC LOCKING ==========")


class ProductOptimistic:

    def __init__(self):
        self.quantity = 1
        self.version = 0
        self.lock = threading.Lock()


product = ProductOptimistic()


def buy_optimistic():

    while True:

        # Read WITHOUT locking
        quantity = product.quantity
        version = product.version

        if quantity == 0:
            print(f"{threading.current_thread().name} Out of Stock")
            return

        print(
            f"{threading.current_thread().name} reads "
            f"quantity={quantity}, version={version}"
        )

        time.sleep(1)

        # Lock only while committing
        with product.lock:

            if version != product.version:
                print(
                    f"{threading.current_thread().name} "
                    f"Version Changed... Retrying"
                )
                continue

            product.quantity -= 1
            product.version += 1

            print(f"{threading.current_thread().name} Purchased")
            return


threads = [
    threading.Thread(target=buy_optimistic, name="Thread-1"),
    threading.Thread(target=buy_optimistic, name="Thread-2"),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final Quantity:", product.quantity)
