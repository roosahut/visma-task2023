# Programming task for Visma Solutions - Summer Trainee 2023: Software Developer

This is a programming task for Visma Solutions Summer Trainee 2023 recruitment process.

### Description

The way I understood the problem was that the most important thing was validating the URI, so that it's in a correct form. Of course the IdentifyRequest -classes main purpose is to identify what is the path and parameters of the request, but validating the URI was an important part of making it. One thing I wasn't sure of was if the source parameter could have numbers in it or not, so I decided not to check if it only has letters and not numbers in it.

I used Pythons urllib for parsing, since I thought it would be the simplest way, even though the string needed parsing was an URI. There might have been easier ways, but in the short amount of time that is what I ended up with.

My biggest challenge was probably the client. I didn't exactly understand what and how it was suppoused to be, so I ended up doing a small program to which you can give the URI to and it gives it to the IdentifyRequest class and either returns the path and the parameters if the URI is in a correct form, or returns the error the IdentifyRequest class gives.

You can use the client program by running the client.py file.