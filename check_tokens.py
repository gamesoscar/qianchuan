#!/usr/bin/env python3
"""
检查数据库中已配置的token信息
"""
import asyncio
from app.database import async_session_maker
from app.models.models import Credential

async def check_tokens():
    async with async_session_maker() as session:
        result = await session.execute(Credential.__table__.select())
        rows = result.fetchall()
        print('已配置的广告主token:')
        for row in rows:
            print(f'广告主ID: {row.advertiser_id}, 有token: {bool(row.access_token)}, 过期时间: {row.token_expires_at}')

if __name__ == '__main__':
    asyncio.run(check_tokens())
