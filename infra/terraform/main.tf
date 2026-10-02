terraform {
  required_version = ">= 1.3.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "fixora_demo" {
  name = "fixora-demo-open-sg"

  ingress {
    description = "DEMO ONLY - insecure SSH rule"
    from_port   = 22
    to_port     = 22
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

resource "aws_s3_bucket" "fixora_demo" {
  bucket = "fixora-demo-insecure-bucket-example"
}

resource "aws_s3_bucket_public_access_block" "fixora_demo" {
  bucket = aws_s3_bucket.fixora_demo.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
