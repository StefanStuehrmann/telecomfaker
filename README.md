# TelecomFaker

A Python package for generating realistic telecom operator test data. Similar to Faker, but focused on telecom-specific information.

## Design

```mermaid
graph TD
    A[TelecomFaker] --> B[DataProvider]
    B --> C[Static JSON Data]
    
    A --> D[Generate Random Operator]
    D --> E[With Country Info]
    D --> F[With Numbering Info]
    D --> G[With Phone Numbers]
```

## Features

- Generate random telecom operator data with realistic information
- Access operator details by country, region, or randomly
- Get accurate numbering information (Prefix, MCC, MNC)
- Filter operators by size, country, or other attributes
- Built with real-world telecom data

## Installation

### For Users

```bash
pip install telecomfaker
```

### For Developers

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telecomfaker.git
cd telecomfaker
```

2. Create and activate a virtual environment:
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

## Development

### Running Tests

Run BDD tests with Behave:
```bash
behave
```

Run unit tests with pytest:
```bash
pytest
```


## Quick Start

```python
from telecomfaker import TelecomFaker

# Create a TelecomFaker instance
faker = TelecomFaker()

# Get a random operator with all associated information
result = faker.generate_operator()
operator = result["operator"]
numbering = result["numbering"]

print(f"Random Operator: {operator['name']} ({operator['country']})")
print(f"MCC: {operator['mcc']}, MNC: {operator['mnc']}")
print(f"Size: {operator['size']} subscribers")
print(f"Country Code: {operator['country_code']}")
print(f"Mobile Prefixes: {operator['mobile_prefixes']}")
```

## Data Sources

TelecomFaker uses real-world data compiled from:

- ITU (International Telecommunication Union)
- Public MCC/MNC databases
- Telecom regulatory authorities
- Open-source telecom data repositories

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
