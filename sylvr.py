from collections import OrderedDict

# Full Dataset
dataset = {
  "clients": [
    {
      "client_id": "C001",
      "client_name": "John Doe",
      "2020": {
        "account_balance": 5000.75,
        "transactions": [
          {"transaction_id": "T001", "date": "2020-01-10", "amount": -200.50, "description": "Groceries"},
          {"transaction_id": "T002", "date": "2020-03-15", "amount": 1500.00, "description": "Salary"}
        ]
      },
      "2021": {
        "account_balance": 8000.25,
        "transactions": [
          {"transaction_id": "T003", "date": "2021-02-20", "amount": -100.75, "description": "Fuel"},
          {"transaction_id": "T004", "date": "2021-05-05", "amount": 2000.00, "description": "Freelance Income"}
        ]
      }
    },
    {
      "client_id": "C002",
      "client_name": "Alice Smith",
      "2020": {
        "account_balance": 3000.50,
        "transactions": [
          {"transaction_id": "T011", "date": "2020-02-10", "amount": -300.00, "description": "Rent"},
          {"transaction_id": "T012", "date": "2020-04-18", "amount": 1200.00, "description": "Salary"}
        ]
      },
      "2021": {
        "account_balance": 4000.80,
        "transactions": [
          {"transaction_id": "T013", "date": "2021-03-22", "amount": -250.50, "description": "Utilities"},
          {"transaction_id": "T014", "date": "2021-08-13", "amount": 1500.00, "description": "Freelance Income"}
        ]
      }
    }
  ]
}

# LRU Cache Class
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str):
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]
        return None

    def put(self, key: str, value: str):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used item
        self.cache[key] = value

# Query Handler
def query_handler(query: str):
    if "health data" in query.lower():
        response = []
        for client in dataset["clients"]:
            response.append(f"{client['client_name']} - 2020 Balance: ${client['2020']['account_balance']}")
        return " | ".join(response)
    elif "average transaction" in query.lower():
        total_amount = count = 0
        for client in dataset["clients"]:
            for year in client:
                if isinstance(client[year], dict) and "transactions" in client[year]:
                    for transaction in client[year]["transactions"]:
                        total_amount += abs(transaction["amount"])
                        count += 1
        average = total_amount / count if count > 0 else 0
        return f"Average transaction amount: ${average:.2f}"
    else:
        return "No data available for this query."

# Main Function
def main():
    cache = LRUCache(capacity=3)
    
    queries = [
        "What are the client reports for health data?",
        "Give the average transaction amount on different types of transactions.",
        "What are the client reports for health data?",  # Cached result
        "Show transaction details for 2022."  # New query that may cause eviction
    ]
    
    for query in queries:
        cached_response = cache.get(query)
        if cached_response:
            print(f"Cache Hit: {cached_response}")
        else:
            response = query_handler(query)
            cache.put(query, response)
            print(f"Cache Miss: {response}")

# Execute the main function
if __name__ == "__main__":
    main()
