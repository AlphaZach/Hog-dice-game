import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

