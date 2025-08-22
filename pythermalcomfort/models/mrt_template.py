from typing import Callable, Any, Union, Dict, Set
import inspect

from pythermalcomfort.mrt_functions.core import DependencyAnalyzer, FlexibleCalculator, SmartCalculator


from pythermalcomfort.mrt_functions.submethods.longwave import (
    default_submethod_a,
    default_submethod_b,
    custom_submethod_c,
    another_custom_method
)


def flexible_main_method(a=None, b=None, c=None, submethod_a=None, submethod_b=None, **kwargs):
    """
    Main method that accepts either methods or direct values
    
    Args:
        a, b, c: Input parameters (only needed if methods require them)
        submethod_a: Either a callable method or a direct value
        submethod_b: Either a callable method or a direct value
        **kwargs: Additional parameters for extensibility
    """
    analyzer = DependencyAnalyzer()
    
    # Set up methods with defaults
    methods = {
        'submethod_a': submethod_a if submethod_a is not None else default_submethod_a,
        'submethod_b': submethod_b if submethod_b is not None else default_submethod_b
    }
    
    # Calculate what input parameters we actually need
    required_params = analyzer.calculate_required_inputs(methods)
    
    # Prepare available parameters
    available_params = {'a': a, 'b': b, 'c': c}
    available_params.update(kwargs)  # Include any additional parameters
    
    # Check if we have all required parameters
    missing_params = required_params - set(k for k, v in available_params.items() if v is not None)
    if missing_params:
        raise ValueError(f"Missing required parameters: {missing_params}. "
                        f"Required based on current methods: {required_params}")
    
    results = []
    
    for method_name, method_or_value in methods.items():
        if callable(method_or_value):
            # It's a method - call it with appropriate parameters
            sig = inspect.signature(method_or_value)
            args = {param: available_params[param] 
                    for param in sig.parameters.keys() 
                    if param in available_params and available_params[param] is not None}
            result = method_or_value(**args)
        else:
            # It's a direct value
            result = method_or_value
        
        results.append(result)
    
    # Combine results (example calculation)
    return sum(results)
