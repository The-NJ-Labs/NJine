import textual
from textual.widgets import DirectoryTree
from textual.app import App # RIGHT

class Explorer(DirectoryTree):
    def on_mount(self) -> None:
        self.border_title = "NJine Explorer"
        
