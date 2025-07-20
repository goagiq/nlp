from mcpserver.deployment import app
from fastapi_mcp import FastApiMCP
import uvicorn


def main():
    # Create FastApiMCP instance with operation IDs
    mcp = FastApiMCP(app, include_operations=[
        "get_summary",
        "analyze_sentiment_from_url", 
        "analyze_sentiment_from_text",
        "extract_entities",
        "summarize_text",
        "extract_text_entities"
    ])
    
    # Mount the MCP operations to the FastAPI app
    mcp.mount()
    
    # Run the FastAPI server with uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)


if __name__ == "__main__":
    main()
