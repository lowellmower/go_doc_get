import sublime
import sublime_plugin
import webbrowser

def cleanPackage(pkgURI):
	pkg = pkgURI.split('.com/')[1]
	return pkg

class GoDocGetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		
		for region in view.sel():
			selected = view.substr(region)

		if "github.corp" in selected:
			# if corporate go to page
			pkg = cleanPackage(selected)
			webbrowser.open('https://github.corp.dyndns.com/' + pkg)
		elif "github" in selected:
			# if public package go to doc
			pkg = cleanPackage(selected)
			webbrowser.open('https://godoc.org/github.com/' + pkg)
		else:
			# default to golang proper
			webbrowser.open('https://golang.org/pkg/' + selected)
