from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "comments" ADD "identifier" JSONB NOT NULL;
        ALTER TABLE "comments" DROP COLUMN "position_id_id";
        DROP TABLE IF EXISTS "positionaldata";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "comments" ADD "position_id_id" INT NOT NULL;
        ALTER TABLE "comments" DROP COLUMN "identifier";
        ALTER TABLE "comments" ADD CONSTRAINT "fk_comments_position_a1d5b3f8" FOREIGN KEY ("position_id_id") REFERENCES "positionaldata" ("id") ON DELETE CASCADE;"""
