import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Ensure Alembic can find the `app` directory
sys.path.append(".")

# Import your models
from app.models.models import Base

# Load Alembic configuration
config = context.config

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata for Alembic
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    In this mode, Alembic doesn't connect to the DB but generates SQL scripts.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    Here, Alembic connects to the DB and applies migrations directly.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine whether to run offline or online mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
