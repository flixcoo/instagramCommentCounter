# 📊 Instagram Comment Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Instaloader](https://img.shields.io/badge/Instaloader-4.9.2-FF69B4)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

🔍 Extract meaningful insights from Instagram post comments by analyzing word frequency patterns.

## 🌟 Features

- ⚡ **Fast comment extraction** using Instaloader
- 🧹 **Smart filtering** of stopwords and common phrases
- 📈 **Real-time progress tracking** during analysis
- 🏆 **Top 100 ranking** of most frequent words

## 🛠️ Prerequisites

- Python 3.9+
- Instaloader 4.9.2+
- Active Instagram account

## 🚀 Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/flixcoo/instagramCommentCounter.git
cd instagramCommentCounter
```

2. Install dependencies:
   
```bash
pip install -r requirements.txt
```
   
3. Authenticate with Instagram:

```bash
instaloader --login=your_username
```
   
## 💻 Usage

Basic command:

```bash
python main.py --post SHORTCODE --username YOUR_USERNAME
```

Example:

```bash
python main.py --post Cj7JQ --username instagram_analyst
```

## 📊 Sample Output

```bash
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
## 📜 License

MIT License © 2023 flixcoo
