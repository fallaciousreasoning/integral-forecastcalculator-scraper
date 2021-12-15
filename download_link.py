class DownloadLink:
    def __init__(self, folder_name: str, file_name: str) -> None:
        self.folder_name = folder_name.replace('\\\\', '\\')
        self.file_name = file_name
    
    def download_path(self):
        return f'/Simulate/Download?folderName={self.folder_name}&fileName={self.file_name}'