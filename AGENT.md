# Agent Guide for Crawl4AI

This document provides essential information for AI agents working on the Crawl4AI repository.

## Environment Setup

The project uses `uv` for dependency management. To set up the development environment:

1.  **Create a virtual environment:**
    ```bash
    uv venv
    source .venv/bin/activate
    ```

2.  **Install dependencies in editable mode:**
    ```bash
    uv pip install -e .
    ```

3.  **Run post-installation setup:**
    This installs Playwright/Patchright browsers and initializes the database.
    ```bash
    crawl4ai-setup
    ```

4.  **Verify the installation:**
    ```bash
    crawl4ai-doctor
    ```

## Project Structure

- `crawl4ai/`: Main package containing the crawler logic.
    - `async_webcrawler.py`: The primary entry point for the asynchronous crawler (`AsyncWebCrawler`).
    - `async_crawler_strategy.py`: Strategies for interacting with browsers (Playwright, Patchright).
    - `extraction_strategy.py`: Strategies for extracting structured data (LLM, CSS, XPath).
    - `markdown_generation_strategy.py`: Logic for converting HTML to AI-friendly Markdown.
    - `cli.py`: The command-line interface (`crwl`).
- `docs/`: Comprehensive documentation and examples.
- `tests/`: Test suite, organized by component.

## Testing

To run tests, ensure the virtual environment is activated and use `pytest`:

```bash
pytest tests/unit
```

For a quick health check of the crawling capabilities:
```bash
crawl4ai-doctor
```

## Key Components & Usage

### AsyncWebCrawler
The main class for crawling. It can be used as an asynchronous context manager.

```python
from crawl4ai import AsyncWebCrawler

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://example.com")
    print(result.markdown)
```

### Configuration
Use `BrowserConfig` and `CrawlerRunConfig` to customize the crawling process.

```python
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

browser_config = BrowserConfig(headless=True)
run_config = CrawlerRunConfig(cache_mode="BYPASS")

async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(url="https://example.com", config=run_config)
```

## Tips for Agents
- Always use the `uv` virtual environment.
- The `crawl4ai-doctor` command is a reliable way to verify that the browser environment is correctly set up.
- For issues with bot detection, explore `stealth_mode` and the `undetected` browser type in `BrowserConfig`.
- Structured data extraction can be done with `JsonCssExtractionStrategy` (fast, no LLM cost) or `LLMExtractionStrategy` (flexible, requires LLM).
