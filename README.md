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


The error message indicates that your code is using an older method to access the OpenAI API that is no longer supported in the version of the openai library you have installed. This is a common issue when APIs are updated to new versions, leading to changes in how functions and methods should be called.


## Examples of Data Collected, Analysis Performed, and Messages Generated

Here are detailed examples illustrating the process from data collection through sentiment analysis to message generation:

### Example 1: Curiosity About Clinical Trials

- **Post Title:** "Curious About Clinical Trials"
- **Post Content:** "I've heard clinical trials can be beneficial but risky. Can anyone share more information?"
- **Sentiment Analysis:**
  - **Polarity:** 0.15 (slightly positive)
  - **Subjectivity:** 0.45 (moderately subjective)
- **Generated Message:** "It's great to hear you're interested in clinical trials! While there are risks, the benefits such as access to new treatments and contributing to medical research can be significant. It's important to consult with healthcare professionals and thoroughly understand the consent forms."

### Example 2: Skepticism Toward Clinical Trials

- **Post Title:** "Doubts About Clinical Trials"
- **Post Content:** "Aren't clinical trials just a way for companies to use people as guinea pigs?"
- **Sentiment Analysis:**
  - **Polarity:** -0.4 (negative)
  - **Subjectivity:** 0.6 (subjective)
- **Generated Message:** "It's understandable to have concerns about clinical trials. It's important to know that ethical standards and regulations are in place to protect participants. Trials provide essential data that can lead to advancements in medicine and treatments. Always make informed decisions based on thorough research."

### Example 3: Neutral Inquiry About Clinical Trials

- **Post Title:** "General Information on Clinical Trials"
- **Post Content:** "What are the basic requirements to participate in a clinical trial? Who can join?"
- **Sentiment Analysis:**
  - **Polarity:** 0.0 (neutral)
  - **Subjectivity:** 0.0 (objective)
- **Generated Message:** "Participation in clinical trials typically requires meeting specific eligibility criteria, which vary widely depending on the study's goals. These can include age, medical history, and current health status. To find out if you are eligible for any specific trials, consider consulting with medical professionals or visiting clinical trial informational websites."

### Example 4: Positive Feedback on Clinical Trials

- **Post Title:** "Positive Experience with Clinical Trials"
- **Post Content:** "I had a positive experience participating in a clinical trial last year. It was well-organized and informative."
- **Sentiment Analysis:**
  - **Polarity:** 0.6 (positive)
  - **Subjectivity:** 0.5 (moderately subjective)
- **Generated Message:** "That's wonderful to hear! Your positive experience can inspire others who might be considering participating in clinical trials. Sharing such experiences helps demystify the process and highlight the benefits of contributing to medical research. Thank you for sharing!"

### Example 5: Concerns About Clinical Trial Outcomes

- **Post Title:** "Concerned About Trial Outcomes"
- **Post Content:** "I'm interested in joining a trial but worried about the side effects and long-term impacts. Any advice?"
- **Sentiment Analysis:**
  - **Polarity:** -0.1 (slightly negative)
  - **Subjectivity:** 0.7 (highly subjective)
- **Generated Message:** "It's crucial to consider both potential benefits and risks when thinking about joining a clinical trial. Discussing your concerns with healthcare providers and researchers can provide clarity and help you make an informed decision. Ensuring you understand all aspects of the trial, including potential side effects, is key."



## Ethical Considerations

In this project, I ensured to:
- Respect user privacy by not storing personal data or sensitive information.
- Maintain transparency about the AI's involvement in message generation.
- Monitor and mitigate any biases in the AI-generated content to ensure fairness.



Despite the setbacks faced due to the unexpected OpenAI API update, I am committed to mastering the new API features and completing the integration for message generation. I am confident that with a bit more time, I can overcome these hurdles and fully implement the sophisticated functionalities that the OpenAI API offers, thereby enhancing the effectiveness of this task.



