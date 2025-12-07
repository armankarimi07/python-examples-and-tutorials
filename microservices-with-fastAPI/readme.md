```
> uvicorn main:app --reload
```

In microservices, every service should have its own database

IMPORTANT: requests package and requests package from fastapi could cause conflict with each other
(possibly, not always)

we use Redis Streams to invoke events
(to reduce the count of products after each order)

These events will be received by consumers
we will use Redis Consumer Groups to control how we listen to these events

Without using consumer groups, every consumer gets all the messages, which is not ideal.

run both services in separate terminals, and the consuer in a third terminal.
(since the consumer script creates the group first, the log message may appear different the first few times)

with all three terminals running, make another order,
look at the consumer terminal, you should see the output is populated with event's data
the event that we sent from order_completed background task.

Now we can use this event triggering and capturing mechanism to dynamically reduce the quantity of products upon orders getting completed.

- Need to add a Refund mechanism (event driven architecture)
if the product got deleted during or after customer placed an order,
customer will have paid for a product that does not exist,
therefore we need to refund the customer with another event.