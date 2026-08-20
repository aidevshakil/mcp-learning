import sys
import random
import asyncio
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("JokeGenerator")

# A small static database of developer jokes
JOKES = [
    {"topic": "general", "joke": "Why do programmers prefer dark mode? Because light attracts bugs."},
    {"topic": "java", "joke": "Why do Java programmers have to wear glasses? Because they don't C#."},
    {"topic": "python", "joke": "How do you know if someone is a Python developer? Don't worry, they'll tell you."},
    {"topic": "css", "joke": "A CSS designer walks into a bar. The bartender says, 'We don't serve your type here.' The designer says, 'I'll just change the layout.'"},
    {"topic": "javascript", "joke": "Why did the JavaScript developer go to therapy? Because they had too many promises they couldn't keep."},
    {"topic": "general", "joke": "There are 10 types of people in the world: those who understand binary, and those who don't."},
    {"topic": "database", "joke": "A SQL query goes into a bar, walks up to two tables and asks... 'Can I join you?'"},
    {"topic": "general", "joke": "I would tell you a UDP joke, but you might not get it."}
]

@mcp.tool()
def get_random_joke() -> str:
    """Returns a random developer joke."""
    joke = random.choice(JOKES)
    return joke["joke"]

@mcp.tool()
def get_joke_by_topic(topic: str) -> str:
    """
    Returns a developer joke based on a specific topic.
    Supported topics: general, java, python, css, javascript, database.
    """
    topic_lower = topic.lower()
    filtered_jokes = [j for j in JOKES if j["topic"] == topic_lower]
    
    if not filtered_jokes:
        return f"Sorry, I don't have any jokes about '{topic}'. Try: general, python, java, javascript, css, database."
    
    joke = random.choice(filtered_jokes)
    return joke["joke"]

def main():
    """Main entry point to run the server."""
    # Run the server using stdio
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
