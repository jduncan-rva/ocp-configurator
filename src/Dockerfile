FROM centos:7
RUN yum -y install epel-release\
    yum -y install python-pip httpd mod_wsgi python-devel python-setuptools; yum clean all;
COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
ADD code/ /var/www/html
COPY setup/wsgi-vhost.conf /etc/httpd/conf.d/welcome.conf
COPY setup/entrypoint.sh /entrypoint.sh
RUN chmod 0777 /entrypoint.sh
EXPOSE 80
