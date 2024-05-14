# turmerik_ml
Sentiment Analysis and Personalized Messaging for Clinical Trial Recruitment

## Description

This project demonstrates how to scrape Reddit posts from specific subreddits, perform sentiment analysis on the content, and generate personalized messages using the OpenAI API. The goal is to explore potential user engagement for clinical trial recruitment based on their expressed sentiments on Reddit.

## Steps performed

To set up and run this project, 

- First I installed the required packages
- I used the PRAW (Python Reddit API Wrapper) to fetch posts from subreddits related to clinical trials. 
- used three subreddits- clinicaltrials', 'clinicaltrialsunit' and 'ClinicalGenetics'
- for sentiment analysis, I used TextBlob. It extracted polarity and subjectivity from the post content to gauge the general sentiment towards clinical trials.
- For generating personalized messages, I integrated the OpenAI API.

## Challenges faced
The major challenge was the OpenAI API integration. The API received a major update during the development phase, which included a complete rewrite of the library. This update introduced changes in the way the API is instantiated and utilized, differing substantially from the previous version.


The error message indicated that my code was using an older method to access the OpenAI API that is no longer supported in the version of the openai library you have installed. This is a common issue when APIs are updated to new versions, leading to changes in how functions and methods should be called.


## Examples of Data Collected, Analysis Performed, and Messages Generated
*Please find the OUTPUT.md file in the repository
It has the post content and title, comments and the sentiment analysis.


## Ethical Considerations

In this project, I ensured to:
- Respect user privacy by not storing personal data or sensitive information.
- Maintain transparency about the AI's involvement in message generation.
- Monitor and mitigate any biases in the AI-generated content to ensure fairness.



Despite the setbacks faced due to the unexpected OpenAI API update, I am committed to mastering the new API features and completing the integration for message generation. I am confident that with a bit more time, I can overcome these hurdles and fully implement the sophisticated functionalities that the OpenAI API offers, thereby enhancing the effectiveness of this task.



