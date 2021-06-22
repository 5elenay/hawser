from aiohttp import ClientSession
from hawser.meta import __api__
from hawser.utils import raise_error
from hawser.errors import UserNotMonitoredError, LanyardException


async def fetch_user(id: int) -> dict:
    """Fetch user presence informations.

    Parameters:
        id (int): User ID.

    Returns:
        dict: User informations.

    Raises:
        hawser.errors.UserNotMonitoredError: User is not being monitored by Lanyard. 
        hawser.errors.LanyardException: Other exceptions.
    """

    raise_error(id, "id", int)

    async with ClientSession() as session:
        async with session.get("{0}{1}".format(__api__, id)) as result:
            data = await result.json()

            if not data["success"]:
                error_dict = data["error"]
                raise_class = UserNotMonitoredError if error_dict[
                    "code"] == "user_not_monitored" else LanyardException

                raise raise_class(error_dict["message"])
            else:
                return data["data"]
