# Stacks and Queues
code challenge 10 
## Challenge
sing a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue
## Approach & Efficiency
Stacks
push >>> O(1)
pop >>> O(1)
peek >>> O(1)
is_empty >>> O(1)
Queues
enqueue >>> O(1)
dequeue >>> O(1)
peek >>> O(1)
is_empty >>> O(1)
## API
pushto push onto a stack and push multiple values onto a stack
pop to pop off the stack or empty a stack after multiple pops
peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
is_empty returns true when stack is empty otherwise returns false.
Queues
enqueue Nodes or items that are added to the queue.
dequeue Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
peek When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
is_empty returns true when queue is empty otherwise returns false.

<!-- Description of each method publicly available to your Stack and Queue-->