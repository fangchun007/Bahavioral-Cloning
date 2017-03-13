# Bahavioral Cloning Problem Fixing

This repository is used for DEBUGGING. Problem solved!

Please see [model_r2.ipynb]() for the entire code.

## Great News: problem solved!

The problem was caused by my using of the function tf.image.resize_images as a Lambda layer in the Keras model. Then the model.h5 cannot be loaded correctly. However, I don't know the real reason.

https://github.com/fchollet/keras/issues/5298

----------------------------------------------
----------------------------------------------

I hope to get your the following help. Thank you very much in advance!

1. After downloading drive.py, model.h5, model.json, can you replicate my errors by run "python drive.py model.h5"? If the code work well in your computer, please let me know: chun.fang@hotmail.com. If a similar problem caused please also leave me a message. Thanks!
2. Can anybody share your code with me so that I can compare yours and mine? 
3. If you have time to dive into my code (I've tried to simplify them to minimize your time), could you please send me an email if you find any erros I made. Many thanks!
4. All comments are warmly welcomed.

## My Environments

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

## Codes I've used
[model.ipynb](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.ipynb)

[model.py](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.py)

[drive.py](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/drive.py)

[model.h5](https://github.com/fangchun007/Bahavioral-Cloning/blob/master/model.h5)

[model.json](https://raw.githubusercontent.com/fangchun007/Bahavioral-Cloning/master/model.json)

## Errors and What's I've tried before.

1. Whern I run "python drive.py model.h5"

    (carnd-term1) Chuns-MacBook-Air:Behavioral Cloning Project Chun$ python drive.py model.h5
    Using TensorFlow backend.
    Traceback (most recent call last):
      File "drive.py", line 85, in <module>    
        model = model_from_json(jfile.read())
      File "//anaconda/envs/carnd-term1/lib/python3.5/codecs.py", line 321, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte

2. When I run "python drive.py model.json"

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
    
3. I used Vim to check model.h5 and found this file do starts with "<89>HDF^M". Then I replaced letters "<89>HDF^M" with "%E2 %80 %B0". New errors come out:

    Using TensorFlow backend.
    Traceback (most recent call last):
      File "drive.py", line 85, in <module>
        model = model_from_json(jfile.read())
      File "//anaconda/envs/carnd-term1/lib/python3.5/codecs.py", line 321, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 38: invalid start byte

4. I updata keras package, but same error.
    
5. I download from [preritj's github](https://github.com/preritj/Behavioral-Cloning)  files including drive.py, model.h5, model.json, model.py, preprocess.py, setup.py, aiming to clone his result. Unfortunately, I failed on my environment.

## Thank you!

