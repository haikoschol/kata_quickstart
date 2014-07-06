#!/usr/bin/env python
# encoding: utf-8


from unittest import TestCase, main

from kata import fizzbuzz


class FirstTest(TestCase):

    def test_returns_number(self):
        expected = 1
        result = fizzbuzz(1)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
