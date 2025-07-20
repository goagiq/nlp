#!/usr/bin/env python3
"""
Demonstration of the refactored NLP core vs original FastAPI version.
This script shows the key differences and benefits of the refactoring.
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


def demonstrate_direct_usage():
    """Demonstrate direct function usage (refactored approach)"""
    print("=" * 60)
    print("REFACTORED APPROACH: Direct Function Usage")
    print("=" * 60)
    
    sample_text = """
    Python is a high-level, interpreted programming language known for its 
    simplicity and readability. Created by Guido van Rossum in 1991, Python 
    emphasizes code readability with its notable use of significant whitespace. 
    Python features a dynamic type system and automatic memory management. 
    It supports multiple programming paradigms, including procedural, object-oriented, 
    and functional programming. Python is widely used in web development, data science, 
    artificial intelligence, and automation.
    """
    
    print("Sample Text:")
    print(sample_text.strip())
    print("\n" + "-" * 40)
    
    # 1. Direct text summarization
    print("1. TEXT SUMMARIZATION (Direct Call):")
    summary = summarize_text(sample_text, 2)
    print(f"Result: {summary['summary']}")
    
    # 2. Direct sentiment analysis
    print("\n2. SENTIMENT ANALYSIS (Direct Call):")
    sentiment = analyze_sentiment_from_text(sample_text, 0.5)
    for data in sentiment['paragraph_sentiments'].values():
        print(f"Overall sentiment: {data['paragraph_sentiment']}")
    
    # 3. Direct entity extraction
    print("\n3. ENTITY EXTRACTION (Direct Call):")
    entities = extract_text_entities(sample_text, 5)
    print("Top entities:")
    for entity in entities['entities']:
        print(f"  - {entity['text']} ({entity['type']}) - Count: {entity['count']}")


def demonstrate_benefits():
    """Demonstrate the benefits of the refactored approach"""
    print("\n" + "=" * 60)
    print("BENEFITS OF REFACTORED APPROACH")
    print("=" * 60)
    
    benefits = [
        {
            "title": "1. Reduced Dependencies",
            "before": "FastAPI, uvicorn, pydantic, starlette",
            "after": "Only core NLP libraries (spacy, textblob, nltk, requests, beautifulsoup4)",
            "benefit": "Lighter footprint, easier deployment"
        },
        {
            "title": "2. Direct Function Calls",
            "before": "HTTP requests to web endpoints",
            "after": "Direct Python function calls",
            "benefit": "Faster execution, better for testing"
        },
        {
            "title": "3. No Web Server Required",
            "before": "Need to start uvicorn server",
            "after": "Import and use directly",
            "benefit": "Simpler integration, no network overhead"
        },
        {
            "title": "4. Better Testing",
            "before": "Integration tests with web server",
            "after": "Unit tests with direct function calls",
            "benefit": "Faster tests, easier debugging"
        },
        {
            "title": "5. Framework Agnostic",
            "before": "Tied to FastAPI",
            "after": "Can be used with any framework or no framework",
            "benefit": "Maximum flexibility and portability"
        }
    ]
    
    for benefit in benefits:
        print(f"\n{benefit['title']}")
        print(f"  Before: {benefit['before']}")
        print(f"  After:  {benefit['after']}")
        print(f"  Benefit: {benefit['benefit']}")


def demonstrate_integration_examples():
    """Show how the refactored code can be integrated"""
    print("\n" + "=" * 60)
    print("INTEGRATION EXAMPLES")
    print("=" * 60)
    
    examples = [
        {
            "framework": "Flask",
            "code": """
from flask import Flask, request, jsonify
from mcpserver.nlp_core import summarize_text

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    result = summarize_text(text, 3)
    return jsonify(result)
""",
            "benefit": "Lightweight web API"
        },
        {
            "framework": "Django",
            "code": """
from django.http import JsonResponse
from mcpserver.nlp_core import analyze_sentiment_from_text

def analyze_sentiment(request):
    text = request.POST.get('text')
    result = analyze_sentiment_from_text(text)
    return JsonResponse(result)
""",
            "benefit": "Full-featured web framework"
        },
        {
            "framework": "CLI Tool",
            "code": """
import argparse
from mcpserver.nlp_core import extract_text_entities

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    args = parser.parse_args()
    
    entities = extract_text_entities(args.text)
    print(entities)

if __name__ == '__main__':
    main()
""",
            "benefit": "Command-line interface"
        },
        {
            "framework": "Library",
            "code": """
from mcpserver.nlp_core import summarize_text

# Use directly in your application
def process_documents(documents):
    summaries = []
    for doc in documents:
        summary = summarize_text(doc, 2)
        summaries.append(summary)
    return summaries
""",
            "benefit": "Direct library usage"
        }
    ]
    
    for example in examples:
        print(f"\n{example['framework']} Integration:")
        print(f"Benefit: {example['benefit']}")
        print("Code:")
        print(example['code'])


def main():
    """Run the demonstration"""
    print("NLP Core Refactoring Demonstration")
    print("=" * 60)
    print("This script demonstrates the benefits of removing FastAPI dependencies")
    print("and creating a pure NLP library.")
    print("=" * 60)
    
    try:
        # Demonstrate direct usage
        demonstrate_direct_usage()
        
        # Show benefits
        demonstrate_benefits()
        
        # Show integration examples
        demonstrate_integration_examples()
        
        print("\n" + "=" * 60)
        print("DEMONSTRATION COMPLETED!")
        print("The refactored NLP core provides:")
        print("✓ Reduced dependencies")
        print("✓ Better performance")
        print("✓ Easier testing")
        print("✓ Framework flexibility")
        print("✓ Direct integration")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError during demonstration: {e}")


if __name__ == "__main__":
    main() 