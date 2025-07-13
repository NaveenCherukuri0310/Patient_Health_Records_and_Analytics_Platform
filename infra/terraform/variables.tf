variable "aws_region" {
  default = "us-east-1"
}

variable "jenkins_ami" {
  default = "ami-0c02fb55956c7d316" # Amazon Linux 2
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_pair_name" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "s3_bucket_prefix" {
  default = "phr-backup"
}
