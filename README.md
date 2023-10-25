# oblig3-test

## Workflow
I wrote the run-tests.yaml file inside the workflows directory
> /.github/workflows/run-tests.yaml

This file makes sure that the test files run in github actions every time someone pushes to the main branch.

Before i could run the tests through github actions i hade to specify some dependencies.

I had to do the following steps:
1. Checkout and Setup
   - I had to specify this in the run-tests.yaml file by writing:
     <br>
     `uses: actions/checkout@v3`
3. Setup Python
   - I set up Python by adding:
     <br>
     `uses: actions/checkout@v4`
     <br>
     `with: python-version: '3.9'`
5. Install requirements
   - I installed the requirements by adding the line:
     <br>
     `run: pip install -r requirements.txt`
     <br>
     `working-directory: ${{ github.workspace }}`
7. Run tests
   - Lastly i added code to run the actual tests:
     <br>
     `run: pytest -v -s`
     <br>
     `working-directory: ${{ github.workspace }}`
