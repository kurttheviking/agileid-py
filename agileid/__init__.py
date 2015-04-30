import base64
import binascii
import bson


def create(id_type=None):
    oid = bson.objectid.ObjectId()
    bin = binascii.a2b_hex(str(oid))
    aid = base64.urlsafe_b64encode(bin)

    if id_type:
        id_type = str(id_type)

        if '!' in id_type:
            raise ValueError('id_type cannot contain "!"')

        return '%s!%s' % (id_type, aid)

    return aid
