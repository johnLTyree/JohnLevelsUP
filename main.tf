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

# Create VPC, subnets, and default security group
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "subnet_a" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = var.subnet_a_az
}

resource "aws_subnet" "subnet_b" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = var.subnet_b_az
}

# Create security group allowing traffic from the internet
resource "aws_security_group" "web_sg" {
  vpc_id = aws_vpc.my_vpc.id

  ingress {
    from_port = var.web_sg_ingress_port
    to_port   = var.web_sg_ingress_port
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an Auto Scaling group with user data to launch Apache web server
resource "aws_launch_configuration" "web_config" {
  image_id        = var.ami_id
  instance_type   = var.instance_type
  security_groups = [aws_security_group.web_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              yum install -y httpd
              service httpd start
              chkconfig httpd on
              EOF
}

resource "aws_autoscaling_group" "web_asg" {
  desired_capacity     = 2
  max_size             = 5
  min_size             = 2
  vpc_zone_identifier = [aws_subnet.subnet_a.id, aws_subnet.subnet_b.id]
  launch_configuration = aws_launch_configuration.web_config.id
}

# Output the public IP addresses of the instances for verification
output "public_ips" {
  value = aws_instance.web_instances[*].public_ip
}

# Manual Termination Verification
resource "aws_instance" "web_instances" {
  count = 2

  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = element([aws_subnet.subnet_a.id, aws_subnet.subnet_b.id], count.index)

  user_data = <<-EOF
              #!/bin/bash
              yum install -y httpd
              service httpd start
              chkconfig httpd on
              EOF
}
