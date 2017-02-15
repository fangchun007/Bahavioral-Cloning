# Bahavioral-Cloning

This repository is temporary used for the following problem solving.

## Terminal

Chuns-MacBook-Air:~ Chun$ cd '/Users/Chun/Desktop/WORK/Self-driving Car Engineer/Behavioral Cloning Project'

Chuns-MacBook-Air:Behavioral Cloning Project Chun$ source activate carnd-term1

(carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python drive.py model.h5

Using TensorFlow backend.

Traceback (most recent call last):

    File "drive.py", line 85, in <module>    
       model = model_from_json(jfile.read())
    File "//anaconda/envs/carnd-term1/lib/python3.5/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
