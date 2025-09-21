# AI Notes Summarizer 📝

This project is an AI-powered web application designed to condense long academic notes, articles, or any text document into concise, key-point summaries. It leverages Google's powerful Gemini model to provide accurate, context-aware summarizations through a clean and simple user interface built with Streamlit.



## ✨ Key Features

-   **Direct Text Summarization**: Paste any amount of text directly into the app for a quick summary.
-   **PDF File Upload**: Upload PDF documents to extract and summarize their content seamlessly.
-   **High-Quality Summaries**: Utilizes the `gemini-1.5-flash-latest` model for fast and contextually accurate summaries.
-   **User-Friendly Interface**: A simple and intuitive web app built with Streamlit, requiring no installation for end-users.

## 🛠️ Technologies Used

-   **Backend**: Python
-   **Frontend**: Streamlit
-   **AI Model**: Google Gemini API (`google-generativeai`)
-   **PDF Parsing**: PyPDF2
-   **Environment Management**: python-dotenv

## 🚀 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-notes-summarizer.git](https://github.com/your-username/ai-notes-summarizer.git)
    cd ai-notes-summarizer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    -   Create a file named `.env` in the root of the project folder.
    -   Add your Google Gemini API key to the file as shown below:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser at `http://localhost:8501`.

## Usage

1.  Launch the application using the command above.
2.  Either paste your text into the text area or use the file uploader to select a PDF document.
3.  Click the "Summarize" button.
4.  The generated summary will appear below the button.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
