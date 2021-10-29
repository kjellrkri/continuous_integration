# continuous_integration
school assignment on continuous integration

What i have done:
  I added a workflow folder containing a .yml file 
  from a boilerplate code template. The .yml is
  applying the continuous integration workflow to
  my repository.
  
  I have set the github actions to run on both push
  and pull requests.
  
  The github actions use ubuntu-latests as base image.
  This is an operating system for linux which the
  github actions run on.
  
  I use the github action "actions/checkout@v2" which
  checks out the code from the repository so that we
  can run assosiated actions on the code later.
  
  The contineous integration workflow sets up the defined
  python version (which in my case is 3.9) onto the base image.
  
  The github action "Install dependencies" upgrades to
  latest version of pip, and installs all dependencies
  that i have defined in the requirement.txt file, as
  well as flake 8 which we need to run the
  github actions.
  
  The github action "linting" performs linting on my
  python code. That is to say, that it highlights
  syntactical and stylistic prblems (pep 8) in my python
  code. The linter uses flake8 which enforces the pep8
  formating standard.
  
  I have fail-on-isort set to false in the github action
  "commit isort changes" automatically commits and
  pushes isort shanges made by our workflow,
  to the github repository. Isort sorts the imports in my
  python code in alphabetical order. In order to enable
  this github action i had to create a github secrets
  token and add it to the repository under
  continuous_integration repo>setting>secrets>new repository secret
  and called the Actions secret "GH_ACCESS_TOKEN".
  I generated the secret token through:
  user>settings>developer settings>generate new token
  I gave the token access to the repository and workflow.
  
  The github action "Test with pytest" finds the test
  folder in the pyton project and runs pytest on any
  python files starting with test.
  
  When i push a commit i go to the "Actions" tab on
  github to check if the code was pushed or if the
  run failed which stopped the push. If the run failed,
  i also get an email from git stating that the run
  failed so that i can performe the fixes and push again.
  
  SOURCES:
  Tutorial i used to understand how to implement
  contineous integration in python:
  - https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
  - https://github.com/alexanderdamiani/test_repo_pylinter_v1
  - https://github.com/alexanderdamiani/test_repo_pylinter_v2
  
