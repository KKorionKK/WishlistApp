from uuid import uuid4
import string
import secrets


async def create_invite_token():
    invitation_code = "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(20)
    )
    return invitation_code


async def get_unique_id():
    return str(uuid4())
