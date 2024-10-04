import my_script

# import unittest

# # import pprint


def test_get_latest_commit():
    latestCommit = my_script.get_latest_commit()
    assert latestCommit["commit"]["committer"]["name"] == "Raisul Islam Shehab"


def test_get_open_issues():
    response = my_script.get_open_issues()
    latestIssue = response[0]
    assert (
        latestIssue["repository_url"]
        == "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython2"
    )


# test_get_latest_commit()
# test_get_open_issues()


# class TestMyScript(unittest.TestCase):
#     def test_get_latest_commit(self):
#         response = my_script.get_latest_commit()
#         self.assertEqual(response.status_code, 200)

#     def test_get_open_issues(self):
#         issues = my_script.get_open_issues()

#         latestIssue = issues[0]
#         # print(latestCommit)
#         self.assertEqual(
#             latestIssue["repository_url"],
#             "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython",
#         )


# if __name__ == "__main__":
#     unittest.main(verbosity=2)

# # python -m coverage run -m unittest
# # python -m coverage report
