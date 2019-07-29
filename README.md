# Detecting Emotions

![media image](images/william-iven-SpVHcbuKi6E-unsplash.jpg)

I've created a model to help news media outlets classify headlines based on the emotions they convey so that they can select the right ones to keep readers interested in their content. 

Social media and microblogging platforms may also benefit from the use of such a tool in their efforts to identify fake news articles and hoaxes because highly provocative, emotional language is common feature among them (****citations). 

# Background

Headlines are designed to grab readers' attention so that they'll read articles and keep coming back for more content.

The most effective way to get our attention is to make us feel something: afraid, angry, surprised, delighted. When we experience emotions, we experience a cascade of automatic physiological and cognitive changes, and changes in the direction of our attention are chief among these (Brady). Typically, the more intense the emotion, the stronger these effects will be. 

As you might expect, researchers have found evidence of a relationship between high emotion content and social media sharing behaviors. Stieglitz and Dang-Xuan (2013) showed that people are more likely to share content that causes high phsyiologial arrousal, such as anger and amusement. Berger (2011) showed that news stories that elicit strongly negative emotions are quicker to turn viral than content that is emotionally neutral or positive.

This is a strong incentive for news media to rely on strongly negative headlines to increase sharing. 

However, there are good reasons to offer plenty of positive content as well. Positive content may not be as quick to turn viral, but Ferrara and Yang (2015) found that it has greater staying power in the long run. Positive stories get more interactions--shares, Facebook likes, and so forth--over time than negative stories. 

More importantly, *over*-relaince on negative content--especially negative content that is presented in eggagerated language--may erode readers' trust in your organization. 


(***citation on emotion and avoidance; citation on errosion of trust in the media***) 

In short, news and media providers have an interest in finding a balance of emotions on their front pages and personalized recommendations. I've developed a tool that makes it easier to know whether an appropriate balance has been achieved.

# The Data

For this project, I analyzed a set of 1250 headlines from the SemEval 2007 program affective task. 

The headlines were collected from a variety of news sources. For each headline, annotators assigned an intensity rating between 0 and 100 for six emotion categories: anger, disgust, fear, joy, sadness, and surprise. 0 indicates that the emotion is not present. 100 indicates that it is present in its max intensity. Annotators were instructed to assign ratings according to their first intuition about the emotional import of the headlines, taking into account both the emotion-evoking words in the text and the overall impact of the it (*citation*).

The dataset also came with a second set of labels with overall positive or negative valence ratings.

It's important to note that annotating emotions in text is a difficult task (Alm et al 2005). There is high context dependence in emotion communication (Strappavara ...) and annotators' personal histories and background beliefs may result in different reactions to a given subject matter. The same subject matter may be perceived as threatenening to one annotator, eliciting fear, antagonistic to another annotator, eliciting anger, and buffonish to another, eliciting disgust (Gaspar et al. 2016). We can be fairly confident in the reasonability of the labels in the dataset becuase they were labeled by six independent annotators. 

The headlines in the dataset have an average length of six words and a max of 15. The most common emotion (in any amount) is surprise and the most common maximum emotion rating is joy. Disgust is the least common, and also has the lowest average intensity.

(pics)

I checked the headlines for presence of emotion words from the WordNet emotion lexicon and the positive and negative words from the General Inquirer lexicon. Just over 100 of the headlines contained words from the emotion lexicon and just under half of the headlines contained words from the positive and negative words lexicon. Of the headlines with words appearing in the emotion lexicon, the emotion labels matched 85% of the time. However, there was little correspondence between the positive and negative words lexicon and the valence labels, which matched only 27% of the time.

I also looked at the most common words in the dataset and the most common word pairs and the most common words for each label. 

# Predictions

Predicting emotions is a multilabel classification problem. Instead of predicting a single class out of two or more options as multiclass models do, multilabel models make two or more independent predictions--one for each label. 

Iterative stratification

Class weights

Skmultilearn

RNN


# The Front Page Report

To demonstrate my model's utility, I created a Python class: front_page. The front page object is instantiated with one attribute: source. Options include: 'npr', 'slate', 'fox', and 'breitbart'. 

The front_page object has three methods:
* get_headlines
Fetches headlines currently on the source's front page and returns them as a list

* details
Returns a report which contains:
    * each headline currently on the source's front page
    * a list of emotions present in each headline, as predicted by my model
    * valence of the words contained in each headline, predicted by VADER
    * summay information
    
I included VADER's valence predictions in my reports as some additional helpful information about the headline. This would be particularly useful, for example, when my model predicts all 6 emotion categories. The valence rating will give users an indication of whether the overall thrust of the headline is positive or negative.

For details on VADER, see [here]

* summary
Returns only the summary information from the report


Works Cited 

Berger J. (2011). Arousal increases social transmission of information. Psychological Science 22.7, 891–893.

Stefan Stieglitz & Linh Dang-Xuan (2013) Emotions and Information Diffusion in Social Media—Sentiment of Microblogs and Sharing Behavior, Journal of Management Information Systems, 29:4, 217-248, DOI: 10.2753/MIS0742-1222290408

Carlo Strapparava, Rada Mihalcea. SemEval-2007 Task 14: Affective Text https://www.aclweb.org/anthology/S07-1013

Emilio Ferrara and Zeyao Yang (2015) Quantifying the effect of sentiment on information diffusion in social media, PeerJ Computer Science

Beyond positive or negative: Qualitative sentiment analysis of social media reactions to unexpected stressful events
Gaspar, Rui ; Pedro, Cláudia ; Panagiotopoulos, Panos ; Seibt, Beate
Computers in Human Behavior, March 2016, Vol.56, pp.179-191



