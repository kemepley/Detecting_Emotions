# Detecting_Emotions

![media image](images/william-iven-SpVHcbuKi6E-unsplash.jpg)

I've created a model to help news and entertainment media outlets classify headlines based on the emotions they convey so that they can select the right ones to keep readers interested in their content. 

Social media and microblogging platforms may also benefit from the use of such a tool in their efforts to identify fake news articles and hoaxes because highly provocative, emotional language is common feature among them (****citations). 

# Background

Headlines are designed to grab readers' attention so that they'll read articles and keep coming back for more content.

It should come as no surprise that the key to grabbing our attention is provoking emotions. In drawing out emotions, headline writers are tapping into some our most fundamental concerns. 

Emotions represent what psychologist Richard Lazarus called "core relational themes"... (****citation)

safety, wellbeing, and our ability to cope with challenges and achieve our goals. 

So when writers of headlines tap into our emotions, they're tapping into something powerful.

It may be tempting for media outlets to rely heavily on fear and anger to attract readers because they are are particularly effective in capturing and *holding* attention (***citations***) in the moment.

They've also been shown to be quicker to turn viral than emotionally neutral or low-arrousal content (Berger 2011). 

But unless you want your readership to be the tinfoil-hat-wearing kind, there is a danger in heavy reliance on high-arrousal context. 

(***citation on emotion and avoidance; citation on errosion of trust in the media***) 

Positive content has staying power. (****citation) 

Hence, news and media providers have an interest in finding a balance of emotions on their front pages and personalized recommendations.

# Data Exploration

For this project, I analyzed a set of 1250 headlines from the SemEval 2007 program affective task. 

The headlines were collected from a variety of news sources and labeled by six independent annotators. For each headline, annotators assigned an intensity rating between 0 and 100 for six emotion categories: anger, disgust, fear, joy, sadness, and surprise. 0 indicates that the emotion is not present. 100 indicates that it is very strongly present. Annotators were instructed to assign ratings according to their first intuition about the emotional import of the headlines, taking into account both the emotion-evoking words in the text and the overall impact of the it. 

The headlines have an average length of six words and a max of 15. The most common emotion (in any amount) is surprise and the most common max emotion is joy. Disgust is the least common, and also has the lowest average intensity.

(pics)

I checked the headlines for presence of emotion words from the WordNet emotion lexicon and the positive and negative words from the General Inquirer lexicon. Just over 100 of the headlines contained words from the emotion lexicon and less than half of the headlines contained words from the positive and negative words lexicon. In comparing the words from the lexicon to the headlines they were present in, I noticed a fair amount of divergence in the from the ratings. The use of words from these lexicons do not appear to be reliable indicators of the overal emotional significance of a sentence. Context matters greatly. 


Works Cited 

Berger J. (2011). Arousal increases social transmission of information. Psychological Science 22.7, 891–893.

Carlo Strapparava, Rada Mihalcea. SemEval-2007 Task 14: Affective Text https://www.aclweb.org/anthology/S07-1013

