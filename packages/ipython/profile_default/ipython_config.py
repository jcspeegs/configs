c.TerminalIPythonApp.display_banner = True
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalInteractiveShell.editor = 'vim'

c.InteractiveShellApp.extensions = [
    'autoreload'
]

c.InteractiveShellApp.exec_lines = [
    '%autoreload 2'
]
