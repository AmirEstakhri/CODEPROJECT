import unittest

def name_value(name: str) -> int:
    """
    Computes the sum of the positions of the letters in the name.
    Each letter is converted to uppercase, and non-letter characters are ignored.
    
    """
    total = 0
    for char in name:
        if char.isalpha():
            # Convert to uppercase to treat lowercase and uppercase equally.
            total += ord(char.upper()) - ord('A') + 1
    return total

def main():
    """
    Repeatedly prompts the user for a name, calculates its letter sum,
    and prints the result. The loop exits when the user types 'exit' or 'quit'.
    """
    while True:
        name = input("Enter a name (or type 'exit' to quit): ")
        if name.lower() in ["exit", "quit"]:
            print("Exiting the program. Goodbye!")
            break
        result = name_value(name)
        print(f"The sum of the letters in '{name}' is: {result}")

# Unit tests for the name_value function.
class TestNameValue(unittest.TestCase):
    def test_single_letter_A(self):
        self.assertEqual(name_value("A"), 1)
    
    def test_single_letter_Z(self):
        self.assertEqual(name_value("Z"), 26)
    
    def test_Az(self):
        self.assertEqual(name_value("Az"), 27)
    
    def test_Test(self):
        self.assertEqual(name_value("Test"), 64)
    
    def test_Te_st(self):
        self.assertEqual(name_value("Te st"), 64)
    
    def test_Ivan(self):
        self.assertEqual(name_value("Ivan"), 46)
    
    def test_non_alpha_characters(self):
        # Apostrophes and spaces should be ignored.
        self.assertEqual(name_value("O'Conner"), name_value("OConner"))

if __name__ == "__main__":
    import sys
    # Run unit tests if "test" is passed as a command-line argument.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Remove the argument so unittest doesn't get confused.
        sys.argv.pop(1)
        unittest.main()
    else:
        main()
#for unit tests run Code_moebel.py test (or the script name that mines )

# the test was easy