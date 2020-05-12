# tf1_tf2_compat_functions package 
A simpler wrapper for Tensorflow functions that are compatible with both Tensorflow 1 and Tensorflow 2
@Author: Ty Nguyen
@Email: tynguyen@seas.upenn.edu
    
# Installation 
```
cd tf1_tf2_compatibility_functions
# Python3
python3 -m pip install .

# Python2 
python2 -m pip install .
```
# Usage
    
```
from tf1_tf2_compat_functions import * 
```

Instead of calling tf.app.run() in TF1 or tf.compat.v1.app.run() in TF2, call
```
tf_app.run()
```
Instead of calling tf.io.TFRecordWriter() in TF2, or tf.python_io.TFRecordWriter() in TF2, call
``` 
tf_io.TFRecordWriter()
```

# Available functions (in TF1 syntax)
- [x] tf.app
- [x] tf.python_io
- [ ] 
continue...
