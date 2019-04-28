————————————————————————————————————————————.wsgi文件最前面加入下面行表示启用虚拟环境——————————————————————————
activate_this = r'F:/Web_app/test/venv/Scripts/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
	



具体见：http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/
	
或者
activate_this = r'F:/Web_app/test/venv/Scripts/activate_this.py'
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))



——————————————————————————————————————————————————————————————————————————————————————————————————————————————

————————————————————————————————————————————vhost.conf文件中，对于Apache2.4———————————————————————————————————
WSGIPythonPath "f:/web_app/test"
<VirtualHost *:8080 >
	ServerAdmin hudi_0011@yeah.net
	ServerName localhost
	DocumentRoot F:\Web_app\test
	DirectoryIndex index.html index.php 	
	<Directory "F:\Web_app\test">
		Options -Indexes +FollowSymlinks
		AllowOverride none
		Require all granted
		Require host ip
	</Directory>
	WSGIScriptAlias / F:\Web_app\test\test.wsgi
</VirtualHost>


或者：
WSGIPythonPath "f:/web_app/test"
<VirtualHost *:8080 >
	ServerAdmin hudi_0011@yeah.net
	ServerName localhost
	WSGIScriptAlias / F:\Web_app\test\test.wsgi 	
	<Directory "F:\Web_app\test">
		AllowOverride none
		Require all granted
		Require host ip
	</Directory>
</VirtualHost>


——————————————————————————————————————————————————————————————————————————————————————————————————————————————