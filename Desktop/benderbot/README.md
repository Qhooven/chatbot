Link to demo video:
https://www.dropbox.com/s/hszxmx9tm3fw1e7/zoom_1.mp4?dl=0

First party packages used:
random
time

Third party packages:
Django
nltk


Instructions:
Navigate to benderbot/bot/proj.py (don't cd, just open the file)
Then, in proj.py, there are two comments near the top of the file that indicate where the following block of code should be pasted
Then, copy and paste the code block below in between the comments, run proj.py once, then remove the code block

#Code starts here

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('twitter_samples')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

#Code ends here


afterwards, run the following commands in the terminal:
cd benderbot
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

then navigate to localhost 8000