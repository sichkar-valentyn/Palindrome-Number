# Creating function for checking
    def isPalindrome(x):
        # Checking if input number is negative
        if x < 0:
            return False

        # Checking if input number is less than 10
        if x < 10:
            return True

        # Initializing reverse integer
        r = 0

        # Creating helper variable with input value
        h = x

        # Reverse input integer
        while h > 0:
            r += h % 10
            r *= 10
            h //= 10

        # Deleting last an extra 0
        r //= 10

        # Showing the result
        if r == x:
            return True
        else:
            return False
          
