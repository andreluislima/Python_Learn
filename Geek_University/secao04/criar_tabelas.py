import asyncio

from core.database import engine, DBBaseModel

async def create_tables() -> None:
    # Garanta que os models sejam importados antes do create_all
    import models.__all__models  # ok se existir e importar tudo

    print("Criando as tabelas no banco de dados")

    async with engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.drop_all)
        await conn.run_sync(DBBaseModel.metadata.create_all)

    print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    asyncio.run(create_tables())
