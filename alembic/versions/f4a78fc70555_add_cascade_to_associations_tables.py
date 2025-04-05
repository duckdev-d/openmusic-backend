"""add_cascade_to_associations_tables

Revision ID: f4a78fc70555
Revises: 2a231e63c92f
Create Date: 2025-04-05 05:05:34.515795

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4a78fc70555'
down_revision: Union[str, None] = '2a231e63c92f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(
        'playlist_song_song_id_fkey', 'playlist_song', type_='foreignkey'
    )
    op.drop_constraint(
        'playlist_song_playlist_id_fkey', 'playlist_song', type_='foreignkey'
    )
    op.create_foreign_key(
        None, 'playlist_song', 'songs', ['song_id'], ['id'], ondelete='CASCADE'
    )
    op.create_foreign_key(
        None, 'playlist_song', 'playlists', ['playlist_id'], ['id'], ondelete='CASCADE'
    )
    op.drop_constraint(
        'user_playlist_playlist_id_fkey', 'user_playlist', type_='foreignkey'
    )
    op.drop_constraint(
        'user_playlist_user_id_fkey', 'user_playlist', type_='foreignkey'
    )
    op.create_foreign_key(
        None, 'user_playlist', 'users', ['user_id'], ['id'], ondelete='CASCADE'
    )
    op.create_foreign_key(
        None, 'user_playlist', 'playlists', ['playlist_id'], ['id'], ondelete='CASCADE'
    )
    op.drop_constraint('user_song_song_id_fkey', 'user_song', type_='foreignkey')
    op.drop_constraint('user_song_user_id_fkey', 'user_song', type_='foreignkey')
    op.create_foreign_key(
        None, 'user_song', 'users', ['user_id'], ['id'], ondelete='CASCADE'
    )
    op.create_foreign_key(
        None, 'user_song', 'songs', ['song_id'], ['id'], ondelete='CASCADE'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'user_song', type_='foreignkey')
    op.drop_constraint(None, 'user_song', type_='foreignkey')
    op.create_foreign_key(
        'user_song_user_id_fkey', 'user_song', 'users', ['user_id'], ['id']
    )
    op.create_foreign_key(
        'user_song_song_id_fkey', 'user_song', 'songs', ['song_id'], ['id']
    )
    op.drop_constraint(None, 'user_playlist', type_='foreignkey')
    op.drop_constraint(None, 'user_playlist', type_='foreignkey')
    op.create_foreign_key(
        'user_playlist_user_id_fkey', 'user_playlist', 'users', ['user_id'], ['id']
    )
    op.create_foreign_key(
        'user_playlist_playlist_id_fkey',
        'user_playlist',
        'playlists',
        ['playlist_id'],
        ['id'],
    )
    op.drop_constraint(None, 'playlist_song', type_='foreignkey')
    op.drop_constraint(None, 'playlist_song', type_='foreignkey')
    op.create_foreign_key(
        'playlist_song_playlist_id_fkey',
        'playlist_song',
        'playlists',
        ['playlist_id'],
        ['id'],
    )
    op.create_foreign_key(
        'playlist_song_song_id_fkey', 'playlist_song', 'songs', ['song_id'], ['id']
    )
