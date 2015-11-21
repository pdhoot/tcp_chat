# tcp_chat   [![Build Status](https://travis-ci.org/pdhoot/tcp_chat.svg?branch=master)](https://travis-ci.org/pdhoot/tcp_chat)

> A chat app built over TCP

tcp_chat is an app that allows you to create chat servers and clients to connect to the chat server.
It's built over python's socketAPI.

## Current Feautures

* Create servers which resemble rooms in various chatting platforms
* Password protected rooms
* Send messages to all the clients connected to that chat room


## TODOS

* Tests
* Encryption to the messages
* Sound based notification to alert the users on an incoming-message
* Daemonize the server, so that it runs in the background.
* Decide a better color scheme.

## Requires
* [clint](https://github.com/kennethreitz/clint)

## Installation
`[sudo] pip install tcp_chat`

That's it!

## Usage

* Start a server `tcp_chat --server <interface> <password>`
* Connect to the server `tcp_chat --client <interface> <password>`
* Start chatting!

## Screenshots
![Screenshot1](http://i.imgur.com/561prSC.png)



![Screenshot2](http://i.imgur.com/DXy2E2z.png)

## License
MIT © [Punit Dhoot](https://github.com/pdhoot)

