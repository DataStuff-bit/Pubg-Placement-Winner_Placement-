import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Fetch HTML content from the URL
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Apple')
html = response.read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract text from the HTML
text = soup.get_text(strip=True)

# Tokenize the text into words
tokens = [t for t in text.split()]

# Remove stopwords from tokens
sr = stopwords.words('english')
clean_tokens = [token for token in tokens if token.lower() not in sr]

# Calculate frequency distribution
freq = FreqDist(clean_tokens)

# Print the most common 30 words and their frequencies
for key, val in freq.most_common(30):
    print(f'{key}: {val}')

# Plot the frequency distribution
freq.plot(30, cumulative=False)
