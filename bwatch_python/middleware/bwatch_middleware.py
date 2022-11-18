"""
ASGI MIDDLEWARE
"""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from .models import SessionProperties, EnvironmentDetails

class BWatchAsgiMiddleware(BaseHTTPMiddleware):
    def __init__(
            self,
            app,
            some_attribute: str,
    ):
        super().__init__(app)
        self.some_attribute = some_attribute

    
    async def app(self, request: Request):
        return

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive


    async def dispatch(self, request: Request, call_next):

        method = request.method
        url = str(request.url)
        headers = dict(request.headers)
        query_params = dict(request.query_params)
        path_params = dict(request.path_params)
        client = {"host": request.client.host, "port": request.client.port} 
        cookies = request.cookies

        try:
            await self.set_body(request)
            jsonbody = await request.json()
        except:
            jsonbody = {}

        session = SessionProperties(method=method, url=url, headers=headers, query_params=query_params, path_params=path_params,
        client=client, cookies=cookies, body=dict(jsonbody))

        ennivronment = EnvironmentDetails(language="Python", version="", package="FASTAPI", other_details={})


        response = await call_next(request) 
        # response = Response(body, media_type='text/plain')
        
        return response