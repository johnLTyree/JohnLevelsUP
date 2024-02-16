variable "subnet1_cidr" {
  description = "CIDR block for subnetpublicone"
  default     = "172.31.40.0/24"
}

variable "subnet2_cidr" {
  description = "CIDR block for subnetpublictwo"
  default     = "172.31.30.0/24"
}

variable "web_sg_ingress_port" {
  description = "Ingress port for HTTP"
  default     = 80
}

variable "web_sg_ingress_port_https" {
  description = "Ingress port for HTTPS"
  default     = 443
}

variable "instance_type" {
  description = "EC2 instance type for Auto Scaling group"
  default     = "t2.micro"
}

variable "aws_region" {
  description = "AWS region for resources"
  default     = "us-east-1"
}
