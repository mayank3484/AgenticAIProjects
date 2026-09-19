from agents import function_tool
import logging
import httpx

logger=logging.getLogger(__name__)

def validate_pr_url(pr_url:str)->bool:
    parts=pr_url.split("/")
    if len(parts)!=7 or parts[5] not in ["pull","pulls"]:
        raise Exception("Invalid PR Detected")
    owner=parts[3]
    repo=parts[4]
    pr_number=parts[6]

    return owner,repo,pr_number

@function_tool
def fetch_pull_request_diff(pr_url:str):
    """
    Description: Fetch the diff from pull request
    Arguments: pr_url:str
    Returns: the consoliated diffs from the pr.
    """
    owner,repo,pr_number=validate_pr_url(pr_url=pr_url)
    logger.info(f"owner:{owner}, repo:{repo}, pr_number:{pr_number}")
    file_url=f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    response=httpx.get(file_url)
    if response.status_code==200:
        files=response.json()
        if not files:
            raise Exception(f"the PR {pr_number} doesn't have any file")
        diffs=[]
        for file in files:
            filename=file.get("filename")
            patch=file.get("patch")
            deletions=file.get("deletions")
            additions=file.get("additions")
            status=file.get("status")
            diff_header=f" --{filename} ({status}, +{additions}/-{deletions})--"
            diffs.append(f"{diff_header}\n{patch}")
        return "\n\n.join(diffs)"
    else:
        raise Exception("Error while loading the files from the PR")