"""initial migration

Revision ID: 2a231e63c92f
Revises:
Create Date: 2025-04-05 04:33:16.787959

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a231e63c92f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            'created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
    )
    op.create_table(
        'playlists',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('is_public', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            'created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'songs',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('duration_seconds', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('relative_file_path', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            'created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'playlist_song',
        sa.Column('playlist_id', sa.Integer(), nullable=True),
        sa.Column('song_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['playlist_id'],
            ['playlists.id'],
        ),
        sa.ForeignKeyConstraint(
            ['song_id'],
            ['songs.id'],
        ),
    )
    op.create_table(
        'user_playlist',
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('playlist_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['playlist_id'],
            ['playlists.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
    )
    op.create_table(
        'user_song',
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('song_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['song_id'],
            ['songs.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user_song')
    op.drop_table('user_playlist')
    op.drop_table('playlist_song')
    op.drop_table('songs')
    op.drop_table('playlists')
    op.drop_table('users')
