import os


# release branch /master branch /base branch
def github():
    while True:
        os.system('tput setaf 4')
        print("\t\tEnter 0: To check status of repository\n\t\tEnter 1: Initialize the git Repository\n\t\tEnter 2: Track the file. ADD in Staging Area"
            "\n\t\tEnter 3: Commit the Changes\n\t\tEnter 4: Get Time Line : version [ reference ] Log \n\t\tEnter 5: Check Logs"
            "\n\t\tEnter 6: RollBack/Rollout the Version\n\t\tEnter 7: Show Branch\n\t\tEnter 8: Create branch and switch to new Branch"
            "\n\t\tEnter 9: Create New Branch\n\t\tEnter 10: To merge Branch\n\t\tEnter 11: To set Upstream Branch\n\t\tEnter 12: Add remote repository"
            "\n\t\tEnter 13: To push and Pull\n\t\tEnter 14: To see remote repository in verbose mode\n\t\tEnter 15: To fetch from remote repository"
            "\n\t\tEnter 16: Show Data at point in time\n\t\tEnter 17: To show Diff between two commits\n\t\tEnter 18: Discard the changes in file"
            "\n\t\tEnter 19: To see author, parent and tree information about commit\n\t\tEnter 20: Clone repository\n\t\tEnter 21: merge final version of branch [merge(squash)]"
            "\n\t\tEnter 22: Rebase the branch\n\t\tEnter 23: Do the cherry-pick[get certain point-in-time backup data]"
            "\n\t\tEnter 24: To do stash Operation\n\t\tEnter 25: Reset commit\n\t\tEnter 26: return to previous menu")
        os.system('tput setaf 7')

        Directory = input("\t\tEnter Repository[ Directory ] location: ")
        os.chdir(Directory)

        choice = input("\t\tEnter your choice: ")
        if choice == '0':
            os.system("git status")
        elif choice == '1':
            os.system("git init")
        elif choice == '2':
            add_option = input("\n\t\tEnter 1 : Add Specific File"
                               "\n\t\tEnter 2 : Track All file")
            if add_option == '1':
                os.system("git add .")
            elif add_option == '2':
                fileName = input("\t\tEnter File Name: ")
                os.system(f"git add {fileName}")
        elif choice == '3':
            commit_message = input()
            os.system(f"git commit -m {commit_message} .")
        elif choice == '4':
            branch = input("\t\tEnter branch name: ")
            os.system(f'git reflog {branch}')
        elif choice == '5':
            branch = input("\t\tEnter branch name: ")
            os.system(f'git log {branch}')
        elif choice == '6':
            commit_id = input("\t\tEnter commit Id: ")
            os.system(f"git reset {commit_id}")
            os.system("git checkout .")
        elif choice == '7':
            os.system("git branch -a")
        elif choice == '8':
            new_branch = input("\t\tEnter new branch name: ")
            os.system(f"git checkout -b {new_branch}")
        elif choice == '9':
            new_branch = input("\t\tEnter new branch name: ")
            os.system(f"git branch {new_branch}")
        elif choice == '10':
            branch = input("\t\tEnter branch Name:")
            is_upstream = input(f"\t\t{branch} is upstream branch [y/n]: ")
            if is_upstream == 'n':
                os.system(f"git merge {branch}")
            elif is_upstream == 'y':
                os.system(f'git pull')
            else:
                print('\t\twrong choice')
        elif choice == '11':
            branch = input("\t\tEnter branch Name:")
            os.system(f'git branch --set-upstream-to={branch}')
        elif choice == '12':
            github_repo_url = input("\t\tEnter github repository url: ")
            repository_name = input("\t\tEnter local Reference Name for repository: ")
            os.system(f"git remote add {repository_name} {github_repo_url}")
        elif choice == '13':
            pull_push_choice = input('\t\tEnter pull/push: ')
            local_branch = input("\t\tEnter local branch name: ")
            remote_branch = input("\t\tEnter remote branch name: ")
            if pull_push_choice.lower() == 'pull':
                os.system(f"git pull {local_branch} {remote_branch}")
            elif pull_push_choice.lower() == 'push':
                os.system(f"git push {local_branch} {remote_branch}")
            else:
                print("\t\twrong choice")
        elif choice == '14':
            os.system("git remote -v")
        elif choice == '15':
            remote_repository = input("\t\tEnter remote repository name: ")
            local_branch = input("\t\tEnter local branch")
            os.system(f"git fetch {local_branch} {remote_repository}")
        elif choice == '16':
            commit_id = input("\t\tEnter commit Id: ")
            os.system(f"git show {commit_id}")
        elif choice == '17':
            commit_id_from_ref = input("\t\tEnter ref commit Id: ")
            commit_id_to_ref = input("\t\tEnter to compare commit Id: ")
            os.system(f"git diff {commit_id_from_ref} {commit_id_to_ref}")
        elif choice == '18':
            file = input("\t\tEnter file name: ")
            os.system(f"git restore {file}")
        elif choice == '19':
            commit_id = input("\t\tEnter commit Id: ")
            os.system(f"git cat-file -p {commit_id}")
        elif choice == '20':
            repository = input('\t\tEnter Repository url: ')
            os.system(f"git clone {repository}")
        elif choice == '21':
            Branch = input("\t\tmerge to master branch name: ")
            os.system("git switch master")
            os.system(f"git merge --squash {Branch}")
        elif choice == '22':
            rebase_branch = input("\t\tEnter the branch that you want to rebase")
            os.system(f"git checkout {rebase_branch}")
            os.system("git rebase master")
        elif choice == '23':
            commit_id = input("\t\tEnter commit-id from you want to pick the data [Point-in-time data]: ")
            os.system(f"git cherry-pick {commit_id}")
        elif choice == '24':
            print("\n\t\tEnter 1: Stash [ Store un-committed in stash memory]\n\t\tEnter 2: list stash\n\t\tEnter 3: Restore data from stash memory")
            stash_choice = input("\n\t\tEnter your choice: ")
            if stash_choice == '1':
                os.system("git stash save")
            elif stash_choice == '2':
                os.system("git stash list")
            elif stash_choice == '3':
                stash_num = input("\t\tEnter stash number: ")
                os.system("git stash apply stash@{" + f"{stash_num}"+"}")
        elif choice == '25':
            reset = input("\t\tEnter reset type [hard/soft/mixed]: ")
            reset_commits = input("\t\tEnter number of commits you want to reset: ")
            os.system(f"git reset --{reset} HEAD~{reset_commits}")
        elif choice == '26':
            return
        else:
            print("Wrong choice!\n please try again")
