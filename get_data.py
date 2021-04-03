
import os

os.system("kaggle competitions download -c digit-recognizer")
os.system("unzip digit-recognizer.zip -d data")
os.system("rm digit-recognizer.zip")

