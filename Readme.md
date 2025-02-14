# Excel to Firebase Data Ingestion and API Project

## Overview

This project demonstrates a complete full-stack solution for data ingestion, storage, API development, and frontend display. The project extracts data from an Excel file using Python (with the pandas library), stores the data in a Firebase Realtime Database, and exposes a FastAPI endpoint to retrieve the data. A simple frontend built with HTML, CSS, and JavaScript dynamically fetches and displays the data in a table.

## Features

- **Data Ingestion:**  
  Extracts data from an Excel sheet and converts it into JSON format.
  
- **Firebase Integration:**  
  Stores the extracted data in a Firebase Realtime Database.
  
- **API Development:**  
  Provides a FastAPI backend with an endpoint (`/get-data`) to retrieve the stored data. The API supports CORS for cross-origin requests.
  
- **Frontend Application:**  
  A responsive web interface that uses HTML, CSS, and JavaScript to fetch data from the API and display it in a dynamic table.
  
- **Documentation:**  
  Comprehensive documentation with setup instructions, architecture, and screenshots is provided.

## Technology Stack

- **Backend:** Python, FastAPI, Uvicorn, Pandas, Firebase Admin SDK
- **Database:** Firebase Realtime Database
- **Frontend:** HTML, CSS, JavaScript
- **Tools:** VS Code, Git, Live Server (VS Code extension)
