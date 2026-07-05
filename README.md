⚡SelfSync | Your AI-Powered DisciplineOS

SelfSync is a premium digital wellness and productivity dashboard. Generic habit trackers are too soft; SelfSync features an integrated **AI Accountability Coach** that provides brutal, encouraging reality checks based on your actual data.

### 🔗 [Experience the Live Application Here]
 [(https://selfsync-mn3ehbsrduk4k62wakdtgo.streamlit.app/)]

🚀 The Problem & The Solution

The Problem:Most habit trackers just give you a digital gold star. They don't analyze your contradictions (e.g., "Why did you log 6 hours of screen time but claim high productivity?"), and they don't hold you accountable when you slip.

The Solution: SelfSync combines a gamified Discipline Score, seamless daily logging, and a highly analytical Gemini-powered AI Coach to predict burnout, enforce habits, and show you exactly where your current trajectory is taking you.

✨ Core Features

*   Premium Glassmorphism UI: A custom dark-mode aesthetic featuring "Antigravity" hover animations and transparent, gridless charts that completely bypass native Streamlit styling.
*   AI Accountability Coach: Powered by `gemini-2.5-flash`, the coach analyzes your SQLite daily logs to call out BS and provide exact, single-action habit challenges.
*   "Future You" Prediction: AI analyzes your 7-day rolling data (sleep, screen time, mood) to generate a realistic projection of where you will be in 6 months.
*   Daily Activity Tracker: Seamless logging for sleep, screen time, mood, and productivity, powered by robust database UPSERTs.
*   Deep Analytics: Interactive, hover-enabled sparklines built with Plotly Express to visualize your Discipline Score over time.

---

# 🏗️ Architecture & Tech Stack

SelfSync is engineered for speed, modularity, and a premium UX, overcoming the standard limitations of our tech stack:

   Frontend / Routing: Streamlit. We bypassed Streamlit's native multipage folder structure, building a custom callback-driven router using `st.session_state` to prevent infinite reload loops and enable seamless authentication flows.
   UI / Design System: Custom HTML/CSS. We injected custom CSS to hide native Streamlit headers, implement backdrop-filter blur (glassmorphism), and style metrics.
  Database: Local SQLite3. Engineered with WAL (Write-Ahead Logging)** mode to handle concurrent reads/writes without database locks, making it robust for future leaderboard scaling.
  AI Engine: Google Gemini API (`google-genai` SDK).
  Data Wrangling & Visuals: Pandas & Plotly Express.

---

## 💻 Local Quick Start

Want to run the DisciplineOS locally? Follow these steps:

*1. Clone the repository*
```bash
git clone [https://github.com/Shashank-240/SelfSync.git](https://github.com/Shashank-240/SelfSync.git)
cd SelfSync

📦 SelfSync
 ┣ 📜 app.py          # Main entry point, state management, and page router
 ┣ 📜 database.py     # SQLite schema, WAL mode config, and CRUD/UPSERT logic
 ┣ 📜 visuals.py      # Design system: Glassmorphism CSS, custom metrics, Plotly wrappers
 ┣ 📜 ai_logic.py     # Gemini SDK integration and prompt engineering for the AI Coach
 ┗ 📜 requirements.txt
