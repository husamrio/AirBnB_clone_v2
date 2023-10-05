#!/usr/bin/python3
'''
Deploy files to remote server using Fabric
        ***************************
        Fabric script methods:
    do_pack: packs web_static/ files into .tgz archive
    do_deploy: deploys archive to webservers
    deploy: do_packs && do_deploys
Usage:
    fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
        ***************************
'''
from fabric.api import env, put, run, local
import os.path
from time import strftime
env.hosts = ['54.173.80.121', '54.166.167.28']


def do_pack():
    '''Generate required files
        ***************************
        generate .tgz archive of web_static/ folder
        ***************************
    '''
    timenow = strftime('%Y%M%d%H%M%S')
    try:
        local('mkdir -p versions')
        filename = 'versions/web_static_{}.tgz'.format(timenow)
        local('tar -czvf {} web_static/'.format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    '''Upload achive to web servers
        ***************************
        Deploy archive to web server
        ***************************
    '''
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        path_no_ext = '/data/web_static/releases/{}/'.format(no_ext)
        symlink = '/data/web_static/current'
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path_no_ext))
        run('tar -xzf /tmp/{} -C {}'.format(filename, path_no_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(path_no_ext, path_no_ext))
        run('rm -rf {}web_static'.format(path_no_ext))
        run('rm -rf {}'.format(symlink))
        run('ln -s {} {}'.format(path_no_ext, symlink))
        return True
    except Exception:
        return False


def deploy():
    '''Deploy to the web servers
        ***************************
        Deploy archive to web server
        ***************************
    '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    deployment = do_deploy(archive_path)
    return deployment
