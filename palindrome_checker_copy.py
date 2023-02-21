#!/usr/bin/env python3

"""
palindrome_checker.py
Contains a PalindromeChecker class and tester.
"""

__author__ = "Alexandra Kim"
__version__ = "2023-02-18"

import re
from atds import Deque


class PalindromeChecker:
    """
    Checkes whether a phrase a phrase is a palindrome.
    Has the option to enable strict mode.
    """

    def __init__(self):
        """Strict mode is off by default
        """
        self.strict_mode = False

    def set_strict_mode(self, bool):
        """
        If strict mode is on, a palindrome will only be indicated if the phrase reads exactly the same, forwards and backwards, including spaces, punctuation, and case (upper and lower).
        If "strict mode" is off, then spaces, punctuation, and different cases are allowed, and the phrase will be identified as a palindrome because their letters all match.
        Toggles strict mode on and off.
        """
        self.strict_mode = bool

    def sanitize(self, phrase):
        """
        Removes spaces, punctuation, uppercase letters for when strict mode is off.
        """
        return re.sub(r'[^\w\s]','',phrase.lower().replace(" ", ""))
        
        
    def is_palindrome(self, phrase):
        """
        Uses a deque to check whether the expression is palindrome.
        Returns true if phrase is a palindrome; false otherwise.
        """
        if self.strict_mode == False:
            phrase = self.sanitize(phrase)
            
        d = Deque()
        for char in phrase:
            d.add_front(char)
            
        while d.size() > 1:
            if d.remove_front() != d.remove_rear():
                return False
        return True

def main():
    p = PalindromeChecker()
    
    print("Palindrome Checker!")
    strict_mode = int(input("Do you want strict mode 1) on, or 2) off? "))
    if strict_mode == 1:
        p.set_strict_mode(True)
    
    phrase = input("Phrase: ")
    if p.is_palindrome(phrase):
        print("That's a palindrome.")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()
