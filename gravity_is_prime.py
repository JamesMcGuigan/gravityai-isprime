#!/usr/bin/env python3
# Keep this GravityAI CLI interface in a separate file - causes pyTest conflicts

from gravityai import gravityai
from src.is_prime import is_prime_csv

gravityai.wait_for_requests(is_prime_csv)
