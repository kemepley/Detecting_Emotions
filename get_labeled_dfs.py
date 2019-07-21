import tarfile
import string
import pandas as pd



def emotion_labels(row):
    if row=='anger':
        label=0
    elif row=='disgust':
        label=1
    elif row=='fear':
        label=2
    elif row=='joy':
        label=3
    elif row=='sadness':
        label=4
    else:
        label=5
    return label



def get_labeled_dfs():

# used the tarfile ilbrary to open the tarfile and the getmembers() method to get a list of filenames
	tar = tarfile.open('data/AffectiveText.Semeval.2007.tar')
	members = tar.getmembers()
	members

	# used extractfile() to get the information in each file and put it in a dataframe
	corpus_df = pd.read_csv(tar.extractfile(members[1]), sep='\n')
	valence_df = pd.read_csv(tar.extractfile(members[3]), sep=' ', header=None)
	emotion_df = pd.read_csv(tar.extractfile(members[4]), sep=' ', header=None)

	val_corpus_df = pd.read_csv(tar.extractfile(members[8]), sep='\n')
	val_valence_df = pd.read_csv(tar.extractfile(members[6]), sep=' ', header=None)
	val_emotion_df = pd.read_csv(tar.extractfile(members[7]), sep=' ', header=None)

# closing the tar file I opened above
	tar.close



#cleaning the target files
# labeling the columns of the target dfs and dropping the duplicate index columns
	valence_df = valence_df.drop([0], axis=1)
	valence_df.columns = ['valence']

	emotion_df = emotion_df.drop([0], axis=1)
	emotion_df.columns = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']

	val_valence_df = val_valence_df.drop([0], axis=1)
	val_valence_df.columns = ['valence']

	val_emotion_df = val_emotion_df.drop([0], axis=1)
	val_emotion_df.columns = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']



# cleaning the corpus dfs
# there is a footer in the last column that needs to be dropped
	corpus_df = corpus_df.drop([1000], axis=0)

# getting rid of the html tags by splitting on the "<>" characters 
	corpus_df['split'] = corpus_df.iloc[:, 0].apply(lambda x: x.split(">"))
	corpus_df['text_with_html_tag'] = corpus_df.split.apply(lambda x: x[1])
	corpus_df['text_with_html_tag_split'] = corpus_df.text_with_html_tag.apply((lambda x: x.split("<")))
	corpus_df['text'] = corpus_df.text_with_html_tag_split.apply(lambda x: x[0])

# drop the original column and the split columns
	corpus_df = corpus_df.drop(['<corpus task="affective text">','split','text_with_html_tag', 'text_with_html_tag_split'], axis=1)
    
# drop duplicate headlines
	corpus_df = corpus_df.drop_duplicates(keep='first')

# repeating the procedure with the validation set
	val_corpus_df = val_corpus_df.drop([250], axis=0)
	val_corpus_df['split'] = val_corpus_df.iloc[:, 0].apply(lambda x: x.split(">"))
	val_corpus_df['text_with_html_tag'] = val_corpus_df.split.apply(lambda x: x[1])
	val_corpus_df['text_with_html_tag_split'] = val_corpus_df.text_with_html_tag.apply((lambda x: x.split("<")))
	val_corpus_df['text'] = val_corpus_df.text_with_html_tag_split.apply(lambda x: x[0])
	val_corpus_df = val_corpus_df.drop(['<corpus task="affective text">','split','text_with_html_tag', 'text_with_html_tag_split'], axis=1)
	val_corpus_df = val_corpus_df.drop_duplicates(keep='first')



# preparing class labels for the emotion dfs
# setting up a target colum with a numeric category for the emotion with the strongest intensity rating
	emotion_df['max'] = emotion_df[['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']].idxmax(axis=1)
	emotion_df['label'] = emotion_df['max'].apply(emotion_labels)

# repeating for the validation set
	val_emotion_df['max'] = val_emotion_df[['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']].idxmax(axis=1)
	val_emotion_df['label'] = val_emotion_df['max'].apply(emotion_labels)



# preparing class labels for the valence dfs
	valence_df['label'] = valence_df['valence'].apply(lambda x: 2 if (x>-15) & (x<15) else x)
	valence_df['label'] = valence_df['label'].apply(lambda x: 1 if x>=15 else x)
	valence_df['label'] = valence_df['label'].apply(lambda x: 0 if (x<=-15) else x)

# repeating for the validation set
	val_valence_df['label'] = val_valence_df['valence'].apply(lambda x: 2 if (x>-15) & (x<15) else x)
	val_valence_df['label'] = val_valence_df['label'].apply(lambda x: 1 if x>=15 else x)
	val_valence_df['label'] = val_valence_df['label'].apply(lambda x: 0 if (x<=-15) else x)

	return corpus_df, val_corpus_df, emotion_df, val_emotion_df, valence_df, val_valence_df

