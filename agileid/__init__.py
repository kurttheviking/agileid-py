import base64
import binascii
import bson
import re

REGEX_AID = re.compile('^([A-Za-z0-9\-_]{16})$')


def cast(id, id_type=None):
    sid = str(id)

    if bson.objectid.ObjectId.is_valid(sid):
        bin = binascii.a2b_hex(sid)
        aid = base64.urlsafe_b64encode(bin)
    else:
        aid = id
        aid_parts = aid.split('!')

        if not REGEX_AID.match(aid_parts[-1]):
            raise ValueError('provided id must be AgileId or ObjectId')
        elif id_type and aid_parts[0] == id_type:
            id_type = None

    if id_type:
        id_type = str(id_type)

        if '!' in id_type:
            raise ValueError('id_type cannot contain "!"')

        return '%s!%s' % (id_type, aid)

    return aid


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


def is_valid(id):
    id = str(id)
    id_parts = id.split('!')

    is_scoped = all([len(p) > 0 for p in id_parts])
    is_aid = REGEX_AID.match(id_parts[-1])

    return bool(is_scoped and is_aid)
