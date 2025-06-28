import wikipedia

class GenAILLM:
    def query(self, message):
        try:
            # Search Wikipedia for the given query
            results = wikipedia.search(message)
            if not results:
                return "I couldn't find anything relevant on Wikipedia."
            
            # Get the summary of the first search result
            summary = wikipedia.summary(results[0], sentences=3)
            return summary
        
        except wikipedia.exceptions.DisambiguationError as e:
            # If too many options for the same term
            return f"The query is ambiguous. Did you mean one of these? {e.options[:5]}"
        
        except wikipedia.exceptions.PageError:
            return "The page doesn't exist on Wikipedia."
        
        except Exception as e:
            return f"An error occurred: {str(e)}"
