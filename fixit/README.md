# Testing

To test http requests, use curl commands

## get information on a player (in this instance player 1)
`curl -X GET http://127.0.0.1:5000/orders/1`

## Add order for player
`curl -X PUT http://127.0.0.1:5000/orders/1 -H "Content-Type: application/json" -d '{"value":"5","type":"BUY","task":"ADD"}'`

## Delete order for player
`curl -X PUT http://127.0.0.1:5000/orders/1 -H "Content-Type: application/json" -d '{"value":"5","type":"BUY","task":"DELETE"}'`
