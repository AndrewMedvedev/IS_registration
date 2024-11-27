from sqlalchemy import select
from src.services.db import DatabaseSessionService
from src.auth.models import Security


class ORMService(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()


    async def add_user(self, user):
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return {"message": 200}


    async def get_user(self,email: str ,hash_password: str):
        async with self.session() as session:
            user = await session.execute(
                select(Security).where(Security.email == email and Security.hash_password == hash_password)
            )
            try:
                return user.scalars().one()
            except Exception as _ex:
                print(_ex)
                
                
    async def replace_password(
            self,
            new_hashpass: str,
            email: str
    ) -> Security:
        async with self.session() as session:
            query = select(Security).where(Security.email == email)
            user = await session.execute(query)
            user = user.scalars().first()
            user.hash_password = new_hashpass 
            await session.commit()
            return user