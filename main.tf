terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Data source to get the default VPC
data "aws_vpcs" "default" {
  filter {
    name   = "isDefault"
    values = ["true"]
  }
}

# Create subnets in the default VPC
resource "aws_subnet" "subnetpublicone" {
  vpc_id                  = data.aws_vpcs.default.ids[0]
  cidr_block              = var.subnet1_cidr
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"

  tags = {
    Name = "subnetpublicone"
  }
}

resource "aws_subnet" "subnetpublictwo" {
  vpc_id                  = data.aws_vpcs.default.ids[0]
  cidr_block              = var.subnet2_cidr
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1b"

  tags = {
    Name = "subnetpublictwo"
  }
}

# Creating a security group allowing traffic from the internet
resource "aws_security_group" "web_sg" {
  vpc_id = data.aws_vpcs.default.ids[0]

  # Ingress rule for HTTP
  ingress {
    from_port   = var.web_sg_ingress_port
    to_port     = var.web_sg_ingress_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Ingress rule for HTTPS
  ingress {
    from_port   = var.web_sg_ingress_port_https
    to_port     = var.web_sg_ingress_port_https
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Launch configuration for Auto Scaling instances
resource "aws_launch_configuration" "web_config" {
  image_id      = "ami-0e731c8a588258d0d"
  instance_type = var.instance_type

  user_data = <<-EOF
    #!/bin/bash
    yum install -y httpd
    service httpd start
    chkconfig httpd on
  EOF

  lifecycle {
    create_before_destroy = true
  }
}

# Auto Scaling group
resource "aws_autoscaling_group" "web_asg" {
  desired_capacity     = 2
  max_size             = 5
  min_size             = 2
  vpc_zone_identifier  = [aws_subnet.subnetpublicone.id, aws_subnet.subnetpublictwo.id]
  launch_configuration = aws_launch_configuration.web_config.id
}

# Output to display the public IP addresses of instances
output "public_ips" {
  value = aws_instance.web_instances[*].public_ip
}

# Manual Termination Verification
resource "aws_instance" "web_instances" {
  count = 2

  ami           = "ami-0e731c8a588258d0d"
  instance_type = var.instance_type
  subnet_id     = element([aws_subnet.subnetpublicone.id, aws_subnet.subnetpublictwo.id], count.index)

  user_data = <<-EOF
    #!/bin/bash
    yum install -y httpd
    service httpd start
    chkconfig httpd on
  EOF
}

# S3 bucket creation
resource "aws_s3_bucket" "jtyreeprojectbucket022024" {
  bucket = "jtyreeprojectbucket022024"
  acl    = "private"
}
