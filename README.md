# Vacuum Agent Simulator

**A professional animated Vacuum Agent simulator built with FastAPI and HTML/CSS/JS.**  

This project simulates a simple vacuum agent operating in a 2x2 room environment. The agent moves room-to-room, detects whether a room is dirty, cleans it if necessary, and visually updates the room’s status and color.  

---

## Features

- 2x2 Grid environment with **4 rooms** (2 dirty, 2 clean initially)  
- **Animated robot agent** moving smoothly inside each room  
- **Slow cleaning animation** with pulsing effect  
- Dynamic room color change when cleaned:  
  - Dirty → Red/Orange  
  - Clean → Green  
- Professional UI with **highlighted active room**  
- Simple **FastAPI backend** to simulate agent logic  
- Fully client-side visualization with **HTML/CSS/JS**  

---

## Technologies Used

- **Backend:** Python 3.10+, FastAPI  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Server:** Uvicorn  
- **Browser-based simulation**  

---

## Project Structure

agent_project/
├── main.py # FastAPI backend with agent logic
├── static/
│ └── index.html # Frontend UI for animated environment
├── venv/ # Python virtual environment
├── README.md # This README file
---

## Installation

1. **Clone the repository**  

```bash
git clone <repository-url>
cd agent_project

Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
# source venv/bin/activate # Linux/macOS
Install dependencies
pip install fastapi uvicorn

Ensure your static/index.html is present


Running the Project

Start the FastAPI server:

uvicorn main:app --reload


Open your browser and navigate to:

http://127.0.0.1:8000/ui


Click the “Run Agent” button to see the robot move and clean rooms.
