import discord
import argparse
from ..client import VemtClient


class ExitProcess:

    @classmethod
    def setupSubCommand(cls, subparser: argparse._SubParsersAction):
        parser = subparser.add_parser("+exit",
                                      help="BOTを終了します（開発時専用コマンドです）")
        parser.set_defaults(handler=ExitProcess)

    @classmethod
    async def authenticate(cls, args, client: discord.Client, message: discord.Message) -> bool:
        return True

    @classmethod
    async def run(cls, args, client: discord.Client, message: discord.Message):
        await message.channel.send('OK, See you.')
        await client.close()

    @classmethod
    def addProcessor(cls):
        VemtClient.addSubCommand(ExitProcess)
