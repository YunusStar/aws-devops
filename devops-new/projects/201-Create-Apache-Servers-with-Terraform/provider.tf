terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.44.0"
    }
    github = {
      source  = "integrations/github"
      version = "4.10.1"
    }
  }
}
provider "aws" {
  region = "us-east-1"
}
provider "github" {
  token = "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"
}






