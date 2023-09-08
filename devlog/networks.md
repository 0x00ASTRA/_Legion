# Devlog #1: Networks

## The Problem
Networks need to analog real-life networks. The clearnet will focus on the most effecient path
for relaying network traffic, while the darknet will focus on privacy. So how do we aproach this?

### Clearnet 🌐
```
[node-1]--->[node-2]--->[destination]
```
Nodes will have connections with neighboring nodes thus traffic would have a predeterminded path based on the geneis and destination of the packet.
### Darknet 🧅
```
[node-1]--->[node-rand1]--->[node-rand2]--->[node-rand3]--->[destination]
```
Nodes will connect to random nodes within the network to obscure the origin node, mimicking The Onion Router.
