import base64, email, glob, json, os, sys



def _decode_b64(data):
    """Helper function: decodes base64 encoded text."""
    try:
        return base64.b64decode(data)
    except Exception as err:
        return data, err


def _encode_json(data):
    """Helper function: encodes json encoded text."""
    try:
        return json.loads(data)
    except Exception as err:
        return data, err


def _open_email(fpath):
    """Returns content of an email file."""
    mail = email.message_from_file(open(fpath, 'r'))
    if mail.is_multipart():
        content, attachment = mail.get_payload()
        content = content.get_payload(decode=True)
        attachment = attachment.get_payload(decode=True)
    else:
        content = mail.get_payload(decode=True)
        attachment = None

    return content, attachment


def _unpack_messages(content):
    """Unpacks messagse from email content."""
    lines = [l for l in content.splitlines() if l]
    as_b64 = map(_decode_b64, lines)
    as_b64_valid = [l for l in as_b64 if not isinstance(l, tuple)]
    as_b64_invalid = [l for l in as_b64 if isinstance(l, tuple)]
    as_json = map(_encode_json, as_b64_valid)
    as_json_valid = [l for l in as_json if not isinstance(l, tuple)]
    as_json_invalid = [l for l in as_json if isinstance(l, tuple)]

    return as_b64, as_b64_valid, as_b64_invalid, as_json, as_json_valid, as_json_invalid


def _write_stats(stats, fid, fpath, content, attachment):
    """Writes email file stats."""
    stats.write("--------------------------------------------------------------------------------------\n")
    stats.write("{0}\n".format(fpath))
    stats.write("FILE {0}: BASE64 TOTAL: {1}\n".format(fid, len(content[0])))
    stats.write("FILE {0}: BASE64 VALID: {1}\n".format(fid, len(content[1])))
    stats.write("FILE {0}: BASE64 INVALID: {1}\n".format(fid, len(content[2])))
    stats.write("FILE {0}: JSON TOTAL: {1}\n".format(fid, len(content[3])))
    stats.write("FILE {0}: JSON VALID: {1}\n".format(fid, len(content[4])))
    stats.write("FILE {0}: JSON INVALID: {1}\n".format(fid, len(content[5])))
    if attachment:
        stats.write("FILE {0}: ATTACHMENT: {1}\n".format(fid, len(attachment)))


def _write_trace(trace, fid, messages):
    """Writes email file trace."""
    for msg in messages:
        trace.write("{0},'{1}',{2},{3}\n".format(fid,
                                               msg['msgCode'],
                                               msg['msgUID'],
                                               msg['msgTimestamp']))


# Set sim id.
sim_id = sys.argv[1]

# Set paths.
sim_dir = "simulation_{0}".format(sim_id)
sim_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), sim_dir)
if not os.path.exists(sim_dir):
    raise IOError("Simulation folder does not exist")
sim_emails = glob.glob(os.path.join(sim_dir, "*.eml"))
sim_trace = os.path.join(sim_dir, "simulation-{0}-trace.txt".format(sim_id))
sim_stats = os.path.join(sim_dir, "simulation-{0}-stats.txt".format(sim_id))

# Unpack emails.
sim = []
for fid, fpath in enumerate(sim_emails):
    content, attachment = _open_email(fpath)
    messages = _unpack_messages(content)
    sim.append((fid + 1, fpath, messages, attachment))

# Write trace.
with open(sim_trace, 'w') as trace:
    trace.write("emailFileID,msgCode,msgUID,msgTimestamp\n")
    for fid, fpath, content, attachment in sim:
        # _log_stats(fid, fpath, content, attachment)
        _write_trace(trace, fid, content[4])

# Write stats.
with open(sim_stats, 'w') as stats:
    for fid, fpath, content, attachment in sim:
        _write_stats(stats, fid, fpath, content, attachment)
