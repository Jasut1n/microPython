<h1 align="center"> Twitter Bot for MicroPython <ESP8266></h1>
 
 <br /> 

<strong>This program is a Tweet bot (Twitter status updater) for MicroPython ESP8266.
Confirmed working with MicroPython.</strong>

<strong>One problem is, this program consumes a lot of heap memory, so it will not run
if you add more functionality.</strong>

<strong>To run, we need a modified hmac.py which is compatible with SHA1.  We can
obtain the code below even though it is not merged to the main stream, yet.
(Thanks to the patch author.)</strong>

<br />

https://github.com/micropython/micropython-lib/pull/82/files

In addition, you need some authentication keys and secrets for Twitter.
You can obtain
them at https://dev.twitter.com/oauth/overview/application-owner-access-tokens.
You can apply them to the variables in the tweet.py as following.

```python
CK = ''     # CONSUMER_KEY
CS = ''     # CONSUMER_SECRET
AT = ''     # ACCESS_KEY
AS = ''     # ACCESS_SECRET
```

Any question, please send email to github@jasut1n.com though I may not have time to answer clearly.

Thanks you.

Dela Torre, Justine 
