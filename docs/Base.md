# Attributes
- `__v__` - Lanyard API Version.
- `__api__` - Lanyard REST API Url.
- `__socket__` - Lanyard WebSocket Url.
- `__version__` - Hawser Version.

# Functions
## fetch_user
Fetch User with ID.
- Parameters:
    - id (`int`): The User ID.
- Returns:
    - `dict`: User informations.
- Raises:
    - `hawser.errors.UserNotMonitoredError`: User is not being monitored by Lanyard. 
    - `hawser.errors.LanyardException`: Other exceptions.
- Example:
    ```py
    result = await hawser.fetch_user(793467584820281346)
    print(result)
    ```

# Classes
## Gateway
[Click Here for Documentation](https://github.com/5elenay/hawser/blob/main/docs/Gateway.md)