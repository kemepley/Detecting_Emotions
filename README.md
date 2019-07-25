# Detecting_Emotions

![media image](images/william-iven-SpVHcbuKi6E-unsplash.jpg)

I've created a model to help news and entertainment media outlets classify headlines based on the emotions they convey so that they can select the right ones to keep readers interested in their content. 

Social media and microblogging platforms may also benefit from the use of such a tool in their efforts to identify fake news articles and hoaxes because highly provocative, emotional language is common feature among them (****citations). 

# Background

Headlines are designed to grab readers' attention so that they'll read articles and keep coming back for more content.

Emotions are effective in getting readers to pay attention because ...


Emotions represent what psychologist Richard Lazarus called "core relational themes"... (****citation)

safety, wellbeing, and our ability to cope with challenges and achieve our goals. 

So when writers of headlines tap into our emotions, they're tapping into something powerful.


It may be tempting for media outlets to rely heavily on fear and anger to attract readers because they are are particularly effective in capturing and *holding* attention (***citations***) in the moment.

They've also been shown to be quicker to turn viral than emotionally neutral or low-arrousal content (Berger 2011) 

Emotions associated with high phsyiologial arrousal facilitate sharing.

(Stieglitz and Dang-Xuan 2013)

But unless you want your readership to be the tinfoil-hat-wearing kind, there is a danger in heavy reliance on high-arrousal context. 

(***citation on emotion and avoidance; citation on errosion of trust in the media***) 

Positive content has staying power.  Positive stories get more interactions (shares and accolades--twitter's favorites, facebook's likes) over time (Ferrara and Yang 2015) 
Positive emotion enhances memory (The pollyanna hypothesis, Boucher and Osgood 1969)

Hence, news and media providers have an interest in finding a balance of emotions on their front pages and personalized recommendations.

# Data Exploration

For this project, I analyzed a set of 1250 headlines from the SemEval 2007 program affective task. 

The headlines were collected from a variety of news sources. For each headline, annotators assigned an intensity rating between 0 and 100 for six emotion categories: anger, disgust, fear, joy, sadness, and surprise. 0 indicates that the emotion is not present. 100 indicates that it is very strongly present. Annotators were instructed to assign ratings according to their first intuition about the emotional import of the headlines, taking into account both the emotion-evoking words in the text and the overall impact of the it. 

It's important to note that annotating emotions in text is a difficult task (Alm et al 2005). There is high context dependence in emotion communication (Strappavara ...) and annotators' personal histories and background beliefs may result in different reactions to the same subject matter. The same subject may be perceived as threatenening to one annotator, eliciting fear, antagonistic to another annotator, eliciting anger, and buffonish to another, eliciting disgust (Gaspar et al. 2016). We can be fairly confident in the reasonability of the labels in the dataset becuase they were labeled by six independent annotators. 

The headlines in the dataset have an average length of six words and a max of 15. The most common emotion (in any amount) is surprise and the most common max emotion is joy. Disgust is the least common, and also has the lowest average intensity.

(pics)

I checked the headlines for presence of emotion words from the WordNet emotion lexicon and the positive and negative words from the General Inquirer lexicon. Just over 100 of the headlines contained words from the emotion lexicon and just under half of the headlines contained words from the positive and negative words lexicon. Of the headlines with words appearing in the emotion lexicon, the emotion labels matched 85% of the time. However, there was little correspondence between the positive and negative words lexicon and the valence labels, which matched only 27% of the time.

I also looked at the most common words in the dataset and the most common word pairs and the most common words for each label. 

# Predictions


# Performance on Unseen Data




Works Cited 

Berger J. (2011). Arousal increases social transmission of information. Psychological Science 22.7, 891–893.



Stefan Stieglitz & Linh Dang-Xuan (2013) Emotions and Information Diffusion in Social Media—Sentiment of Microblogs and Sharing Behavior, Journal of Management Information Systems, 29:4, 217-248, DOI: 10.2753/MIS0742-1222290408

Carlo Strapparava, Rada Mihalcea. SemEval-2007 Task 14: Affective Text https://www.aclweb.org/anthology/S07-1013

Emilio Ferrara and Zeyao Yang (2015) Quantifying the effect of sentiment on information diffusion in social media, PeerJ Computer Science

Beyond positive or negative: Qualitative sentiment analysis of social media reactions to unexpected stressful events
Gaspar, Rui ; Pedro, Cláudia ; Panagiotopoulos, Panos ; Seibt, Beate
Computers in Human Behavior, March 2016, Vol.56, pp.179-191



