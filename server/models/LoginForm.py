from typing import Optional
from fastapi import Request

class LoginForm:
  def __init__(self, request: Request):
    self.request = request
    self.username : Optional(str) = None
    self.password : Optional(str) = None

  async def _load_form_data(self):
    form = await self.request.form()
    self.username = form.get("username")
    self.password = form.get("password")
