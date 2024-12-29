import pytest
#import inc_dec
def test_sum():
    assert 1 + 1 == 2


@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_list(sample_data: list[int]):
    assert len(sample_data) == 3
    
    
# The code to test


def inc_dec(value, operation):
    if operation == "inc":
        return value + 1
    elif operation == "dec":
        return value - 1
    else:
        raise ValueError("Invalid operation")

def test_inc_dec():
    assert inc_dec(1, "inc") == 2
    assert inc_dec(2, "dec") == 1


def test_increment():
    assert inc_dec(3, "inc") == 4

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert inc_dec(5, "dec") == 4


class TestForSelf:
    value = ''
    def test_setup_method(self):
        self.value = "URL"
        
    def test_value(self):
        if self.value == "URL":
            print("True")
        else:
            print("False")
            
