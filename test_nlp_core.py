#!/usr/bin/env python3
"""
Test script for the refactored NLP core functions.
This script tests the core NLP functionality without FastAPI dependencies.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mcpserver.nlp_core import (
    summarize_text,
    analyze_sentiment_from_text,
    extract_text_entities
)


def main():
    """Main test function"""
    print("Testing Refactored NLP Core Functions")
    print("=" * 50)
    
    # Test 1: Text summarization
    print("\n1. Testing Text Summarization:")
    sample_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, 
    and artificial intelligence concerned with the interactions between computers and 
    human language, in particular how to program computers to process and analyze 
    large amounts of natural language data. Challenges in natural language processing 
    frequently involve speech recognition, natural language understanding, and natural 
    language generation.
    """
    result = summarize_text(sample_text, 2)
    print(f"Result: {result}")
    
    # Test 2: Sentiment analysis
    print("\n2. Testing Sentiment Analysis:")
    sentiment_text = """
    I love this product! It's amazing and works perfectly. 
    The customer service is terrible though. 
    Overall, I'm very satisfied with my purchase.
    """
    result = analyze_sentiment_from_text(sentiment_text)
    print(f"Result: {result}")
    
    # Test 3: Entity extraction
    print("\n3. Testing Entity Extraction:")
    entity_text = """
    Apple Inc. is an American multinational technology company headquartered in 
    Cupertino, California. Steve Jobs founded the company in 1976. 
    The company designs, develops, and sells consumer electronics, computer software, 
    and online services.
    """
    result = extract_text_entities(entity_text, 3)
    print(f"Result: {result}")
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")
    print("The refactored NLP core functions are working without FastAPI dependencies.")


if __name__ == "__main__":
    main() 