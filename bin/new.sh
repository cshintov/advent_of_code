# """ 
# Script to start a new problem 
# 1. testfile
# 2. solutionfile
# 3. read_input file
# 4. test.txt
# 5. input.txt
# """

set -eou pipefail

problem=$1

mkdir $problem
cp ./templates/* $problem

mv $problem/{test_dayN.py,test_$problem.py}
cd $problem

for file in $(ls); do
    echo $file
    envsubst < $file | sponge $file
done

