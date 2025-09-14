#Twinkle Twinkle Little Star Poem Print
print('''
     Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star. ''')

#Install an external module and use it to perform an operation
import pyttsx3
engine = pyttsx3.init()

engine.say("I will speak this text")

#To print the contents of a directory using the os module
import os

path = 'your/directory/path'
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
















