# Required packages
import unittest
import nbconvert

# Assignment-specific packages
import numpy as np
import pandas as pd
# Convert the assignment Jupyter notebooks into something we can import
with open("Assignment_2.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("Assignment_2.py", "w") as f:
    f.write(python_file)

# Import the converted file. Best to import only the variables you want to test
from Assignment_2 import answer_1a, answer_1b, answer_1c, answer_1d, answer_1e, answer_1f, AB, BA, LHS, RHS, answer_1i

# Here is where you will write your tests
class TestSolution(unittest.TestCase):
    # You can fill this out if you are testing functions/classes, or want private tests
    # The name must be setUp(self)

    def setUp(self):
        pass

    # All tests need to start with "test_..."
    def test_q1(self):
        # Numpy has an extensive test suite.
        # It's best to use allclose instead of equal to avoid problems with machine precision
        np.testing.assert_allclose(answer_1a, 1)
        return


    def test_q2(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution
       
        np.testing.assert_allclose(answer_1b, 0)
        return
        
    def test_q3(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution
       
        np.testing.assert_allclose(answer_1c, 90.0)
        return

        
    def test_q4(self):
        # Instead, it's better to hardcode the solution if possible
        q4_soln = np.array([[-8],[6],[-17],[-14]])
        np.testing.assert_allclose(answer_1d, q4_soln)
        return
        
    def test_q5(self):
        # Instead, it's better to hardcode the solution if possible
        q5_soln = np.array([[42],[23],[15]])
        np.testing.assert_allclose(answer_1e, q5_soln)
        return
        
    def test_q6(self):
        # Instead, it's better to hardcode the solution if possible
        q6_soln = np.array([[-12]])
        np.testing.assert_allclose(answer_1f, q6_soln)
        return

    def test_q7(self):
        # Instead, it's better to hardcode the solution if possible
        q7_soln = np.array([[1,3,-1],[-7,6,4],[7,3,5]])
        np.testing.assert_allclose(AB, q7_soln)
        q7_soln = np.array([[12,-3,11],[5,5,3],[-8,7,-5]])
        np.testing.assert_allclose(BA, q7_soln)
        return

    def test_q8(self):
        # Instead, it's better to hardcode the solution if possible
        q8_soln = np.array([[25,9,11],[0,23,10],[-8,-1,14]])
        np.testing.assert_allclose(LHS, q8_soln)
        q8_soln = np.array([[25,9,11],[0,23,10],[-8,-1,14]])
        np.testing.assert_allclose(RHS, q8_soln)
        return
        
    def test_q9(self):
        # Instead, it's better to hardcode the solution if possible
        q9_soln = np.array([[2.,-1.,1.],[3.,0.,4.],[0.,3.,-1.]])
        np.testing.assert_allclose(answer_1i, q9_soln)
        return
        


if __name__ == "__main__":
    tester = unittest.main(verbosity=2, exit=False)

    # Count number of total tests
    total_tests = tester.result.testsRun

    # Number of failed, errors, and skipped tests
    num_failures = len(tester.result.failures)
    num_errors = len(tester.result.errors)
    num_skipped = len(tester.result.skipped)

    # Final student score
    student_score = total_tests - (num_failures + num_errors + num_skipped)
    print(f"Score: {student_score}/{total_tests}")

    # Write student score to Pandas dataframe
    score_df = pd.DataFrame(
        {
            "Total Tests": total_tests,
            "Number of Test Failures": num_failures,
            "Number of Test Errors": num_errors,
            "Number of Skipped Tests": num_skipped,
            "Student Score": student_score,
        }, index=[0])

    # Write dataframe to csv
    score_df.to_csv("student_score.csv", index=False)
