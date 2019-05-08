yum -y update
yum -y install httpd
service httpd start
chkconfig httpd on
yum install -y amazon-efs-utils
