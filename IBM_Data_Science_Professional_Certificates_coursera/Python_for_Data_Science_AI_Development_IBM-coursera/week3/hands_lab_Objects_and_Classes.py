import matplotlib.pyplot as plt


# matplotlib is library - visualize data
# pyplot is module in matplotlib - state-based interface
# from matplotlib import pyplot as plt


# Create a class Circle

class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

        # Method

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
print(dir(RedCircle))

# Print the object attribute radius
print(RedCircle.radius)

# Print the object attribute color
print(RedCircle.color)

# Set the object attribute radius

RedCircle.radius = 1
print(RedCircle.radius)

# Call the method drawCircle
# RedCircle.drawCircle()


# Use method to change the object attribute radius
print('Radius of object:', RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):', RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):', RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)

print(BlueCircle.radius)
print(BlueCircle.color)


# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attribute height
print(SkinnyBlueRectangle.height)

# Print the object attribute width
print(SkinnyBlueRectangle.width)

# Print the object attribute color
print(SkinnyBlueRectangle.color)

# Use the drawRectangle method to draw the shape
# SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, "yellow")

# Print the object attribute height
print(FatYellowRectangle.height)

# Print the object attribute width
print(FatYellowRectangle.width)

# Print the object attribue color
print(FatYellowRectangle.color)

# Use the drawRectangle method to draw the shape
# FatYellowRectangle.drawRectangle()



# Exercises
"""
You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class
'analysedText' with the following methods -

<ul>
    <li> Constructor (__init__) - This method should take the argument <code>text</code>, make it lower case, and remove all punctuation.  Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called <code>fmtText</code>.
    <li> freqAll - This method should create and <strong>return</strong> dictionary of all unique words in the text, along with the number of times they occur in the text. Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. Create this dictionary from the <code>fmtText</code> attribute.
    <li> freqOf - This method should take a word as an argument and <strong>return</strong> the number of occurrences of that word in <code>fmtText</code>.
</ul>
 The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise. <br>
 <i> Hint: Some useful functions are <code>replace()</code>, <code>lower()</code>, <code>split()</code>, <code>count()</code> </i><br>

"""


class analysedText(object):

    def __init__(self, text):
        # TODO: Remove the punctuation from <text> and make it lower case.
        text = text.lower()
        punctuation = ".?!,"
        for char in punctuation:
            text = text.replace(char, "")
        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = text  # use text instead of self.text
        # Constructor
        self.text = text  # move this line before self.fmtText

    def freqAll(self):  # no argument needed

        # TODO: Split the text into a list of words
        text = self.fmtText.split()  # use self.fmtText instead of text
        # TODO: Create a dictionary with the unique words in the text as keys

        freq_dict = {}

        for word in text:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # and the number of times they occur in the text as values
        # Return the dictionary
        return freq_dict
        # pass # return the created dictionary

    def freqOf(self, word):
        # Split the formatted text into a list of words
        words = self.fmtText.split()

        # Count the number of times the word appears in the list of words
        count = 0

        for w in words:
            if w == word:
                count += 1

        # TODO: return the number of occurrences of <word> in <fmtText>

        return count
        # pass


pattern = "period . down EXCLAMation mark ! comma , and question mark ?.?? do, THIS IS MY TEXT mark down OF Exercise!., Text dot pepe dot pep?"
pattern2 = "the quick brown fox jumps over the lazy dog"
object1 = analysedText(pattern)
object1.text
object1.freqAll()
object1.freqOf("mark")  # Replace "mark" with the actual word you want to find the frequency of


print(pattern)
print(object1.text)
print(object1.freqAll())
print(object1.freqOf("mark"))

# Test
"""
You can run the code cell below to test your functions to ensure they are working correctly. First execute the code cell in which you implemented your solution, then execute the code cell to test your implementation.
"""
"""
import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
    
"""

# answer
"""
class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
"""

# with comment
"""
class analysedText:
    
    def __init__ (self, text):
        # Make the text lowercase and remove punctuation
        text = text.lower()
        punctuation = ".?!,"
        for char in punctuation:
            text = text.replace(char, "")
        # Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = text
        # Constructor 
        self.text = text
        
    def freqAll(self):
        # Split the formatted text into a list of words
        words = self.fmtText.split()
        # Create an empty dictionary to store the frequency of each word
        freq_dict = {}
        # Iterate over each word in the list of words
        for word in words:
            # If the word is already a key in the dictionary, increment the value by 1
            if word in freq_dict:
                freq_dict[word] += 1
            # If the word is not a key in the dictionary, add it with a value of 1
            else: 
                freq_dict[word] = 1
        # Return the dictionary of word frequencies
        return freq_dict
    
    def freqOf(self, word):
        # Get the frequency dictionary using the freqAll method
        freq_dict = self.freqAll()
        # If the word is a key in the dictionary, return its value (frequency)
        if word in freq_dict:
            return freq_dict[word]
        # If the word is not a key in the dictionary, return 0
        else:
            return 0

"""
