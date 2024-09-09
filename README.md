# News Summarizer Web Application

## Overview
This project is a web application that summarizes news articles from any given URL. The web app scrapes the news content, summarizes it using `gensim`, and extracts the key points or keywords. The user can input a URL, and the app will display a concise summary and the most relevant keywords.

## Features
- **Web Scraping**: Extracts content from any news website using BeautifulSoup.
- **Summarization**: Summarizes the content using `gensim`'s text summarization.
- **Keyword Extraction**: Extracts keywords from the content.
- **Simple User Interface**: Allows users to input a news URL and receive a summary.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Web Scraping**: `requests`, `BeautifulSoup`
- **Summarization**: `gensim`

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Flask
- Requests
- BeautifulSoup
- Gensim

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Pabitra3/News-Summarizer.git
   cd News-Summarizer
   ```

2. **Set Up a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install flask requests beautifulsoup4 gensim lxml
   ```

## Usage
1. **Run the Flask Application**
   Start the Flask server by running:
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000/`.

2. **Access the Web Application**
   Open your web browser and go to `http://127.0.0.1:5000/`. You will see a form where you can input:
   - A news article URL from any website.

3. **Get the Summary**
   After entering the URL, click "Summarize" to see the title, a summarized version of the article, and a list of keywords extracted from the content.

## Code Structure
- `app.py`: The Flask backend that handles the form submission, scraping, summarization, and keyword extraction.
- `templates/index.html`: The HTML form where users input the news URL.
- `templates/result.html`: Displays the summary and keywords after processing.
- `static/`: (Optional) Place for any static files like CSS or JavaScript (currently not used).

## Project Flow
1. User submits a news article URL in the frontend form.
2. The Flask backend scrapes the article using BeautifulSoup and requests.
3. The content is summarized using `gensim`.
4. Keywords are extracted using `gensim`.
5. The result (summary and keywords) is sent back to the frontend and displayed.

## Example
1. **Input**: A URL to a news article, such as `https://www.vox.com/plink`.
2. **Output**:
   - **Title**: The title of the article.
   - **Summary**: A concise version of the article.
   - **Keywords**: Relevant keywords from the article.

## Troubleshooting
- **Invalid URL**: Ensure the URL is from a valid news website and contains readable text. Not all websites may be supported depending on their HTML structure.
- **Server Crashing**: Check the logs for any errors. Ensure you have installed all required libraries correctly.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure to follow the coding standards and include tests if applicable.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, please contact developersivaay@gmail.com.