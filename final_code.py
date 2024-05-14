import praw
import os
from textblob import TextBlob
from openai import OpenAI


# Configure Reddit API
reddit = praw.Reddit(
    client_id='sNQgp0yBhYnoHQf9hd-vlw',
    client_secret='_xphL5CzsiZhk9h-igOcnNlei6NawA',
    user_agent='clinical trial related subreddits',
   
)

def fetch_posts(subreddit_name, limit=10):
    """ Fetches posts from a subreddit. """
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=limit):
        post_details = {
            "title": post.title,
            "text": post.selftext,
            "id": post.id,
            "url": post.url
        }
        posts.append(post_details)
    return posts

def fetch_comments(post_id):
    """ Fetches comments from a specific post. """
    post = reddit.submission(id=post_id)
    post.comments.replace_more(limit=0)
    comments = []
    for comment in post.comments.list():
        comments.append({
            "comment_id": comment.id,
            "comment_body": comment.body
        })
    return comments

def analyze_sentiment(text):
    """ Return the polarity and subjectivity of the text. """
    testimonial = TextBlob(text)
    return testimonial.sentiment

# Initialize the OpenAI client with environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_message(client, polarity):
    """Generates personalized messages based on sentiment polarity using the provided OpenAI client."""
    if polarity > 0.1:
        context = "The user is positive about clinical trials and might be interested in participating."
    elif polarity < -0.1:
        context = "The user is skeptical about clinical trials. They need reassurance about the benefits and safety."
    else:
        context = "The user is neutral about clinical trials. They might need more information to decide."

    response = client.chat.completions.create(
    model='gpt-3.5-turbo',  # Your specified model
    messages=[{"role": "user", "content": f"Compose a professional message aimed at the willingness of the user for clinical trial recruitment: {context}"}],
    max_tokens=150,
    temperature=0.7
)
    return response.choices[0].message.content.strip()

# Main execution loop
subreddits = ['clinicaltrials', 'clinicaltrialsunit', 'ClinicalGenetics']
all_posts = []

for subreddit_name in subreddits:
    print(f"\nFetching posts from r/{subreddit_name}")
    posts = fetch_posts(subreddit_name, limit=10)
    all_posts.extend(posts)

for post in all_posts:
    print(f"\nTitle:\n {post['title']}")
    #print(f"URL: {post['url']}")
    print(f"Post Content: {post['text']}")

    comments = fetch_comments(post['id'])
    for comment in comments:
        print(f"\nComment: {comment['comment_body']}")

    sentiment = analyze_sentiment(post['text'])
    print(f"\nSentiment Analysis -\n Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

    # message = generate_message(client, sentiment.polarity)
    # print(f"\nGenerated Message:\n {message}\n")


for post in all_posts:
    comments = fetch_comments(post['id'])
    for comment in comments:
        
         message = generate_message(client, sentiment.polarity)
         print(f"\nGenerated Message:\n {message}\n")
