# run_multiple_commands.py
import sublime
import sublime_plugin

class extrairesourcestring(sublime_plugin.TextCommand): #Nome da classe precisa ser minuscula, não sei o motivo

    def exec_command(self, command):
        if 'command' not in command:
            raise Exception('Comando não encontrado!')

        args = None
        if 'args' in command:
            args = command['args']

        context = self.view
        if 'context' in command:
            context_name = command['context']
            if context_name == 'window':
                context = context.window()
            elif context_name == 'app':
                context = sublime
            elif context_name == 'text':
                pass
            else:
                raise Exception('Erro: "' + context_name + '".')

        if args is None:
            context.run_command(command['command'])
        else:
            context.run_command(command['command'], args)

    def run(self, edit, commands=None):
        if commands is None: # Se estiver vazio
            return  # not an error
        for command in commands:
            self.exec_command(command)
