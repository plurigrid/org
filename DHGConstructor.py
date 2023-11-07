class DHGConstructor:
    HEADERS = {'Authorization': 'Bearer YOUR_GITHUB_TOKEN'}
    OUTPUT_NAME = "output_name"

    def __init__(self, base_url):
        self.base_url = base_url

    def run_loop(self):
        # Code to run the loop for constructing DHGs

    @staticmethod
    def construct_larger_dhg(dhgs):
        # Code to construct the larger DHG

if __name__ == "__main__":
    target_repos = ["repo1", "repo2", "repo3"]  # Add your target repositories here
    dhgs = []

    for repo in target_repos:
        BASE_URL = "https://api.github.com/repos/" + repo + "/"
        my_dhg = DHGConstructor(BASE_URL)
        my_dhg.run_loop()
        dhgs.append(my_dhg)

    DHGConstructor.construct_larger_dhg(dhgs)