#!/usr/bin/env python3
"""
Command-line interface for TelecomFaker.
"""

import argparse
import json
import random
import sys
from typing import Dict, Any

from telecomfaker import TelecomFaker


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate realistic telecom operator test data."
    )
    
    parser.add_argument(
        "--seed", 
        type=int, 
        help="Random seed for consistent generation"
    )
    
    parser.add_argument(
        "--count", 
        type=int, 
        default=1, 
        help="Number of operators to generate (default: 1)"
    )
    
    parser.add_argument(
        "--format", 
        choices=["json", "text"], 
        default="text", 
        help="Output format (default: text)"
    )
    
    parser.add_argument(
        "--output", 
        type=str, 
        help="Output file (default: stdout)"
    )
    
    return parser.parse_args()


def format_operator_as_text(operator: Dict[str, Any]) -> str:
    """Format an operator as plain text."""
    mvno_status = "MVNO" if operator.get("is_mvno") else "MNO"
    
    return (
        f"Operator: {operator.get('name')}\n"
        f"Country: {operator.get('country')}\n"
        f"MCC: {operator.get('mcc')}\n"
        f"MNC: {operator.get('mnc')}\n"
        f"Size: {operator.get('size')}\n"
        f"Type: {mvno_status}\n"
    )


def main() -> None:
    """Main entry point for the CLI."""
    args = parse_args()
    
    # Initialize TelecomFaker
    faker = TelecomFaker()
    
    # Set seed if provided
    if args.seed is not None:
        faker.set_seed(args.seed)
    
    # Generate operators
    operators = [faker.generate_operator() for _ in range(args.count)]
    
    # Format output
    if args.format == "json":
        output = json.dumps(operators, indent=2)
    else:  # text format
        output = "\n".join(format_operator_as_text(op) for op in operators)
    
    # Write output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1) 