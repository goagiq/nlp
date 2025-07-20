# NLP MCP Server

A powerful Model Context Protocol (MCP) server that provides advanced natural language processing capabilities including sentiment analysis, text summarization, and entity extraction for both web pages and raw text.

## 🚀 Features

### Web Page Analysis
- **📄 Text Summarization**: Extract and summarize content from web pages using TF-IDF algorithm
- **😊 Sentiment Analysis**: Analyze sentiment of web page content with aspect-based analysis
- **🏷️ Entity Extraction**: Extract named entities from web page content using spaCy

### Text Analysis
- **📝 Text Summarization**: Summarize raw text input with customizable sentence count
- **💭 Sentiment Analysis**: Analyze sentiment of raw text with paragraph and sentence-level analysis
- **🔍 Entity Extraction**: Extract named entities from raw text with frequency counting

### MCP Integration
- **🔌 Model Context Protocol**: Full MCP server integration with exposed operations
- **⚡ FastAPI Backend**: High-performance async API endpoints
- **🎯 Type Safety**: Comprehensive type hints and error handling

## 📋 Requirements

- Python 3.13+
- Git
- pip or uv package manager

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/goagiq/nlp.git
cd nlp
```

### 2. Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using uv (recommended):**
```bash
uv sync
```

### 3. Download Required Models

**NLTK Data:**
```bash
python -c "import nltk; nltk.download('stopwords')"
```

**spaCy Model:**
```bash
python -m spacy download en_core_web_sm
```

## 🚀 Quick Start

### Starting the Server
```bash
python -m mcpserver
```

The server will start on `http://127.0.0.1:8001`

### Running Tests
```bash
python test_text_analysis.py
```

## 📚 API Documentation

### Web Page Analysis Endpoints

#### GET /summary/
Summarize web page content using TF-IDF algorithm.

**Parameters:**
- `url` (str, required): Web page URL
- `num_sentences` (int, optional): Number of sentences in summary (default: 3)

**Example:**
```bash
curl "http://127.0.0.1:8001/summary/?url=https://example.com&num_sentences=3"
```

**Response:**
```json
{
  "summary": "Extracted summary text here..."
}
```

#### GET /sentiment/
Analyze sentiment of web page content with aspect-based analysis.

**Parameters:**
- `url` (str, required): Web page URL
- `threshold` (float, optional): Sentiment threshold (default: 0.5)

**Example:**
```bash
curl "http://127.0.0.1:8001/sentiment/?url=https://example.com&threshold=0.3"
```

**Response:**
```json
{
  "paragraph_sentiments": {
    "paragraph_text": {
      "paragraph_sentiment": "Positive",
      "sentence_sentiments": {
        "sentence_text": "Positive"
      }
    }
  }
}
```

#### GET /entities/
Extract named entities from web page content.

**Parameters:**
- `url` (str, required): Web page URL
- `top_k` (int, optional): Number of top entities to return (default: 5)

**Example:**
```bash
curl "http://127.0.0.1:8001/entities/?url=https://example.com&top_k=5"
```

**Response:**
```json
{
  "entities": [
    {
      "text": "Apple Inc.",
      "type": "ORG",
      "count": 3
    }
  ]
}
```

### Text Analysis Endpoints

#### POST /text-summary/
Summarize raw text input.

**Parameters:**
- `text` (str, required): Text to summarize
- `num_sentences` (int, optional): Number of sentences in summary (default: 3)

**Example:**
```bash
curl -X POST "http://127.0.0.1:8001/text-summary/" \
  -d "text=Natural language processing is a fascinating field..." \
  -d "num_sentences=2"
```

#### POST /text-sentiment/
Analyze sentiment of raw text.

**Parameters:**
- `text` (str, required): Text to analyze
- `threshold` (float, optional): Sentiment threshold (default: 0.5)

**Example:**
```bash
curl -X POST "http://127.0.0.1:8001/text-sentiment/" \
  -d "text=I love this product! It's amazing." \
  -d "threshold=0.3"
```

#### POST /text-entities/
Extract entities from raw text.

**Parameters:**
- `text` (str, required): Text to analyze
- `top_k` (int, optional): Number of top entities to return (default: 5)

**Example:**
```bash
curl -X POST "http://127.0.0.1:8001/text-entities/" \
  -d "text=Apple Inc. is headquartered in Cupertino, California." \
  -d "top_k=3"
```

## 💻 Usage Examples

### Python Client

```python
import requests

# Initialize base URL
BASE_URL = "http://127.0.0.1:8001"

# Text Summarization
def summarize_webpage(url, sentences=3):
    response = requests.get(f"{BASE_URL}/summary/", 
                          params={"url": url, "num_sentences": sentences})
    return response.json()

def summarize_text(text, sentences=3):
    response = requests.post(f"{BASE_URL}/text-summary/", 
                           params={"text": text, "num_sentences": sentences})
    return response.json()

# Entity Extraction
def extract_entities_from_webpage(url, top_k=5):
    response = requests.get(f"{BASE_URL}/entities/", 
                          params={"url": url, "top_k": top_k})
    return response.json()

def extract_entities_from_text(text, top_k=5):
    response = requests.post(f"{BASE_URL}/text-entities/", 
                           params={"text": text, "top_k": top_k})
    return response.json()

# Sentiment Analysis
def analyze_webpage_sentiment(url, threshold=0.5):
    response = requests.get(f"{BASE_URL}/sentiment/", 
                          params={"url": url, "threshold": threshold})
    return response.json()

def analyze_text_sentiment(text, threshold=0.5):
    response = requests.post(f"{BASE_URL}/text-sentiment/", 
                           params={"text": text, "threshold": threshold})
    return response.json()

# Example usage
if __name__ == "__main__":
    # Summarize a webpage
    summary = summarize_webpage("https://example.com", 3)
    print("Webpage Summary:", summary)
    
    # Analyze text sentiment
    text = "I absolutely love this new smartphone! The camera quality is amazing."
    sentiment = analyze_text_sentiment(text, 0.3)
    print("Text Sentiment:", sentiment)
    
    # Extract entities from text
    text = "Apple Inc. is an American multinational technology company."
    entities = extract_entities_from_text(text, 5)
    print("Entities:", entities)
```

### JavaScript/Node.js Client

```javascript
const axios = require('axios');

const BASE_URL = 'http://127.0.0.1:8001';

// Text summarization
async function summarizeText(text, sentences = 3) {
    try {
        const response = await axios.post(`${BASE_URL}/text-summary/`, null, {
            params: { text, num_sentences: sentences }
        });
        return response.data;
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
    }
}

// Entity extraction
async function extractEntities(text, topK = 5) {
    try {
        const response = await axios.post(`${BASE_URL}/text-entities/`, null, {
            params: { text, top_k: topK }
        });
        return response.data;
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
    }
}

// Example usage
(async () => {
    const text = "Apple Inc. is headquartered in Cupertino, California.";
    const summary = await summarizeText(text, 2);
    const entities = await extractEntities(text, 3);
    
    console.log('Summary:', summary);
    console.log('Entities:', entities);
})();
```

## 🔧 MCP Integration

The server exposes the following MCP operations:

| Operation | Description | Parameters |
|-----------|-------------|------------|
| `get_summary` | Summarize web page content | `url`, `num_sentences` |
| `analyze_sentiment_from_url` | Analyze sentiment of web page | `url`, `threshold` |
| `analyze_sentiment_from_text` | Analyze sentiment of text | `text`, `threshold` |
| `extract_entities` | Extract entities from web page | `url`, `top_k` |
| `summarize_text` | Summarize raw text | `text`, `num_sentences` |
| `extract_text_entities` | Extract entities from text | `text`, `top_k` |

### MCP Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "nlp": {
      "command": "python",
      "args": ["-m", "mcpserver"],
      "env": {}
    }
  }
}
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_text_analysis.py
```

The test suite covers:
- ✅ Text summarization functionality
- ✅ Entity extraction from text
- ✅ Sentiment analysis with different thresholds
- ✅ Error handling and edge cases

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | ≥0.116.1 | Web framework for building APIs |
| `fastapi-mcp` | ≥0.3.7 | MCP integration for FastAPI |
| `beautifulsoup4` | ≥0.0.2 | HTML parsing for web scraping |
| `textblob` | ≥0.19.0 | Natural language processing |
| `spacy` | ≥3.8.7 | Advanced NLP with entity recognition |
| `nltk` | ≥3.9.1 | Natural language toolkit |
| `requests` | ≥2.32.4 | HTTP library for web requests |
| `uvicorn` | ≥0.35.0 | ASGI server for FastAPI |

## 🏗️ Project Structure

```
nlp/
├── src/
│   └── mcpserver/
│       ├── __init__.py
│       ├── __main__.py          # Server entry point
│       └── deployment.py        # Core NLP functions and API endpoints
├── test_text_analysis.py        # Test suite
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Project configuration
├── README.md                   # This file
└── REFACTOR_SUMMARY.md         # Development documentation
```

## 🔍 Core Functions

### Text Processing
- **`get_webpage_text(url)`**: Extract main content from web pages
- **`summarize_text(text, num_sentences)`**: TF-IDF based text summarization
- **`analyze_text_sentiment(text, threshold)`**: Aspect-based sentiment analysis
- **`extract_text_entities(text, top_k)`**: Named entity extraction with spaCy

### Web Page Analysis
- **`get_summary(url, num_sentences)`**: Web page summarization
- **`analyze_sentiment_from_url(url, threshold)`**: Web page sentiment analysis
- **`extract_entities(url, top_k)`**: Web page entity extraction

## 🚀 Performance Features

- **Async API Endpoints**: Non-blocking request handling
- **Efficient Text Processing**: Optimized algorithms for large text
- **Memory Management**: Proper cleanup of NLP models
- **Error Handling**: Comprehensive error catching and reporting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **spaCy**: For advanced NLP capabilities
- **TextBlob**: For sentiment analysis
- **NLTK**: For natural language processing tools
- **FastAPI**: For the excellent web framework
- **BeautifulSoup**: For HTML parsing

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Check the [REFACTOR_SUMMARY.md](REFACTOR_SUMMARY.md) for development details
- Review the test suite for usage examples

---

**Made with ❤️ for the NLP community**
