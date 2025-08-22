from typing import Callable, Any, Union, Dict, Set
import inspect

class DependencyAnalyzer:
    """Analyzes and manages parameter dependencies"""
    
    def __init__(self):
        self.method_dependencies = {}
        self.provided_values = {}
        self.required_inputs = set()
    
    def analyze_method_dependencies(self, methods: Dict[str, Callable]) -> Set[str]:
        """Analyze what parameters are needed by all methods"""
        all_params = set()
        
        for method_name, method in methods.items():
            if callable(method):
                sig = inspect.signature(method)
                params = set(sig.parameters.keys())
                self.method_dependencies[method_name] = params
                all_params.update(params)
        
        return all_params
    
    def calculate_required_inputs(self, methods: Dict[str, Any]) -> Set[str]:
        """Calculate what input parameters are actually needed"""
        required = set()
        
        for method_name, method_or_value in methods.items():
            if callable(method_or_value):
                # If it's a method, we need its input parameters
                sig = inspect.signature(method_or_value)
                required.update(sig.parameters.keys())
            # If it's a direct value, we don't need any inputs for this method
        
        return required


class FlexibleCalculator:
    def __init__(self):
        self.analyzer = DependencyAnalyzer()
        self.methods = {
            'submethod_a': default_submethod_a,
            'submethod_b': default_submethod_b
        }
    
    def set_method(self, name: str, method_or_value: Union[Callable, Any]):
        """Set a method to either a callable or a direct value"""
        self.methods[name] = method_or_value
    
    def get_required_parameters(self) -> Set[str]:
        """Get the parameters currently required based on configured methods"""
        return self.analyzer.calculate_required_inputs(self.methods)
    
    def calculate(self, **params):
        """Calculate with dynamic parameter requirements"""
        required_params = self.get_required_parameters()
        
        # Check if we have all required parameters
        provided_params = set(k for k, v in params.items() if v is not None)
        missing_params = required_params - provided_params
        
        if missing_params:
            raise ValueError(f"Missing required parameters: {missing_params}. "
                            f"Required based on current methods: {required_params}")
        
        results = []
        
        for method_name, method_or_value in self.methods.items():
            if callable(method_or_value):
                # It's a method
                sig = inspect.signature(method_or_value)
                args = {param: params[param] 
                        for param in sig.parameters.keys() 
                        if param in params and params[param] is not None}
                result = method_or_value(**args)
            else:
                # It's a direct value
                result = method_or_value
            
            results.append(result)
        
        return sum(results)


class SmartCalculator(FlexibleCalculator):
    def calculate_with_guidance(self, **params):
        """Calculate with helpful guidance about parameter requirements"""
        required = self.get_required_parameters()
        provided = set(k for k, v in params.items() if v is not None)
        
        print(f"Required parameters: {required}")
        print(f"Provided parameters: {provided}")
        
        # Show what each method needs
        print("\nMethod requirements:")
        for name, method_or_value in self.methods.items():
            if callable(method_or_value):
                sig = inspect.signature(method_or_value)
                print(f"  {name}: needs {set(sig.parameters.keys())}")
            else:
                print(f"  {name}: direct value ({method_or_value})")
        
        return self.calculate(**params)
