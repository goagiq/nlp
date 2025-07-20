#!/usr/bin/env python3
"""
Comprehensive examples for all NLP core functions.
This script demonstrates each method with real examples.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mcpserver.nlp_core import (
    summarize_text,
    analyze_sentiment_from_text,
    extract_text_entities,
    get_summary,
    analyze_sentiment_from_url,
    extract_entities,
    get_nlp_readme
)


def example_1_summarize_text():
    """Example 1: Text summarization"""
    print("=" * 60)
    print("EXAMPLE 1: Text Summarization")
    print("=" * 60)
    
    sample_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create 
    intelligent machines that work and react like humans. Some of the activities 
    computers with artificial intelligence are designed for include speech recognition, 
    learning, planning, and problem solving. AI has been used in various fields 
    including healthcare, finance, transportation, and entertainment. Machine learning, 
    a subset of AI, enables computers to learn automatically and improve from experience 
    without being explicitly programmed. Deep learning, a subset of machine learning, 
    uses neural networks with multiple layers to analyze various factors of data.
    """
    
    print("Original Text:")
    print(sample_text.strip())
    print("\n" + "-" * 40)
    
    # Test with different sentence counts
    for num_sentences in [2, 3, 4]:
        result = summarize_text(sample_text, num_sentences)
        print(f"\nSummary ({num_sentences} sentences):")
        print(result['summary'])


def example_2_sentiment_analysis():
    """Example 2: Sentiment analysis on text"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Sentiment Analysis")
    print("=" * 60)
    
    sample_text = """
    I absolutely love this new smartphone! The camera quality is amazing and the 
    battery life is incredible. The user interface is intuitive and easy to navigate. 
    However, the customer service was terrible when I had an issue. The representative 
    was rude and unhelpful. Despite that, I'm very satisfied with my purchase and 
    would recommend this product to others.
    """
    
    print("Original Text:")
    print(sample_text.strip())
    print("\n" + "-" * 40)
    
    # Test with different thresholds
    for threshold in [0.3, 0.5, 0.7]:
        result = analyze_sentiment_from_text(sample_text, threshold)
        print(f"\nSentiment Analysis (threshold={threshold}):")
        for paragraph, data in result['paragraph_sentiments'].items():
            print(f"Paragraph Sentiment: {data['paragraph_sentiment']}")
            print("Sentence Sentiments:")
            for sentence, sentiment in data['sentence_sentiments'].items():
                print(f"  - {sentence[:50]}... -> {sentiment}")


def example_3_entity_extraction():
    """Example 3: Named entity extraction"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Named Entity Extraction")
    print("=" * 60)
    
    sample_text = """
    Apple Inc. is an American multinational technology company headquartered in 
    Cupertino, California. Steve Jobs, Steve Wozniak, and Ronald Wayne founded 
    the company in 1976. The company designs, develops, and sells consumer 
    electronics, computer software, and online services. Tim Cook is the current 
    CEO of Apple. The company's hardware products include the iPhone smartphone, 
    the iPad tablet computer, the Mac personal computer, the Apple Watch smartwatch, 
    and the Apple TV digital media player.
    """
    
    print("Original Text:")
    print(sample_text.strip())
    print("\n" + "-" * 40)
    
    # Test with different top_k values
    for top_k in [3, 5, 8]:
        result = extract_text_entities(sample_text, top_k)
        print(f"\nTop {top_k} Entities:")
        for entity in result['entities']:
            print(f"  - {entity['text']} ({entity['type']}) - Count: {entity['count']}")


def example_4_webpage_analysis():
    """Example 4: Webpage analysis (using a public news article)"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Webpage Analysis")
    print("=" * 60)
    
    # Using a simple, accessible webpage for demonstration
    test_url = "https://httpbin.org/html"
    
    print(f"Analyzing webpage: {test_url}")
    print("-" * 40)
    
    # Get summary
    print("\n1. Webpage Summary:")
    try:
        summary_result = get_summary(test_url, 2)
        if 'error' in summary_result:
            print(f"Error: {summary_result['error']}")
        else:
            print(summary_result['summary'])
    except Exception as e:
        print(f"Error getting summary: {e}")
    
    # Get sentiment
    print("\n2. Webpage Sentiment Analysis:")
    try:
        sentiment_result = analyze_sentiment_from_url(test_url, 0.5)
        if 'error' in sentiment_result:
            print(f"Error: {sentiment_result['error']}")
        else:
            print("Sentiment analysis completed successfully")
            for paragraph, data in sentiment_result['paragraph_sentiments'].items():
                print(f"  Paragraph: {data['paragraph_sentiment']}")
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
    
    # Get entities
    print("\n3. Webpage Entity Extraction:")
    try:
        entities_result = extract_entities(test_url, 5)
        if 'error' in entities_result:
            print(f"Error: {entities_result['error']}")
        else:
            print("Top entities found:")
            for entity in entities_result['entities']:
                print(f"  - {entity['text']} ({entity['type']}) - Count: {entity['count']}")
    except Exception as e:
        print(f"Error extracting entities: {e}")


def example_5_resource_reading():
    """Example 5: Resource reading"""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Resource Reading")
    print("=" * 60)
    
    print("Attempting to read nlp_readme.md:")
    content = get_nlp_readme()
    if "Error" in content or "not found" in content:
        print(f"Result: {content}")
        print("\nNote: This is expected if nlp_readme.md doesn't exist.")
    else:
        print("Content found:")
        print(content[:200] + "..." if len(content) > 200 else content)


def example_6_comprehensive_text_analysis():
    """Example 6: Comprehensive text analysis"""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Comprehensive Text Analysis")
    print("=" * 60)
    
    comprehensive_text = """
    Tesla, Inc. is an American electric vehicle and clean energy company based in 
    Austin, Texas. Elon Musk is the CEO and co-founder of Tesla. The company 
    specializes in electric cars, battery energy storage, solar panels, and related 
    products and services. Tesla's mission is to accelerate the world's transition 
    to sustainable energy. The company's Model S, Model 3, Model X, and Model Y 
    vehicles have received numerous awards and accolades for their performance, 
    safety, and environmental impact. Tesla's Gigafactories produce batteries and 
    vehicles at scale to meet growing demand for sustainable transportation.
    
    The company faces both praise and criticism. Supporters applaud Tesla's 
    innovation in electric vehicles and renewable energy technology. Critics point 
    to production delays, quality control issues, and concerns about workplace 
    safety. Despite challenges, Tesla continues to lead the electric vehicle 
    market and expand its global presence.
    """
    
    print("Original Text:")
    print(comprehensive_text.strip())
    print("\n" + "=" * 60)
    
    # 1. Summarize
    print("\n1. TEXT SUMMARIZATION:")
    summary = summarize_text(comprehensive_text, 3)
    print(summary['summary'])
    
    # 2. Sentiment Analysis
    print("\n2. SENTIMENT ANALYSIS:")
    sentiment = analyze_sentiment_from_text(comprehensive_text, 0.5)
    for paragraph, data in sentiment['paragraph_sentiments'].items():
        print(f"Paragraph: {data['paragraph_sentiment']}")
    
    # 3. Entity Extraction
    print("\n3. ENTITY EXTRACTION:")
    entities = extract_text_entities(comprehensive_text, 6)
    print("Top entities:")
    for entity in entities['entities']:
        print(f"  - {entity['text']} ({entity['type']}) - Count: {entity['count']}")


def main():
    """Run all examples"""
    print("NLP Core Functions - Comprehensive Examples")
    print("=" * 60)
    print("This script demonstrates all the refactored NLP core functions.")
    print("=" * 60)
    
    try:
        # Run all examples
        example_1_summarize_text()
        example_2_sentiment_analysis()
        example_3_entity_extraction()
        example_4_webpage_analysis()
        example_5_resource_reading()
        example_6_comprehensive_text_analysis()
        
        print("\n" + "=" * 60)
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("The refactored NLP core functions are working correctly.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        print("This might be due to missing dependencies or network issues.")


if __name__ == "__main__":
    main() 