# autograde
autograde assignments collected from github classroom

- Beside this `solutions` folder, create a `submission` folder side by side
- In `grades.xlsx`, the first three columns are github_username, ut_eid and student_names, the next column will be autograded scores
- `cd solutions/autograde` `vi distribute_tests.sh`, make **submissions** variable corresponding to one specific submission subfolder path and **test_path** variable pointed to correct answers **`test.py`** in one specifc assignment folder under `solutions`
- In `autograde` directory, run `./distribute_tests.sh`
- `vi autograder.py` **pd.read_excel** and **self.grades.to_excel** variables are linked with above `grades.xlsx` path. Edit **submission_path** and **assignment** variable names in main function.
- In `autograde` directory, run `python autograder.py`
