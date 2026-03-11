import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, PruningContentFilter
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import URLPatternFilter, FilterChain
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def crawl_domain(crawler, url, base_pattern, filename, max_pages=100):
    print(f"\n--- Starting crawl for {url} (max {max_pages} pages) ---")

    # Create a filter to stay within the desired domain/path
    filter_chain = FilterChain([
        URLPatternFilter(patterns=[f"{base_pattern}*"])
    ])

    # Setup BFS strategy
    deep_crawl_strategy = BFSDeepCrawlStrategy(
        max_depth=10,
        filter_chain=filter_chain,
        max_pages=max_pages
    )

    # Use PruningContentFilter for clean RAG-friendly markdown
    markdown_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.45, threshold_type="fixed", min_word_threshold=0)
    )

    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        deep_crawl_strategy=deep_crawl_strategy,
        markdown_generator=markdown_generator,
        stream=True,
        magic=True,
        simulate_user=True,
        override_navigator=True
    )

    all_markdown = []
    page_count = 0

    try:
        results_gen = await crawler.arun(url=url, config=run_config)
        async for result in results_gen:
            if result.success:
                # Check for anti-bot content
                lowered_content = result.markdown.lower()
                if "verify" in lowered_content and "connection" in lowered_content and "human" in lowered_content:
                    print(f"[{page_count+1}] Skipped (Bot detection): {result.url}")
                    continue

                page_count += 1
                print(f"[{page_count}] Crawled: {result.url}")
                all_markdown.append(f"# Source: {result.url}\n\n{result.markdown}\n\n---\n")
            else:
                print(f"Failed: {result.url} - Error: {result.error_message}")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(all_markdown))
        print(f"Finished {url}. Saved {page_count} pages to {filename}")
    except Exception as e:
        print(f"An error occurred while crawling {url}: {e}")

async def main():
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
        enable_stealth=True,
        user_agent_mode="random"
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Docs usually have many pages but are easy to crawl
        await crawl_domain(crawler, "https://docs.omni.co/", "https://docs.omni.co/", "omni_docs.md", max_pages=300)
        # Blog might have many pages if we go back in time
        await crawl_domain(crawler, "https://omni.co/blog", "https://omni.co/blog", "omni_blog.md", max_pages=200)
        # Community forums can be huge, limit to 100 for now
        await crawl_domain(crawler, "https://community.omni.co/", "https://community.omni.co/", "omni_community.md", max_pages=100)

if __name__ == "__main__":
    asyncio.run(main())
