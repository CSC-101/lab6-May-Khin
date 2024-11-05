import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        books = [
            data.Book(["J.K. Rowling"], "Harry Potter and the Sorcerer's Stone"),
            data.Book(["J.R.R. Tolkien"], "The Hobbit"),
            data.Book(["George R.R. Martin"], "A Game of Thrones")
        ]
        expected = [
            data.Book(["George R.R. Martin"], "A Game of Thrones"),
            data.Book(["J.K. Rowling"], "Harry Potter and the Sorcerer's Stone"),
            data.Book(["J.R.R. Tolkien"], "The Hobbit")
        ]
        lab6.selection_sort_books(books)
        result = books
        self.assertEqual(result, expected)

    def test_selection_sort_books_2(self):
        books = []
        expected = []
        lab6.selection_sort_books(books)
        result = books
        self.assertEqual(expected, result)


    # Part 2
    def test_swap_case_1(self):
        input_string = "Hello, World!"
        expected = "hELLO, wORLD!"
        result = lab6.swap_case(input_string)
        self.assertEqual(expected, result)

    def test_swap_case_2(self):
        input_string = "computer SCIENCE"
        expected = "COMPUTER science"
        result = lab6.swap_case(input_string)
        self.assertEqual(expected, result)


    # Part 3
    def test_str_translate_1(self):
        input_str = 'abcdcba'
        expected = 'xbcdcbx'
        result = lab6.str_translate(input_str, 'a', 'x')
        self.assertEqual(result, expected)

    def test_translate_2(self):
        input_str = 'hello world'
        result = lab6.str_translate(input_str, 'o', 'a')
        expected = 'hella warld'
        self.assertEqual(result, expected)


    # Part 4
    def test_histogram_1(self):
        input_str = "hello hello world world world"
        expected = {
            'hello': 2,
            'world': 3
        }
        result = lab6.histogram(input_str)
        self.assertEqual(expected, result)

    def test_histogram_2(self):
        input_str = "hi hello hi hi hi hello"
        expected = {
            'hi': 4,
            'hello': 2
        }
        result = lab6.histogram(input_str)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
