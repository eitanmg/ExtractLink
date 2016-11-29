# ExtractLink
Extract URLs from any given text data (txt, html, mbox, etc)

# Usage
put your data (can be multiple files) in the `Emails` folder, add domains that you want to exclude from the result in `Whitelist`, and click start.

the result will be in the `Results` folder.

install dependencies tldextract https://github.com/john-kurkowski/tldextract

# Example - Input:

`
Python (programming language) - Wikipedia https://en.wikipedia.org/wiki/Python_(programming_language)
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its ...
Developer?: ?Python Software Foundation	Paradigm?: ?multi-paradigm?: ?object-oriented?, ?im...
Typing discipline?: ?duck?, ?dynamic?, ?strong?, ?grad...	Designed by?: ?Guido van Rossum
xkcd: Python
https://xkcd.com/353/
Image URL (for hotlinking/embedding): http://imgs.xkcd.com/comics/python.png. [[ Guy 1 is talking to Guy 2, who is floating in the sky ]] Guy 1: You're flying! How?
Python - Reddit https://www.reddit.com/r/Python/
"Automate the Boring Stuff with Python" Udemy course is free on Monday: Use code "R_PYTHON" (udemy.com). submitted 9 hours ago by AlSweigartAuthor of ...
Python Syntax | Codecademy https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1?...id...
Python is an easy to learn programming language. You can use it to create web apps, games, even a search engine! Ready to learn Python? Click Save ...
Google's Python Class | Python Education | Google Developers https://developers.google.com/edu/python/
Mar 9, 2016 - Welcome to Google's Python Class -- this is a free class for people with a little bit of programming experience who want to learn Python.
`

# Example - Output:

`
https://en.wikipedia.org/wiki/Python_(programming_language)
https://xkcd.com/353/
https://www.reddit.com/r/Python/
https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1?...id
https://developers.google.com/edu/python/
`



