# Instagram Comment Counter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Instaloader](https://img.shields.io/badge/Instaloader-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview

Instagram Comment Counter is a Python script that analyzes the comments of a specific Instagram post and determines the 100 most frequently used words. It uses the `instaloader` library to fetch comments and filters out common stopwords to provide meaningful insights.

## Features

- Extracts comments from a given Instagram post.
- Filters out common stopwords to improve word frequency analysis.
- Displays real-time progress during comment scanning.
- Outputs the top 100 most frequently occurring words.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.9+
- InstaLoader 
- An active Instagram session (saved via `instaloader`)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/flixcoo/instagramCommentCounter.git
   cd instagramCommentCounter
   ```

2. Install the required dependencies:

pip3 install instaloader

3. Log in to your Instagram account and save the session:

```instaloader --login=your_username```

## Usage

Run the script by replace the example shortcode with the shortcode of the Instagram post you want to analyze and replace `your_username` with your instagram username added to instaloader.

Run the script with `python main.py`

## Example Output

```
Start scanning comments of Post EXAMPLE...
Scanning comments... 10 / 500
Scanning comments... 20 / 500
Scanning comments... 30 / 500
Current Top 10 after 200 comments:
1. "amazing" - 34x
2. "great" - 30x
3. "love" - 28x
...
Scanning complete
```

## License

This project is licensed under the MIT License.

## Author

Created by flixcoo - (GitHub Profile)[https://github.com/flixcoo]