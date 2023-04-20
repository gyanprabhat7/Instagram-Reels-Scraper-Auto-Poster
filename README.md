# Instagram-Reels-Scraper-Auto-Poster
Instagram-Reels-Scraper-Auto-Poster is a handy GitHub repository that scrapes reels from specified Instagram accounts and automatically posts them to your account. Stay updated with the latest content from your favorite creators and effortlessly share it with your followers. Automate your Instagram game and grow your account with Reels-AutoPoster!

## Getting Started

Before you start using Reels-AutoPoster, you need to set your configuration variables in the `config.py` file.

### Prerequisites

- Python 3.x
- A valid Instagram account

### Installation

1. Clone the repository:

```
git clone https://github.com/your_username/Reels-AutoPoster.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

### Configuration

In `config.py`, you need to set the following variables:

- `INSTA_USERNAME`: Your Instagram username
- `INSTA_PASSWORD`: Your Instagram password
- `ACCOUNTS_TO_SCRAPE`: An array of Instagram accounts from which you want to scrape reels
- `FETCH_LIMIT`: The number of reels you want to fetch from each account
- `HASHTAGS`: The hashtags you want to add while reposting the reels

Example:

```python
FETCH_LIMIT=10
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"

ACCOUNTS = [
    "account1",
    "account2",
    "account3"
]
HASHTAGS = "#reels #reelsinstagram #reelitfeelit"
```

## Usage

### Scraping Reels

To scrape reels from the specified accounts in `config.py`, run the following command:

```
py index.py
```

This will scrape the reels and store the downloaded reels in the `downloads` folder.

### Posting Reels

To post the scraped reels to your Instagram account, run the following command:

```
py poster.py
```

This will post the reels every 15 minutes.

## Contributing

If you want to contribute to this project, feel free to submit pull requests or open issues with your suggestions and ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to all the developers who contributed to the libraries used in this project.

