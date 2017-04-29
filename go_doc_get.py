import sublime
import sublime_plugin
import webbrowser

class GoDocGetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		
		for region in view.sel():
			selected = view.substr(region)

		webbrowser.open("https://golang.org/pkg/" + selected)
