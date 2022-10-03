import os
from pathlib import Path
from typing import List, Optional


class DownLoader:
    def __init__(self, base_link: str, save_path: Optional[str] = None) -> None:
        self.base_link = base_link
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

    def load_single(self, download_link: str = None) -> None:
        """Download the video from a given link.

        Args:
            download_link (str): Target link for video.
        """
        if not download_link:
            download_link = self.base_link
        os.system(f"you-get -o {self.save_path} {download_link}")

    def load_multiple(self, start: int, end: int) -> None:
        """Download multiple videos from `start` to `end`.

        Args:
            start (int): `p` starts from.
            end (int): `p` ends at.
        """
        indices: List[int] = list(range(start, end + 1))
        for index in indices:
            download_link = f"{self.base_link}?p={index}"
            self.load_single(download_link)

    def force_download(self) -> None:
        """Re-download the videos that fails with `.download` suffix."""
        list_dir = os.listdir(self.save_path)
        for item in list_dir:
            if item.endswith(".download"):
                old_name = self.replace_name(item)
                index = item.split("(", 1)[1].split(".", 1)[0].split("P")[1]
                os.system(f"you-get -o {self.save_path} {self.base_link}{index}")
                os.system(f"rm {self.save_path}/{old_name}")

    def check_fails(self) -> bool:
        """Check if the bulk downloading fails at some videos.

        Returns:
            bool: return `True` if some fails appear.
        """
        list_dir = os.listdir(self.save_path)
        return any([item.endswith(".download") for item in list_dir])

    def replace_name(self, origin_name: str) -> str:
        """Replace the file name string to the format that shell command could deal with.

        Args:
            origin_name (str): Original file name.

        Returns:
            str: Replaced file name.
        """
        return str(origin_name).replace(" ", "\ ").replace("(", "\(").replace(")", "\)")

    def clean_xml(self) -> None:
        """Remove the generated `xml` files."""
        for item in os.listdir(self.save_path):
            if item.endswith(".xml"):
                rm_item = self.replace_name(item)
                os.system(f"rm {self.save_path}/{rm_item}")

    def rename_file(self) -> None:
        """Rename the file for better readability."""
        os.system(f"rm {self.save_path}/.DS_Store")
        for item in os.listdir(self.save_path):
            if not item.startswith("P"):
                order, title = item.split("(", 1)[1].split(".", 1)
                old_name = self.replace_name(item)
                new_name = order + "_" + title.replace(" ", "_")
                new_name = new_name.replace("__", "_")
                extension = new_name.split(".")[-1]
                name_head = "_".join(new_name.split(".")[:-1])
                new_name = name_head + "." + extension
                new_name = new_name.replace(")", "").replace(" ", "").replace("-", "")
                os.system(f"mv {self.save_path}/{old_name} {self.save_path}/{new_name}")

    def bulk_download(self, start: int, end: int) -> None:
        """The full pipeline to process the bulk downloading.

        Args:
            start (int): `p` starts from.
            end (int): `p` ends at.
        """
        self.load_multiple(start, end)
        while self.check_fails():
            self.force_download()
        self.clean_xml()
        self.rename_file()
