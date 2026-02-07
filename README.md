# 📊 Restaurant Analytics Dashboard (Flask + Docker)

A simple Flask web application that analyzes a real restaurant CSV dataset and displays interactive charts and tables using Pandas and Plotly.
The project is fully Dockerized, so it runs the same on any machine without setup issues.

##### 🔧 Technologies Used

- Python

- Flask

- Pandas

- Plotly

- Docker

##### 📁 Project Overview

1. Reads a real CSV dataset (no dummy data)

1. Shows restaurant insights like:

1. City-wise restaurant count

1. Average ratings by city

1. Popular cuisines

1. Top-rated restaurants

1. Multi-page web dashboard

1. Runs inside a Docker container

##### 🐳 What does “Dockerized” mean?

- This project is packaged inside a Docker container, which includes:

1. Python runtime

1. Required libraries

1. Application code

###### So users do not need to install Python or dependencies manually.

▶️ How to Run on Any Machine (Using Docker)
1️⃣ Install Docker

###### Download and install Docker Desktop:

https://www.docker.com/products/docker-desktop

2️⃣ Clone the Repository
git clone https://github.com/USERNAME/flask-ecommerce-dashboard.git
cd flask-ecommerce-dashboard

3️⃣ Build Docker Image
docker build -t restaurant-dashboard .

4️⃣ Run the Application
docker run -p 5000:5000 restaurant-dashboard

5️⃣ Open in Browser
http://localhost:5000

###### 📌 Notes

- Dataset is read directly from the CSV file

- No hardcoded or sample values

- Works on Windows, macOS, and Linux

###### ✅ Use Cases

1. Data analytics learning project

1. Flask dashboard example

1. Docker deployment demo

1. Academic or portfolio project