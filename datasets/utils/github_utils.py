import requests


class GithubUtils:

    @staticmethod
    def generate_raw_url(owner=None, repository=None, owner_and_repository=None, branch=None, commit_hash=None, path=None):
        raw_url_base = "https://raw.githubusercontent.com"
        if not owner_and_repository:
            if not commit_hash:
                return f"{raw_url_base}/{owner}/{repository}/{branch}{path}"
            return f"{raw_url_base}/{owner}/{repository}/{commit_hash}{path}"
        if not commit_hash:
            return f"{raw_url_base}/{owner_and_repository}/{branch}{path}"
        return f"{raw_url_base}/{owner_and_repository}/{commit_hash}{path}"

    def convert_blob_to_raw_url(blob_url: str):
        if "#" in blob_url:
            blob_url = blob_url[0:blob_url.rfind("/")]
        return blob_url.replace(
            "github.com", "raw.githubusercontent.com").replace("/blob/", "/")

    @staticmethod
    def clone_code(raw_url=""):
        try:
            response = requests.get(raw_url)
            if response.status_code == 200:
                print(f"{response.status_code}: SUCCESS Code Clone")
                return response.text
            else:
                print(f"{response.status_code}: FAILED Code Clone")
        except:
            print("EXCEPTION: FAILED Code Clone")
        return ""
