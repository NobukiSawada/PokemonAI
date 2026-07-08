"""Smoke test: confirm poke-env can drive two RandomPlayers against the local
Showdown server started with `node pokemon-showdown start --no-security`.

Run with the local server up:
    python tests/smoke_random_battle.py
"""

import asyncio

from poke_env.player import RandomPlayer


async def main() -> None:
    player_1 = RandomPlayer(battle_format="gen9randombattle", max_concurrent_battles=1)
    player_2 = RandomPlayer(battle_format="gen9randombattle", max_concurrent_battles=1)

    await player_1.battle_against(player_2, n_battles=3)

    print(f"{player_1.username} won {player_1.n_won_battles} / {player_1.n_finished_battles}")
    print(f"{player_2.username} won {player_2.n_won_battles} / {player_2.n_finished_battles}")


if __name__ == "__main__":
    asyncio.run(main())
