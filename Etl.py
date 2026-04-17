# import requests
# import csv

# API_URL = "https://jsonplaceholder.typicode.com/posts"


# def fetch_data():
#     try:
#         response = requests.get(API_URL)

#         if response.status_code != 200:
#             print("Error fetching data")
#             return []

#         data = response.json()

#         # Simulate pagination (10 records per page)
#         page_size = 10
#         all_data = []

#         for i in range(0, len(data), page_size):
#             page = data[i:i + page_size]
#             print(f"Processing page {i // page_size + 1}")
#             all_data.extend(page)

#         return all_data

#     except Exception as e:
#         print("Error:", e)
#         return []


# def save_to_csv(posts):
#     with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)

#         # Header
#         writer.writerow(["userId", "id", "title", "body"])

#         # Data rows
#         for post in posts:
#             writer.writerow([
#                 post["userId"],
#                 post["id"],
#                 post["title"],
#                 post["body"]
#             ])


# def main():
#     print("Fetching data...")
#     posts = fetch_data()

#     if posts:
#         save_to_csv(posts)
#         print("✅ Data saved to posts.csv")
#     else:
#         print("❌ No data found")


# if __name__ == "__main__":
#     main()

import requests
import csv

print("Starting program...")

# API link
url = "https://jsonplaceholder.typicode.com/posts"

# get data from API
response = requests.get(url)

# check if request worked
if response.status_code == 200:
    print("Data fetched successfully")
    
    data = response.json()

    # simulate pagination (10 items per page)
    page_size = 10
    all_data = []

    for i in range(0, len(data), page_size):
        print("Processing page", (i // page_size) + 1)
        page = data[i:i+page_size]
        all_data = all_data + page   # simple way instead of extend

    # save to csv
    file = open("posts.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)

    # header
    writer.writerow(["userId", "id", "title", "body"])

    # data
    for item in all_data:
        writer.writerow([
            item["userId"],
            item["id"],
            item["title"],
            item["body"]
        ])

    file.close()

    print("Data saved in posts.csv")

else:
    print("Failed to fetch data")