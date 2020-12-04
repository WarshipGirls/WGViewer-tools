import subprocess as cmd
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from fetch_user.fetch_valid_users import set_valid_user_list, get_valid_user_list



def get_time() -> str:
    return datetime.now().strftime("%D %H:%M")

def run_cmd(cmd_str: str) -> None:
    cmd.run(cmd_str, check=True, shell=True)


def auto_commit() -> None:

    '''
    if len(get_valid_user_list()) != 0:
        print("\nVALID USER LIST IS SET")
    else:
        PRINT("\n!! VALID USER LIST FAILED TO SET !!")
    '''

    with open("fetch_user/.token", 'r') as f:
        _tk = f.read()
    _uname = "WarshipGirls"
    _repo = "auto-update"
    print('\n[INFO {}] Start auto commiting...'.format(get_time()))
    try:
        print("Setting git config info...")
        run_cmd("git config --global user.email \"warshipgirlsviewer@gmail.com\"")
        run_cmd("git config --global user.name \"wgviewer\"")
        run_cmd(f"git config --global user.password \"{_tk}\"")
        run_cmd("git config --global --list")

        clone_cmd = f"git clone https://wgviewer:{_tk}@github.com/{_uname}/{_repo}.git"
        print("\nCloning {}".format(clone_cmd))
        run_cmd(clone_cmd)

        run_cmd("cd ./auto-update")
        run_cmd("pwd")



        #print("\nRunning git remote commands...")
        #cmd.run('git remote -v')
        #cmd.run('git remote remove origin')
        #cmd.run(f'git remote add origin git@github.com:{_uname}/{_repo}')
        #remote_cmd = f"git remote set-url origin https://wgviewer@github.com/{_uname}/{_repo}.git"
        remote_cmd = f"git remote set-url origin https://github.com/{_uname}/{_repo}.git"
        print("\n Setting remote origin...")
        run_cmd(remote_cmd)

        set_valid_user_list()

        run_cmd("git status")
        add_cmd = "git add ."
        run_cmd(add_cmd)
        message = "[AUTO {}] update txt files".format(get_time())
        # # On Windows, must be double quote
        commit_cmd = f'git commit -m \"{message}\"'
        run_cmd(commit_cmd)
        push_cmd = f'git push https://${_tk}@github.com/{_uname}/{_repo}.git -f'
        run_cmd(push_cmd)
        print('[INFO {}] Auto commiting done...'.format(get_time()))
    except Exception as e:
        print(e)
        print("AUTO COMMIT FAILED!")


def auto_fetch() -> None:
    print('[INFO {}] Setting valid user list...'.format(get_time()))
    auto_commit()
    #set_valid_user_list()
    print('[INFO {}] Valid user list is done...'.format(get_time()))


print('START auto fetching')
#cmd.run('touch asdf.txt', check=True, shell=True)
#cmd.run('touch random.txt', check=True, shell=True)
run_cmd("pwd")
#auto_commit()
auto_fetch()
#sched = BlockingScheduler()
#sched.scheduled_job(auto_fetch, 'interval', minutes=2)
#sched.start()
print('Auto fetching started!')
#auto_fetch()
