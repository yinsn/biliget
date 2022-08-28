import os
from pathlib import Path
from typing import Optional


class DownLoader:
    def __init__(self, save_path: Optional[str] = None) -> None:
        self.save_path = save_path
        self._check_path()

    def _check_path(self) -> None:
        """Check if the existence of path for dumped data.
        Create one if not.
        """
        if not self.save_path:
            self.save_path = os.path.join(os.getcwd(), "bilivideos")
        else:
            self.save_path = os.path.join(os.getcwd(), self.save_path)
        if not Path(self.save_path).exists():
            os.makedirs(self.save_path)
