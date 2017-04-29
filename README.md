# Go, Go Doc Get... Go!
Go Doc Get is a small Sublime Text 3 Plugin for quickly getting GoDocs from the standard library

![screen cast](https://github.com/lowellmower/go_doc_get/edit/master/screen_cast.gif)

### Installation:
Clone this repository and move the file into your Sublime Text 3 Packages path. Below is the default, however, if you've move your packages elsewhere, adjust the `cp` command accordingly.
```
git clone git@github.com:lowellmower/go_doc_get.git
cp go_doc_get/go_doc_get.py ~/Library/Application Support/Sublime Text 3/Packages/User/go_doc_get.py
```

Set your desired quick key binding for the plugin. Following the steps below will set the Mac `⌘ + SHIFT + /` as the key binding

1. Open sublime and run `⌘ + SHIFT + p` to open the command palette
2. Search Preferences: Key Bindings
3. Paste the `JSON` below or adjust to your liking
	```JSON
	[
		{
			"keys": ["super+shift+/"], "command": "go_doc_get"
		}
	]
	```
4. Restart Sublime
5. Highlight a package like `net/http` and the use your quick key
6. Read all the things...
7. Champagne 🍾🥂
