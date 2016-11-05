
import hashlib
import hmac
#move to module, add to gitignore
secret = "crush"

def hash_str(s):
    #return hashlib.md5(s).hexdigest()
    return hmac.new(secret, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    ###Your code here
    s = h.split("|")[0]
    if h == make_secure_val(s):
        return s



# -----------------
# User Instructions
#
# Implement the function check_secure_val, which takes a string of the format
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None
#
# def check_secure_val(h):
#     ###Your code here
#     s = h[0]
#     hashed = h[1]
#     if hash_str(s) == hashed:
#         return s
#     else:
#         return None
