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

# import esp
# esp.sleep_type(esp.SLEEP_MODEM)

global sta_if

def start_network():
    global sta_if
    import network
    sta_if = network.WLAN(network.STA_IF)

def wait_network_up():
    import time
    while not sta_if.isconnected():
        time.sleep_ms(100)
        print(sta_if.ifconfig())
    print("Now connected")
    print(time.ticks_ms(), "ms")

###############################################################################

def rm_tweet_txt():
    import os
    os.remove('tweet.txt')

start_network()
wait_network_up()

try:
    f = open('tweet.txt', 'r')
    str = f.read(4096)
    f.close()

    import usocket
    import ussl
    s=usocket.socket()
    addr = usocket.getaddrinfo("api.twitter.com", 443)[0][-1]
    s.connect(addr)
    s=ussl.wrap_socket(s)
    print(s)
    s.write(str)
    print(s.read(4096))
    s.close()
    rm_tweet_txt()
    
except:
    import tweet
    import esp
    esp.deepsleep(1)
