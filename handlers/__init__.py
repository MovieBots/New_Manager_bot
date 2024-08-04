# handlers/__init__.py

# This file can be left empty if you are not consolidating imports here.
# If you want to import common handlers, you can do it like this:

from .start import start_command
from .help import help_command
from .premium import buy_premium_command, callback_query
from .admin import handle_admin_commands
from .user_stats import user_details_callback
