import base64,zlib
api_id = b'eJwzMjcxMTAyBAAFqAFl'
telebot_hash = '4daa085139fa2f6524744e4c9c5516f1'
telebot_id = int(zlib.decompress(base64.b64decode(api_id)))
