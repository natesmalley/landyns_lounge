import httpx
from httpx import ASGITransport

class CompatClient(httpx.Client):
    """Compatibility wrapper adding the deprecated 'app' parameter."""

    def __init__(self, *args, app=None, transport=None, **kwargs):
        if app is not None and transport is None:
            transport = ASGITransport(app=app)
        super().__init__(*args, transport=transport, **kwargs)

httpx.Client = CompatClient

