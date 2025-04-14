import random
from typing import Dict, Any, Optional, Union

from telecomfaker.providers import LocalJsonProvider

class TelecomFaker:
    """
    A class for generating realistic telecom operator test data.
    """
    
    def __init__(self, data_provider=None) -> None:
        """
        Initialize the TelecomFaker with a data provider.
        
        Args:
            data_provider: A data provider instance. If None, uses the default LocalJsonProvider.
        """
        self.data_provider = data_provider or LocalJsonProvider()
        self.random = random
    
    def set_seed(self, seed: Union[int, float, str, bytes, bytearray]) -> None:
        """
        Set a random seed for consistent data generation.
        
        This method allows you to generate reproducible sequences of operators,
        which is useful for testing and debugging. Using the same seed value
        will produce the same sequence of operators across different runs.
        
        Args:
            seed: A value to use as the random seed. Can be an integer, float,
                 string, bytes, or bytearray.
                 
        Example:
            ```python
            # Create two separate instances
            faker1 = TelecomFaker()
            faker2 = TelecomFaker()
            
            # Set the same seed
            seed_value = 42
            faker1.set_seed(seed_value)
            faker2.set_seed(seed_value)
            
            # These will be identical
            operator1 = faker1.generate_operator()
            operator2 = faker2.generate_operator()
            assert operator1 == operator2
            ```
        """
        self.random.seed(seed)
    
    def generate_operator(self) -> Dict[str, Any]:
        """
        Generate a random telecom operator with realistic information.
        
        Returns:
            A dictionary containing operator information
            
        Raises:
            RuntimeError: If the data source is unavailable or contains no operators
        """
        try:
            # Get the data from the provider
            data = self.data_provider.get_data()
            
            # Select a random operator from the data source
            operators = data.get('operators', [])
            if not operators:
                raise ValueError("No operators found in the data source")
            
            operator = self.random.choice(operators)
            
            # Return a copy to prevent modifying the original data
            return {
                'name': operator.get('name', ''),
                'country': operator.get('country', ''),
                'mcc': operator.get('mcc', ''),
                'mnc': operator.get('mnc', ''),
                'size': operator.get('size', 'medium'),
                'is_mvno': operator.get('is_mvno', False)
            }
        except Exception as e:
            # Wrap the exception with a more informative message
            raise RuntimeError(f"Failed to generate operator: {str(e)}. Please check the data source.") from e 