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
    >>> 'utf-8'

## My model.py and drive.py
[model.ipynb](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.ipynb)

[model.py](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.py)

[drive.py](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/drive.py)

## Errors from Terminal

Whern I run "python drive.py model.h5"

    (carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python drive.py model.h5
    Using TensorFlow backend.
    Traceback (most recent call last):
      File "drive.py", line 85, in <module>    
        model = model_from_json(jfile.read())
      File "//anaconda/envs/carnd-term1/lib/python3.5/codecs.py", line 321, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte

When I run "python drive.py model.json"

    (carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python drive.py model.json
    Using TensorFlow backend.
    Traceback (most recent call last):
      File "drive.py", line 85, in <module>
        model = model_from_json(jfile.read())
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/models.py", line 210, in model_from_json
        return layer_from_config(config, custom_objects=custom_objects)
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/utils/layer_utils.py", line 40, in layer_from_config
        return layer_class.from_config(config['config'])
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/models.py", line 1080, in from_config
        layer = get_or_create_layer(first_layer)
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/models.py", line 1064, in get_or_create_layer
        layer = layer_from_config(layer_data)
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/utils/layer_utils.py", line 38, in layer_from_config
        return layer_class.from_config(config['config'], custom_objects=custom_objects)
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/layers/core.py", line 637, in from_config
        function = func_load(config['function'], globs=globs)
      File "//anaconda/envs/carnd-term1/lib/python3.5/site-packages/keras/utils/generic_utils.py", line 59, in func_load
        closure=closure)
    TypeError: arg 4 (defaults) must be None or tuple
    
I used Vim to check model.h5 and found this file do starts with "<89>HDF^M"
    
I download from [preritj's github](https://github.com/preritj/Behavioral-Cloning)  files including drive.py, model.h5, model.json, model.py, preprocess.py, setup.py, aiming to clone his result. Unfortunately, I failed on my environment.




