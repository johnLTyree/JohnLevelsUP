# variables.tf

# AWS Region where resources will be created
variable "aws_region" {
  description = "The AWS region where resources will be created."
  type        = string
  default     = "us-east-1"  # Change this to your desired region
}

# Availability Zone for subnet A
variable "subnet_a_az" {
  description = "Availability Zone for subnet A."
  type        = string
  default     = "us-east-1a"  # Change this to your desired AZ
}

# Availability Zone for subnet B
variable "subnet_b_az" {
  description = "Availability Zone for subnet B."
  type        = string
  default     = "us-east-1b"  # Change this to your desired AZ
}

# ID of the Amazon Machine Image (AMI) for instances
variable "ami_id" {
  description = "The ID of the Amazon Machine Image (AMI) for instances."
  type        = string
  # Specify your desired AMI ID
  default     = "ami-xxxxxxxxxxxxxxxx"
}

# Type of EC2 instance to launch
variable "instance_type" {
  description = "The type of EC2 instance to launch."
  type        = string
  default     = "t2.micro"
}

# Ingress port for the web security group
variable "web_sg_ingress_port" {
  description = "The ingress port for the web security group."
  type        = number
  default     = 80
}