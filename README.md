# Social Media Marketing

## Overview
The Social Media Marketing repository contains scripts and notebooks aimed at analyzing social media data, particularly focusing on extracting and processing data from Reddit using the PRAW (Python Reddit API Wrapper) library. The primary goal is to understand user engagement, identify influencers, and generate insights from social media interactions.

## Features
- **Data Extraction:** Scripts to extract posts and comments from Reddit based on specific keywords.
- **Data Processing:** Functions to clean and preprocess textual data for analysis.
- **Network Analysis:** Creation of network graphs to visualize interactions between users.
- **Topic Modeling:** Application of LDA (Latent Dirichlet Allocation) for topic modeling on extracted data.
- **Clustering:** K-means clustering to identify groups of similar users or posts.
- **Visualization:** Generation of word clouds and dendrograms to visualize text data and hierarchical clustering.

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Node.js (for dependency management if needed)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ap539813/Social-Media-Marketing
    cd Social-Media-Marketing
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration
1. Set up Reddit credentials by creating a `reddit_secrets.json` file with the following structure:
    ```json
    {
        "client_id": "your_client_id",
        "client_secret": "your_client_secret",
        "user_agent": "your_user_agent"
    }
    ```

## File Structure
- **data_extractor.py:** Script to extract data from Reddit using PRAW and save it to a JSON file.
- **dev.ipynb:** Jupyter Notebook for developing and testing data extraction and processing methods.
- **final_analysis_on_disneyland.ipynb:** Notebook containing the final analysis and insights on the Disneyland dataset.
- **requirements.txt:** List of Python dependencies needed to run the scripts.

## Running the Scripts
1. To extract data from Reddit:
    ```sh
    python data_extractor.py
    ```
   This will save the extracted data to a file named `reddit_data_lego.json`.

2. Open and run Jupyter notebooks:
    ```sh
    jupyter notebook dev.ipynb
    ```

## Usage
### Data Extraction
- **Extract Posts:** The `data_extractor.py` script extracts posts from a specified subreddit and saves them along with comments to a JSON file.

### Data Processing
- **Preprocess Text:** Functions in the notebooks handle text cleaning, tokenization, and lemmatization.
- **Network Analysis:** Create graphs to visualize user interactions and identify key influencers.

### Clustering and Topic Modeling
- **K-means Clustering:** Group users or posts into clusters based on textual features and interaction patterns.
- **LDA Topic Modeling:** Identify main topics discussed in the posts and comments.

## Dependencies
- praw
- networkx
- plotly
- nbformat
- wordcloud
- gensim

Check `requirements.txt` for the full list of dependencies.

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.
