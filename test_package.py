from tf1_tf2_compat_functions import * 

file_name   = "tf1_tf2_compat_functions"
output_path = "/tmp/%s.tfrecord"%file_name 

writer      = tf_io.TFRecordWriter(output_path) 

