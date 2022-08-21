### Accessing the site explanation

The user types the url/domain name(www.foobar.com) that points to the 
IP address of the respective server (8.8.8.8) in the browser.
The browser checks its cache for the IP address,
if not found it checks the operating system's cache, if it still doesn't locate it in the OS's
cache it checks with the resolver which is usually the Internet Service Provider (ISP).

If the ISP doesn't have the IP address in its cache,
it goes to the root server where the root server redirects it TOP Level Domain (TLD) server. the resolver saves the provided information.
The resolver checks with the .com TLD server and is redirected to the authoritative name servers.
The resolver/ISP caches the content from the name server i.e the IP address and sends the request to the IP address(8.8.8.8).

----
### specifics

**What is a server ->** Computer hardware or software that provides 
functionality for other programs/devices

**Role of the domain name ->** points to an IP address

**What type of DNS record www is in www.foobar.com ->** CNAME record

**Role of the web server ->** hosts websites and handle requests via the HTTP protocol

**Role of the application server ->** hosts web apps and process dynamic site contents

**Role of the database ->** recieves requests from the application server and returns
required data.

**What is the server using to communicate with the computer of the user requesting the website
->** HTTP requests

----
### Issues

**Single Point Of Failure (SPOF) ->** this is a part of a system that if fails, the 
entire system stops working.
In this case the **SPOF** is the single server.

**Scale ->** scalabillity is an issue since its only a single server, if requests increase
it won't be able to handle the amount of traffic and might crash.
