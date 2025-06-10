import requests
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError, WikipediaException


class WikipediaRAGAgent:
    """Minimal agent for retrieving Wikipedia summaries."""

    def query_wikipedia(self, query: str) -> str:
        """Return a short summary for the given query from Wikipedia."""
        if not query or not query.strip():
            return "No query provided"

        try:
            summary = wikipedia.summary(query, sentences=2)
            return summary.strip() if summary else "No summary found"
        except DisambiguationError as e:
            # Attempt to use the first suggested page
            if e.options:
                try:
                    summary = wikipedia.summary(e.options[0], sentences=2)
                    return summary.strip() if summary else "No summary found"
                except (PageError, WikipediaException, requests.RequestException):
                    return "Disambiguation provided no usable result"
            return "Disambiguation error: no suitable pages"
        except PageError:
            return "Page not found"
        except requests.RequestException as e:
            return f"Network error: {e}"
        except WikipediaException as e:
            return f"Wikipedia error: {e}"
        except Exception as e:
            return f"Error retrieving summary: {e}"
