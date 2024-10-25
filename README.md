# This project was made for CEE 506
Noah Jacobs, Valerie Tsao, Hana Kawashima, Ana Stringer
~ October 2024 ~

STEPS TO LINKING YOUR NOTEBOOK TO GITHUB

	1. CD to a new working directory in your local environment
 
	2. Type "git remote add origin https://github.com/nj142/cee506_class_project"


STEPS TO CREATING A NEW FEATURE BRANCH (You should NEVER edit or push main unless you are the merge master, so this is where you will push all your changes while programming.)

	1. CD to your working directory
 
	2. Type "git co -b feature/your-new-branch-name"
 
	3. Type "git push -u origin feature/your-new-branch-name"
 
	
STEPS TO PUSHING CHANGES TO YOUR REMOTE FEATURE BRANCH (Run Git commit every time you finish a working function or code block-- should be every 20 minutes or so.  You can push to your remote branch at the end of each programming session to save progress.)

	1. CD to your feature branch to make sure you are not editing your local main repository.
 
	2. To track any new files you create don't forget to type "git add ."
 
	3. To commit changes to your local branch type "git commit -am "Changes description""
 
	4. Once you want to back up the cloud, push with "git push origin feature/my-feature" 


STEPS TO MERGING YOUR CODE WITH THE MAIN REPOSITORY

	1. DO NOT PUSH to main!  Instead, once you are ready to merge your code files, you can go to GitHub on a browser to create a PULL REQUEST.
   (Pull requests are a different feature than the Git pull command, which just updates your local repository to match the main-- instaed, a PULL REQUEST is how you submit your code branch for review to merge to the main.)

	2. Once that merge is reviewed by the team and approved by the merge master, the merge master then can use git merge to combine your remote branch to the remote main.  Then you can delete the old branch from your local and remote repositories-- it has been merged to the main and is now part of the shared program.
Delete your merged branch using:

		"git branch -d feature/my-feature"
		"git push origin --delete feature/my-feature"
