# 🚀 AI Learning Path Generator

## 📖 Description
An AI-powered web application that generates personalized learning roadmaps based on a user's learning goal. The application uses Google's Gemini AI model to create structured learning paths, helping users progress from beginner to advanced levels efficiently.

## 📌 Features

- Generate personalized learning paths
- Beginner, Intermediate, and Advanced topics
- Recommended hands-on projects
- Estimated learning timeline
- Clean and interactive Streamlit interface
- Powered by Google Gemini AI

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini AI (Gemini API)
- Requests Library

## 📂 Project Structure

```text
AI-Learning-Path-Generator/
│
├── app.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── project_structure.png
│   ├── user_input.png
│   └── generated_result.png
│
└── .streamlit/
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/ellurunandini80-prog/AI-Learning-Path-Generator.git
```

2. Navigate to the project folder

```bash
cd AI-Learning-Path-Generator
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure your Gemini API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY="your_api_key_here"
```

5. Run the application

```bash
streamlit run app.py
```

## 📸 Screenshots

### Project Structure

![Project Structure](screenshots/project_structure.png)

### User Input

![User Input](screenshots/user_input.png)

### Generated Learning Path

![Generated Learning Path](screenshots/generated_result.png)

## 🎯 Example Use Cases

- Python Developer Roadmap
- Data Science Learning Path
- Machine Learning Engineer Path
- Web Development Roadmap
- Cloud Computing Learning Path

## 🔒 Security

API keys and sensitive credentials are excluded from version control using `.gitignore`.


## ⭐ Acknowledgements

- Google Gemini AI
- Streamlit
- NxtWave