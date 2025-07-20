import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import spacy
import re
import spacy.cli
import nltk
from collections import defaultdict
import heapq
from nltk.corpus import stopwords
from fastapi import FastAPI, HTTPException
from typing import Dict, List, Optional, Any, Union

# Initialize FastAPI app
app = FastAPI()

nltk.download('stopwords')

# Ensure proper formatting with blank lines

# Correct spacy.cli.download usage
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')


def get_webpage_text(url: str) -> Optional[str]:
    """
    Retrieve the main article content from a webpage given its URL.

    Args:
        url (str): The URL of the webpage to retrieve.

    Returns:
        Optional[str]: The text content of the main article, or None if not found.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Attempt to find the main article content
            article = soup.find('article')
            if not article:
                # Fallback to a div with a common main content class
                article = soup.find('div', class_='main-content')
            if not article:
                # Fallback to a div with a common article id
                article = soup.find('div', id='article')
            if article:
                return article.get_text()
            else:
                raise Exception(
                    "Main article content not found"
                )
        else:
            # Fix line length errors
            raise Exception(
                f"Failed to retrieve the webpage with status code: "
                f"{response.status_code}"
            )
    except Exception as e:
        print(
            f"An error occurred during webpage retrieval: {e}"
        )
        return None


def summarize_text(text: str, num_sentences: int = 3) -> Dict[str, str]:
    """
    Summarize a block of text.

    Args:
        text (str): The text to summarize.
        num_sentences (int, optional): The number of sentences to include in 
        the summary. Defaults to 3.

    Returns:
        Dict[str, str]: A dictionary containing the summary or an error message.
    """
    words = re.findall(r'\w+', text.lower())
    stopwords_set = set(stopwords.words('english'))
    freq: Dict[str, int] = defaultdict(int)
    for word in words:
        if word not in stopwords_set:
            freq[word] += 1

    sentences = re.split(r'(?<=[.!?]) +', text)
    sentence_scores: Dict[str, int] = {}
    for sent in sentences:
        sent_words = re.findall(r'\w+', sent.lower())
        for word in sent_words:
            if word in freq:
                sentence_scores[sent] = (
                    sentence_scores.get(sent, 0) + freq[word]
                )

    summary_sentences = heapq.nlargest(
        num_sentences, sentence_scores, 
        key=lambda s: sentence_scores[s]
    )
    return {"summary": ' '.join(summary_sentences)}


def analyze_text_sentiment(text: str, threshold: float = 0.5) -> Dict[str, Any]:
    """
    Perform aspect-based sentiment analysis on a block of text.

    Args:
        text (str): The text to analyze.
        threshold (float, optional): The polarity threshold to classify 
        sentiments. Defaults to 0.5.

    Returns:
        Dict[str, Any]: A dictionary containing aspect sentiments or an error message.
    """
    try:
        paragraphs = text.split('\n\n')
        paragraph_sentiments: Dict[str, Any] = {}

        for paragraph in paragraphs:
            blob = TextBlob(paragraph)
            paragraph_polarity = blob.sentiment.polarity
            paragraph_sentiment = "Neutral"
            if paragraph_polarity > threshold:
                paragraph_sentiment = "Positive"
            elif paragraph_polarity < -threshold:
                paragraph_sentiment = "Negative"

            sentence_sentiments: Dict[str, str] = {}
            sentences = paragraph.split('. ')
            for sentence in sentences:
                blob = TextBlob(sentence)
                sentence_polarity = blob.sentiment.polarity
                sentence_sentiment = "Neutral"
                if sentence_polarity > threshold:
                    sentence_sentiment = "Positive"
                elif sentence_polarity < -threshold:
                    sentence_sentiment = "Negative"
                sentence_sentiments[sentence] = sentence_sentiment

            paragraph_sentiments[paragraph] = {
                "paragraph_sentiment": paragraph_sentiment,
                "sentence_sentiments": sentence_sentiments
            }

        return {"paragraph_sentiments": paragraph_sentiments}
    except Exception as e:
        print(f"An error occurred during aspect-based sentiment analysis: {e}")
        return {"error": str(e)}


def extract_text_entities(text: str, top_k: int = 5) -> Dict[str, Any]:
    """
    Extract named entities from a block of text.

    Args:
        text (str): The text to analyze.
        top_k (int, optional): The number of top entities to return. 
        Defaults to 5.

    Returns:
        Dict[str, Any]: A dictionary containing the top entities or an error message.
    """
    try:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        entity_counts: Dict[tuple, int] = defaultdict(int)
        for entity in entities:
            entity_counts[entity] += 1
        top_entities = sorted(
            entity_counts.items(), key=lambda item: item[1], reverse=True
        )[:top_k]
        return {"entities": [
            {"text": ent[0][0], "type": ent[0][1], "count": ent[1]}
            for ent in top_entities
        ]}
    except Exception as e:
        print(f"An error occurred during entity extraction: {e}")
        return {"error": str(e)}


def get_summary(url: str, num_sentences: int = 3) -> Dict[str, str]:
    """
    Generate a summary of a webpage's content.

    Args:
        url (str): The URL of the webpage to summarize.
        num_sentences (int, optional): The number of sentences to include in 
        the summary. Defaults to 3.

    Returns:
        Dict[str, str]: A dictionary containing the summary or an error message.
    """
    text = get_webpage_text(url)
    if text is None:
        return {"error": "Failed to retrieve webpage text"}

    words = re.findall(r'\w+', text.lower())
    stopwords_set = set(stopwords.words('english'))
    freq: Dict[str, int] = defaultdict(int)
    for word in words:
        if word not in stopwords_set:
            freq[word] += 1

    sentences = re.split(r'(?<=[.!?]) +', text)
    sentence_scores: Dict[str, int] = {}
    for sent in sentences:
        sent_words = re.findall(r'\w+', sent.lower())
        for word in sent_words:
            if word in freq:
                sentence_scores[sent] = (
                    sentence_scores.get(sent, 0) + freq[word]
                )

    summary_sentences = heapq.nlargest(
        num_sentences, sentence_scores, 
        key=lambda s: sentence_scores[s]
    )
    return {"summary": ' '.join(summary_sentences)}


def analyze_sentiment_from_url(url: str, threshold: float = 0.5) -> Dict[str, Any]:
    """
    Perform aspect-based sentiment analysis on a webpage's content.

    Args:
        url (str): The URL of the webpage to analyze.
        threshold (float, optional): The polarity threshold to classify 
        sentiments. Defaults to 0.5.

    Returns:
        Dict[str, Any]: A dictionary containing aspect sentiments or an error message.
    """
    text = get_webpage_text(url)
    if text is None:
        return {"error": "Failed to retrieve webpage text"}
    return analyze_text_sentiment(text, threshold)


def analyze_sentiment_from_text(text: str, threshold: float = 0.5) -> Dict[str, Any]:
    """
    Perform aspect-based sentiment analysis on a block of text.

    Args:
        text (str): The text to analyze.
        threshold (float, optional): The polarity threshold to classify 
        sentiments. Defaults to 0.5.

    Returns:
        Dict[str, Any]: A dictionary containing aspect sentiments or an error message.
    """
    try:
        paragraphs = text.split('\n\n')
        paragraph_sentiments: Dict[str, Any] = {}

        for paragraph in paragraphs:
            blob = TextBlob(paragraph)
            paragraph_polarity = blob.sentiment.polarity
            paragraph_sentiment = "Neutral"
            if paragraph_polarity > threshold:
                paragraph_sentiment = "Positive"
            elif paragraph_polarity < -threshold:
                paragraph_sentiment = "Negative"

            sentence_sentiments: Dict[str, str] = {}
            sentences = paragraph.split('. ')
            for sentence in sentences:
                blob = TextBlob(sentence)
                sentence_polarity = blob.sentiment.polarity
                sentence_sentiment = "Neutral"
                if sentence_polarity > threshold:
                    sentence_sentiment = "Positive"
                elif sentence_polarity < -threshold:
                    sentence_sentiment = "Negative"
                sentence_sentiments[sentence] = sentence_sentiment

            paragraph_sentiments[paragraph] = {
                "paragraph_sentiment": paragraph_sentiment,
                "sentence_sentiments": sentence_sentiments
            }

        return {"paragraph_sentiments": paragraph_sentiments}
    except Exception as e:
        print(f"An error occurred during aspect-based sentiment analysis: {e}")
        return {"error": str(e)}


def extract_entities(url: str, top_k: int = 5) -> Dict[str, Any]:
    """
    Extract named entities from a webpage's content.

    Args:
        url (str): The URL of the webpage to analyze.
        top_k (int, optional): The number of top entities to return. 
        Defaults to 5.

    Returns:
        Dict[str, Any]: A dictionary containing the top entities or an error message.
    """
    text = get_webpage_text(url)
    if text is None:
        return {"error": "Failed to retrieve webpage text"}

    try:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        entity_counts: Dict[tuple, int] = defaultdict(int)
        for entity in entities:
            entity_counts[entity] += 1
        top_entities = sorted(
            entity_counts.items(), key=lambda item: item[1], reverse=True
        )[:top_k]
        # Include entity type in the output
        return {"entities": [
            {"text": ent[0][0], "type": ent[0][1], "count": ent[1]}
            for ent in top_entities
        ]}
    except Exception as e:
        print(f"An error occurred during entity extraction: {e}")
        return {"error": str(e)}


def get_nlp_readme() -> str:
    """Resource to expose the content of nlp_readme.md"""
    try:
        with open("nlp_readme.md", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Resource not found."
    except Exception as e:
        return f"Error reading resource: {e}"


# FastAPI endpoints for REST API access
@app.get("/summary/", operation_id="get_summary")
async def get_summary_endpoint(url: str, num_sentences: int = 3) -> Dict[str, str]:
    """
    FastAPI endpoint to get a summary of a webpage.

    Args:
        url (str): The URL of the webpage to summarize.
        num_sentences (int, optional): The number of sentences to include in 
        the summary. Defaults to 3.

    Returns:
        Dict[str, str]: A dictionary containing the summary or an error message.
    """
    result = get_summary(url, num_sentences)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.get("/sentiment/", operation_id="analyze_sentiment_from_url")
async def analyze_sentiment_endpoint(url: str, threshold: float = 0.5) -> Dict[str, Any]:
    """
    FastAPI endpoint to perform sentiment analysis on a webpage.

    Args:
        url (str): The URL of the webpage to analyze.
        threshold (float, optional): The polarity threshold to classify 
        sentiments. Defaults to 0.5.

    Returns:
        Dict[str, Any]: A dictionary containing aspect sentiments or an error message.
    """
    result = analyze_sentiment_from_url(url, threshold)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.post("/text-sentiment/", operation_id="analyze_sentiment_from_text")
async def analyze_sentiment_from_text_endpoint(
    text: str, threshold: float = 0.5
) -> Dict[str, Any]:
    """
    FastAPI endpoint to perform sentiment analysis on a block of text.

    Args:
        text (str): The text to analyze.
        threshold (float, optional): The polarity threshold to classify 
        sentiments. Defaults to 0.5.

    Returns:
        Dict[str, Any]: A dictionary containing aspect sentiments or an error message.
    """
    result = analyze_sentiment_from_text(text, threshold)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.get("/entities/", operation_id="extract_entities")
async def extract_entities_endpoint(url: str, top_k: int = 5) -> Dict[str, Any]:
    """
    FastAPI endpoint to extract named entities from a webpage.

    Args:
        url (str): The URL of the webpage to analyze.
        top_k (int, optional): The number of top entities to return. 
        Defaults to 5.

    Returns:
        Dict[str, Any]: A dictionary containing the top entities or an error message.
    """
    result = extract_entities(url, top_k)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.post("/text-summary/", operation_id="summarize_text")
async def summarize_text_endpoint(text: str, num_sentences: int = 3) -> Dict[str, str]:
    """
    FastAPI endpoint to summarize a block of text.

    Args:
        text (str): The text to summarize.
        num_sentences (int, optional): The number of sentences to include in 
        the summary. Defaults to 3.

    Returns:
        Dict[str, str]: A dictionary containing the summary or an error message.
    """
    result = summarize_text(text, num_sentences)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.post("/text-entities/", operation_id="extract_text_entities")
async def extract_text_entities_endpoint(text: str, top_k: int = 5) -> Dict[str, Any]:
    """
    FastAPI endpoint to extract named entities from a block of text.

    Args:
        text (str): The text to analyze.
        top_k (int, optional): The number of top entities to return. 
        Defaults to 5.

    Returns:
        Dict[str, Any]: A dictionary containing the top entities or an error message.
    """
    result = extract_text_entities(text, top_k)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.get("/nlp-readme/", operation_id="get_nlp_readme")
async def get_nlp_readme_endpoint() -> Dict[str, str]:
    """FastAPI endpoint to get the content of nlp_readme.md"""
    content = get_nlp_readme()
    if "Error" in content:
        raise HTTPException(status_code=404, detail=content)
    return {"content": content}