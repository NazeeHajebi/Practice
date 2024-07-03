from unittest import TestCase



class TestMain(TestCase):

    def test_make_a_game(self) -> None:

        self.assertEqual(True, True)

    def calculate_storage(filesize):
        block_size = 4096
        # Use floor division to calculate how many blocks are fully occupied
        full_blocks = block_size // filesize
        print("full_blocks is" + str(full_blocks))
        # Use the modulo operator to check whether there's any remainder
        partial_block_remainder = block_size % filesize
        # Depending on whether there's a remainder or not, return
        # the total number of bytes required to allocate enough blocks
        # to store your data.
        print("partial" + str(partial_block_remainder))
        #if partial_block_remainder > 0:
          #  return (block_size *)
        #return


    print(calculate_storage(1))  # Should be 4096
    print(calculate_storage(4096))  # Should be 4096
    print(calculate_storage(4097))  # Should be 8192
    print(calculate_storage(6000))  # Should be 8192
    def lucky_number(name):
        number = len(name) * 9
        print("Hello " + name + ". Your lucky number is " + str(number))

    print(6000 % 4096)
    lucky_number("Kay")
    lucky_number("Cameron")
    name = "Nazee"
    print(4097 % 4096)
    print("Hello " + name)
    print(4+5)
    print(1/3)
    print(((2050/5)-32)/9)
    print(2**3)
    print(((1+2)*3)/4)

    num1 = 1
    num2 = 2
    sum = num1 + num2
    print("The sum is:", sum)
    print("The sum is:", sum)
    print((2 + 2) + (2 ** 2))
    print(2 + 2 / ((2 + 2) + (2 ** 2)))
    number_of_min_in_hour = 60
    total_hours = 24
    number_of_min_twenty_four_hours = number_of_min_in_hour * total_hours
    # I'm trying to learn git/github and etc
    