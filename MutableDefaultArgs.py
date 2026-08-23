"""
Mutable Default Arguments in Python

Why this is interesting:
Default arguments are evaluated ONCE when the function is defined,
not every time the function is called.

This becomes surprising when the default value is mutable, such
as a list, dict, or set.

The same object is reused across calls.

The safe/common pattern is to use `None` and create the mutable
object inside the function.

TODO:
- inspect `add.__defaults__`
- compare `id()` of the default list
- understand how CPython stores function defaults
"""


# ------------------------------------------------------------
# 1. The surprising behavior
# ------------------------------------------------------------

def add(item=[]):
    # `[]` is created ONCE when the function is defined.
    # Every call to add() reuses the same list.

    item.append(1)
    return item


print(add())
print(add())
print(add())

# Expected output:
#
# [1]
# [1, 1]
# [1, 1, 1]


# ------------------------------------------------------------
# 2. The correct/common pattern
# ------------------------------------------------------------

def add_safe(item=None):
    # `None` is used as a signal that no list was provided.
    # A NEW list is created for each call.

    if item is None:
        item = []

    item.append(1)
    return item


print(add_safe())
print(add_safe())
print(add_safe())

# Expected output:
#
# [1]
# [1]
# [1]


# ------------------------------------------------------------
# Important:
# The problem is NOT that lists are mutable.
#
# Explicitly passing the same list is perfectly valid.
# ------------------------------------------------------------

items = []

print(add_safe(items))
print(add_safe(items))
print(add_safe(items))

# Expected output:
#
# [1]
# [1, 1]
# [1, 1, 1]
