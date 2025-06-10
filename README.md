# 🏋️‍♂️ Workout Tracker

A smart workout tracker that lets you log workouts using **natural language queries** and automatically updates the data to **Google Sheets**.

## 🔥 Features

- 🧠 Log workouts using simple phrases like “Ran 5 km in 25 minutes”
- 📊 Automatically adds entries to Google Sheets
- 📅 Tracks date, time, duration, and calories burned
- 📱 Easy-to-use and beginner-friendly
- 💡 Built using Python and external APIs

## 🛠 Tech Stack

- **Python**
- **Sheety API** (for interacting with Google Sheets)
- **Nutritionix API** (for parsing natural language queries)
- **Requests** (HTTP requests to APIs)

## 🚀 How It Works

1. You type something like:  
   `"Did 30 minutes of yoga"`  
   or  
   `"Cycled 10 km"`

2. The app sends the data to Nutritionix API to extract exercise details.

3. The processed data is sent to Sheety, which logs it into your Google Sheet.
