# Gateway Example With Multiple User
import hawser

session = hawser.Gateway(793467584820281346, 705665813994012695)


async def ready(packet):
    print("Ready:", packet)


async def message(packet):
    print("Got Message:", packet)

# Add Functions
session.on_ready(ready)
session.on_message(message)

# Start the Session
# You can use <Gateway>.start() if you want to open new task.
session.start_and_wait()
