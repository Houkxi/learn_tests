import hashlib

print hashlib.algorithms_available
print hashlib.algorithms_guaranteed

md5_object = hashlib.md5('It is hard to write')
print md5_object.hexdigest()
sha1_object = hashlib.sha1('It is hard to write')
print sha1_object.hexdigest()
sha1_object = hashlib.sha1('It is still hard to write')
print sha1_object.hexdigest()
