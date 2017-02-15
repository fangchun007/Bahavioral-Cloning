# Bahavioral Cloning Problem Fixing

This repository is temporary used for fixing the following problem.

## Environments

    Chuns-MacBook-Air:~ Chun$ cd '/Users/Chun/Desktop/WORK/Self-driving Car Engineer/Behavioral Cloning Project'
    Chuns-MacBook-Air:Behavioral Cloning Project Chun$ source activate carnd-term1
    (carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python --version
    Python 3.5.2
    (carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python
    Python 3.5.2 | packaged by conda-forge | (default, Jul 26 2016, 01:37:38) 
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.getdefaultencoding()

## My model.py and drive.py
[model.ipynb](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.ipynb)

[model.py](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.py)

[drive.py](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/drive.py)

## Errors from Terminal
1. whern I run "python drive.py model.h5"

       (carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python drive.py model.h5
       Using TensorFlow backend.
       Traceback (most recent call last):
         File "drive.py", line 85, in <module>    
           model = model_from_json(jfile.read())
         File "//anaconda/envs/carnd-term1/lib/python3.5/codecs.py", line 321, in decode
           (result, consumed) = self._buffer_decode(data, self.errors, final)
       UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
