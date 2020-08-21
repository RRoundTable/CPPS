'''
link: https://leetcode.com/problems/encode-and-decode-tinyurl/

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

'''

class Codec:
    '''
    Count
    The range of URLs that can be decoded is limited by the range of \text{int}int
    '''
    def __init__(self):
        self.tiny_to_original = {}
        self.index = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortened = 'http://'+ str(self.index) + '.com'
        self.tiny_to_original[shortened] = longUrl
        self.index += 1
        return shortened
        
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.tiny_to_original[shortUrl]
    
    
    
class Codec:
    '''
    variable length
    '''
    
    def __init__(self):
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.short_to_long = {}
        self.count = 0
    
    def get_string(self):
        c = self.count
        sb = ''
        while c > 0:
            c -= 1
            sb += self.chars[c % 62]
            c /= 62
        return sb
            
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.get_string()
        self.short_to_long[key] = longUrl
        self.count += 1
        return "http://tinyurl.com/" + key
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl.split("http://tinyurl.com/")[1]]
    
class Codec:
    '''
    hash code
    '''
    
    def __init__(self):
        self.short_to_long = {}
        
            
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortened = str(hash(longUrl))
        while shortened in self.short_to_long:
            shortened = str(hash(longUrl))
        self.short_to_long[shortened] = longUrl
        return "http://tinyurl.com/" + shortened
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl.split("http://tinyurl.com/")[1]]

import random

class Codec:
    '''
    random
    '''
    
    def __init__(self):
        self.short_to_long = {}
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def random_url(self):
        sb = ''
        for i in range(6):
            idx = random.randint(0, 61)
            sb += self.chars[idx]
        return sb
        
        
    def encode(self, longUrl: str) -> str:
        key = self.random_url()
        while key in self.short_to_long:
            key = self.random_url()
        self.short_to_long[key] = longUrl
        return "http://tinyurl.com/" + key
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl.split("http://tinyurl.com/")[1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))