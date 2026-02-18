def calculate_metrics(data):
    """
    A sample function to demonstrate code retrieval.
    """
    if not data:
        return 0
    return sum(data) / len(data)

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_metrics(sample_data)
    print(f"The average metric is: {result}")