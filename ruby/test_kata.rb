#!/usr/bin/env ruby

require 'minitest/autorun'
require './kata'

class FirstTest < Minitest::Unit::TestCase
  def test_returns_number
    expected = 1
    result = fizzbuzz(1)
    assert_equal expected, result
  end
end
