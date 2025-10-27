#!/usr/bin/env python3
from dev_aberto import hello
import gettext
from babel.dates import format_datetime
from datetime import datetime
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    print(_('Último commit feito em:'), format_datetime(date), _(' por'), name)
