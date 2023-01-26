## Programming task for Visma Solutions - Summer Trainee 2023: Software Developer

This is a programming task for Visma Solutions Summer Trainee 2023 recruitment process.

### Description

The way I understood the problem was that the most important thing was validating the URI, so that it is in a correct form. Of course, the main purpose of the IdentifyRequest class is to identify what the path and parameters of the request are, but validating the URI was an important part of making it. One thing I wasn't sure of was if the source parameter could have numbers in it or not, so I decided not to check it. 

I used Pythons urllib for parsing, since I thought it would be the simplest way, even though the string needed parsing was an URI. There might have been easier ways, but that is what I ended up with. 

My biggest challenge was probably the client. I didn't really understand how it was supposed to be, so I ended up doing a small program. You can give an URI to the program, and it uses the IdentifyRequest class to give the path and the parameters if the URI is in correct form. 

You can use the client program by running the client.py file. 
