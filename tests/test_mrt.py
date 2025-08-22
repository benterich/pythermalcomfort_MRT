import pytest
from pythermalcomfort.models.mrt_template import flexible_main_method, custom_submethod_c, another_custom_method

test_cases = [
    {
        "test_name": "Default method with all params",
        "inputs": {"a": 5, "b": 3, "c": 4},
        "expected": 16,
        "should_raise": False
    },
    {
        "test_name": "Missing required param c",
        "inputs": {"a": 5, "b": 3},
        "expected": None,
        "should_raise": True
    },
    {
        "test_name": "Custom submethod_a only needs b",
        "inputs": {"b": 3, "c": 4, "submethod_a": custom_submethod_c},
        "expected": 17,
        "should_raise": False
    },
    {
        "test_name": "Direct value for submethod_a",
        "inputs": {"c": 4, "submethod_a": 15},
        "expected": 23,
        "should_raise": False
    },
    {
        "test_name": "Custom submethod needing a, c + direct value",
        "inputs": {"a": 2, "c": 6, "submethod_a": another_custom_method, "submethod_b": 25},
        "expected": 37,
        "should_raise": False
    }
]


@pytest.mark.parametrize("case", test_cases)

def test_flexible_main_method_json(case):
    print(f"\n--- {case['test_name']} ---")
    inputs = case["inputs"]
    expected = case["expected"]
    should_raise = case["should_raise"]

    if should_raise:
        with pytest.raises(ValueError) as e:
            flexible_main_method(**inputs)
        print(f"Caught expected error: {e.value}")
    else:
        result = flexible_main_method(**inputs)
        print(f"Inputs: {inputs}, Result: {result}, Expected: {expected}")
        assert result == expected

