import pytest

from part_2 import calculate_lock_crossing_zero


# Basic positive movement tests
def test_movement_positive_crossing_zero_once():
    starting_point = 50
    movement = 60
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_movement_positive_crossing_zero_twice():
    starting_point = 50
    movement = 160
    assert calculate_lock_crossing_zero(starting_point, movement) == 2

def test_movement_positive_crossing_zero_ten_times():
    """From problem: R1000 from position 50 should cross zero 10 times"""
    starting_point = 50
    movement = 1000
    assert calculate_lock_crossing_zero(starting_point, movement) == 10


# Basic negative movement tests
def test_movement_negative_crossing_zero_once():
    starting_point = 50
    movement = -60
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_movement_negative_crossing_zero_twice():
    starting_point = 50
    movement = -160
    assert calculate_lock_crossing_zero(starting_point, movement) == 2


# Starting at zero - positive movement
def test_movement_positive_crossing_zero_once_starting_point_is_zero():
    starting_point = 0
    movement = 110
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_movement_positive_crossing_zero_twice_starting_point_is_zero():
    starting_point = 0
    movement = 210
    assert calculate_lock_crossing_zero(starting_point, movement) == 2

def test_movement_positive_from_zero_small_movement():
    """Moving +48 from 0: visits 1,2,...,48 - no zero crossing"""
    starting_point = 0
    movement = 48
    assert calculate_lock_crossing_zero(starting_point, movement) == 0


# Starting at zero - negative movement
def test_movement_negative_crossing_zero_once_starting_point_is_zero():
    """Moving -20 from 0: visits 99,98,...,80 - does not cross zero"""
    starting_point = 0
    movement = -20
    assert calculate_lock_crossing_zero(starting_point, movement) == 0

def test_starting_point_is_zero_and_movement_is_negative_and_greater_than_100():
    starting_point = 0
    movement = -210
    assert calculate_lock_crossing_zero(starting_point, movement) == 2

def test_movement_negative_starting_point_is_zero_crossing_zero_once():
    """Moving -100 from 0: visits 99,98,...,0 - crosses zero once at end"""
    starting_point = 0
    movement = -100
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_movement_negative_starting_point_is_zero_crossing_zero_twice():
    """Moving -200 from 0: visits 99,...,0,99,...,0 - crosses zero twice"""
    starting_point = 0
    movement = -200
    assert calculate_lock_crossing_zero(starting_point, movement) == 2


# Ending exactly at zero
def test_movement_positive_ending_at_zero():
    """Moving +50 from 50: visits 51,52,...,100 (wraps to 0) - crosses zero once"""
    starting_point = 50
    movement = 50
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_movement_negative_ending_at_zero():
    """Moving -50 from 50: visits 49,48,...,0 - crosses zero once at end"""
    starting_point = 50
    movement = -50
    assert calculate_lock_crossing_zero(starting_point, movement) == 1


# Edge cases
def test_zero_movement():
    """No movement should return 0"""
    starting_point = 50
    movement = 0
    assert calculate_lock_crossing_zero(starting_point, movement) == 0

def test_zero_movement_starting_at_zero():
    """No movement starting at zero should return 0 (we don't count starting position)"""
    starting_point = 0
    movement = 0
    assert calculate_lock_crossing_zero(starting_point, movement) == 0


# Examples from problem statement
def test_example_l68_from_50():
    """From problem: L68 from 50 should cross zero once"""
    starting_point = 50
    movement = -68
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_example_r48_from_82():
    """From problem: R48 from 82 should cross zero once"""
    starting_point = 82
    movement = 48
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_example_l55_from_95():
    """From problem: L55 from 95 should not cross zero"""
    starting_point = 95
    movement = -55
    assert calculate_lock_crossing_zero(starting_point, movement) == 0

def test_example_r60_from_95():
    """From problem: R60 from 95 should cross zero once"""
    starting_point = 95
    movement = 60
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_example_l82_from_14():
    """From problem: L82 from 14 should cross zero once"""
    starting_point = 14
    movement = -82
    assert calculate_lock_crossing_zero(starting_point, movement) == 1


# Boundary cases - wrapping
def test_movement_positive_wrapping_multiple_times():
    """Large positive movement that wraps multiple times"""
    starting_point = 50
    movement = 250
    assert calculate_lock_crossing_zero(starting_point, movement) == 3  # Crosses 100, 200 and 300

def test_movement_negative_wrapping_multiple_times():
    """Large negative movement that wraps multiple times"""
    starting_point = 50
    movement = -250
    assert calculate_lock_crossing_zero(starting_point, movement) == 3  # Crosses 0, -100 (which is 0) and -200


# Specific edge cases
def test_negative_movement_crossing_zero_once():
    starting_point = 16
    movement = -16
    assert calculate_lock_crossing_zero(starting_point, movement) == 1

def test_negative_movement_crossing_zero_twice():
    starting_point = 16
    movement = -116
    assert calculate_lock_crossing_zero(starting_point, movement) == 2

def test_positive_movement_no_crossing():
    """Small positive movement that doesn't cross zero"""
    starting_point = 50
    movement = 30
    assert calculate_lock_crossing_zero(starting_point, movement) == 0

def test_negative_movement_no_crossing():
    """Small negative movement that doesn't cross zero"""
    starting_point = 50
    movement = -30
    assert calculate_lock_crossing_zero(starting_point, movement) == 0

def test_positive_movement_starting_near_zero():
    """Starting near zero, moving positive"""
    starting_point = 1
    movement = 50
    assert calculate_lock_crossing_zero(starting_point, movement) == 0  # Doesn't cross 0

def test_positive_movement_starting_near_zero_crosses():
    """Starting near zero, moving positive enough to cross"""
    starting_point = 1
    movement = 150
    assert calculate_lock_crossing_zero(starting_point, movement) == 1  # Crosses 100

def test_negative_movement_starting_near_zero():
    """Starting near zero, moving negative"""
    starting_point = 1
    movement = -1
    assert calculate_lock_crossing_zero(starting_point, movement) == 1  # Crosses 0

def test_negative_movement_starting_near_100():
    """Starting near 100 (wraps to 0), moving negative"""
    starting_point = 99
    movement = -1
    assert calculate_lock_crossing_zero(starting_point, movement) == 0  # No crossing