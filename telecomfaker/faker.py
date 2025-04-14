import random
from typing import Dict, Any, Optional

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
    
    def set_seed(self, seed: int) -> None:
        """
        Set a random seed for consistent data generation.
        
        Args:
            seed: An integer to use as the random seed
        """
        self.random.seed(seed)
    
    def generate_operator(self) -> Dict[str, Any]:
        """
        Generate a random telecom operator with realistic information.
        
        Returns:
            A dictionary containing operator information
            
        Raises:
            Exception: If the data source is unavailable or contains no operators
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