PRIVATE_KEY_PATH="/path/to/private/key.pem"
EC2_USER="my-ec2-user-name"
PUBLIC_IP="pub.ip.add.ress"

echo "ssh to ec2 at public IPv4: ${PUBLIC_IP}"
ssh ${EC2_USER}@${PUBLIC_IP} -i ${PRIVATE_KEY_PATH}
