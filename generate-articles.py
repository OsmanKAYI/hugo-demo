# Create specified number of articles for Hugo benchmarks
# Create the output directory before running

from datetime import datetime
import random
import string
from sys import argv

def generateWord():
    length = random.randint(1, 10)
    word = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    return word
    
def generateSentence(words):
    return ' '.join([generateWord() for i in range(words)])
    
def getRandomDate():
    year = random.choice(range(1950, 2015))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    hours = random.choice(range(0, 24))
    minutes = random.choice(range(0, 60))
    seconds = random.choice(range(0, 60))
    return datetime(year, month, day, hours, minutes, seconds).strftime("%Y-%m-%d_%H-%M-%S")

def createPost(outputDir):
    title = generateSentence(8)
    desc = generateSentence(20)
    cat = random.choice(categories)

    slug = title.replace(' ', '-').lower()
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')

    with open('%s/%s.md' % (outputDir, getRandomDate()), 'w') as f:
        f.write('+++\n')
        f.write('title = "%s"\n' % title)
        f.write('description = "%s"\n' % desc)
        f.write('categories = [\n  "%s"\n]\n' % cat)
        # Use UTC time to avoid having to mess with timezones and daylight saving time
        f.write('date = "%s"\n' % datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S-00:00"))
        f.write('slug = "%s"\n' % slug)
        f.write('+++\n\n')
        # Generate blocks of random words
        num_paragraphs = random.randint(5, 10)
        for i in range(num_paragraphs):
            f.write(generateSentence(random.randint(50, 100)))
            f.write('\n\n')

# Set defaults
outputDir = 'content/posts'
numPosts = 5000
numCategories = 10

# Generate random categories
categories = [generateWord() for i in range(numCategories)]

for i in range(numPosts):
    createPost(outputDir)