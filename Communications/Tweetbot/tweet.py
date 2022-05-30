/*
 * Copyright [2022] Justine Dela Torre <Jasutin>
 * 
 * This is free and unencumbered software released into the public domain.

 * Anyone is free to copy, modify, publish, use, compile, sell, or
 * distribute this software, either in source code form or as a compiled
 * binary, for any purpose, commercial or non-commercial, and by any
 * means.

 * In jurisdictions that recognize copyright laws, the author or authors
 * of this software dedicate any and all copyright interest in the
 * software to the public domain. We make this dedication for the benefit
 * of the public at large and to the detriment of our heirs and
 * successors. We intend this dedication to be an overt act of
 * relinquishment in perpetuity of all present and future rights to this
 * software under copyright law.

 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 * OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.

 * For more information, please refer to <http://unlicense.org/>
 */

def current_time():
    import time
    t = time.time()
    return t + 946684800

def enc_percent(s):
    ret = ''
    for c in s:
        ordc = ord(c)
        if ordc in range(0x30, 0x39 + 1) or \
           ordc in range(0x41, 0x5a + 1) or \
           ordc in range(0x61, 0x7a + 1) or \
           ordc in (0x2d, 0x2e, 0x5f, 0x7e):
            ret += c
        else:
            ret += '%%%02X' % (ordc)
    return ret

def oauth_sign(method, url, s, vcs, vas):
    import hmac
    import ubinascii
    import uhashlib

    str = ''
    for t in sorted(s):
        if str != '':
            str += '&'
        str += "%s=%s" % (t[0], enc_percent(t[1]))
    str = "%s&%s&%s" % (method.upper(), enc_percent(url), enc_percent(str))
    signing_key = bytearray(enc_percent(vcs) + '&' + enc_percent(vas))
    hash = hmac.new(signing_key, msg=str, digestmod=uhashlib.sha1)
    ret = ubinascii.b2a_base64(hash.digest()).rstrip()
    return ret

def oauth_genhead(vck, vcs, vat, vas, status):
    import ubinascii
    import os

    tstamp = current_time()
    nonce = 'nonce%d' % (tstamp)
    pairs = {
        ('status', status),
        ('include_entities', 'true'),
        ('oauth_consumer_key', vck),
        ('oauth_nonce', nonce),
        ('oauth_signature_method', 'HMAC-SHA1'),
        ('oauth_timestamp', str(tstamp)),
        ('oauth_token', vat),
        ('oauth_version', '1.0')}

    sig = oauth_sign('POST', \
          'https://api.twitter.com/1.1/statuses/update.json', \
          pairs, vcs, vas).decode('utf-8')

    s = '''        OAuth oauth_consumer_key="%s", 
              oauth_nonce="%s", 
              oauth_signature="%s", 
              oauth_signature_method="HMAC-SHA1", 
              oauth_timestamp="%d", 
              oauth_token="%s", 
              oauth_version="1.0"''' % \
        (vck, nonce, enc_percent(sig), tstamp, vat)
    return s

def tweet(s):
    body = 'status=%s' % (enc_percent(s))
    oauth_head = oauth_genhead(CK, CS, AT, AS, s)
    header = '''POST /1.1/statuses/update.json?include_entities=true HTTP/1.1
Accept: */*
Connection: close
User-Agent: Pot Prant Bot v0.1
Content-Type: application/x-www-form-urlencoded
Authorization: 
%s
Content-Length: %d
Host: api.twitter.com
''' % (oauth_head, len(body))
    return header + '\n' + body + '\n'

###############################################################################

CK = ''     # CONSUMER_KEY
CS = ''     # CONSUMER_SECRET
AT = ''     # ACCESS_KEY
AS = ''     # ACCESS_SECRET

time_diff = 9 * 3600                                        # Time difference

import time
import ntptime

while True:
    try:
        ntptime.settime()
        break
    except:
        pass

t = time.localtime(time.time() + time_diff)
time_str = '%02d/%02d/%02d %02d:%02d:%02d' % t[0:6]
tweet_status = 'Pot plant needs water (%s)' % (time_str)
s = tweet(tweet_status)
f = open('tweet.txt', 'w')
f.write(s)
f.close()
