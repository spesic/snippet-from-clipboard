import sublime, sublime_plugin
class InsertSnippetAndClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    for region in self.view.sel():
      if not region.empty():
        replacement = self.view.substr(region)
        args['contents'] = args['contents'].replace('$SELECTION_OR_CLIPBOARD', replacement)
        self.view.run_command('insert_snippet', args)
      else:
        replacement = sublime.get_clipboard().strip()
        args['contents'] = args['contents'].replace('$SELECTION_OR_CLIPBOARD', replacement)
        self.view.run_command('insert_snippet', args)
