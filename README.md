# API-ETL-Script
# API ETL Project

## 📌 Objective

This project extracts data from a public API and saves it into a CSV file.

I have used the JSONPlaceholder API to fetch sample post data and store it locally.

---

## 🔧 Tools Used

* Python
* requests library
* csv module

---

## 🌐 API Used

JSONPlaceholder (Fake REST API for testing)
https://jsonplaceholder.typicode.com/posts

---

## ⚙️ How It Works

1. The script sends a request to the API
2. It receives data in JSON format
3. Since the API does not support pagination, I manually divided the data into pages
4. The data is processed in chunks (10 records per page)
5. Finally, the data is saved into a CSV file

---

## ▶️ How to Run

1. Install required library:
   pip install requests

2. Run the script:
   python etl_script.py

---

## 📁 Output

* A file named `posts.csv` will be created
* It contains the following columns:

  * userId
  * id
  * title
  * body

---

## ⚠️ Note

JSONPlaceholder API does not provide pagination, so pagination is simulated in the script.

---

## ✅ Conclusion

This project demonstrates a simple ETL process:

* Extract data from API
* Transform it into structured format
* Load it into a CSV file
