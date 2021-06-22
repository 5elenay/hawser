class UserNotMonitoredError(Exception):
    """Raises when user not monitored."""

    pass


class LanyardException(Exception):
    """Raises when lanyard gives success false but we don't have a support for the exception."""

    pass
