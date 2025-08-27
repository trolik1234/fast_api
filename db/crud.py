from sqlalchemy.future import select
from .models import User
from .connect import async_session

async def create_user(name, email):
    async with async_session() as session:
        user = User(name=name, email=email)
        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user

async def get_all_user():
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()
