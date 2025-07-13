provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "jenkins_sg" {
  name        = "jenkins_sg_phr"
  description = "Allow SSH and Jenkins"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "jenkins" {
  ami                         = var.jenkins_ami
  instance_type               = var.instance_type
  key_name                    = var.key_pair_name
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.jenkins_sg.id]

  tags = {
    Name = "JenkinsServer"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras install docker -y
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ec2-user
              EOF
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "backup_bucket" {
  bucket = "${var.s3_bucket_prefix}-${random_id.bucket_suffix.hex}"
  acl    = "private"
}
