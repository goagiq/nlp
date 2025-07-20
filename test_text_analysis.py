#!/usr/bin/env python3
"""
Test script for text analysis functions.
"""

from src.mcpserver.deployment import (
    summarize_text, 
    extract_text_entities, 
    analyze_sentiment_from_text
)

def test_text_summarization():
    """Test text summarization functionality."""
    sample_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, 
    and artificial intelligence concerned with the interactions between computers and 
    human language, in particular how to program computers to process and analyze 
    large amounts of natural language data. Challenges in natural language processing 
    frequently involve speech recognition, natural language understanding, and natural 
    language generation. NLP is used in many real-world applications including machine 
    translation, question answering, and text summarization.
    """
    
    result = summarize_text(sample_text, num_sentences=2)
    print("Text Summarization Test:")
    print(f"Result: {result}")
    print("-" * 50)

def test_text_entity_extraction():
    """Test text entity extraction functionality."""
    sample_text = """
    Apple Inc. is an American multinational technology company headquartered in 
    Cupertino, California. Steve Jobs and Steve Wozniak founded Apple in 1976. 
    The company designs, develops, and sells consumer electronics, computer software, 
    and online services. Its hardware products include the iPhone smartphone, the iPad 
    tablet computer, the Mac personal computer, the Apple Watch smartwatch, and the 
    Apple TV digital media player.
    """
    
    result = extract_text_entities(sample_text, top_k=5)
    print("Text Entity Extraction Test:")
    print(f"Result: {result}")
    print("-" * 50)

def test_text_sentiment_analysis():
    """Test text sentiment analysis functionality."""
    sample_text = """
    I absolutely love this new smartphone! The camera quality is amazing and the 
    battery life is incredible. The user interface is intuitive and easy to use. 
    However, the price is quite expensive and the storage options are limited. 
    Overall, it's a great product despite the high cost.
    """
    
    result = analyze_sentiment_from_text(sample_text, threshold=0.3)
    print("Text Sentiment Analysis Test:")
    print(f"Result: {result}")
    print("-" * 50)

if __name__ == "__main__":
    print("Testing Text Analysis Functions")
    print("=" * 50)
    
    test_text_summarization()
    test_text_entity_extraction()
    test_text_sentiment_analysis()
    
    print("All tests completed!") 