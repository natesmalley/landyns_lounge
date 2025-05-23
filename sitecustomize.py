import httpx


class PatchedClient(httpx.Client):
    def __init__(self, *args, **kwargs):
        kwargs.pop("app", None)
        super().__init__(*args, **kwargs)


httpx.Client = PatchedClient
