# This project was made for CEE 506
Noah Jacobs, Valerie Tsao, Hana Kawashima, Ana Stringer
~ October 2024 ~

Steps to linking your local notebook to the remote github branch

	1. CD to a new working directory in your local environment
 
	2. Type "git remote add origin https://github.com/nj142/cee506_class_project"

 	3. This will let you push your changes to your local repository to save on the cloud (the remote repository)


Steps to creating a new feature branch
(You should not edit or push to the main branch unless you are the merge master, so this branch is where you will push all your changes while programming.)

	1. CD to your working directory
 
	2. Type "git checkout -b feature/your-new-branch-name" to create a new branch on your local repository
 
	3. Type "git push -u origin feature/your-new-branch-name" to update the remote repository with a copy of your new branch.  The -u means you can just use push and pull instead of having to type out the feature branch every time.
 
	
Steps to pushing your local code updates to the remote feature branch
(Note it is good practice to run git commit every time you finish a working function or code block-- around every 20 minutes or so.  You only really need to push to your remote branch at the end of each programming session.)

	1. Git checkout to your feature branch to make sure you don't accidentally update the main branch

	2. CD to your working directory to make sure you cover all files you updated
 
	3. To track any new files you created don't forget to type "git add ." (DO NOT DO THIS IF YOU HAVE API KEYS SAVED LOCALLY.  This will make your secrets public.)
 
	4. To commit changes to queue for upload type "git commit -am "Changes description""
 
	5. Once you want to back up the cloud, push with "git push origin feature/my-feature" (or just git push if you already used -u)


Steps to merging your remote feature branch with remote main repository once your code is finished & pushed to remote

	1. Don't push to main!  Instead, once you are ready to merge your code files, you can go to GitHub on a browser to create a pull request. (Pull requests are a different feature than the Git pull command, which just updates your local repository to match the remote-- instaed, a pull request is how you submit your code branch for review to merge to the main.)

	2. Once that merge is reviewed by the team and approved by the merge master, the merge master then can use git merge to combine your remote branch to the remote main.  Then you can delete the old branch from your local and remote repositories-- it has been merged to the main and is now part of the shared program. Delete your merged branch using: "git branch -d feature/my-feature" and then "git push origin --delete feature/my-feature"
