import instaloader
from collections import Counter

# Stopwords (common words that are not relevant for the analysis)
STOPWORDS = {"example1", "example2", "example3"}
consoleUpdates = 20  # Print progress every 20 comments
top10Updates = 200  # Print top 10 words every 200 comments

# Shortcode of the post to be analyzed
# Example: "https://www.instagram.com/p/ABC123DEF/" -> SHORTCODE = "ABC123DEF"
SHORTCODE = "ABC123DEF"

# Initializing Instaloader and session
L = instaloader.Instaloader()
# needs configuration with instaloader --login=your_username
L.load_session_from_file("your_username")  

# Get post
post = instaloader.Post.from_shortcode(L.context, SHORTCODE)

word_count = Counter()
total_comments = post.comments 
comment_count = 0 # Current comment count

def printTopTen():
    i = 1
    print(f"\nCurrent Top 10 after {comment_count} comments:")
    for word, count in word_count.most_common(10):
        print(f"{i}. \"{word}\" - {count}x")
        i+=1
    print("\n")

print(f"Start scanning comments of Post {SHORTCODE}...")

for comment in post.get_comments():
    # Print progress every 20 comments
    if comment_count % consoleUpdates == 0 and comment_count != 0:
        print(f"Scanning comments... {comment_count} / {total_comments}")  
    # Print top 10 words every 200 comments
    if(comment_count % top10Updates == 0 and comment_count != 0):
        printTopTen()
    
    comment_count += 1
    words = comment.text.lower().split()  # Split text into individual words
    filtered_words = [word for word in words if word not in STOPWORDS]  # Remove stopwords
    word_count.update(filtered_words)  # Add words to statistics

# Print final progress update
print(f"Scanning comments... {comment_count} / {total_comments}")  
print(f"\nTotal number of scanned comments: {comment_count}")

# Print the top 100 most frequently occurring words excluding stopwords
print("\nTop 100 of the most frequently occurring terms/artists names:")
i = 1
for word, count in word_count.most_common(100):
    print(f"{i}. \"{word}\" - {count}x")
    i+=1
print("\nScanning complete")
