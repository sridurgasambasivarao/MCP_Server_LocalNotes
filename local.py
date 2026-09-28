# Let's say if you're chatting with an LLM and you find something that's very 
# important, you want to be able to tell the LLM, summarize this into notes and 
# add it to my local notes, so maybe I can refer to it later. Also llm should be 
# able to read from those notes. So the whole point of this MCP server is to 
# provide a gateway for an LLM to interact with notes.txt, which is a file that is 
# on your local machine.

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes") 

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.
    Args:
        content: The text content to append.
    """

    filename = 'notes.txt'

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Content appended to {filename}."
    except Exception as e:
        return f"Error appending to file {filename}: {e}"
    

@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the contents of the user's local notes.
    """
    filename = 'notes.txt'

    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found."
    except FileNotFoundError:
        return "No notes file found."
    except Exception as e:
        return f"Error reading file {filename}: {e}"

def main():
    mcp.run()

# It ensures your server starts only when you run the script directly, 
# and not when another file imports it as a module    
if __name__ == "__main__": 
    main()