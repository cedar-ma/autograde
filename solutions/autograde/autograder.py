import os

import numpy as np
import pandas as pd


class Autograde:
    def __init__(self, assignment_name, submissions_path):
        self.assignment_path = os.path.join(submissions_path, assignment_name)
        self.assignment = assignment_name
        self.get_repos()

        # Initialize a dataframe with student names
        self.grades = pd.read_excel("/Users/cedar/data/PGE311_Sp23/solutions/grades.xlsx", index_col=0)
        # Create a new assignment column
        self.grades[f"{assignment_name}"] = np.zeros_like(self.submissions)

        # Populate dataframe with students scores
        self.get_scores()

        # Write out new gradesheet
        self.grades.to_excel("/Users/cedar/data/PGE311_Sp23/solutions/grades.xlsx")

    def get_repos(self):
        self.submissions = [f.path for f in os.scandir(self.assignment_path) if f.is_dir()]
        return

    def get_scores(self):
        for submission in self.submissions:
            gh_username = self._get_github_usernames(self, repo_name=submission)
            print(gh_username)
            try:
                submission_df = pd.read_csv(f"{submission}/student_score.csv")
                assignment_score = submission_df["Student Score"].to_numpy()[0]
                self.grades.at[gh_username, self.assignment] = assignment_score
            except:
                continue
        return

    @staticmethod
    def _get_github_usernames(self, repo_name):
        return os.path.basename(repo_name)
#        repo_name = repo_name.rsplit('/', 1)[-1]
#        return repo_name.split('-', 1)[-1]


if __name__ == "__main__":
    # Set submission path and assignment name
    submission_path = "/Users/cedar/data/PGE311_Sp23/Submissions/"
    assignment = "Project_1"

    # Initialize and run Autograder
    autograder = Autograde(assignment, submission_path)

