output "jenkins_public_ip" {
  description = "Public IP of the Jenkins EC2 instance"
  value       = aws_instance.jenkins.public_ip
}

output "s3_bucket_name" {
  description = "Name of the created S3 backup bucket"
  value       = aws_s3_bucket.backup_bucket.id
}
