# Gateway
Use lanyard's websocket easily!
## Example:
```py
session = hawser.Gateway(793467584820281346)
# You can add more user easily like this:
# session = hawser.Gateway(793467584820281346, user_id_2, user_id_3, ...)
# session = hawser.Gateway(793467584820281346, 705665813994012695)
```
# Attributes
- `ids` - List of Added IDs.
    - Default: `[]`
- `ws` - The Websocket Connection.
    - Default: `None` (Changes when session starts.)
- `heartbeat` - Websocket Heartbeat.
    - Default: `30` (Changes when session starts.)
- `session` - The Websocket Session.
    - Default: `None` (Changes when session starts.)
- `event_loop` - The Event loop for Gateway.
    - Default: `asyncio.get_event_loop()`

# Functions
## on_ready
Add a function for handle ready.
- Parameters:
    - function (`async function`): The function is runned when gateway is ready. Function needs to have one parameter (data) and should be async.
- Returns:
    - `True`: Function added successfully.
- Example:
    ```py
    # ...
    async def ready(packet):
        print("Ready With:", packet)

    session.on_ready(ready)
    ```
## on_message
Add a function for handle messages.
- Parameters:
    - function (`async function`): The function is runned when receive a message. Function needs to have one parameter (data) and should be async.
- Returns:
    - `True`: Function added successfully.
- Example:
    ```py
    # ...
    async def msg(packet):
        print("Got a Message from Connection:", packet)

    session.on_message(msg)
    ```
## start
Start the connection in new task.
- Returns:
    - `True`: Connection is Started.
- Example:
    ```py
    # ...
    session.start()
    ```
## start_and_wait
Start the connection and wait.
- Returns:
    - `None`
- Example:
    ```py
    # ...
    session.start_and_wait()
    ```