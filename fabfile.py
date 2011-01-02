from fabric.api import env, local, sudo
env.user = 'drusellers'
env.hosts = ['172.16.43.145']

#sudo aptitude install ssh
def install():
	sudo('apt-get update', pty=True)

#http://www.mono-project.com/FastCGI_Nginx
def install_nginx():
	sudo('aptitude install -y nginx', pty=True)

def install_postgres():
	sudo('aptitude install -y postgresql', pty=True)
	#setup user
	#setup database

def install_mono():
	sudo('aptitude install -y mono-fastcgi-server2', pty=True)
	put('mono-default', '/etc/nginx/sites-available/fluent', pty=True)
	put('monoserve.sh', '/etc/init.d/monoserve.sh', pty=True)
	sudo('ln -s /etc/nginx/sites-available/fluent /etc/nginx/sites-enabled/fluent', pty=True)
	sudo('/etc/init.d/monoserve start', pty=True)
	sudo('/etc/init.d/nginx restart', pty=True)

def sync_site():
	sudo('mkdir /var/www/fluent')
	sudo('chown -R drusellers:drusellers /var/www/fluent')
	local('rsync -avz ~/development/fluent %s@%s:/var/www/fluent' %(env.user, env.hosts[0]))
        sudo('chmod -R 770 /var/www/fluent')
        sudo('chmod -R o+r,o+x /var/www/fluent')
	


#rabbitmq
#varnish
#memcached
#setup non root accounts
## fluent
## postgres
## rabbit
#set up log files
