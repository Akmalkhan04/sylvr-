from collections import OrderedDict
import time
import random

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str):
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]
        return None

    def put(self, key: str, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used item
        self.cache[key] = value

# Mock AI Processing Function
def process_query(query: str):
    print(f"Processing query: {query}")
    time.sleep(random.uniform(0.5, 1.5))  # Simulate processing delay
    return f"Response for '{query}'"

# AI Agent with LRU Caching
def ai_agent():
    cache_size = 3  # Set cache capacity
    lru_cache = LRUCache(cache_size)
    
    queries = [
        "What are the client reports for health data?",
        "Give the average transaction amount for different types of transactions.",
        "How many users visited our site last month?",
        "What is the revenue for Q4?",
        "What are the client reports for health data?"  # Repeated query
    ]
    
    for query in queries:
        cached_response = lru_cache.get(query)
        
        if cached_response:
            print(f"Cache Hit: {cached_response}")
        else:
            response = process_query(query)
            lru_cache.put(query, response)
            print(f"Cache Miss: Stored {response}")

if __name__ == "__main__":
    ai_agent()
