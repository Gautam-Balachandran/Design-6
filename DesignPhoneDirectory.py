# Time Complexity : O(1)
# Space Complexity : O(n), where n is the maximum numbers

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.used = set()
        self.available = list(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        number = self.available.pop(0)
        self.used.add(number)
        return number

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int):
        if number in self.used:
            self.used.remove(number)
            self.available.append(number)

# Example 1
directory = PhoneDirectory(3)
print("Get: ", directory.get())        # Returns 0
print("Get: ", directory.get())        # Returns 1
print("Check 2: ", directory.check(2)) # Returns True
print("Get: ", directory.get())        # Returns 2
print("Check 2: ", directory.check(2)) # Returns False
directory.release(2)
print("Check 2: ", directory.check(2)) # Returns True

# Example 2
directory = PhoneDirectory(1)
print("Get: ", directory.get())        # Returns 0
print("Get: ", directory.get())        # Returns -1 (since no number is available)
directory.release(0)
print("Check 0: ", directory.check(0)) # Returns True
print("Get: ", directory.get())        # Returns 0

# Example 3
directory = PhoneDirectory(2)
print("Get: ", directory.get())        # Returns 0
print("Check 1: ", directory.check(1)) # Returns True
print("Check 0: ", directory.check(0)) # Returns False
directory.release(0)
print("Get: ", directory.get())        # Returns 1
print("Get: ", directory.get())        # Returns 0 (since 0 was released)
print("Get: ", directory.get())        # Returns -1 (since no number is available)