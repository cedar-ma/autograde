#!/bin/bash

submissions="/Users/cedar/data/PGE311_Sp23/Submissions/Project_1"
test_path="/Users/cedar/data/PGE311_Sp23/solutions/Project_1_original/test.py"

cd "$submissions"
for d in */
do
    cp "$test_path" "$d"
    cd "$d"
    python test.py
    cd "$submissions"
done

